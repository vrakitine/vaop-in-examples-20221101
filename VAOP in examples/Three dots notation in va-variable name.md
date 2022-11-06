
# VAOP: Va-script (type B) решает все проблемы новичков при написании ботов
## Введение
<!-- Updated Three dots notation in va-variable name-->
Когда в апреле 2021 года я опубликовал статью - Введение в v-agent ориентированное программирование (https://habr.com/ru/post/554014/), в которой сформулировал идеологию и заложил основной понятийный аппарат новой методологии программирования v-agent, va-script, va-box, action, direction, то напомнил себе изобретателя радио - Сделал Маркони радио, включил, а слушать то нечего.
Еще веселее было с наличием тогда убойных примеров применения новой методологии. Тут я, еще раз улыбнулся, вспомнив старый анегдот про ученого выступившего на симпозиуме и заявившего, что мы изобрели чудо лекарство и осталось только выяснить - от чего же оно лечит?
Нельзя сказать, что VAOP не помогало мне решать проблемы, но они имели локальный характер. Ну кого интересует, например, проблема реализации алгоритма TTC (https://en.wikipedia.org/wiki/Top_trading_cycle). VAOP очень помог облегчить мои страдания на этом проекте.
Не знаю как дела у того ученого с его чудо лекарством, но в моем случае, случилось чудо и ко мне обратился парень у которого были проблемы с написанием бота и я, за три часовых сеанса консультаций, облегчил его страдания, причем, больше половины времени ушло у нас на объяснение мне что такое бот и что там вызывает головную боль. Стало очевидно, что головная боль при написании ботов очень хорощо лечится, если сразу начать применять VAOP методологию.
К слову, парень, с которым я писал свой первый VaBot, каким-то образом догадался, прослушав мое видео - (https://youtu.be/6xzn78onzQk) что я именно тот, кто сможет ему помочь. Он, как я понял, перелопатил кучу источников, где хоть что-то говорилось про конечные автоматы. Понял он много и теоретически был подкован, но реализовать на практике не мог. Я его успокаивал, что он не один такой, что и я в 1981 году после окончания МИфИ все знал про КА, но мне потребовалось три месяца, чтобы привязать мои знания к решению конкретной задачи и выдолбить все в коде.
Это, говорил я, как облака на небе - воды много, но попробуй напейся из них. Его летание в облаках не прошло даром, и для меня. Узнал от него много интересных вещей касательно КА и всего того нового тумана, который успели напустить вокруг этой замечательно идеи- разбить всю задачу, которую надо запрограммировать на состояния (states) и прыгать от состояния к состоянию. Все понятно и все довольны. На деле, же не все так просто потому, что это совершенно другой подход к программированию, своя парадигма программирования и этому надо учить и учиться.
Еще немного отвлекусь и мы вернемся к ботам. Вот, например, я всегда начинаю свои консультации по VAOP с решения очень простой задачи - найти сумму положительных элементов массива. Предположим на языке python.
Обычное рещение, которому всех учат выглядит примерно так:

```python
# Update 010 / Regular code
M = [1,2,7, -5, 1]
sum_01 = 0
for a in M:
  if a > 0:
    sum_01 += a
print(str(sum_01))
~~~

а в VAOP смотрите в репозитории:

Код в тысячу раз длиннее и напрягаться надо, чтобы понять новую методологию программирования. У любого нормального человека возникает вопрос -  Зачем такая сложность, когда все решается десятью строчкоми кода? Так и у моих студентов (назовем из так, хотя часто это были довольно крутые программеры) возникал такой вопрос - зачем?
Я говорю им, что в идеале процесс обучения должен быть максимально приближен к тому с чем студент сталкнется в реальности. Поэтому, я предлагаю им сыграть в такую игру-работу. 
Заказчику нужно знать сумму элементов, которые находятся в подсписке, начинающемся и заканчивающемся элементом, равным 777. Элемент, равный 7, останавливает добавление всех последующих элементов в подсписке к sum_01
 
In array M = [1.4, 777, 5, 4.3, 7, 8, 777, 9,23, 777, 5, 6.5, 777, 3] sum will be equal to 10
In array M = [1.4, 777, 2, 4.3, 7, 8, 777, 777, 5, 6.5, 777, 3] sum will be equal to 7
In array M = [3, 2, 5.9, 777, 12, 4.76, 2] sum will be equal to 0 

Примеры обычного решения Вы можете вообразить себе сами и они будут у каждого свои.
В VAOP решение будет одно и записать в виде Va-script (type B)

~~~python
####################################################################
### VA-script | Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
####################################################################

class VA_script:
  def getVaScript():
    va_script = {
      "Action_000":{
          "_agent_position":{
              "en-US":"In the Init block of VA-box and the v-agent is waiting for 777",
              "ru-RU":"В блоке Init VA-box и v-agent ждет 777"
          },
          "_action_description":{
              "comment_010":"--> init action"
          },
          "Direction_10":"Action_005",  "comment_010":" > 0 and int and (first or third)",
          "Direction_20":"Action_005",  "comment_010":" <= 0 or not int or not first or third",
          "Direction_30":"Action_005",  "comment_010":" == 7",
          "Direction_40":"Action_040",  "comment_010":" == 777",
          "Direction_1000":"Action_9000",  "comment_010":"The end of array"
      },
      "Action_005":{
          "_agent_position":{
              "en-US":"The v-agent is waiting for 777",
              "ru-RU":"v-agent ждет 777"
          },
          "_action_description":{
              "comment_010":"--> init action"
          },
          "Direction_10":"Action_005",  "comment_010":" > 0 and int and (first or third)",
          "Direction_20":"Action_005",  "comment_010":" <= 0 or not int or not first or third",
          "Direction_30":"Action_005",  "comment_010":" == 7",
          "Direction_40":"Action_040",  "comment_010":" == 777",
          "Direction_1000":"Action_9000",  "comment_010":"The end of array"
      },
      "Action_010":{
          "_agent_position":{
              "en-US":"The v-agent is adding current element of array to the range_list",
              "ru-RU":"v-agent добавляет текущий элемент массива к range_list"
          },
          "_action_description":{
              "comment_010":"empty"
          },
          "Direction_10":"Action_010",  "comment_010":" > 0 and int and (first or third)",
          "Direction_20":"Action_020",  "comment_010":" <= 0 or not int or not first or third",
          "Direction_30":"Action_030",  "comment_010":" == 7",
          "Direction_40":"Action_050",  "comment_010":" == 777",
          "Direction_1000":"Action_9000",  "comment_010":"The end of array"
      },
      "Action_020":{
          "_agent_position":{
              "en-US":"The v-agent is doing nothing",
              "ru-RU":"v-agent ничего не делает"
          },
          "_action_description":{
              "comment_010":"empty"
          },
          "Direction_10":"Action_010",  "comment_010":" > 0 and int and (first or third)",
          "Direction_20":"Action_020",  "comment_010":" <= 0 or not int or not first or third",
          "Direction_30":"Action_030",  "comment_010":" == 7",
          "Direction_40":"Action_050",  "comment_010":" == 777",
          "Direction_1000":"Action_9000",  "comment_010":"The end of array"
      },
      "Action_030":{
          "_agent_position":{
              "en-US":"The v-agent after met 7",
              "ru-RU":"V-агент после встречи с 7"
          },
          "_action_description":{
              "comment_010":"empty"
          },
          "Direction_10":"Action_030",  "comment_010":" > 0 and int and (first or third)",
          "Direction_20":"Action_030",  "comment_010":" <= 0 or not int or not first or third",
          "Direction_30":"Action_030",  "comment_010":" == 7",
          "Direction_40":"Action_050",  "comment_010":" == 777",
          "Direction_1000":"Action_9000",  "comment_010":"The end of array"
      },
      "Action_040":{
          "_agent_position":{
              "en-US":"The v-agent after met 777 as a start of range",
              "ru-RU":"V-агент после встречи с 777 в качестве начала диапазона"
          },
          "_action_description":{
              "comment_010":"empty"
          },
          "Direction_10":"Action_010",  "comment_010":" > 0 and int and (first or third)",
          "Direction_20":"Action_020",  "comment_010":" <= 0 or not int or not first or third",
          "Direction_30":"Action_030",  "comment_010":" == 7",
          "Direction_40":"Action_050",  "comment_010":" == 777",
          "Direction_1000":"Action_9000",  "comment_010":"The end of array"
      },
      "Action_050":{
          "_agent_position":{
              "en-US":"The v-agent after met 777 as a end of range",
              "ru-RU":"V-агент после того, как встретил 777 как конец диапазона"
          },
          "_action_description":{
              "comment_010":"empty"
          },
          "Direction_10":"Action_005",  "comment_010":" > 0 and int and (first or third)",
          "Direction_20":"Action_005",  "comment_010":" <= 0 or not int or not first or third",
          "Direction_30":"Action_005",  "comment_010":" == 7",
          "Direction_40":"Action_040",  "comment_010":" == 777",
          "Direction_1000":"Action_9000",  "comment_010":"The end of array"
      },       
      "Action_9000":{
          "_agent_position":{
              "en-US":"The v-agent found the end of array",
              "ru-RU":"v-agent нашел конец массива"
          },
          "_action_description":{
              "comment_010":"empty"
          },
          "Direction_10":"Action_END",  "comment_010":" > 0 and int and (first or third)",
          "Direction_20":"Action_END",  "comment_010":" <= 0 or not int or not first or third",
          "Direction_30":"Action_END",  "comment_010":" == 7",
          "Direction_40":"Action_END",  "comment_010":" == 777",
          "Direction_1000":"Action_END",  "comment_010":"The end of array"
      }
    }

    return va_script
~~~

Видно, что без всех этих сложностей с "777" промежутками, сценарий работы Va-engine выглядел бы проще:

~~~python
## U-020-N/VAOP

####################################################################
### VA-script | Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
####################################################################

class VA_script:
  def getVaScript():
    va_script = {
      "Action_000":{
          "_agent_position":{
              "en-US":"In Init block of VA-box",
              "ru-RU":"В блоке Init VA-box"
          },
          "_action_description":{
              "comment_010":"--> init action"
          },
          "Direction_10":"Action_010",  "comment_010":" > 0 and int and (first or third)",
          "Direction_20":"Action_020",  "comment_010":" <= 0 or not int or not first or third",
          "Direction_30":"Action_030",  "comment_010":" == 7",
          "Direction_1000":"Action_9000",  "comment_010":"The end of array"
      },
      "Action_010":{
          "_agent_position":{
              "en-US":"The v-agent is adding current element of array to the sum_01",
              "ru-RU":"v-agent добавляет текущий элемент массива к sum_01"
          },
          "_action_description":{
              "comment_010":"empty"
          },
          "Direction_10":"Action_010",  "comment_010":" > 0 and int and (first or third)",
          "Direction_20":"Action_020",  "comment_010":" <= 0 or not int or not first or third",
          "Direction_30":"Action_030",  "comment_010":" == 7",
          "Direction_1000":"Action_9000",  "comment_010":"The end of array"
      },
      "Action_020":{
          "_agent_position":{
              "en-US":"The v-agent is skipping the current element of array",
              "ru-RU":"v-agent пропускает текущий элемент массива"
          },
          "_action_description":{
              "comment_010":"empty"
          },
          "Direction_10":"Action_010",  "comment_010":" > 0 and int and (first or third)",
          "Direction_20":"Action_020",  "comment_010":" <= 0 or not int or not first or third",
          "Direction_30":"Action_030",  "comment_010":" == 7",
          "Direction_1000":"Action_9000",  "comment_010":"The end of array"
      },   
      "Action_030":{
          "_agent_position":{
              "en-US":"The v-agent is skipping the current element of array after met the element of array equal 7",
              "ru-RU":"v-агент пропускает текущий элемент массива после того, как встретил элемент массива, равный 7"
          },
          "_action_description":{
              "comment_010":"empty"
          },
          "Direction_10":"Action_030",  "comment_010":" > 0 and int and (first or third)",
          "Direction_20":"Action_030",  "comment_010":" <= 0 or not int or not first or third",
          "Direction_30":"Action_030",  "comment_010":" == 7",
          "Direction_1000":"Action_9000",  "comment_010":"The end of array"
      },
      "Action_9000":{
          "_agent_position":{
              "en-US":"The v-agent found the end of array",
              "ru-RU":"v-agent нашел конец массива"
          },
          "_action_description":{
              "comment_010":"empty"
          },
          "Direction_10":"Action_END",  "comment_010":" > 0 and int and (first or third)",
          "Direction_20":"Action_END",  "comment_010":" <= 0 or not int or not first or third",
          "Direction_30":"Action_END",  "comment_010":" == 7",
          "Direction_1000":"Action_END",  "comment_010":"The end of array"
      }
    }

    return va_script
~~~

Тут мы приходим к моменту когда надо вспомнить знаменитый афоризм - "Нет ничего практичнее хорошей теории"
Смотрите! Мы добавили всего одно новое направление и одно новое действие
"Direction_40":"Action_040",  "comment_010":" == 777",
И все заработало.
Правда, добавление "Action_005" и "Action_050" это своего рода искусство и на так очевидно, но всему можно научиться в этой новой парадигме.
Обычно уже после третьего занятия, когда студенты паралельно выполняют требования Заказчика обычным путем и с VAOP к ним приходит озарение и ответ на вопрос - Зачем?

Я что-то увлекся и забыл про боты, хотя с ними такая же ситуация и здесь много общего. Ведь в ботах так же надо реагировать на ответы, которые тоже своего рода элементы массива и никогда не знаешь какой следующий. Причем, каждый ответ пользователя может по-разному пониматься в зависимости от последнего дейстия (Action) в которое выполнил Va-engine или бот, как Вам удобнее это называть в контексте этой статьи
Va-движку (Va-engine) все равно кто в нем едет бот или приложение для подсчета суммы всяких там эмелентов массива по самым замысловатым правилам, которые могут прийти в голову Заказчику.

Va-engine легко переписывается на любом языке программирования. 
На pyton и php есть работвющие реализации Va-engine. 
Я консультировал как прикрутить VAOP к написанию ботов первый раз и парень писал на php, но это нисколько не мешало, потому что идеи важнее структур, в общем смысле и я, просто передал ему ключевые моменты для реализации VAOP в среде php для телеграма. Параллельно с ним я, как всегда увлекся и реализовал все в это в python.
Лечение первого пострадавшего при работы над ботом, показало мне, что нужно немного изменить, подпилить Va-engine для ботов, добавить модули VaData, VaConfig и VaConfigLocal для реализации, придуманной мною,  "Three dots notation in va-variable names" и выделить новый модуль directionDetector для определения направления (Direction) при Va-script (type B). Как известно, при реализации Va-script (type А) направление (Direction) определяется в каждом действии (Action) самостоятельно.

```python
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
```

Для облегчения написания ботЧатРулеток пришлось внести незначительные изменения в организацию данных в Va-engine, что теперь позволяет вызывать его из различный действий и там запускать свои сценарии и даже рекурсивно.

Я думаю, что этого вполне достаточно на сейчас. Постараюсь, если будет заинтерисованность, раскрыть некоторые моменты в следующих публикациях и поделиться кодом решений если у кого-то возникнут вопросы. У меня есть продвинутые ученики и наша команда готова оказывать консультационные увлуги


