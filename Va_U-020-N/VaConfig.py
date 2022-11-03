from VaScript import getVaScript

def setup(va):

    ### The VAOP engine variables setting

    va.defineVariable('The sequential number of the v-agent jump...p10', 0)
    va.defineVariable('The max number of the v-agent jump. It is for prevent looping...p11', 1000)
    va.defineVariable('The default locale language code...p12_0', 'en-US')
    va.defineVariable('The locale language code...p12_1', 'en-US')
    va.defineVariable('VA script...va_script', getVaScript()) 
    va.defineVariable('The previous Action...previous action', 'Unknown') 
    va.defineVariable('The current Action...current action', 'Action__start') 
    va.defineVariable('Direction...direction', 'Direction_10') 

    va.defineVariable('This is the log array for tracking custom variables in actions...custom_log', []) 
    va.defineVariable('Number of jumps...jump', 0)
    va.defineVariable('Max number of jumps...max_jump', 1000)
