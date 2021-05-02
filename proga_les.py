from tkinter import *
from tkinter.ttk import *  # для combobox
from tkinter.filedialog import *  # для askopenfilename
import fileinput  # для fileinput.fileinput
import os, sys, stat
from datetime import datetime
from tkinter.messagebox import *

target_dir_TXT = 'Result_TXT'
if not os.path.exists(target_dir_TXT):
    os.mkdir(target_dir_TXT)  # создание каталога Result_TXT
    print('Каталог успешно создан', target_dir_TXT)
else:
    print("Каталог " + target_dir_TXT + " уже есть")

target_dir_PNG = 'Result_PNG'
if not os.path.exists(target_dir_PNG):
    os.mkdir(target_dir_PNG)  # создание каталога Result_TXT
    print('Каталог успешно создан', target_dir_PNG)
else:
    print("Каталог " + target_dir_PNG + " уже есть")

root = Tk()

root.minsize(width=700, height=740)
root.title('Лесорубы')

spisokigrok = ["03_Волков", "09_Кашуба", "11_Сулик", "13_Николаев",
               "15_Агафонов", "16_Хохлов", "17_Стовпяга", "24_Селиванов",
               "25_Владимиров", "26_Цюк", "27_Ключников", "28_Талан",
               "33_Пантелеев", "35_Шастин", "56_Петрищев", "59_Волков ст.",
               "64_Ерюшкин", "77_Гребнев", "78_Смовж", "79_Гурин",
               "81_Тараканов", "85_Лукоянов", "87_Тихонов", "97_Рейнский"]

spisokigrokFIO = ["Волков", "Кашуба", "Сулик", "Николаев",
                  "Агафонов", "Хохлов", "Стовпяга", "Селиванов",
                  "Владимиров", "Цюк", "Ключников", "Талан",
                  "Пантелеев", "Шастин", "Петрищев", "Волков ст.",
                  "Ерюшкин", "Гребнев", "Смовж", "Гурин", "Тараканов",
                  "Лукоянов", "Тихонов", "Рейнский"]

spisokkomand = ["Триумф-2", "ХК Гроза", "Оккервиль", "Легион 98",
                "Балткомплект-2", "Лидер Трак"]

spisoktipmatch = ["Товарняк", "Кубок Старт 2016"]

spisokcount = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

spisokarena = ["Домашка", "Коховского"]

spisokyear = [2016]

##spisokmonth = ["Январь", "Февраль", "Март","Апрель","Май","Июнь","Июль",
##               "Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]

spisokmonth = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

spisokday = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", 11, 12, 13, 14,
             15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

spisokgol = [1, 2, 3]
##
##spisoklab=[lab03, lab09, lab11, lab13, lab15,
##           lab16, lab17, lab24, lab25, lab26,
##           lab27, lab28, lab33, lab35, lab56,
##           lab59, lab64, lab77, lab78, lab79,
##           lab81, lab85, lab87, lab97]


# объявление имен игроков 
fontsize = "Arial 11"
lab03 = Label(root, text="03_Волков", font=fontsize)
lab09 = Label(root, text="09_Кашуба", font=fontsize)
lab11 = Label(root, text="11_Сулик", font=fontsize)
lab13 = Label(root, text="13_Николаев", font=fontsize)
lab15 = Label(root, text="15_Агафонов", font=fontsize)
lab16 = Label(root, text="16_Хохлов", font=fontsize)
lab17 = Label(root, text="17_Стовпяга", font=fontsize)
lab24 = Label(root, text="24_Селиванов", font=fontsize)
lab25 = Label(root, text="25_Владимиров", font=fontsize)
lab26 = Label(root, text="26_Цюк", font=fontsize)
lab27 = Label(root, text="27_Ключников", font=fontsize)
lab28 = Label(root, text="28_Талан", font=fontsize)
lab33 = Label(root, text="33_Пантелеев", font=fontsize)
lab35 = Label(root, text="35_Шастин", font=fontsize)
lab56 = Label(root, text="56_Петрищев", font=fontsize)
lab59 = Label(root, text="59_Волков ст.", font=fontsize)
lab64 = Label(root, text="64_Ерюшкин", font=fontsize)
lab77 = Label(root, text="77_Гребнев", font=fontsize)
lab78 = Label(root, text="78_Смовж", font=fontsize)
lab79 = Label(root, text="79_Гурин", font=fontsize)
lab81 = Label(root, text="81_Тараканов", font=fontsize)
lab85 = Label(root, text="85_Лукоянов", font=fontsize)
lab87 = Label(root, text="87_Тихонов", font=fontsize)
lab97 = Label(root, text="97_Рейнский", font=fontsize)

var03 = IntVar()
var09 = IntVar()
var11 = IntVar()
var13 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
var28 = IntVar()
var33 = IntVar()
var35 = IntVar()
var56 = IntVar()
var64 = IntVar()
var77 = IntVar()
var78 = IntVar()
var79 = IntVar()
var85 = IntVar()
var87 = IntVar()
var97 = IntVar()
var59 = IntVar()
var81 = IntVar()

spisokvar = [var03.get(), var09.get(), var11.get(), var13.get(),
             var15.get(), var16.get(), var17.get(), var24.get(),
             var25.get(), var26.get(), var27.get(), var28.get(),
             var33.get(), var35.get(), var56.get(), var59.get(),
             var64.get(), var77.get(), var78.get(), var79.get(),
             var81.get(), var85.get(), var87.get(), var97.get()]

