from VaData import VaData

def setup(local):

    ### The  variables setting:

    local.defineVariable('Input array...M', [])
    local.defineVariable('Index of current element of array...i_main', -1)
    local.defineVariable('The current element of array M...current element', 'Unknown')
    local.defineVariable('The sum of elements of array...sum', 0)

    local.defineVariable('The depth level description...d_level_description_obj', VaData())
    local.get('The depth level description...d_level_description_obj').defineVariable("The depth level...d_level_type","Unknown")
    local.get('The depth level description...d_level_description_obj').defineVariable("The depth level index...d_index", -1)
    local.get('The depth level description...d_level_description_obj').defineVariable("The depth level max index...d_max_index", -1)
    
    local.defineVariable('The depth level pointer...d_level_pointer', -1)
    local.defineVariable('The depth level stack array...d_level_stack', [])
    local.defineVariable('The depth level stack pointer...d_level_stack_pointer', -1)

