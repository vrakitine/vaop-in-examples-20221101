
# VAOP как low code инструмент для разработки telegram BOT и не только  
Когда в апреле 2021 года я опубликовал статью на хабре: [Введение в v-agent ориентированное программирование (VAOP)](https://habr.com/ru/post/554014/), в которой сформулировал идеологию и заложил основной понятийный аппарат новой методологии программирования: v-agent, va-script, va-box, action, direction и т.п., то напомнил себе изобретателя радио - Сделал Маркони радио, включил, а слушать то нечего. Наверное подобное происходит со всеми пионерами новых методологий программирования.
> Почитайте, что понимается под [методологиями программирования](https://ru.m.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F)

Еще веселее было с отсутствием тогда убойных примеров применения новой методологии. Тут я, еще раз улыбнулся, вспомнив анекдот про ученого, выступившего на симпозиуме и заявившего, что он изобрел чудо лекарство и осталось только выяснить - от чего же оно лечит?
Нельзя сказать, что VAOP не помогало мне решать проблемы, но они имели локальный характер. Ну кого интересует, например, проблема реализации [алгоритма TTC](https://en.wikipedia.org/wiki/Top_trading_cycle). VAOP очень помог облегчить мои страдания на этом проекте.

И только в декабре 2021 года, благодаря моему внуку Эрику, все узнали как выглядит этот загадочный v-agent:

![v-agent](https://www.vaop.dev/img/v-agent-r.png)

Не знаю как дела у того ученого с его чудо лекарством, но в моем случае, произошло чудо - ко мне обратился парень у которого были проблемы с написанием бота и я, за три часовых сеанса консультаций, облегчил его страдания, причем, больше половины времени ушло у нас на объяснение мне что такое бот и что там вызывает головную боль. Стало очевидно, что головная боль при написании ботов очень хорошо лечится, если сразу начать применять VAOP методологию.
К слову, парень, с которым я писал свой первый VaBot, каким-то образом догадался, прослушав мое видео - (https://youtu.be/6xzn78onzQk) что я именно тот, кто сможет ему помочь. Он, как я понял, перелопатил кучу источников, где хоть что-то говорилось про конечные автоматы. Разобрался во многом и теоретически был подкован, но реализовать на практике не мог. 

Я его успокаивал, что он не один такой, что и я в 1981 году после окончания МИФИ многое знал про Формальные языки, Грамматики, Автоматы из книги заведующего кафедрой «Кибернетики» [Льва Тимофеевича Кузина](https://ru.wikipedia.org/wiki/%D0%9A%D1%83%D0%B7%D0%B8%D0%BD,_%D0%9B%D0%B5%D0%B2_%D0%A2%D0%B8%D0%BC%D0%BE%D1%84%D0%B5%D0%B5%D0%B2%D0%B8%D1%87) "Основы кибернетики. — М.: Энергия, 1973. — 504 с. — 30 000 экз", но мне потребовалось три месяца, чтобы привязать мои знания к решению конкретной задачи и выдолбить все в коде. 

> "Выдолбить" это, в данном случае, не метафора, если вспомнить, что я в 1981 году писал программу для дублирования перфолент и сама программа хранилась на [бумажной перфоленте](https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D1%84%D0%BE%D0%BB%D0%B5%D0%BD%D1%82%D0%B0_(%D0%BD%D0%BE%D1%81%D0%B8%D1%82%D0%B5%D0%BB%D1%8C_%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%B8)).

Это, говорил я, как облака на небе - воды много, но попробуй напейся из них. Его летание в облаках не прошло даром, и для меня. Узнал от него много интересных вещей касательно Конечных Автоматов и всего того нового тумана, который успели напустить вокруг этой замечательно идеи - разбить всю задачу, которую надо запрограммировать на состояния (states) и прыгать от состояния к состоянию. Все понятно и все довольны. На деле, же не все так просто потому, что это совершенно другой подход к программированию, своя парадигма программирования и этому надо учить и учиться.

Кто-то хорошо подметил, что все мы ищем Правильный Ответ на вопрос, а куда важнее найти Правильный Вопрос. Вопрос, ответ на который позволит по новому взглянуть на привычные вещи. Исходя из классического определения Алгорима как модели Действий (Algorithm is model of actions). Я задавал разработчикам программ вопрос - можете ли вы показать Алгоритм который Вы реализуете для решения задачи поставленной Заказчиком. Они не могли его показать. Читая, что я сейчас пишу почти никто не понимает - о чем я спрашиваю, что еще раз говорит о том как далеко стоит описание бизнес задачи от Заказчика и ее конкретной реализации в коде. VAOP как раз и есть ответ на этот вопрос. В этой новой методологии программирования мы как раз и представляем Алгоритм как модель Действий. В VAOP не возникает проблем ответить на вопрос - покажите мне Алгоритм следуя которыму Вы решаете бизнес задачу, поставленную Заказчиком. В VAOP для этого существует Va-script. 

Понятно, что в одной статье всё на объяснишь, но опыт показывает, что уже через несколько занятий с применением VAOP на очень простых примерах, программисты понимают как им повезло, что они узнали об этой новой методологии программирования. Важно понять и согласовать множество моделей методов, которые реализуют данную методологию. Туману напустил много, но без этого нельзя, перед переходом к конкретным примерам. От общего к частному и потом наоборот - в частном учиться находить новые зерна общего подхода таков диалектический путь познания и мы тут не оригинальны.

Еще немного отвлекусь и мы вернемся к ботам. Вот, например, я всегда начинаю свои консультации/лекции по VAOP с решения очень простой задачи - найти сумму положительных элементов массива. Предположим на языке python, обычное решение, которому всех учат, выглядит примерно так:

```python
# Update 010 / Regular code
M = [1,2,7, -5, 1]
sum_01 = 0
for a in M:
  if a > 0:
    sum_01 += a
print(str(sum_01))
```

Код в VAOP для решения этой задачи в тысячу раз длиннее.

> В моих [паблик репозиториях](https://github.com/vrakitine) Вы найдете много примеров применения VAOP. <p>Есть [репозиторий](https://github.com/vrakitine/pyVa_U-010-N_2022-10-18) в котором начинаем решать простенькую задачу, которую постепенно усложняем до тех пор пока не будет очевидны преимущества VAOP:
>- Заказчик попросил: *Найти сумму положительных элементов массива*. Pешение в ветке [Va_U-010-N__r1](https://github.com/vrakitine/pyVa_U-010-N_2022-10-18/tree/Va_U-010-N__r1)
> ![v-agent](https://www.vaop.dev/img/U-950-10__sum_of_greater_than_zero.png)
>- У заказчика новые требования: *В списке могут быть массивы и массивы в массиве и так до неограниченой глубины вложенности*. Pешение в ветке [Va_U-020-N__r1](https://github.com/vrakitine/pyVa_U-010-N_2022-10-18/tree/Va_U-020-N__r1)
>- Заказчик забыл уточнить, что: *В списке могут быть массивы без элементов (пустые)*. Pешение в ветке [Va_U-030-N__r1](https://github.com/vrakitine/pyVa_U-010-N_2022-10-18/tree/Va_U-030-N__r1) 


Напрягаться надо, чтобы понять новую методологию программирования. У любого нормального человека возникает вопрос -  *Зачем такая сложность, когда все решается десятью строчкоми кода?* <p>Так и у моих *студентов* (назовем из так, хотя часто это были довольно крутые программеры) возникал законный вопрос - *Зачем?*
Я говорю им, что в идеале процесс обучения должен быть максимально приближен к тому с чем студент сталкнется в реальности. Поэтому, я предлагаю им сыграть в такую игру-работу. 

Заказчику нужно знать сумму элементов, которые находятся в подсписке, начинающемся и заканчивающемся элементом, равным 777. Элемент, равный 7, останавливает добавление всех последующих элементов в подсписке к общей сумме
 
In array M = [1.4, 777, 5, 4.3, 7, 8, 777, 9,23, 777, 5, 6.5, 777, 3] sum will be equal to 10<p>In array M = [1.4, 777, 2, 4.3, 7, 8, 777, 777, 5, 6.5, 777, 3] sum will be equal to 7<p>In array M = [3, 2, 5.9, 777, 12, 4.76, 2] sum will be equal to 0 

Примеры обычного решения Вы можете вообразить себе сами и они будут у каждого свои.
В VAOP решение будет одно и записать в виде Va-script (type B)

> Для тех, кто хочет узнать в чем отличие сценария (type A) от (type B) скажу, что в публикации ["Введение в v-agent ориентированное программирование"](https://habr.com/ru/post/554014/) для решения этой же задачи используется Va-script (type A) и все выглядит иначе, но методология таже, просто с Va-script (type B), который заточен под парсинг, задача решается намного проще.

~~~python
####################################################################
### VA-script (type B) | Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
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

Тут мы приходим к моменту, когда надо вспомнить знаменитый афоризм - "Нет ничего практичнее хорошей теории"

Смотрите! Мы добавили в сценарий всего одно новое направление и одно новое действие
"Direction_40":"Action_040",  "comment_010":" == 777", и все заработало.

Правда, добавление "Action_005" и "Action_050" это своего рода искусство и не так очевидно, но всему можно научиться в этой новой парадигме.
Обычно уже после третьего занятия, когда студенты параллельно выполняют требования Заказчика обычным путем и с VAOP к ним приходит озарение и ответ на вопрос - Зачем?

Я что-то увлёкся и забыл про боты, хотя с ними такая же ситуация и здесь много общего. Ведь в ботах так же надо реагировать на ответы, которые тоже своего рода элементы массива и никогда не знаешь какой следующий. Причем, каждый ответ пользователя может по-разному пониматься в зависимости от последнего дейстия (Action) , которое выполнил Va-engine или бот, как Вам удобнее это называть в контексте этой статьи.
Va-движку (Va-engine) все равно кто в нем едет: бот или приложение для подсчета суммы всяких там элелентов массива по самым замысловатым правилам, которые могут прийти в голову Заказчику.

В статью на хабре: [Введение в v-agent ориентированное программирование](https://habr.com/ru/post/554014/) читаем:

 > Идеологически v-agent ориентированное программирование - добивается того, чтобы алгоритм был записан в одном месте в виде, понятном всем - (1) заказчикам, (2) програмистам и (3) исполняюшей среде (компьютеру), что улучшает процесс взаимодействия всех при создания программного продукта и, что особенно важно, существенно снижает затраты на этапе поддержания работы и адаптации к изменению внешних условий в Будущем.

Va-engine легко переписывается на любом языке программирования. Самое замечательное, что при этом Va-script остается без изменения. Да, **без изменения остается Алгоритм (Algorithm is model of actions) решения задачи**. Это именно, то о чем я спрашиваю программистов, когда задаю правильный вопрос - а где у Вас Алгоритм? Потому, что в будущем, другому программисту, уже без Вас, придется внести изменения в Алгоритм по просьбе Заказчика. 

В VAOP c этим нет проблем и (1) Заказчик, посмотрев в Va-script, вспомнит, что он хотел сделать и вместе с программистом внесет изменения в сценарий и, потом (2) Программист добавит новые Actions. (3) Va-engine будет выполнять алгоритм, записанный в Va-script. Все происходит как и заложено в идеологии VAOP. Всем троим участникам процесса (1), (2) и (3) все предельно понятно что и как делать.

Как все это происходит без VAOP все хорошо знают. Программа как-то работает, но что она делает уверенности нет ни у кого. Внесения изменений со временем превращают программу в "гроб", который легче закопать и забыть и переписать все заново. С VAOP подходом, превратить программу в "гроб" невозможно. Последнне проверено мною не практике и не раз.

На python и php есть работающие реализации Va-engine. 
Я консультировал как прикрутить VAOP к написанию ботов первый раз и парень, упомянутый в начале публикации, писал на php, но это нисколько не мешало, потому что ***идеи важнее структур***, в общем смысле, конечно. V-agent Oriented Programming (VAOP) также как и Object Oriented Programming (OOP) только идея, подход, своя философия, которая реализуется в разных средах по своему. 
Я, просто, передал ему ключевые моменты, познакомил с философией VAOP, а написать Va-engine в среде php с привязкой для бота в телеграмме не сложно для программиста средней руки. Параллельно с ним я, как всегда, увлекся и реализовал все это в python.

Лечение первого пострадавшего при работы над ботом, показало мне, что нужно немного изменить, подпилить Va-engine для ботов, добавить модули VaData, VaConfig и VaConfigLocal для реализации, придуманной мною,  *"three dots notation in va-variable names"* (об этом будет отдельная статья) и выделить новый модуль directionDetector для определения направления (Direction) при Va-script (type B) и получается отличный low code инструмент для написания ботов. Как известно, при реализации Va-script (type А) направление (Direction) определяется в каждом действии (Action) самостоятельно.

Этот код [[отсюда]](https://github.com/vrakitine/pyVa_U-010-N_2022-10-18/blob/Va_U-010-N__r1/Va_U-010-N/main.py) 

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

Вся реализация Va-engine [[здесь]](https://github.com/vrakitine/pyVa_U-010-N_2022-10-18/tree/Va_U-010-N__r1)

Для облегчения написания ботов-чат-рулеток пришлось внести незначительные изменения в организацию данных в Va-engine, что теперь позволяет вызывать его из различных действий и там запускать свои сценарии и даже рекурсивно.

Я думаю, что этого вполне достаточно для одной статьи. Постараюсь, если будет заинтересованность, раскрыть некоторые моменты в следующих публикациях и поделиться кодом решений, если у кого-то возникнут вопросы. У меня есть продвинутые ученики и наша команда готова оказывать консультационные услуги.

## Вперед в Прошлое или ответы на замечания и рекомендации по еще не опубликованной статье.

Воспользовавшись тем, что есть команды разработчиков и отдельные программисты, которым мы оказали и продолжаем оказывать консультационные услуги по применению VAOP, я разослал им черновик этой статьи. 

Почитаем письмо от программиста, видевшего эту статью такой, какой она была в Прошлом.
Признаюсь, что я многое изменил благодаря этому письму. Большое спасибо Юрию за поддержку.

> Здравствуйте, Валерий!<p>Статью я прочитал на одном дыхании. Легко читается, и думаю, если кто-то уже смотрел Ваше видео и читал [предыдущую статью на хабре](https://habr.com/ru/post/554014/) - должен понять без проблем что здесь происходит и как.<p>Однозначно в конце статьи нужно добавить ссылки на все Ваши репозитории с примерами, чтобы людям было проще искать примеры.<p>Статью кроме хабра рекомендую потом продублировать на какую-то независимую площадку, например на [telegra.ph](https://telegra.ph/), так как не у всех есть доступ к хабру без проксей (да и делиться своей статьей проще, когда она находится на площадке без рекламы)<p>Что касается терминологии и теории - так как по VAOP Вы являетесь единственным источником знания, то отказываться от аналогии в конечных автоматах не стоит. Если мы говорим о состояниях, у Вас они называются например Action, в конечных автоматах - это States - то как раз это важно понимать (мне это нужно было понять). После чего уже можно продолжить искать теорию на ютубе или в гугле. Если же отталкиваться только от Action - то при поиске не получится как-то углубиться в эту тему, и понять почему именно это работает или должно работать.<p>Чтобы например разобраться с тем, как эти состояния работают, и какое доказательство их работоспособности я искал материалы по QA тестированию (что-то вроде этого: https://www.youtube.com/watch?v=kkwHSev7mn4 и книги Тестирование черного ящика Б.Бейзер )и конечных автоматах (по этой теории: https://www.youtube.com/watch?v=SFdE5wjLqqc ).<p>После чего по схеме и примерам из Вашего видео ( https://www.youtube.com/watch?v=6xzn78onzQk ) стало понятно, что необходимо сначала определить входной сигнал, и по этому сигналу переходить в другое состояние, после чего уже выполнять код, который сделает целевую работу и останется в этом состоянии.<p>Сложность, из-за которой я обратился заключалась в том, что я никак не мог понять как мне вычленить эти сигналы, по которым я собирался изменять состояние. В конечном итоге решил составить табличку состояний, и присвоить возможные варианты выходного сигнала из каждого состояния. После чего код заработал как это было необходимо.<p>Но, дальше, через неделю после нашего общения я добавил примерно 50 кнопок. И для каждой кнопки примерно 50 разных вариантов развития событий.<p>Получилось так, что для каждого Action пришлось заполнять 50 Direction. А так как делать это руками мне не хотелось, то я просто составил две таблицы в базе данных, в одной список всех сообщений, в другой - список всех возможных реакций.После чего просто связал их в третей табилице по первычному ключу, что позволило мне гарантировано отработать все возможные варианты (и подправлять их просто в базе, не меняя код), а с другой стороы пропала необходимость постоянно править json файл.<p>Я знаю однозначно, что если бы мне не встретился Ваш материал, то мне пришлось бы либо отказаться от идеи внедрения подобной системы, либо потратить куда больше времени на то, чтобы понять как собрать такой код самостоятельно.<p>Мне не понятен хейт пользователей хабра - они вообще должны быть благодарны, что Вы нашли время чтобы поделиться своим подходом к решению подобных проблем (ведь отметим что пост бесплатный, общедоступный - а времени на его подготовку потрачено не мало).

Прочитали, что Va-script у Юрия записан в виде трех таблицы в базе данных. Отличное решение когда, количество Действий (Action) очень большое. Для наглядности, при небольшом количестве Action можно обойтись одной таблицей. Actions надо поместить в строки, а Направленя движения (Direction) в название полей таблицы. Опыт показывает, что Напралений намного меньше чем узлов в графе алгоритма задачи.

Здесь самое время сказать почему в VAOP вместо привычной пары терминов для Конечных Автоматов - Состояния (state) и Событие (event) я ввел другую пара терминов Действие (action) и Направление (direction) потому, что VAOP это больше про запись алгоритма задачи как модели действий, по определению того, что такое Алгоритм выполнения задачи Заказчика. У нас появляется возможность взглянуть на "конечный автомат" не находясь внутри (state/event), а со стороны, переведя внимание не как, а что он делает (Action/Direction). Увидеть "исполняющего агента (интерпретатор модели)" движущегося от Действия к Действию.

Впервые это гениально сформулировал Дмитрий Понятов в комментарии к моему видео [Бесконечные возможности конечных автоматов | Введение в "eco-programming"](https://www.youtube.com/watch?v=6xzn78onzQk):

> **Dmitry Ponyatov**:
По описанию задачи видится не просто конечный автомат, а более широкий принцип - интерпретация структуры данных. Т.е некий программный агент бегает по структуре данных, описывающей задачу, и выполняет операции, определенные его состоянием, предыщими узлами данных, и потенциально следующими в которые возможен переход. Причем в этом подходе главный цимес отличающий его от конечного автомата - исполняющий агент (интерпретатор модели) может эту структуру менять в рантайме: добавлять типизованные узлы и связи, и перестраивать части исходной структуры.

С этого комментария, можно сказать, началась история VAOP.
Именно некий агент (я назвал его v-agent) бегает по сценарию (Va-script) и выполняет некоторые действия (actions), а после завершения дейстия идет в определенном направлении (direction), в зависимости от которого приступает к выполнению следующего действия и так далее по сценарию.

Юрий правильно советует использовать привычные термины для Конечных Автоматов, а то никто ничего в поиске не найдет. У меня только что появилась идея - может, на время, совместить эти термины и будут термины - ActionState и DirectionEvent. Тут и язычники и ортодоксальные виэйоуписты будут довольны и будут жить в мире вместе развивать новое учение о программировании. Надо над этим подумать и продолжить обсуждение в нашей группе в телеграме


## VAOP в развитии

VAOP применяется на практике, в VAOP community идут обсуждения и это приводит к тому, что появляются новые примочки к Va-engine и новые области, где применение VAOP подхода приводит к неожиданным результатам.

Хочу проанонсировать то, что можно от меня ждать в виде публикаций:

1. Introduction of three dots notation in Va-variables name
1. Updating existing Va-engine to enable recursive self call 
1. Adding a Va-script graphic using the xstate library
1. How Va-trace helps find the similarity of complex nested arrays

Постараюсь сохранить названия как анонсировал, но не обещаю.

Название (1) скорее всего не изменится. Вы можете уже сейчас увидеть о чем все это в примерах в модуле VaData. Хорошая тема курсовой. Надо добавить методы и сделать из этого package для Python и переписать для других сред.

(1) как раз делалось для (2), а второе понадобилось для облегчения написания ботов-чат-рулеток. Да и не только. Можно просто так, без рекурсии в каком-нибудь Действии (Action) одного сценария (Va-script-1) запустить свой Va-engine со своим сценарием (Va-script-2). Пока не делал, но почему такое не может кому-то пригодиться, когда при усложнении сценария есть возможность разбить сценарий на части.

(3) будет о том, как прикрутить xstate визуализацию к Va-script. Красиво получается. Заказчику приятно показать свою работу. Внести изменения в бизнес-сценарий. Прильнуть к монитору и пальчиком тыкать в Action и наглядно объяснять как мы в него попали, по какому Direction и после какого Action. 

(4) Коротко не получится. Скажу только, что родилась у меня эта идея когда я консультировал одну команду разработчиков, прикручивал VAOP к решению задачи "корзина покупателя" (shopping cart). Стандартно все шло с применение Va-script type B, тот же Va-engine (есть ссылки на код в начале статьи), что и для вычисления суммы положительных элементов массива с вложенными массивами, учитывали скидки по замысловатым, маркетинговым правилам. Простая для "type B" задачка и ничего интересного, пока я не обратил внимание на то, что V-agent, бегая по массиву с покупками (сложный массив и массив в массиве и так далее) как бы сканирует его, оставляя следы (Va-trace я эти следы назвал и стал запоминать) и по этим следам можно много узнать о структуре массива.
Это уже тема для хорошего диплома. Думаю на меня выйдут ребята, кто понял о чем это я и в чем тут научная новизна со всеми из этого вытекающими последстиями. 

## Мысли вслух

Первая мысль: Меня тревожит размывание терминологии VAOP:

> v-agent (va), va-script, va-box, va-tools, va-engine, action, direction

Пионерам применения VAOP в среде ReactJS понравилось вместо "engine" использовать "machine". Хорошо, что хоть модули свои formMachine.js и inputMachine.js положили в папку VAOP, чтобы было понятно в какой парадигме они творят.

Вторая мысль: Надо найти время и написать статью "Introduction of eco-programming paradigm". Еще три года назад я сформулировал новую парадигму в [публичном репозитории](https://github.com/vrakitine/eco-programming-paradigm). Многие, использующие VAOP, не знают, что методология программирования, которую они применяют, является одним из практических воплощений eco-programming парадигмы. Как и во всем, по классичесной схеме, имеем три уровня принятия решения. Зачем, Что и Как делать? 

- eco-programming парадигма отвечает на вопрос - Зачем так делать? Какая у Вас цель?

- VAOP методология отвечает на вопрос - Что делать, если решили так зачем-то делать?

- Как делать, если приняли решение, что делать, мы видим уже на процедурном уровне, на реальных примерах реализации Va-engine в данных нам программных средах. 

Хотелось чтобы на вопрос Как отвечало больше методологий программирования. Я думаю, что Человечество, не скоро, но к этому прийдет. Не спросто же так, в последнее время растет спрос на технологии типа low code. Видимо, задумываются над вопросом уменьшения затрат на разработку, поддержание и модификацию программного продукта для работы с новыми данными в новых условиях.


## В заключении

Получилось обо всем по-немногу. Обещал, помню, при обсуждении первой статьи привести примеры применения VAOP. 

Чисто описание примеров - это, вроде, как не для статьи. Можно, просто, вместо статьи дать ссылки на VAOP-проекты в репозитории (смотрите в начале этой статьи), а потом поговорить с теми, у кого будут вопросы, как с Юрием, например, получилось и с другими ребятами.  
 
Я открыт к общению в  [группе в телеграме](https://t.me/evaclick) Мне, серьезно, очень интересно, когда Вы приходите с задачами о которых и я не подозревал и где VAOP может оказаться единственным лекарством и простым способом решения.

Contact us: [[t.me/evaclick](https://t.me/evaclick)]
