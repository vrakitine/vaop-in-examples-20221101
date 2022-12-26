# VAOP в примерах: va-calculator-v1.0 на ReactJS

// https://youtube.com/shorts/xbDUdGfPRQY?feature=share

План статьи такой:
<ol>
    <li>
    Сразу дам ссылку на работающий пример, вернее, на va-calculator https://va-calculator.vercel.app/
    </li>
    <li>
    Ссылка на открытый источник кода там есть, но приведу его и в статье: https://github.com/vrakitine/my-app <br/>
    Надо не забыть написать, что это код из 'master' ветки.
    </li>
    <li>
    Понятно, что все эанятые и нервные и сразу хотят все понять, но в коде разбираться не будут. Для них напишу, что в примере есть кнопка 'Show va-trace' и можно проследить перемещение v-agent от Действия к Дейсивию (from Action to Action)
    </li>
    <li>
    Все равно мало, что понятно, поэтому напишу, что с терминологией VAOP можно познакомиться по этой ссылке: https://vaop.notion.site/1312be70852044ef8db1a9863627df62 а, вообще про все найти здесь: https://vaop.notion.site/82c7784f41af4739bf1a185fc4e12bbc
    </li>
    <li>
    После такого вступления напишу, что кальтулятор хоть и "мини", но у него всЁ есть для роста. Добавить новые цифорки и операции не составляет большого труда. С каждой кнопочкой добавляется новый Direction и Action
    </li>
    <li>
    Не забуду подчеркнуть, что весь Алгоритм, которому следует v-agent, записан в va-script. Напомню, что Алгоритм, по определению - это модель Действий . Если надо что-то изменить, то мы, просто, вносим изменения в va-script. В этом случае все (Заказчик, Программист и Компьютер) работают по одному Алгоритму, записанному в одном месте, а именно, в va-script
    </li>
</ol>

<p>
Теперь осталось написать "развернутую" и "нудную" статью, которую почти никто читать не будет. 

О, чуть не забыл про линк на "Статьи и полезный ресурсы" по теме VAOP и eco-programming парадигме программирования: https://vaop.notion.site/d0822e13fd914c3a94da01a97805ca1d 

Продвинутые в ReactJS, обычно, сразу замечают, что такой подход можно использовать при реализиции и других приложений. Будут идеи пишите. Помогу. Понятно, что VAOP - это Mетодология программирования и также как и OOP (Object Oriented Programming) может быть реализована в любых программых средах.

Меня всегда можно найти здесь: https://vaop.notion.site/3de5d8b45f8a4966a39a974f22a93c04

Жду Ваших предложений и замечаний по еще не написанной "большой" статье.

Хочу такую статью опубликовать на vc.ru
Прямо так и будет выглядеть как вы видите. Рассуждения на тему будущей статьи )

https://vaop.notion.site/vc_vaop_react_2022-12-25-97c92cbf425e43018629856c835423b8

Предлагаю теги:
reactjs, react, v-agent, vaop, eco-programming, fsm, xstate