ch03 = Checkbutton(root, variable=var03, onvalue=1, offvalue=0)
ch09 = Checkbutton(root, variable=var09, onvalue=1, offvalue=0)
ch11 = Checkbutton(root, variable=var11, onvalue=1, offvalue=0)
ch13 = Checkbutton(root, variable=var13, onvalue=1, offvalue=0)
ch15 = Checkbutton(root, variable=var15, onvalue=1, offvalue=0)
ch16 = Checkbutton(root, variable=var16, onvalue=1, offvalue=0)
ch17 = Checkbutton(root, variable=var17, onvalue=1, offvalue=0)
ch24 = Checkbutton(root, variable=var24, onvalue=1, offvalue=0)
ch25 = Checkbutton(root, variable=var25, onvalue=1, offvalue=0)
ch26 = Checkbutton(root, variable=var26, onvalue=1, offvalue=0)
ch27 = Checkbutton(root, variable=var27, onvalue=1, offvalue=0)
ch28 = Checkbutton(root, variable=var28, onvalue=1, offvalue=0)
ch33 = Checkbutton(root, variable=var33, onvalue=1, offvalue=0)
ch35 = Checkbutton(root, variable=var35, onvalue=1, offvalue=0)
ch56 = Checkbutton(root, variable=var56, onvalue=1, offvalue=0)
ch64 = Checkbutton(root, variable=var64, onvalue=1, offvalue=0)
ch77 = Checkbutton(root, variable=var77, onvalue=1, offvalue=0)
ch78 = Checkbutton(root, variable=var78, onvalue=1, offvalue=0)
ch79 = Checkbutton(root, variable=var79, onvalue=1, offvalue=0)
ch85 = Checkbutton(root, variable=var85, onvalue=1, offvalue=0)
ch87 = Checkbutton(root, variable=var87, onvalue=1, offvalue=0)
ch97 = Checkbutton(root, variable=var97, onvalue=1, offvalue=0)
ch59 = Checkbutton(root, variable=var59, onvalue=1, offvalue=0)
ch81 = Checkbutton(root, variable=var81, onvalue=1, offvalue=0)

sop = StringVar()
score = StringVar()
score1 = StringVar()
data = StringVar()

now = datetime.now()
d0 = now.strftime("%Y.%m.%d")

namePNG = "Result_PNG/" + str(d0) + "_" + str(sop.get()) + ".png"

var1 = IntVar()


##rad0 = Radiobutton(root,text="Дома",variable=var1,value=1)
##rad1 = Radiobutton(root,text="В гостях", variable=var1,value=2)
##rad3 = Radiobutton(root,text="Товарняк", variable=var2,value="Товарняк")
##rad4 = Radiobutton(root,text="Кубок", variable=var2,value="Кубок Старт 2016")

def savePNG(event):
    print("Файл PNG создан и сохранен")
    target_dir_PNG = 'Result_PNG'
    if not os.path.exists(target_dir_PNG):
        os.mkdir(target_dir_PNG)  # создание каталога Result_PNG
        print('Каталог успешно создан', target_dir_PNG)
        f_PNG = open(namePNG)
        print("Файл PNG создан и сохранен")


def saveTXT(event):
    i = 0
    j = 0
    sum1 = 0
    spisokvar = [var03.get(), var09.get(), var11.get(), var13.get(),
                 var15.get(), var16.get(), var17.get(), var24.get(),
                 var25.get(), var26.get(), var27.get(), var28.get(),
                 var33.get(), var35.get(), var56.get(), var59.get(),
                 var64.get(), var77.get(), var78.get(), var79.get(),
                 var81.get(), var85.get(), var87.get(), var97.get()]

    spisokpenalty = [penalty03.get(), penalty09.get(), penalty11.get(), penalty13.get() \
        , penalty15.get(), penalty16.get(), penalty17.get(),
                     penalty24.get(),
                     penalty25.get(), penalty26.get(), penalty27.get(), penalty28.get(),
                     penalty33.get(), penalty35.get(), penalty56.get(), penalty59.get(),
                     penalty64.get(), penalty77.get(),
                     penalty78.get(), penalty79.get(),
                     penalty81.get(), penalty85.get(),
                     penalty87.get(), penalty97.get()]

    nameTXT = "Result_TXT/" + str(menuyear.get()) + "_" + \
              str(menumonth.get()) + "_" + str(menuday.get()) + "_" + \
              str(menukomand.get()) + ".txt"
    sumgol = gol03.get() + gol09.get() + gol11.get() + gol13.get() \
             + gol15.get() + gol16.get() + gol17.get() + \
             gol24.get() + \
             gol25.get() + gol26.get() + gol27.get() + gol28.get() + \
             gol33.get() + gol35.get() + gol56.get() + gol59.get() + \
             gol64.get() + gol77.get() + gol78.get() + gol79.get() + \
             gol81.get() + gol85.get() + gol87.get() + gol97.get()
    spisokgol = [gol03.get(), gol09.get(), gol11.get(), gol13.get() \
        , gol15.get(), gol16.get(), gol17.get(),
                 gol24.get(),
                 gol25.get(), gol26.get(), gol27.get(), gol28.get(),
                 gol33.get(), gol35.get(), gol56.get(), gol59.get(),
                 gol64.get(), gol77.get(), gol78.get(), gol79.get(),
                 gol81.get(), gol85.get(), gol87.get(), gol97.get()]

    if not os.path.exists(nameTXT):
        f = open(nameTXT, "w")
        for g in range(0, 10):
            f = open(nameTXT, "a")
            if g == 0:
                f = open(nameTXT, "a")
                f.write("Тип матча: " + str(menutipmatch.get()) + "\n")
            if g == 1:
                f = open(nameTXT, "a")
                f.write("Соперник: " + str(menukomand.get()) + "\n")
            if g == 2:
                f = open(nameTXT, "a")
                f.write("Счет: " + str(menucount.get()) + ":" +
                        str(menucount2.get()) + "\n")
            if g == 3:
                f = open(nameTXT, "a")
                f.write("Дата Матча: " + str(menuyear.get()) + "_"
                        + str(menumonth.get()) + "_"
                        + str(menuday.get()) + "\n")
            if g == 4:
                f = open(nameTXT, "a")
                f.write("Арена: " + str(menuarena.get()) + "\n")
            if g == 5:
                f = open(nameTXT, "a")
                sum1 = 0
                for ge in spisokvar:
                    if spisokvar[i] == 1:
                        sum1 = sum1 + 1
                    i = i + 1
                f.write("Общее кол-во игроков: " + str(sum1) + "\n")
            if g == 6:
                i = 0
                f = open(nameTXT, "a")
                f.write("Состав: ")
                for gel in spisokvar:
                    if spisokvar[i] == 1:
                        f.write(spisokigrokFIO[i] + ", ")
                    i = i + 1
                f.write("\n")
            if g == 7:
                print("\n" + "Забито шайб: " + str(sumgol) + "\n")
            if g == 8:
                f = open(nameTXT, "a")
                f.write("Шайбы забили: ")
                z = 1
                i = 0
                for zzz in spisokgol:
                    if spisokgol[i] > 0 and spisokvar[i] == 1:
                        f.write(spisokigrokFIO[i] + " - " + str(spisokgol[i]) + ", ")
                        i = i + 1
                        z = z + 1
                    else:
                        i = i + 1
            if g == 9:
                f.write("\n" + "Удаления: ")
                z = 1
                i = 0
                for yyy in spisokpenalty:
                    if spisokpenalty[i] > 0 and spisokvar[i] == 1:
                        f.write(spisokigrokFIO[i] + " - " + str(spisokpenalty[i]) + ", ")
                        i = i + 1
                        z = z + 1
                    else:
                        i = i + 1
        g = g + 1
        f.close()
        os.chmod(nameTXT, stat.S_IREAD)
        print("Файл " + str(menuyear.get()) + "_" + \
              str(menumonth.get()) + "_" + str(menuday.get()) + "_" + \
              str(menukomand.get()) + ".txt создан и сохранен")
    else:
        estprint = "Файл " + str(menuyear.get()) + "_" + \
                   str(menumonth.get()) + "_" + str(menuday.get()) + "_" + \
                   str(menukomand.get()) + ".txt уже есть"
        print(estprint)
        est = Tk()
        labest = Label(est, text=estprint, font="Arial 12").pack()
        Buttonest = Button(est, text="Ok", command=est.destroy).pack()
        makemodal = 1
        if makemodal:
            est.focus_set()
            est.grab_set()
            est.wait_window()


