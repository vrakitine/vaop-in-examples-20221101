## U-030-N-Color/VAOP code in Classes with new VA-script

####################################################################
### VA-script | Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
####################################################################

class VA_script:
  def getVaScript():
    va_script = {
      "Action__start":{
          "_agent_position":{
              "en-US":"In Init block of VA-box",
              "ru-RU":"В блоке Init VA-box"
          },
          "_action_description":{
              "_010":"--> init action"
          },
          "Direction_green":"Action__add_to_sum",  "_010":" > 0)",
          "Direction_blue":"Action__do_nothing",  "_010":" <= 0",
          "Direction_brown":"Action__met_array",  "_010":"Met an array",
          "Direction_deep_brown":"Action__met_empty_array",  "_010":"Met an empty array",
          "Direction_red":"Action_9000",  "_010":"The end of array"
      },
      "Action__add_to_sum":{
          "_agent_position":{
              "en-US":"The v-agent is adding current element of array to the sum_01",
              "ru-RU":"v-agent добавляет текущий элемент массива к sum_01"
          },
          "_action_description":{
              "_010":"empty"
          },
          "Direction_green":"Action__add_to_sum",  "_010":" > 0)",
          "Direction_blue":"Action__do_nothing",  "_010":" <= 0",
          "Direction_brown":"Action__met_array",  "_010":"Met an array",
          "Direction_deep_brown":"Action__met_empty_array",  "_010":"Met an empty array",
          "Direction_red":"Action_9000",  "_010":"The end of array"
      },
      "Action__do_nothing":{
          "_agent_position":{
              "en-US":"The v-agent is skipping the current element of array",
              "ru-RU":"v-agent пропускает текущий элемент массива"
          },
          "_action_description":{
              "_010":"empty"
          },
          "Direction_green":"Action__add_to_sum",  "_010":" > 0)",
          "Direction_blue":"Action__do_nothing",  "_010":" <= 0",
          "Direction_brown":"Action__met_array",  "_010":"Met an array",
          "Direction_deep_brown":"Action__met_empty_array",  "_010":"Met an empty array",
          "Direction_red":"Action_9000",  "_010":"The end of array"
      }, 
      "Action__met_array":{
          "_agent_position":{
              "en-US":"The v-agent is skipping the current element of array",
              "ru-RU":"v-agent пропускает текущий элемент массива"
          },
          "_action_description":{
              "_010":"empty"
          },
          "Direction_green":"Action__add_to_sum",  "_010":" > 0)",
          "Direction_blue":"Action__do_nothing",  "_010":" <= 0",
          "Direction_brown":"Action__met_array",  "_010":"Met an array",
          "Direction_deep_brown":"Action__met_empty_array",  "_010":"Met an empty array",
          "Direction_red":"Action_9000",  "_010":"The end of array"
      }, 
      "Action__met_empty_array":{
          "_agent_position":{
              "en-US":"The v-agent is skipping the current element of array",
              "ru-RU":"v-agent пропускает текущий элемент массива"
          },
          "_action_description":{
              "_010":"empty"
          },
          "Direction_green":"Action__add_to_sum",  "_010":" > 0)",
          "Direction_blue":"Action__do_nothing",  "_010":" <= 0",
          "Direction_brown":"Action__met_array",  "_010":"Met an array",
          "Direction_deep_brown":"Action__met_empty_array",  "_010":"Met an empty array",
          "Direction_red":"Action_9000",  "_010":"The end of array"
      },     
      "Action_9000":{
          "_agent_position":{
              "en-US":"The v-agent found the end of array",
              "ru-RU":"v-agent нашел конец массива"
          },
          "_action_description":{
              "_010":"empty"
          },
          "Direction_green":"Action_END",  "_010":" > 0",
          "Direction_blue":"Action_END",  "_010":" <= 0",
          "Direction_brown":"Action_END",  "_010":"Met an array",
          "Direction_deep_brown":"Action_END",  "_010":"Met an empty array",
          "Direction_red":"Action_END",  "_010":"The end of array"
      }
    }

    return va_script

####################################################################
### VA-script | End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
####################################################################

####################################################################
### Actions Class | Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
####################################################################

