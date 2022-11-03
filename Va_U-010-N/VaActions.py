from VaDirectionDetector import getDirection

### Action__start ###################################################
def Action__start(va_data, local_data):
    print('Action__start')



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

### Action_9000 ###################################################
def Action_9000(va_data, local_data):
    print('Action_9000')


    return getDirection(va_data, local_data)