lis = Listbox(root, width=5, height=1)
lisgol = Listbox(root, width=5, height=1)


def provTXT(event):
    print("-" * 50)
    i = 0
    j = 0
    l = 0
    z = 1
    sum1 = 0
    sumgol = 0
    k = 0
    a1 = menucount.get()
    a2 = menucount2.get()
    lis.delete(0, 2)
    lisgol.delete(0, 2)
    spisokvar = [var03.get(), var09.get(), var11.get(), var13.get(),
                 var15.get(), var16.get(), var17.get(), var24.get(),
                 var25.get(), var26.get(), var27.get(), var28.get(),
                 var33.get(), var35.get(), var56.get(), var59.get(),
                 var64.get(), var77.get(), var78.get(), var79.get(),
                 var81.get(), var85.get(), var87.get(), var97.get()]
    spisokgol = [gol03.get(), gol09.get(), gol11.get(), gol13.get() \
        , gol15.get(), gol16.get(), gol17.get(),
                 gol24.get(),
                 gol25.get(), gol26.get(), gol27.get(), gol28.get(),
                 gol33.get(), gol35.get(), gol56.get(), gol59.get(),
                 gol64.get(), gol77.get(), gol78.get(), gol79.get(),
                 gol81.get(), gol85.get(), gol87.get(), gol97.get()]

    spisokpenalty = [penalty03.get(), penalty09.get(), penalty11.get(), penalty13.get() \
        , penalty15.get(), penalty16.get(), penalty17.get(),
                     penalty24.get(),
                     penalty25.get(), penalty26.get(), penalty27.get(), penalty28.get(),
                     penalty33.get(), penalty35.get(), penalty56.get(), penalty59.get(),
                     penalty64.get(), penalty77.get(),
                     penalty78.get(), penalty79.get(),
                     penalty81.get(), penalty85.get(),
                     penalty87.get(), penalty97.get()]

    sumgol = gol03.get() + gol09.get() + gol11.get() + gol13.get() \
             + gol15.get() + gol16.get() + gol17.get() + \
             gol24.get() + \
             gol25.get() + gol26.get() + gol27.get() + gol28.get() + \
             gol33.get() + gol35.get() + gol56.get() + gol59.get() + \
             gol64.get() + gol77.get() + gol78.get() + gol79.get() + \
             gol81.get() + gol85.get() + gol87.get() + gol97.get()
    for g in range(0, 10):
        if g == 0:
            print("Тип матча: " + str(menutipmatch.get()) + "\n")
        if g == 1:
            print("Соперник: " + str(menukomand.get()) + "\n")
        if g == 2:
            print("Счет: " + str(menucount.get()) + ":" +
                  str(menucount2.get()) + "\n")
        if g == 3:
            print("Дата Матча: " + str(menuyear.get()) + "_"
                  + str(menumonth.get()) + "_"
                  + str(menuday.get()) + "\n")
        if g == 4:
            print("Арена: " + str(menuarena.get()))
        if g == 6:
            sum1 = 0
            for ge in spisokvar:
                if spisokvar[i] == 1:
                    sum1 = sum1 + 1
                    i = i + 1
                else:
                    i = i + 1
            print("\n" + "Состав(Общее кол-во игроков - " + str(sum1) + "): ")
            for gel in spisokvar:
                if spisokvar[j] == 1:
                    print(str(z) + ". " + spisokigrokFIO[j])
                    j = j + 1
                    z = z + 1
                else:
                    j = j + 1
        if g == 8:
            print("\n" + "Шайбы забили(Всего забито шайб - " + str(sumgol) + "): ")
            z = 1
            i = 0
            for zzz in spisokgol:
                if spisokgol[i] > 0 and spisokvar[i] == 1:
                    print(str(z) + ". " + spisokigrokFIO[i] +
                          ": " + str(spisokgol[i]))
                    i = i + 1
                    z = z + 1
                else:
                    i = i + 1
        if g == 9:
            print("\n" + "Удаления: ")
            z = 1
            i = 0
            for yyy in spisokpenalty:
                if spisokpenalty[i] > 0 and spisokvar[i] == 1:
                    print(str(z) + ". " + spisokigrokFIO[i] +
                          ": " + str(spisokpenalty[i]))
                    i = i + 1
                    z = z + 1
                else:
                    i = i + 1
    if str(sumgol) == str(menucount.get()):
        print("\n" + "Голы проставны верно")
    else:
        print("\n" + "Забитые голы не проставлены/ не совпадают")
        g = g + 1
    lis.insert(1, str(sum1))
    lisgol.insert(1, str(sumgol))
    print("-" * 50)