class Actions:
  
  ### Action__start ###################################################
  def Action__start(va_data):

    ### Start | Init setting 
 
    va_data['sum_01'] = {}
    va_data['sum_01']['d'] = "The sum of elements of array"
    va_data['sum_01']['v'] = 0

    va_data['i_main'] = {}
    va_data['i_main']['d'] = "The index in the all array" 
    va_data['i_main']['v'] = -1

    va_data['current_element'] = {}
    va_data['current_element']['d'] = "It is element of array, the v-agent is working with in this time in the current Action_xxx"
    va_data['current_element']['v'] = 'Unknown'

    va_data['d_level_desc'] = {}
    va_data['d_level_desc']['d'] = "The depth level description"
    va_data['d_level_desc']['v'] = {"d_level_type":"Unknown", "d_index":-1, "d_max_index":-1}

    va_data['d_level_pointer'] = {}
    va_data['d_level_pointer']['d'] = "The depth level pointer"
    va_data['d_level_pointer']['v'] = -1

    va_data['d_level_stack'] = {}
    va_data['d_level_stack']['d'] = "The depth level stack"
    va_data['d_level_stack']['v'] = []

    va_data['d_level_stack_pointer'] = {}
    va_data['d_level_stack_pointer']['d'] = "The depth level stack pointer"
    va_data['d_level_stack_pointer']['v'] = -1

    va_data['custom_log'] = {}
    va_data['custom_log']['d'] = "This is the log array for tracking custom variables in actions."
    va_data['custom_log']['v'] = [] 

    va_data['va']['v']['va_trace']['v'] = 'Action__start'

    """
    va_data[''] = {}
    va_data['']['v'] = 0
    va_data['']['d'] = "Empty"
    """
    ### End | Init setting

    ### Check Input Data

    if isinstance(va_data['M']['v'], list) and len(va_data['M']['v']) > 0:
      va_data['d_level_desc']['v'] = {
            "d_level_type":"list", 
            "d_index":0, 
            "d_max_index":len(va_data['M']['v']) - 1
          }
      va_data['d_level_stack']['v'].append(va_data['d_level_desc']['v'])
      va_data['d_level_stack_pointer']['v'] = 0 # ???


    ### for log
    va_data['custom_log']['v'].append('current_element')
    va_data['custom_log']['v'].append('sum_01')

    return Actions_tools.getDirectionCodeDependedOfTheValueOfTheCurrentElementOfArray(va_data)

  ### Action__add_to_sum ###################################################
  def Action__add_to_sum(va_data):
    va_data['sum_01']['v'] += va_data['current_element']['v']

    ### for log 
    va_data['custom_log']['v'].append('current_element')
    va_data['custom_log']['v'].append('sum_01')

    return Actions_tools.getDirectionCodeDependedOfTheValueOfTheCurrentElementOfArray(va_data)

  ### Action__do_nothing ###################################################
  def Action__do_nothing(va_data):

    ### for log
    va_data['custom_log']['v'].append('current_element')
    va_data['custom_log']['v'].append('sum_01')

    return Actions_tools.getDirectionCodeDependedOfTheValueOfTheCurrentElementOfArray(va_data)

  ### Action__met_array ###################################################
  def Action__met_array(va_data):

    va_data['d_level_desc']['v'] = {
            "d_level_type":"list", 
            "d_index":0, 
            "d_max_index":len(va_data['current_element']['v']) - 1
          }
    va_data['d_level_stack']['v'].append(va_data['d_level_desc']['v'])
    va_data['d_level_stack_pointer']['v'] = 0

    ### for log
    va_data['custom_log']['v'].append('current_element')
    va_data['custom_log']['v'].append('sum_01')

    return Actions_tools.getDirectionCodeDependedOfTheValueOfTheCurrentElementOfArray(va_data)

  ### Action__met_empty_array ###################################################
  def Action__met_empty_array(va_data):

    ### for log
    va_data['custom_log']['v'].append('current_element')
    va_data['custom_log']['v'].append('sum_01')

    return Actions_tools.getDirectionCodeDependedOfTheValueOfTheCurrentElementOfArray(va_data)

  ### Action_9000 ###################################################
  def Action_9000(va_data):

    return Actions_tools.getDirectionCodeDependedOfTheValueOfTheCurrentElementOfArray(va_data)

