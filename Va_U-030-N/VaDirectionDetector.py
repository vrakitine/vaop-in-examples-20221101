def getDirection(va_data, local_data):

  # In this function below we are determine the direction depending on the current element of the array.

  # "Direction_green" -> "If the current element of the array > 0",
  # "Direction_blue"  -> "If the current element of the array <= 0",
  # "Direction_brown" -> "If the current element of the array is array",
  # "Direction_deep_brown"  -> "If the current element of the array is empty array",
  # "Direction_red"   -> "If the current element of the array can not be taken in case of end of array"


  va_data.set('Direction...direction', 'The_code_of_the_direction_is _unknown')

  if len(local_data.get('The depth level stack array...d_level_stack')) == 0:
    va_data.set('Direction...direction', 'Direction_red')

    return va_data  #-----------> Direction_red "d_level_stack is empty"

  # get current element of array      
  local_data.set('The current element of array...current element', getCurrentElement(va_data, local_data))

  if isinstance(local_data.get('The current element of array...current element'), list): 
    if len(local_data.get('The current element of array...current element')) > 0:
      va_data.set('Direction...direction', 'Direction_brown')

      return va_data  #-----------> Direction_brown

    if len(local_data.get('The current element of array...current element')) == 0:
      va_data.set('Direction...direction', 'Direction_deep_brown')

      return va_data  #-----------> Direction_deep_brown

  if local_data.get('The current element of array...current element') > 0: 
    va_data.set('Direction...direction', 'Direction_green')

    return va_data  #-----------> Direction_green

  if not (local_data.get('The current element of array...current element') > 0):
    va_data.set('Direction...direction', 'Direction_blue')

    return va_data  #-----------> Direction_blue  

  return va_data  

def getCurrentElement(va_data, local_data):
    temp_list = local_data.get('Input array...M')
    local_data.set('The depth level stack pointer...d_level_stack_pointer', -1)
    for temp_d_level_desc in local_data.get('The depth level stack array...d_level_stack'):
      local_data.set('The depth level stack pointer...d_level_stack_pointer', local_data.get('The depth level stack pointer...d_level_stack_pointer') + 1)  
      if temp_d_level_desc.get('The depth level...d_level_type') == 'list':
        if local_data.get('The depth level stack pointer...d_level_stack_pointer') < len(local_data.get('The depth level stack array...d_level_stack')) - 1:
          temp_list = temp_list[temp_d_level_desc.get('The depth level index...d_index') - 1 ]
        if local_data.get('The depth level stack pointer...d_level_stack_pointer') >= len(local_data.get('The depth level stack array...d_level_stack')) - 1:
          temp_list = temp_list[temp_d_level_desc.get('The depth level index...d_index')]

    temp_d_level_desc.set('The depth level index...d_index', temp_d_level_desc.get('The depth level index...d_index') + 1)

    if temp_d_level_desc.get('The depth level index...d_index') > temp_d_level_desc.get('The depth level max index...d_max_index'):      #if not isinstance(temp_list, list): 
      if not isinstance(temp_list, list) or (isinstance(temp_list, list) and len(temp_list) == 0): 
        temp_d_level_stack = []
        for temp_d_level_desc in local_data.get('The depth level stack array...d_level_stack'):
          if temp_d_level_desc.get('The depth level index...d_index') <= temp_d_level_desc.get('The depth level max index...d_max_index'):
            temp_d_level_stack.append(temp_d_level_desc)
        local_data.set('The depth level stack array...d_level_stack',temp_d_level_stack)

    return temp_list