spisoksostavchek = [ch03.select(), ch09.select(), ch11.select(),
                    ch13.select(), ch15.select(), ch16.select(),
                    ch17.select(), ch24.select(), ch25.select(),
                    ch26.select(), ch27.select(), ch28.select(),
                    ch33.select(), ch35.select(), ch56.select(),
                    ch64.select(), ch77.select(), ch78.select(),
                    ch79.select(), ch85.select(), ch87.select(),
                    ch97.select(), ch59.select(), ch81.select()]


def openTXT(event):
    spisokigrok = ["03_Волков", "09_Кашуба", "11_Сулик", "13_Николаев",
                   "15_Агафонов", "16_Хохлов", "17_Стовпяга", "24_Селиванов",
                   "25_Владимиров", "26_Цюк", "27_Ключников", "28_Талан",
                   "33_Пантелеев", "35_Шастин", "56_Петрищев", "59_Волков ст.",
                   "64_Ерюшкин", "77_Гребнев", "78_Смовж", "79_Гурин",
                   "81_Тараканов", "85_Лукоянов", "87_Тихонов", "97_Рейнский"]

    spisokigrokFIO = ["Волков", "Кашуба", "Сулик", "Николаев",
                      "Агафонов", "Хохлов", "Стовпяга", "Селиванов",
                      "Владимиров", "Цюк", "Ключников", "Талан",
                      "Пантелеев", "Шастин", "Петрищев", "Волков ст.",
                      "Ерюшкин", "Гребнев", "Смовж", "Гурин", "Тараканов",
                      "Лукоянов", "Тихонов", "Рейнский"]

    ##    spisokentdel=[ent03.delete(0,END),ent09.delete(0,END)]
    ##    spisokentins=[ent03.insert(END,1),ent09.insert(END,1)]

    op = askopenfilename(title='Открыть протокол матча',
                         filetypes=[('TXT files', '*.txt'), ],
                         initialdir='')

    textopenTXT = StringVar()
    for i in fileinput.input(op):
        findtipmatch = i.find("Тип матча: ")
        if not findtipmatch == -1:
            xx = i.strip("Тип матча: ")
            menutipmatch.set(xx)
        findSOP = i.find("Соперник: ")
        if not findSOP == -1:
            zz = i.strip("Соперник: ")
            menukomand.set(zz)
        findcount = i.find("Счет: ")
        if not findcount == -1:
            count = i.split(":")
            menucount.set(count[1])
            menucount2.set(count[2])
        finddata = i.find("Дата Матча: ")
        if not finddata == -1:
            data = i.strip("Дата Матча: ")
            menuyear.set(data[0:4])
            menumonth.set(data[5:7])
            menuday.set(data[8:10])
        findarena = i.find("Арена: ")
        if not findarena == -1:
            yy = i.strip("Арена: ")
            menuarena.set(yy)
        findsostav = i.find("Состав: ")
        if not findsostav == -1:
            sos = i.strip("Состав: ")
            j = 0
            for ddds in range(0, len(spisokigrokFIO)):
                if spisokigrokFIO[0] in sos:
                    ch03.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[1] in sos:
                    ch09.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[2] in sos:
                    ch11.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[3] in sos:
                    ch13.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[4] in sos:
                    ch15.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[5] in sos:
                    ch16.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[6] in sos:
                    ch17.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[7] in sos:
                    ch24.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[8] in sos:
                    ch25.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[9] in sos:
                    ch26.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[10] in sos:
                    ch27.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[11] in sos:
                    ch28.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[12] in sos:
                    ch33.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[13] in sos:
                    ch35.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[14] in sos:
                    ch56.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[15] in sos:
                    ch59.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[16] in sos:
                    ch64.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[17] in sos:
                    ch77.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[18] in sos:
                    ch78.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[19] in sos:
                    ch79.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[20] in sos:
                    ch81.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[21] in sos:
                    ch85.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[22] in sos:
                    ch87.select()
                    j = j + 1
                else:
                    j = j + 1
                if spisokigrokFIO[23] in sos:
                    ch97.select()
                    j = j + 1
                else:
                    j = j + 1
        findgol = i.find("Шайбы забили:")
        if not findgol == -1:
            goll = i.strip("Шайбы забили: ")
            j = 0
            ##            print (goll)
            z = 0
            for xxx in range(0, len(spisokigrokFIO)):

                if spisokigrokFIO[z] in goll:
                    print("7" * 50)
                    findgol = goll.find(spisokigrokFIO[z])
                    print(goll[findgol:])
                    findgol_2 = goll[findgol:]
                    findgol_2 = findgol_2.split(",")
                    findgol_3 = findgol_2[0]
                    print(findgol_3[-2:])
                    ent03.delete(0, END)
                    ent03.insert(END, 1)
                    print()
                    print("8" * 50)
                    if spisokigrokFIO[0] in goll:
                        ent03.delete(0, END)
                        ent03.insert(END, 1)
                    if spisokigrokFIO[1] in goll:
                        ent09.delete(0, END)
                        ent09.insert(END, 1)
                    if spisokigrokFIO[2] in goll:
                        ent11.delete(0, END)
                        ent11.insert(END, 1)
                    if spisokigrokFIO[3] in goll:
                        ent13.delete(0, END)
                        ent13.insert(END, 1)
                    if spisokigrokFIO[4] in goll:
                        ent15.delete(0, END)
                        ent15.insert(END, 1)
                    if spisokigrokFIO[5] in goll:
                        ent16.delete(0, END)
                        ent16.insert(END, 1)
                    if spisokigrokFIO[6] in goll:
                        ent17.delete(0, END)
                        ent17.insert(END, 1)
                    if spisokigrokFIO[7] in goll:
                        ent24.delete(0, END)
                        ent24.insert(END, 1)
                    if spisokigrokFIO[8] in goll:
                        ent25.delete(0, END)
                        ent25.insert(END, 1)
                    if spisokigrokFIO[9] in goll:
                        ent26.delete(0, END)
                        ent26.insert(END, 1)
                    if spisokigrokFIO[10] in goll:
                        ent27.delete(0, END)
                        ent27.insert(END, 1)
                    if spisokigrokFIO[11] in goll:
                        ent28.delete(0, END)
                        ent28.insert(END, 1)
                    if spisokigrokFIO[12] in goll:
                        ent33.delete(0, END)
                        ent33.insert(END, 1)
                    if spisokigrokFIO[13] in goll:
                        ent35.delete(0, END)
                        ent35.insert(END, 1)
                    if spisokigrokFIO[14] in goll:
                        ent56.delete(0, END)
                        ent56.insert(END, 1)
                    if spisokigrokFIO[15] in goll:
                        ent59.delete(0, END)
                        ent59.insert(END, 1)

                    z = z + 1
                else:
                    z = z + 1