####################################################################
### Actions Class | End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
####################################################################
####################################################################
### Actions_tools | Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
####################################################################
class Actions_tools:

  def getDirectionCodeDependedOfTheValueOfTheCurrentElementOfArray(va_data):


    # In this function below we are determine the direction depending on the current element of the array.

    # "Direction_green"       -> "If the current element of the array > 0 and int and (first or third)",
    # "Direction_blue"        -> "If the current element of the array <= 0 or not int or not first or third",
    # "Direction_brown"       -> "If the current element of the array is array",
    # "Direction_deep_brown"  -> "If the current element of the array is empty array",
    # "Direction_red"         -> "If the current element of the array can not be taken in case of end of array"

    va_data['va']['v']['direction']['d'] = "The description of the direction is unknown"
    va_data['va']['v']['direction']['v'] = "The_code_of_the_direction_is_unknown"

    if len(va_data['d_level_stack']['v']) == 0:
      va_data['va']['v']['direction']['d'] = "The d_level_stack is empty"
      va_data['va']['v']['direction']['v'] = "Direction_red"

      return va_data  #-----------> Direction_red "d_level_stack is empty"

    # get current element of array      
    va_data['current_element']['v'] = Actions_tools.getCurrentElement(va_data)

    if isinstance(va_data['current_element']['v'], list): 
      if len(va_data['current_element']['v']) > 0:
        va_data['va']['v']['direction']['d'] = "The current element is an array"
        va_data['va']['v']['direction']['v'] = "Direction_brown"

        return va_data  #-----------> Direction_brown

      if len(va_data['current_element']['v']) == 0:
        va_data['va']['v']['direction']['d'] = "The current element is an empty array"
        va_data['va']['v']['direction']['v'] = "Direction_deep_brown"

        return va_data  #-----------> Direction_deep_brown

    if va_data['current_element']['v'] > 0: 
      va_data['va']['v']['direction']['d'] = "The current element is a positive number"
      va_data['va']['v']['direction']['v'] = "Direction_green"

      return va_data  #-----------> Direction_green

    if not (va_data['current_element']['v'] > 0):
      va_data['va']['v']['direction']['d'] = "The current element is not a positive number"
      va_data['va']['v']['direction']['v'] = "Direction_blue"
      
      return va_data  #-----------> Direction_blue  

    return va_data  

  def getCurrentElement(va_data):
    temp_list = va_data['M']['v']
    va_data['d_level_stack_pointer']['v'] = -1
    for temp_d_level_desc in va_data['d_level_stack']['v']:
      va_data['d_level_stack_pointer']['v'] += 1      
      if temp_d_level_desc['d_level_type'] == 'list':
        if va_data['d_level_stack_pointer']['v'] < len(va_data['d_level_stack']['v']) - 1:
          temp_list = temp_list[temp_d_level_desc['d_index'] - 1 ]
        if va_data['d_level_stack_pointer']['v'] >= len(va_data['d_level_stack']['v']) - 1:
          temp_list = temp_list[temp_d_level_desc['d_index']]

    temp_d_level_desc['d_index'] += 1
 
    if temp_d_level_desc['d_index'] > temp_d_level_desc['d_max_index']:
      if not isinstance(temp_list, list) or (isinstance(temp_list, list) and len(temp_list) == 0):
        temp_d_level_stack = []
        for temp_d_level_desc in va_data['d_level_stack']['v']:
          if temp_d_level_desc['d_index'] <= temp_d_level_desc['d_max_index']:
            temp_d_level_stack.append(temp_d_level_desc)
        va_data['d_level_stack']['v'] = temp_d_level_stack

    return temp_list   

  def Action_variables_tracking_row(va_data):
    print(">>> custom_log -->")
    if len(va_data['custom_log']['v']) == 0:
      print("\tEmpty")
    for temp in va_data['custom_log']['v']:
      print("\t" + temp ,"= [" + str(va_data[temp]['v']) + "] <-- " +  va_data[temp]['d'])
    va_data['custom_log']['v'] = []

    return va_data 

####################################################################
### Actions_tools Class | End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
####################################################################
####################################################################
### VA_box | Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
####################################################################

