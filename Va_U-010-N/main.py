import VaBox
import VaActions
import VaScript
import VaConfig
import VaConfigLocal
from VaData import VaData


va_data = VaData()
VaConfig.setup(va_data)
local_data = VaData()

VaConfigLocal.setup(local_data)

local_data.set('Input array...M', [2, -3 , 3])

"""
test = va_data.getAll()
print(test)
print('------------------------')
test = local_data.getAll()
print(test)
print('------------------------')

"""

VaBox.start(va_data,local_data)

print(local_data.getNameValue('The sum of elements of array...sum'))

local_data.printNameValue('*...sum')

print('\nThe end')