##        op.next()
##        op.close()


# отображение ФИО игрока
lab03.place(x=15, y=100)
lab09.place(x=15, y=125)
lab11.place(x=15, y=150)
lab13.place(x=15, y=175)
lab15.place(x=15, y=200)
lab16.place(x=15, y=225)
lab17.place(x=15, y=250)
lab24.place(x=15, y=275)
lab25.place(x=15, y=300)
lab26.place(x=15, y=325)
lab27.place(x=15, y=350)
lab28.place(x=15, y=375)
lab33.place(x=15, y=400)
lab35.place(x=15, y=425)
lab56.place(x=15, y=450)
lab64.place(x=15, y=475)
lab77.place(x=15, y=500)
lab78.place(x=15, y=525)
lab79.place(x=15, y=550)
lab85.place(x=15, y=575)
lab87.place(x=15, y=600)
lab97.place(x=15, y=625)
lab59.place(x=15, y=650)
lab81.place(x=15, y=675)

# по умолчанию  сняты все галочки в поле ИГРА
ch03.deselect()
ch09.deselect()
ch11.deselect()
ch13.deselect()
ch15.deselect()
ch16.deselect()
ch17.deselect()
ch24.deselect()
ch25.deselect()
ch26.deselect()
ch27.deselect()
ch28.deselect()
ch33.deselect()
ch35.deselect()
ch56.deselect()
ch64.deselect()
ch77.deselect()
ch78.deselect()
ch79.deselect()
ch85.deselect()
ch87.deselect()
ch97.deselect()
ch59.deselect()
ch81.deselect()


# снять все галочки в поле ИГРА
def vsegalkis(event):
    ch03.deselect()
    ch09.deselect()
    ch11.deselect()
    ch13.deselect()
    ch15.deselect()
    ch16.deselect()
    ch17.deselect()
    ch24.deselect()
    ch25.deselect()
    ch26.deselect()
    ch27.deselect()
    ch28.deselect()
    ch33.deselect()
    ch35.deselect()
    ch56.deselect()
    ch64.deselect()
    ch77.deselect()
    ch78.deselect()
    ch79.deselect()
    ch85.deselect()
    ch87.deselect()
    ch97.deselect()


# поставить все галочки в поле ИГРА 
def vsegalki(event):
    ch03.select()
    ch09.select()
    ch11.select()
    ch13.select()
    ch15.select()
    ch16.select()
    ch17.select()
    #    ch24.select()
    ch25.select()
    ch26.select()
    ch27.select()
    ch28.select()
    #    ch33.select()
    ch35.select()
    ch56.select()
    ch64.select()
    ch77.select()
    ch78.select()
    ch79.select()
    ch85.select()
    ch87.select()
    ch97.select()


##---------------------------------
##-                               -
##-      *ОБЪЯВЛЕНИЕ*              -
##-                               -
##-                               -
##---------------------------------

# объявление выпадающего меню 
menukomand = Combobox(root, values=spisokkomand, height=7)  # команд
menutipmatch = Combobox(root, values=spisoktipmatch,
                        width=13, height=3)  # тип матча
menucount = Combobox(root, values=spisokcount, width=2, height=11)  # счет_1
menucount2 = Combobox(root, values=spisokcount, width=2, height=11)  # счет_2
menuarena = Combobox(root, values=spisokarena, width=10, height=11)
menuyear = Combobox(root, values=spisokyear, width=4, height=11)
menumonth = Combobox(root, values=spisokmonth, width=2, height=12)
menuday = Combobox(root, values=spisokday, width=2, height=31)

menutipmatch.set("Кубок Старт 2016")
menuarena.set("Домашка")
menuyear.set(2016)

# объявление рамок гол
gol03 = IntVar()
gol09 = IntVar()
gol11 = IntVar()
gol13 = IntVar()
gol15 = IntVar()
gol16 = IntVar()
gol17 = IntVar()
gol24 = IntVar()
gol25 = IntVar()
gol26 = IntVar()
gol27 = IntVar()
gol28 = IntVar()
gol33 = IntVar()
gol35 = IntVar()
gol56 = IntVar()
gol64 = IntVar()
gol77 = IntVar()
gol78 = IntVar()
gol79 = IntVar()
gol85 = IntVar()
gol87 = IntVar()
gol97 = IntVar()
gol59 = IntVar()
gol81 = IntVar()

