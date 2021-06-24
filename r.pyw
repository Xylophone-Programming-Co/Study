# Xylophone Programming.
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import random
import codecs

try:
    def open_pt():
        global text
        global entry
        tkint =  Toplevel(tk)
        tkint.config(bg = 'white')
        tkint.geometry('300x200')
        entry = Entry(tkint, highlightthickness=0, bd=0, bg = 'orange', font=15)
        text = Label(tkint, font = ('Bahnschrift', 25), bg = 'white')
        okbutton = Button(tkint, text = 'Ok')
        file = filedialog.askopenfilename()
        file = codecs.open(file, 'r', 'utf-8').read()
        exec(file)
    def d():
        global label

        def basa(string, dat):
            var = IntVar()
            var.set(8)
            spin = Spinbox(new_tk, from_=8, to=72, width=5, textvariable=var, bg='orange', fg='black')
            spin.pack()
            btn1 = Button(new_tk, text='OK', command=lambda: txt.config(font=('Consolas', spin.get())), bg='yellow',
                          highlightthickness=0, bd=0)
            btn1.pack()
            label.config(text="Урок %s" % dat)
            txt = Text(new_tk, font=('Consolas', 8), bg='white', highlightthickness=0, bd=0)
            txt.pack(fill=BOTH, expand=YES)
            txt.insert(END, str(string))
            txt.config(state=DISABLED, bg='white')
            scrll = Scrollbar(new_tk, command=txt.yview, bg='yellow', highlightthickness=0, bd=0 )
            txt.configure(yscrollcommand=scrll.set)
            txt.pack(side=LEFT)
            scrll.pack(side=RIGHT, fill=Y)

        def bas(string, dat, gm):

            global epta
            global start
            new_tk.geometry(gm)
            label.config(text='А теперь ты!')
            laboratory = Label(new_tk, text=string, bg='white ')
            laboratory.pack()
            epta = Entry(new_tk, bg='violet', highlightthickness=0, bd=0, font=15)
            epta.pack()
            a = Button(new_tk, text='OK', font=('Candara', 15), bg='yellow', highlightthickness=0, bd=0,
                       command=provery)
            a.pack()
            start = dat

        data = variablef.get()
        new_tk = Toplevel(tk)
        new_tk.config(bg='white')
        new_tk.geometry('700x500')
        label = Label(new_tk, text='[LEVEL xx]', font=('Bahnschrift', 30), bg='white')
        label.pack()
        if data == 'Урок 1':
            basa('''Чтобы умножить сумму на число, нужно каждое слагаемое умножить на это число и полученные результаты сложить.
Это свойство называется распределительным законом умножения относительно сложения.
Пример:
выполним умножение, пользуясь распределительным законом умножения относительно сложения:

59⋅8=(50+9)⋅8=50⋅8+9⋅8=400+72=472.

Умножим число 59 на число 8. Воспользуемся распределительным законом умножения относительно сложения. Каждое слагаемое 50 и 9 по отдельности умножим на число 8. Получим 50⋅8=400 и 9⋅8=72. Сложим эти результаты и получим результат, равный 472.
При умножении числа в столбик знак умножения — точку «⋅» — заменим крестиком «x».
Пример:
796×54420+474.

Умножим число 79 на 6. Запишем эти числа в столбик. Начнём умножать с единиц: 9 единиц умножить на 6, получится 54.
Затем умножаем 7 десятков на 6, получается 42 десятка, то есть 420. Сложив эти результаты в столбик, получим 474.
Запись этого способа умножения можно сократить:

7956×474.

Умножаем 9 единиц на 6, получается 54. Подписываем 4 единицы под единицами, а 5 десятков надписываем над десятками верхнего множителя.
Затем умножаем 7 десятков на 6, получаем 42 десятка. Прибавляем к ним 5 десятков, которые получились от умножения 9 единиц на 6.
Всего получится 47 десятков, которые записываем слева от единиц.

Получаем тот же ответ: значение произведения чисел 79 и 6 равно 474.''', 1)
        elif data == 'Урок 2':
            basa('''Умножение многозначного числа на однозначное выполняется в столбик так же, как и умножение двузначного числа на однозначное.

Умножим число 537 на 4 в столбик. Начинаем умножать с единиц: 7 единиц умножить на 4 — получится 28 единиц. Затем умножаем 3 десятка на 4, получается 12 десятков, то есть 120; 5 сотен умножить на 4 — получится 20 сотен, то есть 2000. Сложив эти результаты в столбик, получим: 2148. Значение произведения чисел 537 и 4 равно 2148. 

Запишем этот способ умножения сокращённо:

×5371242148.   

Умножаем 7 единиц на 4, получается 28 единиц. Подписываем 8 единиц под единицами, а 2 десятка надписываем над десятками верхнего множителя. Теперь умножаем 3 десятка на 4, получается 12 десятков. Прибавляем к ним 2 десятка, которые получены от умножения 7 единиц на 4. Всего получится 14 десятков. Подписываем 4 десятка над десятками, а 1 сотню надписываем над сотнями верхнего множителя. И умножим 5 сотен на 4, получится 20 сотен и ещё 1 сотня, всего 21 сотня. Это число сотен записываем в произведении слева от 4 десятков.

Получаем тот же ответ: значение произведения чисел 537 и 4 равно 2148.''', 2)
        elif data == 'Урок 3':
            basa('''Сравни вычисления. Объясни записи:

2400⋅4=24сот.⋅4=96сот.=9600,

24сот.×496 сот. =2 4 0 0×4     9 6 0 0.

Рассуждай так:

1.  нужно умножить 2400 на 4, или 24 сотни на 4. Поэтому напишу второй множитель 4 под цифрой 4 первого множителя.

2. Умножаю 24 на 4, получаю 96.

3. Помню, что умножали не 24 единицы, а 24 сотни, поэтому переведу результат в единицы. Для этого допишу к полученному числу 96 справа две цифры 0.

4. Читаю ответ: 9600.''', 3)
        elif data == "Урок 4":
            basa('''Сравни вычисления. Объясни записи:

18⋅300=18⋅3сот.=54сот.=5400,

1 8   ×3сот.       5 4 сот.;         1 8       ×300     5 4 0 0.

Рассуждай так:

1. нужно умножить 18 на 300, или 18 на 3 сотни. Поэтому напишу число сотен — 3 — под последней цифрой  первого множителя.

2. Умножаю 18 на 3, получаю 54.

3. Помню, что умножали не 3 единицы, а 3 сотни, поэтому переведу результат в единицы. Для этого допишу к полученному числу 54 справа две цифры 0.

4. Читаю ответ: 5400. 

Обрати внимание!
Очевидно, что при умножении на круглое число с одним нулём к результату будем дописывать один нуль, при умножении на круглое с тремя нулями — три нуля''',
                 4)
        elif data == 'Урок 5':
            basa('''Вспомним основные правила умножения, которые ещё называются переместительным и сочетательным законами умножения.
От перестановки множителей произведение не меняется:
a⋅b=b⋅a.
Два соседних множителя можно заменить их произведением:
a⋅(b⋅с)=(b⋅a)⋅с.
Умножим 160 на 300:
 
160⋅300=(16⋅10)⋅(3⋅100)=(16⋅3)⋅(10⋅100)=(16⋅3)⋅1000=48⋅1000=48000.
 
Можно сделать вывод:
чтобы найти произведение круглых чисел, можно выполнить умножение, не глядя на нули, а затем приписать справа столько нулей, сколько в обоих множителях вместе.
При умножении столбиком это записывается так:
 
160х300=48000.''',5)
        elif data == 'Урок 6':
            basa('''По-разному можно умножить число на сумму:
  
1) 16⋅(2+3)=16⋅5=80 —
 
сначала найти сумму в скобках 2+3=5, а потом число 16 умножить на эту сумму 16⋅5=80.
 
2) 16⋅(2+3)=16⋅2+16⋅3=80 —
 
сначала умножить число на каждое слагаемое 16⋅2=32 и 16⋅3=48, а потом сложить полученные числа 32+48=80.
Пример:
12⋅15=12⋅(10+5)=12⋅10+12⋅5=180,40⋅32=40⋅(30+2)=40⋅30+40⋅2=1280.
58⋅23=58⋅(20+3)=58⋅20+58⋅3=58⋅3+58⋅20.
 
Последнее выражение можно записать так:
 
58x23=174+116=1334
 
Объяснение:
 
Умножим число 58 на число единиц второго числа:
  
58⋅3=174.
 
Первое неполное произведение: 174.
  
Умножим число 58 на число десятков второго числа:
  
58⋅2=116.
 
Второе неполное произведение: 116дес.
 
Сложим два неполных произведения, подписывая второе под десятками первого:
  
174+1160=1334.
  
Ответ: произведение чисел 58 и 23 равно 1334.''', 6 )

        elif data == 'Урок 7':
            basa('''Умножение любого числа на трёхзначное число выполняется так же, как умножение на двузначное число.
Начнём умножать  число на единицы трёхзначного числа, затем на десятки, а потом на сотни. Число десятков, которое получили при умножении, подпишем под десятками, а получившееся число сотен — под сотнями.
573х486=3438+4584+2292=278478
 
 
784х308=6272+0000+2352=241472
 
 Второе неполное произведение (0000) можем не записывать.
 
784х308=6272+2352=241472
 
Умножаем круглое число на трёхзначное так же. Начнём подписывать второй множитель под первым значимым разрядом, который записан цифрой большей, чем 0.
 
36700х413=1101+367+1468=15157100''', 7)
        elif data == 'Урок 8':
            basa('''Деление на однозначное число(к примеру, 24:6) решается по такому принципу:
1. В уме вспоминаем таблицу умножения на указанный делитель(у нас это 6).
2. Ищем в таблице ответ 24.
3. Получаем второй множитель.
4. Записываем второй множитель как частное.
Ответ: 24:6 = 4.''', 8)
        elif data == 'Урок 9':
            basa('''Деление на двухзначное число(возьмём 360:12):
1. Ищем первое неполное делимое(у нас будет 36).
2. Делаем прикидку. 3:1 = 3.
3. Записываем к ответу 3, ведь 36:12 = 3.
4. Сносим 0.
Ответ: 36:12 = 30
Но бывает и посложнее(например 663:13):
1. Ищем первое неполное делимое(у нас будет 66)
2. Делаем прикидку. 6:1 = 6.
3. Так как 13 x 6 = 78, то возьмём по 5. 13 х 5 = 65 👍. Подойдёт!
4. 66 - 65 = 1, внизу подпишите 1, но здесь есть цифра 3, Если их соединить, то получится 13. прибавте к 1 ещё 3.
5. Конечно же, 13 : 13 = 1
Ответ: 663: 13 = 51.''', 9)
        elif data == 'Урок 10':
            basa(
                '''Деление на круглые числа очень простые(после этого урока порешай их в разделе Примеры)
Самые простые примеры типа 100 : 10 или 200:20 и т.д:
1. Убираем столько нулей в делимом, сколько в делителе.
2. Получаем ответ.
⚠НО! ТАКОЙ АЛГОРИТМ ПОДЕЙСТВУЕТ, ЕСЛИ ДЕЛИТЕЛЬ БУДЕТ 10, 100, 1000, 10000, 100000 И Т. Д⚠
Если попадётся 200 : 20, то:
1. Убираем столько нулей в делимом, сколько в делителе. Столько же нулей убираем в делителе и полученный пример решаем.
2. Получаем ответ.
‼НАВЕРНОЕ, ПО ЭТОМУ АЛГОРИТМУ РЕШАЮТСЯ ПРИМЕРЫ ТИПА 200:20‼''',10)

    def vkm():
        global variablef
        toplevel = Toplevel(tk)
        toplevel.geometry('300x300')
        toplevel.config(bg = "white")
        label = Label(toplevel, text = 'Уроки по математике', font = ('Bahnschrift', 15), bg = 'white')
        label.pack()
        option2 = ['Урок 1',
                   "Урок 2",
                   "Урок 3",
                   "Урок 4",
                   'Урок 5',
                   'Урок 6',
                   'Урок 7',
                   'Урок 8',
                   'Урок 9',
                   'Урок 10'


                   ]

        variablef = StringVar(toplevel)
        variablef.set(option2[0])
        w1 = OptionMenu(toplevel, variablef, *option2)
        w1.pack()


        a = Button(toplevel, text='Старт', font=('Candara', 15), bg='yellow', highlightthickness=0, bd=0, command=d)
        a.pack()
    def provery():
        iriska = epta.get()
        if iriska in start:
            label.config(text = 'Правильно 👍!')
        else:
            label.config(text = 'Неправильно 😫!')
    def database():
        global label
        def basa(string, dat):
            var = IntVar()
            var.set(8)
            spin = Spinbox(new_tk, from_=8, to=72, width=5, textvariable=var, bg='orange', fg='black')
            spin.pack()
            btn1 = Button(new_tk, text='OK', command=lambda: txt.config(font=('Consolas', spin.get())), bg='yellow', highlightthickness=0, bd=0 )
            btn1.pack()
            label.config(text="Урок %s" % dat)
            txt = Text(new_tk, font=('Consolas', 8), bg='white', highlightthickness=0, bd=0)
            txt.pack(fill=BOTH, expand=YES)
            txt.insert(END, str(string))
            txt.config(state=DISABLED, bg='white')
            scrll = Scrollbar(new_tk, command=txt.yview, bg='yellow')
            txt.configure(yscrollcommand=scrll.set)
            txt.pack(side=LEFT)
            scrll.pack(side=RIGHT, fill=Y)

        def bas(string, dat, gm):

            global epta
            global start
            new_tk.geometry(gm)
            label.config(text='А теперь ты!')
            laboratory = Label(new_tk, text=string, bg='white')
            laboratory.pack()
            epta = Entry(new_tk, bg='violet', highlightthickness=0, bd=0, font=15)
            epta.pack()
            a = Button(new_tk, text='OK', font=('Candara', 15), bg='yellow', highlightthickness=0, bd=0,
                       command=provery)
            a.pack()
            start = dat

        data = variablef.get()
        new_tk = Toplevel(tk)
        new_tk.config(bg = 'white')
        new_tk.geometry('700x500')
        label = Label(new_tk, text ='[LEVEL xx]', font = ('Bahnschrift', 30), bg = 'white')
        label.pack()
        if data == 'Урок 1':
            basa('''Итак, сегодня мы начнём изучать Python.
Вначале я расскажу, что такое Python. Python - это простой язык программирования. 
С 1 по 10 уроки мы будем изучать Python.
Приступим!
Установка Python. 
Скачайте Python 3(только 3!) c cайта https://www.python.org/getit/
Когда файл скачается, откройте его. Когда он откроется, нажмите Install. Подождите. Затем, когда всё установилось, выберите в меню программу IDLE. 
Установка завершена!Зайди на урок 2(обязательно закрой это окно!)''', 1)
        elif data == 'Урок 2':
            basa('''Ну наконец, мы будем писать функции!
Если вы открыли IDLE, то вы увидете в окне надпись: >>>. Это приветсвие. Вообще, в данном окне нет смысла писать большие программы, так как в нём нельзя сохранить ранее набраный код, но всё равно, для проверок и обучения Python это вполне хорошее окно.
В нём можно получить результат. Напишите print('Hello, world!').
Эта функция(print) нужна для того, чтобы она выводила данные, записанные в скобках и кавычках после неё. Видите результат? Кстати, можно писать и цифры(но без кавычек)!''',
                 2)
        elif data == 'Урок 3':
            basa('''На этом уроке мы будем сохранять файлы. Нажмите в меню File. Нажмите New Window. Напишите: print('Test text').
Нажмите F5. Выйдет окно спрашивая вас: Сохранить и запустить?  Нажмите ОК или Enter. Сохраните ваш файл. Теперь в консоли выйдет наш текст!''',
                 3)
        elif data == "Урок 4":
            basa('''Этот урок будет посвящён  переменным. Переменные - это объекты, хранящие данные. Но как их создать? Очень просто!  Просто напишите название переменной и задайте ему значение(пример: a = 1 ) . Напишите по этому алгоритму значение переменной. Потом напишите print(название вашей переменной).
Но главное: не пишите это в кавычках! Если будет в кавычках, выйдет просто название(Python подумает, что это просто текст). Консоль покажет значение(в переменных можно хранить и другие типы данных, например текст, но он должен быть в кавычках).''',
                 4)
        elif data == 'Урок 5':
            basa('''Этот урок посвящён вводу данных в консоль. За это отвечает функция input(). Создайте файл и создайте переменную i со значением input('Скажите, как вас зовут? ').
А затем print(i). То, что мы вписали в скобках внутри input, это как бы "вопрос". А потом ваши данные сохранятся в переменной i! И с помощью print выводит на экран ваше значение!''',5)
        elif data == 'Вопрос 1':
            bas('''Напиши в консоль текст: 'Я учусь в Решариуме!\'''', ['print(\'Я учусь в Решариуме!\')', 'print("Я учусь в Решариуме!")'], '300x200' )

        elif data == 'Вопрос 2':
            bas('''Какую функцию надо использовать, чтобы запросить данные у пользователя?''', ['input', 'input()'], '450x200' )
        elif data == 'Вопрос 3':
            bas('''Какая программа для разработки входит в пакет Python?''', ['IDLE', 'idle', 'ИДЛЕ', 'идле'], '400x200' )
        elif data == 'Вопрос 4':
            bas('''Какой символ надо использовать, чтобы присвоить переменной "а" значение 1?''', ['=', 'равно', 'Равно'], '470x200' )
        elif data == 'Пролог':
            basa('''Это были уроки по информатике. НО!!! Это самая малость того, что надо изучить. Поэтому советуем прочитать книгу Джейсона Бриггса: \'Python для детей\'. Пока! ''', 'последний')
    def infor():
        global variablef
        toplevel = Toplevel(tk)
        toplevel.geometry('300x300')
        toplevel.config(bg = "white")
        label = Label(toplevel, text = 'Информатика', font = ('Bahnschrift', 15), bg = 'white' )
        label.pack()
        option2 = ['Урок 1',
                   "Урок 2",
                   "Урок 3",
                   "Урок 4",
                   'Урок 5',
                   'Вопрос 1',
                   'Вопрос 2',
                   'Вопрос 3',
                   'Вопрос 4',
                   'Пролог'


                   ]

        variablef = StringVar(toplevel)
        variablef.set(option2[0])
        w1 = OptionMenu(toplevel, variablef, *option2)
        w1.pack()


        a = Button(toplevel, text='Старт', font=('Candara', 15), bg='yellow', highlightthickness=0, bd=0, command=database)
        a.pack()

    def pravilno1():
        try:
            e = int(entry.get())

            if guess_is == e:
                labelerdd.config(text ='Правильно!', font = ('Impact', 25), bg ='white', fg ='green')
            elif guess_is == '':
                labelerdd.config(text='Напиши ответ цифрами или выйди', font=('Impact', 25), bg='orange', fg='green')
            else:
                labelerdd.config(text='Неправильно!', font=('Impact', 25), bg='white', fg='red')
        except:
            labelerdd.config(text='Напиши ответ ЦИФРАМИ или выйди', font=('Impact', 25), bg='white', fg='green')


    def primer2():

        global pr
        global guess_is
        global entry
        global labelerdd
        pr = Toplevel(tk)
        pr.title('Сложение')
        pr.config(bg ='white')
        pr.geometry('520x300')
        guess1 = random.randint(1,100001)
        guess2 = random.randint(1, 100001)

        guess_is = guess1 + guess2
        label = Label(pr, text='%s + %s ' % (guess1, guess2), font = ('Bahnschrift' , 20), bg ='white')
        label.pack()
        entry = Entry(pr, highlightthickness = 0, bd = 0, bg ='orange', font = ('Bahnschrift', 15))
        entry.pack()
        a = Button(pr, text ='Проверим!', font = ('Candara' , 15), bg ='yellow', highlightthickness = 0, bd = 0, command = pravilno1)
        a.pack()
        labelerdd = Label(pr, text='Нажми на кнопку "Проверим!"', font = ('Bahnschrift' , 15), bg ='white')
        labelerdd.pack()

    def umnoz1():
        try:
            e = int(entry1.get())

            if guess_is == e:
                labelers.config( text = 'Правильно!', font = ('Impact', 25), bg = 'white', fg = 'green')
            elif guess_is == '':
                labelers.config(text='Напиши ответ цифрами или выйди', font=('Impact', 25), bg='orange', fg='green')
            else:
                labelers.config( text='Неправильно!', font=('Impact', 25), bg='white', fg='red')
        except:
            labelers.config(text='Напиши ответ ЦИФРАМИ или выйди', font=('Impact', 25), bg='white', fg='green')

    def umnoz2():
        global u
        global guess_is
        global entry1
        global labelers
        u = Toplevel(tk)
        u.title('Умножение')
        u.config(bg ='white')
        u.geometry('520x300')
        guess1 = random.randint(1,10001)
        guess2 = random.randint(1, 101)

        guess_is = guess1 * guess2
        label = Label(u, text='%s x %s ' % (guess1, guess2), font = ('Bahnschrift' , 20), bg ='white')
        label.pack()
        entry1 = Entry(u, highlightthickness = 0, bd = 0, bg ='orange', font = ('Bahnschrift', 15))
        entry1.pack()
        a = Button(u, text ='Проверим!', font = ('Candara' , 15), bg ='yellow', highlightthickness = 0, bd = 0, command = umnoz1)
        a.pack()
        labelers = Label(u, text='Нажми на кнопку "Проверим!"', font = ('Bahnschrift' , 15), bg ='white')
        labelers.pack()

    def vychit1():
        try:
            e = int(entry1.get())

            if guess_is == e:
                labelerd.config( text = 'Правильно!', font = ('Impact', 25), bg = 'white', fg = 'green')
            elif guess_is == '':
                labelerd.config(text='Напиши ответ цифрами или выйди', font=('Impact', 25), bg='orange', fg='green')
            else:
                labelerd.config( text='Неправильно!', font=('Impact', 25), bg='white', fg='red')
        except:
            labelerd.config(text='Напиши ответ ЦИФРАМИ или выйди', font=('Impact', 25), bg='white', fg='green')
    def vychit2():
        global v
        global guess_is
        global entry1
        global labelerd
        v = Toplevel(tk)
        v.title('Вычитание')
        v.config(bg='white')
        v.geometry('520x300')
        guess1 = random.randint(1, 10001)
        guess2 = random.randint(1, 101)
        while guess2 > guess1:
            guess1 = random.randint(1, 10001)
            guess2 = random.randint(1, 101)

        guess_is = guess1 - guess2
        label = Label(v, text='%s - %s ' % (guess1, guess2), font=('Bahnschrift', 20), bg='white')
        label.pack()
        entry1 = Entry(v, highlightthickness=0, bd=0, bg='orange', font=('Bahnschrift', 15))
        entry1.pack()
        a = Button(v, text='Проверим!', font=('Candara', 15), bg='yellow', highlightthickness=0, bd=0, command=vychit1)
        a.pack()
        labelerd = Label(v, text='Нажми на кнопку "Проверим!"', font=('Bahnschrift', 15), bg='white')
        labelerd.pack()
    def deli1():
        try:
            e = int(entryd.get())

            if guess_is == e:
                labelerdd.config( text = 'Правильно!', font = ('Impact', 25), bg = 'white', fg = 'green')
            elif guess_is == '':
                labelerdd.config(text='Напиши ответ цифрами или выйди', font=('Impact', 25), bg='orange', fg='green')
            else:
                labelerdd.config( text='Неправильно!', font=('Impact', 25), bg='white', fg='red')
        except:
            labelerdd.config(text='Напиши ответ ЦИФРАМИ или выйди', font=('Impact', 25), bg='white', fg='green')
    def deli2():
        global pdr
        global guess_is
        global entryd
        global labelerdd
        pdr = Toplevel(tk)
        pdr.title('Деление')
        pdr.config(bg ='white')
        pdr.geometry('520x300')
        guess1 = random.choice([100,1000,10000,100000,1000000,10000000])
        guess2 = random.choice([10,100,1000,10000,100000,1000000])
        try:
            while guess2 > guess1:
                guess1 = random.choice([100, 1000, 10000, 100000, 1000000, 10000000])
                guess2 = random.choice([10, 100, 1000, 10000, 100000, 1000000])
        except TypeError:
            guess1 = random.choice([100, 1000, 10000, 100000, 1000000, 10000000])
            guess2 = random.choice([10, 100, 1000, 10000, 100000, 1000000])
        except:
            messagebox.showerror('О нет!', 'Дом с примерами разваливается! Великую книгу математики смогли спасти! Но надежда на тебя! Открой окно ещё раз! Тогда всё будет в норме!')
        try:
            guess_is = int(guess1 / guess2)
        except:
            if guess1 == None or guess2 == None:

                while guess1 != None or guess2 != None:
                    guess1 = random.shuffle([100, 1000, 10000, 100000, 1000000, 10000000])
                    guess2 = random.shuffle([10, 100, 1000, 10000, 100000, 1000000])
                    guess_is = int(guess1 / guess2)

            print()
        label = Label(pdr, text='%s : %s ' % (guess1, guess2), font = ('Bahnschrift' , 20), bg ='white')
        label.pack()
        entryd = Entry(pdr, highlightthickness = 0, bd = 0, bg ='orange', font = ('Bahnschrift', 15))
        entryd.pack()
        a = Button(pdr, text ='Проверим!', font = ('Candara' , 15), bg ='yellow', highlightthickness = 0, bd = 0, command = deli1)
        a.pack()
        labelerdd = Label(pdr, text='Нажми на кнопку "Проверим!"', font = ('Bahnschrift' , 15), bg ='white')
        labelerdd.pack()
    def primer1():
        global hp
        hp = Toplevel(tk)
        hp.resizable(0,0)
        hp.geometry('300x150')
        hp.config(bg = 'white')
        hp.title('Примеры')
        label = Label(hp, text='Начать!', font = ('Bahnschrift' , 20), bg = 'white')
        label.pack()

        a = Button(hp, text = 'Приступим решать сложение!', font = ('Candara' , 10), bg = 'red',fg = 'white', highlightthickness = 0, bd = 0,command = primer2 )
        a.pack()
        b = Button(hp, text = 'Приступим решать умножение!', font = ('Candara' , 10), bg = 'orange',fg = 'green', highlightthickness = 0, bd = 0,command = umnoz2 )
        b.pack()
        с = Button(hp, text = 'Приступим решать вычитание!', font = ('Candara' , 10), bg = 'magenta',fg = 'white', highlightthickness = 0, bd = 0,command = vychit2 )
        с.pack()
        с = Button(hp, text = 'Приступим решать деление(простые примеры)!', font = ('Candara' , 10), bg = 'cyan',fg = 'green', highlightthickness = 0, bd = 0,command = deli2 )
        с.pack()



    tk = Tk()
    tk.geometry('500x300')
    tk.config(bg = 'white')
    tk.title('Решариум. 4 класс')
    logo_image = PhotoImage(file = 'решариум.gif')
    c = Canvas(tk, width = 99, height = 99)
    c.pack()
    c.create_image(0, 0, image = logo_image, anchor = NW)
    main_label = Label(tk, text = 'Привет!', font = ('Bahnschrift' , 20), bg = 'white')
    main_label.pack()
    other_label = Label(tk, text = 'Ты готов к супер - примерам? Ты ещё можешь  почитать Великую книгу математики!',  bg = 'white')
    other_label.pack()
    menu = Menu(tk)
    item1 = Menu(menu,tearoff = 0 )
    menu.add_cascade(label = 'Решение',   menu=item1)
    item1.add_command(label = 'Примеры', command = primer1)
    ii = Menu(menu, tearoff = 0)
    menu.add_cascade(label='Информатика', menu = ii)
    ii.add_command(label = 'Начать', command = infor )
    item1.add_command(label = 'Уроки по математике', command = vkm)
    i2 = Menu(menu, tearoff = 0)
    menu.add_cascade(label = 'Тесты', menu = i2)
    i2.add_command(label= 'Открыть python - тест...', command = open_pt)
    tk.configure(menu = menu)
    tk.mainloop()


except:
    messagebox.showerror('Ой!', 'Нам очень жаль, если ошибка из-за нашего недоделанного кода! Но всё равно ещё раз ознакомтесь с правилами использования Решариума.')