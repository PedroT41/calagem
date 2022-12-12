from tarfile import PAX_FIELDS
from tkinter import *
from tkinter import ttk


#----------------------cor-------------------------
cor1 = '#251D3A' #Roxo/escuro
cor2 = '#2A2550' #Roxo/claro
cor3 = '#25502A' #laranja/forte
cor4 = '#FF7700' #Laranja/fraco
cor5 = '#502A25'

#--------------------janela------------------------
janela = Tk()
janela.title( 'Calagem' )
janela.configure(bg=cor1)
janela.geometry("855x405+60+60")

#--------------------calculos----------------------

def calcular(op):
    global resposta, e_Ca, e_Mg, e_K, e_AlH, e_P, e_v2, e_PRNT, x, t, v1

    try:
        float(e_Ca.get())
        float(e_Mg.get())
        float(e_K.get())
        float(e_AlH.get())
        float(e_P.get())
        float(e_v2.get())
        float(e_PRNT.get())

        if op == 1:
            t = float(e_Ca.get()) + float(e_Mg.get()) + float(e_K.get()) + float(e_AlH.get())
            v1 = ((float(e_Ca.get()) + float(e_Mg.get()) + float(e_K.get()))*100) / t
            x = (float(e_v2.get()) - v1)*t/ float(e_PRNT.get())

        elif op == 2:
            e_Ca.delete(0, END)
            e_Mg.delete(0, END)
            e_K.delete(0, END)
            e_AlH.delete(0, END)
            e_P.delete(0, END)
            e_v2.delete(0, END)
            e_PRNT.delete(0, END)
            x= 0

        return resposta.config(text=round(x))

    except ValueError:
        resposta.config(text="Só Numeros")

#--------------------frames------------------------
frame_cima = Frame(janela, width=855, height=50, bg=cor2,pady=0, padx=3, relief='flat')
frame_cima.place(x=2, y=2)

frame_esquerda = Frame(janela, width=350, height=350, bg=cor2,pady=0, padx=3, relief='flat')
frame_esquerda.place(x=2, y=55)

frame_direita = Frame(janela, width=500, height=350, bg=cor2,pady=0, padx=3, relief='flat')
frame_direita.place(x=357, y=55)

#--------------------Frame cima--------------------
l_app_nome = Label(frame_cima, text='Calculadora de Adubação', height=1,padx=0, relief='flat',justify=CENTER, anchor='center', font=('Ivyy 15 bold'), bg=cor2, fg=cor4)
l_app_nome.place(x=275, y=2)

#-----------------Frame esquerda--------------------
l_elementos = Label(frame_esquerda, text='Elementos', width=20, height=1, padx=0,pady=3, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor3, fg=cor4)
l_elementos.place(x=2, y=2)

l_cmolcdm3 = Label(frame_esquerda, text='(cmolc/dm3)', width=10, height=1, padx=0,pady=3, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor3, fg=cor4)
l_cmolcdm3.place(x=205, y=2)

e_Ca = Entry(frame_esquerda, width=10, font=('Ivy 12 bold'), justify='center', relief=SOLID, fg=cor1)
e_Ca.place(x=210, y=32, height=25)

l_Ca = Label(frame_esquerda,   text='Ca', width=20, height=1, padx=0,pady=3, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor3, fg=cor4)
l_Ca.place(x=2, y=32)

e_Mg = Entry(frame_esquerda, width=10, font=('Ivy 12 bold'), justify='center', relief=SOLID, fg=cor1)
e_Mg.place(x=210, y=62, height=25)

l_Mg = Label(frame_esquerda, text='Mg', width=20, height=1, padx=0,pady=3, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor3, fg=cor4)
l_Mg.place(x=2, y=62)

e_K = Entry(frame_esquerda,   width=10, font=('Ivy 12 bold'), justify='center', relief=SOLID, fg=cor1)
e_K.place(x=210, y=92, height=25)

l_K = Label(frame_esquerda, text='K', width=20, height=1, padx=0,pady=3, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor3, fg=cor4)
l_K.place(x=2, y=92)

e_AlH = Entry(frame_esquerda, width=10, font=('Ivy 12 bold'), justify='center', relief=SOLID, fg=cor1)
e_AlH.place(x=210, y=122, height=25)

l_AlH = Label(frame_esquerda, text='Al+H', width=20, height=1, padx=0,pady=3, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor3, fg=cor4)
l_AlH.place(x=2, y=122)

e_P = Entry(frame_esquerda, width=10, font=('Ivy 12 bold'), justify='center', relief=SOLID, fg=cor1)
e_P.place(x=210, y=152, height=25)

l_P = Label(frame_esquerda, text='Fósforo (mg/dm3)', width=20, height=1, padx=0,pady=3, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor3, fg=cor4)
l_P.place(x=2, y=152)

e_v2 = Entry(frame_esquerda, width=10, font=('Ivy 12 bold'), justify='center', relief=SOLID, fg=cor1)
e_v2.place(x=210, y=182, height=25)

l_Saturação_desejada = Label(frame_esquerda, text='Saturação desejada (%)', width=20, height=1, padx=0,pady=3, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor3, fg=cor4)
l_Saturação_desejada.place(x=2, y=182)

e_PRNT = Entry(frame_esquerda, width=10, font=('Ivy 12 bold'), justify='center', relief=SOLID, fg=cor1)
e_PRNT.place(x=210, y=212, height=25)

l_PRNT = Label(frame_esquerda, text='PRNT (%)', width=20, height=1, padx=0,pady=3, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor3, fg=cor4)
l_PRNT.place(x=2, y=212)

resposta_titulo = Label(frame_direita, text="Quantidade de calcario(t.ah)", height=1,padx=0, relief='flat', anchor='center', font=('Ivyy 15 bold'), bg=cor2, fg=cor4, border=5)
resposta_titulo.place(height=50, width=300, x=110, y=5)

resposta = Label(frame_direita,text="0", fg=cor1, relief='flat', anchor='center', font=('Ivyy 15 bold'))
resposta.place(height=75, width=350, x=80 , y=60)


#--------------------Frame cima--------------------
bt1 = Button(frame_direita, text="Calcular", bg=cor3, fg=cor4, activeforeground= cor3, activebackground=cor5, font=('Ivy 12 bold'),   command=lambda: calcular(1))
bt1.place(width=200, height=50, x=25, y=220)

bt2 = Button(frame_direita, text="Resetar", bg=cor3, fg=cor4,activeforeground= cor3, activebackground=cor5, font=('Ivy 12 bold'), command=lambda: calcular(2))
bt2.place(width=200, height=50, x=275, y=220)

e_Ca.insert(END, 0) 
e_Mg.insert(END, 0)
e_K.insert(END, 0) 
e_AlH.insert(END, 0) 
e_P.insert(END, 0) 
e_v2.insert(END, 0) 
e_PRNT.insert(END, 0) 

pedro=Label(frame_esquerda, text="Por Pedro Manoel C. Timoteo", bg=cor2, fg=cor4, font=('Helvetica 10 bold'))
pedro.place(x=1, y=330)

janela.mainloop()