ent03 = Entry(root, width=2, bd=2, textvariable=gol03)
ent09 = Entry(root, width=2, bd=2, textvariable=gol09)
ent11 = Entry(root, width=2, bd=2, textvariable=gol11)
ent13 = Entry(root, width=2, bd=2, textvariable=gol13)
ent15 = Entry(root, width=2, bd=2, textvariable=gol15)
ent16 = Entry(root, width=2, bd=2, textvariable=gol16)
ent17 = Entry(root, width=2, bd=2, textvariable=gol17)
ent24 = Entry(root, width=2, bd=2, textvariable=gol24)
ent25 = Entry(root, width=2, bd=2, textvariable=gol25)
ent26 = Entry(root, width=2, bd=2, textvariable=gol26)
ent27 = Entry(root, width=2, bd=2, textvariable=gol27)
ent28 = Entry(root, width=2, bd=2, textvariable=gol28)
ent33 = Entry(root, width=2, bd=2, textvariable=gol33)
ent35 = Entry(root, width=2, bd=2, textvariable=gol35)
ent56 = Entry(root, width=2, bd=2, textvariable=gol56)
ent64 = Entry(root, width=2, bd=2, textvariable=gol64)
ent77 = Entry(root, width=2, bd=2, textvariable=gol77)
ent78 = Entry(root, width=2, bd=2, textvariable=gol78)
ent79 = Entry(root, width=2, bd=2, textvariable=gol79)
ent85 = Entry(root, width=2, bd=2, textvariable=gol85)
ent87 = Entry(root, width=2, bd=2, textvariable=gol87)
ent97 = Entry(root, width=2, bd=2, textvariable=gol97)
ent59 = Entry(root, width=2, bd=2, textvariable=gol59)
ent81 = Entry(root, width=2, bd=2, textvariable=gol81)

# объявление рамок передача
peredacha03 = IntVar()
peredacha09 = IntVar()
peredacha11 = IntVar()
peredacha13 = IntVar()
peredacha15 = IntVar()
peredacha16 = IntVar()
peredacha17 = IntVar()
peredacha24 = IntVar()
peredacha25 = IntVar()
peredacha26 = IntVar()
peredacha27 = IntVar()
peredacha28 = IntVar()
peredacha33 = IntVar()
peredacha35 = IntVar()
peredacha56 = IntVar()
peredacha64 = IntVar()
peredacha77 = IntVar()
peredacha78 = IntVar()
peredacha79 = IntVar()
peredacha85 = IntVar()
peredacha87 = IntVar()
peredacha97 = IntVar()
peredacha59 = IntVar()
peredacha81 = IntVar()

ent_peredacha03 = Entry(root, width=2, bd=2, textvariable=peredacha03)
ent_peredacha09 = Entry(root, width=2, bd=2, textvariable=peredacha09)
ent_peredacha11 = Entry(root, width=2, bd=2, textvariable=peredacha11)
ent_peredacha13 = Entry(root, width=2, bd=2, textvariable=peredacha13)
ent_peredacha15 = Entry(root, width=2, bd=2, textvariable=peredacha15)
ent_peredacha16 = Entry(root, width=2, bd=2, textvariable=peredacha16)
ent_peredacha17 = Entry(root, width=2, bd=2, textvariable=peredacha17)
ent_peredacha24 = Entry(root, width=2, bd=2, textvariable=peredacha24)
ent_peredacha25 = Entry(root, width=2, bd=2, textvariable=peredacha25)
ent_peredacha26 = Entry(root, width=2, bd=2, textvariable=peredacha26)
ent_peredacha27 = Entry(root, width=2, bd=2, textvariable=peredacha27)
ent_peredacha28 = Entry(root, width=2, bd=2, textvariable=peredacha28)
ent_peredacha33 = Entry(root, width=2, bd=2, textvariable=peredacha33)
ent_peredacha35 = Entry(root, width=2, bd=2, textvariable=peredacha35)
ent_peredacha56 = Entry(root, width=2, bd=2, textvariable=peredacha56)
ent_peredacha64 = Entry(root, width=2, bd=2, textvariable=peredacha64)
ent_peredacha77 = Entry(root, width=2, bd=2, textvariable=peredacha77)
ent_peredacha78 = Entry(root, width=2, bd=2, textvariable=peredacha78)
ent_peredacha79 = Entry(root, width=2, bd=2, textvariable=peredacha79)
ent_peredacha85 = Entry(root, width=2, bd=2, textvariable=peredacha85)
ent_peredacha87 = Entry(root, width=2, bd=2, textvariable=peredacha87)
ent_peredacha97 = Entry(root, width=2, bd=2, textvariable=peredacha97)
ent_peredacha59 = Entry(root, width=2, bd=2, textvariable=peredacha59)
ent_peredacha81 = Entry(root, width=2, bd=2, textvariable=peredacha81)

# объявление рамок удал
penalty03 = IntVar()
penalty09 = IntVar()
penalty11 = IntVar()
penalty13 = IntVar()
penalty15 = IntVar()
penalty16 = IntVar()
penalty17 = IntVar()
penalty24 = IntVar()
penalty25 = IntVar()
penalty26 = IntVar()
penalty27 = IntVar()
penalty28 = IntVar()
penalty33 = IntVar()
penalty35 = IntVar()
penalty56 = IntVar()
penalty64 = IntVar()
penalty77 = IntVar()
penalty78 = IntVar()
penalty79 = IntVar()
penalty85 = IntVar()
penalty87 = IntVar()
penalty97 = IntVar()
penalty59 = IntVar()
penalty81 = IntVar()

