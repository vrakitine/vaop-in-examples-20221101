def getDirection(va_data, local_data):

    # In this function below we are determine the direction depending on the current element of the array.

    # "Direction_green"    -> "If the current element of the array > 0",
    # "Direction_blue"    -> "If the current element of the array <= 0",
    # Direction_red"   -> "If the current element of the array can not be taken in case of end of array"

    va_data.set('Direction...direction', 'The_code_of_the_direction_is _unknown')

    local_data.set('Index of current element of array...i_main', local_data.get('Index of current element of array...i_main') + 1)
    
    if local_data.get('Index of current element of array...i_main') > len(local_data.get('Input array...M')) - 1:
      va_data.set('Direction...direction', 'Direction_red')

      return

    temp_array = local_data.get('Input array...M')
    local_data.set('The current element of array...current element', temp_array[local_data.get('Index of current element of array...i_main')])
  
    if local_data.get('The current element of array...current element') > 0:

      va_data.set('Direction...direction', 'Direction_green')

      return

    if not local_data.get('The current element of array...current element') > 0:      

      va_data.set('Direction...direction', 'Direction_blue')

      return
