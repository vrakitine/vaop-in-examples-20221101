Считая сумму элементов Вы следовали алгоритму-сценарию, прочитанному не в va-script, а в каком-то месте, которое уже устарело. Так часто бывает. Вот и я ошибся и забыл сказать что v-agent суммирует только "comment_010":" > 0 and int and (first or third)" первый и потом каждый третий злетент при условии если они целые и положительные. При этом, очень важно, что если даже он не посчитал первый элемент отрезка потому, что он не целый и меньше нуля или ноль, то va ведет отсчет третьего элемента от этого элемента. Это к вопросу - покажите мне Алгоритм. В VAOP c этим нет проблем и разобраться и поменять при необходимости.
Для сравнения попробуйте понять что и как делается в программах решающих эту задачу заказчика, написанный дедовским подходом. Там, вообще, не понять что и как складывается )
Заказчик может повеселиться и сказать, что если элемент = 0, то его не замечать и не считать первым и не вести от него отсчет каждого третьего.
Вот так и играем со студентами, пока они не понимают как, вообще, раньше писали без VAOP, особено, когда я даю подправить код доугого студента на в VAOP, то первый вопрос - А что этот код делает и как? На что я отвечаю - Спроси разработчика если найдешь и если он вспомнит )
И все приходится переписывать самому с чистого листа. А это ведь лишние затраты ресурсов ...

VAOP подход в целом одинаков, что для ботов, что для других вещей где используют va-script (Type B)
Я уже писал, что реализовал va-engine на Python для телеграм бота.
Приходите в нашу группу, может, кто Вам и поможет или мне понравится Ваш бот и я его сам помогу Вам реализовать в VAOP

> Так что будем править, постановку задачи или примеры?

Отвечая на Ваш вопрос, ничего не будем править ) Будем считать это проверкой на мнимательность чтения статьи. Я часто использую такой прмем при чтении лекций - заявляю одно, а код пишу про другое ) и смотрю на реакцию студентов ). Это типа обратной связи такой ... все уснули или не все )