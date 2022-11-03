import VaBox
import VaConfig
import VaConfigLocal
from VaData import VaData


va_data = VaData()
VaConfig.setup(va_data)
local_data = VaData()
VaConfigLocal.setup(local_data)

local_data.set('Input array...M', [5, -6 , [3,[3,-1]]])

print('------------------------')
print(local_data.getNameValue('Input array...M'))
print('------------------------')
VaBox.start(va_data,local_data)

print(local_data.getNameValue('The sum of elements of array...sum'))

print('\nThe end')