class VA_box:
  
  def start(va_data):

    ### Start | The VAOP variables setting


    if 'va' not in va_data:
      va_data['va']= {}
      va_data['va']['v'] = {}
      va_data['va']['d'] = "The VAOP sysrem variables"   

    va_data['va']['v']['jump'] = {}
    va_data['va']['v']['jump']['v'] = 0
    va_data['va']['v']['jump']['d'] = "The sequential number of the v-agent's jump"

    va_data['va']['v']['max_jump'] = {}
    va_data['va']['v']['max_jump']['v'] = 1000
    va_data['va']['v']['max_jump']['d'] = "The max number of the v-agent's jump. It is for prevent looping."

    va_data['va']['v']['locale_lang_code_defaulf'] = {}
    va_data['va']['v']['locale_lang_code_defaulf']['v'] = 'en-US'
    va_data['va']['v']['locale_lang_code_defaulf']['d'] = "The default locale language code"

    if VA_box_tools.isNotDefinedOutsideOfVaBox(va_data['va']['v'],'locale_lang_code'):
      va_data['va']['v']['locale_lang_code'] = {}
      va_data['va']['v']['locale_lang_code']['v'] = 'en-US'
      va_data['va']['v']['locale_lang_code']['d'] = "The locale language code"

    va_data['va']['v']['agent_position'] = {}
    va_data['va']['v']['agent_position']['v'] = 'Unknown'
    va_data['va']['v']['agent_position']['d'] = "It is info about what is v-agent doing at this moment"

    va_data['va']['v']['script'] = {}
    va_data['va']['v']['script']['v'] = VA_script.getVaScript()
    va_data['va']['v']['script']['d'] = "VA script"

    va_data['va']['v']['previous_action'] = {}
    va_data['va']['v']['previous_action']['v'] = 'Unknown'
    va_data['va']['v']['previous_action']['d'] = "The previous Action"

    va_data['va']['v']['current_action'] = {}
    va_data['va']['v']['current_action']['v'] = 'Action__start'
    va_data['va']['v']['current_action']['d'] = "The current Action"

    va_data['va']['v']['direction'] = {}
    va_data['va']['v']['direction']['d'] = "The description of the direction is unknown"
    va_data['va']['v']['direction']['v'] = "The_code_of_the_direction_is _unknown"

    ### for va-tracking
    if VA_box_tools.isNotDefinedOutsideOfVaBox(va_data['va']['v'],'is_tracking_on'):
      va_data['va']['v']['is_tracking_on'] = {}
      va_data['va']['v']['is_tracking_on']['v'] = False
      va_data['va']['v']['is_tracking_on']['d'] = "Is tracking ON? (True/False)"

    if VA_box_tools.isNotDefinedOutsideOfVaBox(va_data['va']['v'],'content_of_va_tracking_row'):
      va_data['va']['v']['content_of_va_tracking_row'] = {}
      va_data['va']['v']['content_of_va_tracking_row']['v'] = ['jump', 'previous_action', 'direction', 'agent_position']
      va_data['va']['v']['content_of_va_tracking_row']['d'] = "The content of va-tracking row"

    if VA_box_tools.isNotDefinedOutsideOfVaBox(va_data['va']['v'],'tracking_actions'):
      va_data['va']['v']['tracking_actions'] = {}
      va_data['va']['v']['tracking_actions']['v'] = VA_script.getVaScript().keys()
      va_data['va']['v']['tracking_actions']['d'] = "The list of actions to track"

    if VA_box_tools.isNotDefinedOutsideOfVaBox(va_data['va']['v'],'jump_pause_after_actions'):
      va_data['va']['v']['jump_pause_after_actions'] = {}
      va_data['va']['v']['jump_pause_after_actions']['v'] = []
      va_data['va']['v']['jump_pause_after_actions']['d'] = "The jump pause after actions"

    ### for va-trace
    va_data['va']['v']['va_trace'] = {}
    va_data['va']['v']['va_trace']['d'] = "The va-trace"
    va_data['va']['v']['va_trace']['v'] = ''

    ### End | The VAOP variables setting
  
    va_data = Actions.Action__start(va_data)
  
    while 1 == 1: 
      va_data['va']['v']['jump']['v'] += 1
      if va_data['va']['v']['jump']['v'] > va_data['va']['v']['max_jump']['v']:
        print(va_data)
        print("\n\n Error: Looping")
        break

      temp = va_data['va']['v']['script']['v'][va_data['va']['v']['current_action']['v']][va_data['va']['v']['direction']['v']]

      va_data['va']['v']['previous_action']['v'] = va_data['va']['v']['current_action']['v']
      va_data['va']['v']['current_action']['v'] = temp  

      va_data['va']['v']['va_trace']['v'] += '|' + va_data['va']['v']['direction']['v'] + '|' + temp

      if va_data['va']['v']['is_tracking_on']['v'] and (va_data['va']['v']['previous_action']['v'] in va_data['va']['v']['tracking_actions']['v']):
        va_data = VA_box_tools.VA_tracking_row(va_data)
        va_data = Actions_tools.Action_variables_tracking_row(va_data)
        print("\n")
      
      if va_data['va']['v']['current_action']['v'] in va_data['va']['v']['script']['v']:
        if va_data['va']['v']['current_action']['v'] in va_data['va']['v']['jump_pause_after_actions']['v'] and va_data['va']['v']['is_tracking_on']['v'] and (va_data['va']['v']['current_action']['v'] in va_data['va']['v']['tracking_actions']['v']):
          print("jump_pause_after_actions:", va_data['va']['v']['jump_pause_after_actions']['v'])
          temp = input("pause ===> after action:[" + va_data['va']['v']['current_action']['v'] + "] <enter> - continue, <space><enter> - break")
          if temp == ' ':
            break
        va_data['va']['v']['direction']['v'] = 'direction unknown'        
        eval('Actions.' + va_data['va']['v']['current_action']['v'] + "(va_data)")
      else:
        break

    print('The v-agent is finished jumping in the action [', va_data['va']['v']['current_action']['v'], ']')    

    return va_data