ent_penalty03 = Entry(root, width=2, bd=2, textvariable=penalty03)
ent_penalty09 = Entry(root, width=2, bd=2, textvariable=penalty09)
ent_penalty11 = Entry(root, width=2, bd=2, textvariable=penalty11)
ent_penalty13 = Entry(root, width=2, bd=2, textvariable=penalty13)
ent_penalty15 = Entry(root, width=2, bd=2, textvariable=penalty15)
ent_penalty16 = Entry(root, width=2, bd=2, textvariable=penalty16)
ent_penalty17 = Entry(root, width=2, bd=2, textvariable=penalty17)
ent_penalty24 = Entry(root, width=2, bd=2, textvariable=penalty24)
ent_penalty25 = Entry(root, width=2, bd=2, textvariable=penalty25)
ent_penalty26 = Entry(root, width=2, bd=2, textvariable=penalty26)
ent_penalty27 = Entry(root, width=2, bd=2, textvariable=penalty27)
ent_penalty28 = Entry(root, width=2, bd=2, textvariable=penalty28)
ent_penalty33 = Entry(root, width=2, bd=2, textvariable=penalty33)
ent_penalty35 = Entry(root, width=2, bd=2, textvariable=penalty35)
ent_penalty56 = Entry(root, width=2, bd=2, textvariable=penalty56)
ent_penalty64 = Entry(root, width=2, bd=2, textvariable=penalty64)
ent_penalty77 = Entry(root, width=2, bd=2, textvariable=penalty77)
ent_penalty78 = Entry(root, width=2, bd=2, textvariable=penalty78)
ent_penalty79 = Entry(root, width=2, bd=2, textvariable=penalty79)
ent_penalty85 = Entry(root, width=2, bd=2, textvariable=penalty85)
ent_penalty87 = Entry(root, width=2, bd=2, textvariable=penalty87)
ent_penalty97 = Entry(root, width=2, bd=2, textvariable=penalty97)
ent_penalty59 = Entry(root, width=2, bd=2, textvariable=penalty59)
ent_penalty81 = Entry(root, width=2, bd=2, textvariable=penalty81)

# объявление текста
fontsize0 = "Arial 12"
labSOPERNIK = Label(root, text="Соперник", font=fontsize0)  # текст "Соперник"          
labScore = Label(root, text="Счет", font=fontsize0)  # текст "Счет"
labData = Label(root, text="Дата Матча", font=fontsize0)  # текст "Дата"
lab2dots = Label(root, text=":", font=fontsize0)  # текст ":"
labgame = Label(root, text="Игра", font=fontsize0)  # текст "игры"
labgol = Label(root, text="Гол", font=fontsize0)  # текст "гол"
labperedacha = Label(root, text="Пер.", font=fontsize0)
labpenalty = Label(root, text="Удал.", font=fontsize0)
labarena = Label(root, text="Арена", font=fontsize0)
labtip = Label(root, text="Тип матча", font=fontsize0)  # текст "тип матча"
labspisok = Label(root, text="Лесорубы", font=fontsize0)  # текст "Лесорубы матча"
labarena = Label(root, text="Арена", font=fontsize0)  # текст "Арена"

butPNG = Button(root, text="Сохранить PNG",
                # width=30,height=5,     #ширина и высота
                bg="white", fg="blue")  # цвет фона и надписи
butSAVETXT = Button(root, text="Сохранить TXT ", command=saveTXT)
butOPENTXT = Button(root, text="Открыть TXT ")
butvsegalki = Button(root, text="Поставить")
butvsegalkis = Button(root, text="Снять")
butprov = Button(root, text="Проверить ТХТ")

##---------------------------------
##-                               -
##-      *ПОЛОЖЕНИЯ*              -
##-                               -
##-                               -
##---------------------------------

# отображение чекбокса ИГРА
ch03.place(x=215, y=100)
ch09.place(x=215, y=125)
ch11.place(x=215, y=150)
ch13.place(x=215, y=175)
ch15.place(x=215, y=200)
ch16.place(x=215, y=225)
ch17.place(x=215, y=250)
ch24.place(x=215, y=275)
ch25.place(x=215, y=300)
ch26.place(x=215, y=325)
ch27.place(x=215, y=350)
ch28.place(x=215, y=375)
ch33.place(x=215, y=400)
ch35.place(x=215, y=425)
ch56.place(x=215, y=450)
ch64.place(x=215, y=475)
ch77.place(x=215, y=500)
ch78.place(x=215, y=525)
ch79.place(x=215, y=550)
ch85.place(x=215, y=575)
ch87.place(x=215, y=600)
ch97.place(x=215, y=625)
ch59.place(x=215, y=650)
ch81.place(x=215, y=675)

# положения рамок ввода данных ГОЛ
x_gol = 350
ent03.place(x=x_gol, y=100)
ent09.place(x=x_gol, y=125 + 3)
ent11.place(x=x_gol, y=150 + 3)
ent13.place(x=x_gol, y=175 + 3)
ent15.place(x=x_gol, y=200 + 3)
ent16.place(x=x_gol, y=225 + 3)
ent17.place(x=x_gol, y=250 + 3)
ent24.place(x=x_gol, y=275 + 3)
ent25.place(x=x_gol, y=300 + 3)
ent26.place(x=x_gol, y=325 + 3)
ent27.place(x=x_gol, y=350 + 3)
ent28.place(x=x_gol, y=375 + 3)
ent33.place(x=x_gol, y=400 + 3)
ent35.place(x=x_gol, y=425 + 3)
ent56.place(x=x_gol, y=450 + 3)
ent64.place(x=x_gol, y=475 + 3)
ent77.place(x=x_gol, y=500 + 3)
ent78.place(x=x_gol, y=525 + 3)
ent79.place(x=x_gol, y=550 + 3)
ent85.place(x=x_gol, y=575 + 3)
ent87.place(x=x_gol, y=600 + 3)
ent97.place(x=x_gol, y=625 + 3)
ent59.place(x=x_gol, y=650 + 3)
ent81.place(x=x_gol, y=675 + 3)

