from tarfile import PAX_FIELDS
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

#----------------------cor-------------------------
cor1 = '#022a3b' #Azul
cor2 = '#39634e' #Verde
cor3 = '#e3e3e3'
cor4 = '#076b0e'

#--------------------janela------------------------
janela = Tk()
janela.title( 'Calagem' )
janela.configure(bg=cor1)
janela.geometry("1290x725")

#--------------------frames------------------------
frame_cima = Frame(janela, width=1280, height=50, bg=cor2,pady=0, padx=3, relief='flat')
frame_cima.place(x=2, y=2)

frame_esquerda = Frame(janela, width=350, height=665, bg=cor2,pady=0, padx=3, relief='flat')
frame_esquerda.place(x=2, y=55)

frame_direita_cima = Frame(janela, width=925, height=330, bg=cor2,pady=0, padx=3, relief='flat')
frame_direita_cima.place(x=357, y=55)

frame_direita_baixo = Frame(janela, width=925, height=330, bg=cor2,pady=0, padx=3, relief='flat')
frame_direita_baixo.place(x=357, y=390)

#--------------------Frame cima--------------------
l_app_nome = Label(frame_cima, text='Calculadora de Adubação', height=1,padx=0, relief='flat', anchor='center', font=('Ivyy 15 bold'), bg=cor2, fg=cor3)
l_app_nome.place(x=500, y=2)

#-----------------Frame esquerda--------------------
l_elementos = Label(frame_esquerda, text='Elementos', width=20, height=1, padx=0,pady=3, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor4, fg=cor3)
l_elementos.place(x=2, y=2)

l_cmolcdm3 = Label(frame_esquerda, text='(cmolc/dm3)', width=10, height=1, padx=0,pady=3, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor4, fg=cor3)
l_cmolcdm3.place(x=205, y=2)

e_Ca = Entry(frame_esquerda, width=10, font=('Ivy 12 bold'), justify='center', relief=SOLID)
e_Ca.place(x=210, y=32)

l_Ca = Label(frame_esquerda, text='Ca', width=20, height=1, padx=0,pady=3, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor4, fg=cor3)
l_Ca.place(x=2, y=32)

e_Mg = Entry(frame_esquerda, width=10, font=('Ivy 12 bold'), justify='center', relief=SOLID)
e_Mg.place(x=210, y=62)

l_Mg = Label(frame_esquerda, text='Mg', width=20, height=1, padx=0,pady=3, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor4, fg=cor3)
l_Mg.place(x=2, y=62)

e_K = Entry(frame_esquerda, width=10, font=('Ivy 12 bold'), justify='center', relief=SOLID)
e_K.place(x=210, y=92)

l_K = Label(frame_esquerda, text='K', width=20, height=1, padx=0,pady=3, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor4, fg=cor3)
l_K.place(x=2, y=92)

e_Al = Entry(frame_esquerda, width=10, font=('Ivy 12 bold'), justify='center', relief=SOLID)
e_Al.place(x=210, y=122)

l_Al = Label(frame_esquerda, text='Al', width=20, height=1, padx=0,pady=3, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor4, fg=cor3)
l_Al.place(x=2, y=122)

e_AlH = Entry(frame_esquerda, width=10, font=('Ivy 12 bold'), justify='center', relief=SOLID)
e_AlH.place(x=210, y=152)

l_AlH = Label(frame_esquerda, text='Al+H', width=20, height=1, padx=0,pady=3, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor4, fg=cor3)
l_AlH.place(x=2, y=152)

e_fosforo = Entry(frame_esquerda, width=10, font=('Ivy 12 bold'), justify='center', relief=SOLID)
e_fosforo.place(x=210, y=182)

l_fosforo = Label(frame_esquerda, text='Fósforo (mg/dm3)', width=20, height=1, padx=0,pady=3, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor4, fg=cor3)
l_fosforo.place(x=2, y=182)

e_Argila = Entry(frame_esquerda, width=10, font=('Ivy 12 bold'), justify='center', relief=SOLID)
e_Argila.place(x=210, y=212)

l_Argila = Label(frame_esquerda, text='Teor de argila (%)', width=20, height=1, padx=0,pady=3, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor4, fg=cor3)
l_Argila.place(x=2, y=212)

janela.mainloop()