class VA_box_tools: ##########################################################
  def isNotDefinedOutsideOfVaBox(var_array, var_key_name):
    temp = True
    if var_key_name in var_array:
      if ('v' in var_array[var_key_name]) and ('d' in var_array[var_key_name]):
        temp = False

    return temp

  def getAgentPosition(va_data):
    va_data['va']['v']['agent_position']['v'] = "Now in [" + va_data['va']['v']['previous_action']['v'] + "]"
    if '_agent_position' in va_data['va']['v']['script']['v'][va_data['va']['v']['previous_action']['v']]:
      if va_data['va']['v']['locale_lang_code']['v'] in va_data['va']['v']['script']['v'][va_data['va']['v']['previous_action']['v']]['_agent_position']:
        va_data['va']['v']['agent_position']['v'] = va_data['va']['v']['script']['v'][va_data['va']['v']['previous_action']['v']]['_agent_position'][va_data['va']['v']['locale_lang_code']['v']]
        if va_data['va']['v']['agent_position']['v'] == '':
          if va_data['va']['v']['locale_lang_code_defaulf']['v'] in va_data['va']['v']['script']['v'][va_data['va']['v']['previous_action']['v']]['_agent_position']:
            va_data['va']['v']['agent_position']['v'] = va_data['va']['v']['script']['v'][va_data['va']['v']['previous_action']['v']]['_agent_position'][va_data['va']['v']['locale_lang_code_defaulf']['v']]
      if va_data['va']['v']['locale_lang_code']['v'] not in va_data['va']['v']['script']['v'][va_data['va']['v']['previous_action']['v']]['_agent_position']:
        if va_data['va']['v']['locale_lang_code_defaulf']['v'] in va_data['va']['v']['script']['v'][va_data['va']['v']['previous_action']['v']]['_agent_position']:
          va_data['va']['v']['locale_lang_code']['v'] = va_data['va']['v']['script']['v'][va_data['va']['v']['previous_action']['v']]['_agent_position'][va_data['va']['v']['locale_lang_code_defaulf']['v']]
    
    return va_data  

  def VA_tracking_row(va_data):
    va_data = VA_box_tools.getAgentPosition(va_data)
    print("va-agent tracking -->")
    for temp in va_data['va']['v']['content_of_va_tracking_row']['v']:
      print("\t" + temp ,"= [" + str(va_data['va']['v'][temp]['v']) + "] <-- " +  va_data['va']['v'][temp]['d'])
      
    return va_data 

################################# ###################################
### VA_box | End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
####################################################################
va_data = {}

va_data['va'] = {}
va_data['va']['v'] = {}
va_data['va']['d'] = "The VA box variables"  

va_data['va']['v'] = {"is_tracking_on":{"d":"Is tracing ON?? (True/False)","v":False}}

"""
va_data['va']['v']['tracking_actions'] = {}
va_data['va']['v']['tracking_actions']['v'] = ['Action__add_to_sum']
va_data['va']['v']['tracking_actions']['d'] = "The list of actions to track"
    
va_data['va']['v']['jump_pause_after_actions'] = {}
va_data['va']['v']['jump_pause_after_actions']['v'] = ['Action__add_to_sum']
va_data['va']['v']['jump_pause_after_actions']['d'] = "The jump pause after actions"
"""

#####################################################
va_data['M'] = {}
va_data['M']['d'] = "Input array"
va_data['M']['v'] = [4,[],6]


print(va_data['M'])

va_data = VA_box.start(va_data)

temp_trace_01 = va_data['va']['v']['va_trace']['v'] 

print(va_data['sum_01'])
print('\n########################################')
print(va_data['va']['v']['va_trace'])
#####################################################
va_data['M']['v'] = [4,[5,[]]]


print('\n')
print(va_data['M'])

va_data = VA_box.start(va_data)

temp_trace_02 = va_data['va']['v']['va_trace']['v'] 

print(va_data['sum_01'])
print('\n########################################')
print(va_data['va']['v']['va_trace'])

if temp_trace_01 == temp_trace_02:
  print('\nIt is similar lists')

if temp_trace_01 != temp_trace_02:
  print('\nIt is not similar lists')

print('\nThe end')
