from VaDirectionDetector import getDirection
from VaData import VaData

### Action__start ###################################################
def Action__start(va_data, local_data):
    print('Action__start')

    ### Check Input Data

    if isinstance(local_data.get('Input array...M'), list) and len(local_data.get('Input array...M')) > 0:
        temp_d_level_description_obj = VaData()
        temp_d_level_description_obj.defineVariable("The depth level...d_level_type","list")
        temp_d_level_description_obj.defineVariable("The depth level index...d_index", 0)
        temp_d_level_description_obj.defineVariable("The depth level max index...d_max_index",len(local_data.get('Input array...M')) - 1)

        temp_d_level_stack = []
        temp_d_level_stack.append(temp_d_level_description_obj)
        local_data.set('The depth level stack array...d_level_stack', temp_d_level_stack)

    return getDirection(va_data, local_data)

### Action__add_to_sum ###################################################
def Action__add_to_sum(va_data, local_data):
    print('Action__add_to_sum')

    local_data.set('The sum of elements of array...sum', 
    local_data.get('The sum of elements of array...sum') + local_data.get('The current element of array M...current element'))


    return getDirection(va_data, local_data)

### Action__do_nothing ###################################################
def Action__do_nothing(va_data, local_data):
    print('Action__do_nothing')


    return getDirection(va_data, local_data)

### Action__met_array ###################################################
def Action__met_array(va_data, local_data):
    print('Action__met_array')

    temp_d_level_description_obj = VaData()
    temp_d_level_description_obj.defineVariable("The depth level...d_level_type","list")
    temp_d_level_description_obj.defineVariable("The depth level index...d_index", 0)
    temp_d_level_description_obj.defineVariable("The depth level max index...d_max_index",
        len(local_data.get('The current element of array M...current element')) - 1)

    temp_d_level_stack = local_data.get('The depth level stack array...d_level_stack')
    temp_d_level_stack.append(temp_d_level_description_obj)
    local_data.set('The depth level stack array...d_level_stack', temp_d_level_stack)

    local_data.set('The depth level stack pointer...d_level_stack_pointer', 0)

    return getDirection(va_data, local_data)

### Action_9000 ###################################################
def Action_9000(va_data, local_data):
    print('Action_9000')


    return getDirection(va_data, local_data)