# положения рамок ввода данных ПЕРЕДАЧА
x_peredacha = 410
ent_peredacha03.place(x=x_peredacha, y=100)
ent_peredacha09.place(x=x_peredacha, y=125 + 3)
ent_peredacha11.place(x=x_peredacha, y=150 + 3)
ent_peredacha13.place(x=x_peredacha, y=175 + 3)
ent_peredacha15.place(x=x_peredacha, y=200 + 3)
ent_peredacha16.place(x=x_peredacha, y=225 + 3)
ent_peredacha17.place(x=x_peredacha, y=250 + 3)
ent_peredacha24.place(x=x_peredacha, y=275 + 3)
ent_peredacha25.place(x=x_peredacha, y=300 + 3)
ent_peredacha26.place(x=x_peredacha, y=325 + 3)
ent_peredacha27.place(x=x_peredacha, y=350 + 3)
ent_peredacha28.place(x=x_peredacha, y=375 + 3)
ent_peredacha33.place(x=x_peredacha, y=400 + 3)
ent_peredacha35.place(x=x_peredacha, y=425 + 3)
ent_peredacha56.place(x=x_peredacha, y=450 + 3)
ent_peredacha64.place(x=x_peredacha, y=475 + 3)
ent_peredacha77.place(x=x_peredacha, y=500 + 3)
ent_peredacha78.place(x=x_peredacha, y=525 + 3)
ent_peredacha79.place(x=x_peredacha, y=550 + 3)
ent_peredacha85.place(x=x_peredacha, y=575 + 3)
ent_peredacha87.place(x=x_peredacha, y=600 + 3)
ent_peredacha97.place(x=x_peredacha, y=625 + 3)
ent_peredacha59.place(x=x_peredacha, y=650 + 3)
ent_peredacha81.place(x=x_peredacha, y=675 + 3)

# положения рамок ввода данных УДАЛЕНИЯ
x_penalty = 470
ent_penalty03.place(x=x_penalty, y=100)
ent_penalty09.place(x=x_penalty, y=125 + 3)
ent_penalty11.place(x=x_penalty, y=150 + 3)
ent_penalty13.place(x=x_penalty, y=175 + 3)
ent_penalty15.place(x=x_penalty, y=200 + 3)
ent_penalty16.place(x=x_penalty, y=225 + 3)
ent_penalty17.place(x=x_penalty, y=250 + 3)
ent_penalty24.place(x=x_penalty, y=275 + 3)
ent_penalty25.place(x=x_penalty, y=300 + 3)
ent_penalty26.place(x=x_penalty, y=325 + 3)
ent_penalty27.place(x=x_penalty, y=350 + 3)
ent_penalty28.place(x=x_penalty, y=375 + 3)
ent_penalty33.place(x=x_penalty, y=400 + 3)
ent_penalty35.place(x=x_penalty, y=425 + 3)
ent_penalty56.place(x=x_penalty, y=450 + 3)
ent_penalty64.place(x=x_penalty, y=475 + 3)
ent_penalty77.place(x=x_penalty, y=500 + 3)
ent_penalty78.place(x=x_penalty, y=525 + 3)
ent_penalty79.place(x=x_penalty, y=550 + 3)
ent_penalty85.place(x=x_penalty, y=575 + 3)
ent_penalty87.place(x=x_penalty, y=600 + 3)
ent_penalty97.place(x=x_penalty, y=625 + 3)
ent_penalty59.place(x=x_penalty, y=650 + 3)
ent_penalty81.place(x=x_penalty, y=675 + 3)

# положения радиокнопок в окне программы
##rad0.place(x=450,y=35) # "Дома"
##rad1.place(x=450,y=60) # "В гостях"
##rad3.place(x=550,y=35) # "Товарняк"
##rad4.place(x=550,y=60) # "Кубок"

# положения текста в окне программы 
labSOPERNIK.grid(row=0, column=0, padx=20)  # "соперник"
labScore.grid(row=0, column=1, padx=20)  # "СЧЕТ"
labData.place(x=370, y=1)  # "дата матча"
lab2dots.grid(row=1, column=1, padx=20)  # ":"
# labspisok.grid(row=3,column=0,padx=20)   #  Лесорубы
labgame.place(x=203, y=70)  # "игры"
labgol.place(x=343, y=70)  # "гол"
labperedacha.place(x=403, y=70)  # "гол"
labpenalty.place(x=463, y=70)  # "гол"
labtip.place(x=555, y=1)  # "Тип матча"
labarena.place(x=560, y=70)  # "Арена"

# положения кнопок в окне программы
xbutton = 550
butSAVETXT.place(x=xbutton, y=200)  # сохранение TXT
butPNG.place(x=xbutton, y=440)  # о сохранение PNG
butOPENTXT.place(x=xbutton, y=240)  # открыть TXT
butvsegalki.place(x=250, y=100)
butvsegalkis.place(x=260, y=140)
butprov.place(x=xbutton, y=150)  # отображение кнопки сохранение TXT
# tex.grid(row=6,column=2,padx=20,pady=10) # размер окна

# положение выпадающего меню команд
menukomand.grid(row=1, column=0, padx=20)
menutipmatch.place(x=550, y=30)
menucount.place(x=220, y=30)
menucount2.place(x=290, y=30)
menuarena.place(x=550, y=100)
menuyear.place(x=370, y=30)
menumonth.place(x=410, y=30)
menuday.place(x=450, y=30)

# положение окон счетчика всего 
lis.place(x=205, y=705)
lisgol.place(x=340, y=705)

# назначания событий на кнопку
butSAVETXT.bind('<Button-1>', saveTXT)
butOPENTXT.bind('<ButtonRelease-1>', openTXT)
butvsegalki.bind('<Button-1>', vsegalki)
butvsegalkis.bind('<Button-1>', vsegalkis)
butprov.bind('<Button-1>', provTXT)

root.mainloop()
