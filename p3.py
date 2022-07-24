from tkinter import *

menu_inicial = Tk()


menu_inicial.title('')
menu_inicial.geometry("295x230")
menu_inicial['bg'] = "white"


frame_cima= Frame(menu_inicial, width=295, height=50, bg='white', pady=0, padx=0, relief='flat' )
frame_cima.grid(row=0, column=0, sticky=NSEW )


def Calcular():

    peso =float( e_peso.get())
    altura =float( e_altura.get())

    imc = peso / (altura * altura)

    resultado = imc

    if (imc < 18.5):
        l_resultado_texto['text'] = 'Seu IMC e:Abaixo do peso'
      
    elif (imc < 25):
       l_resultado_texto['text'] = 'Seu IMC é: Normal '

    elif (imc < 30):
       l_resultado_texto['text'] = ' Seu IMC é: Sobre peso '

    elif (imc < 35):
        l_resultado_texto['text'] ='Seu IMC é: Obesidade de 1 grau '

    elif (imc < 40):
         l_resultado_texto['text'] = 'Seu IMC é :Obesidade de 2 grau '

    else:
       l_resultado_texto ['text'] = 'Seu IMC é: Obesidade de 3 grau '



    l_resultado['text'] = "{:.{}f}".format(resultado, 2)





frame_baixo= Frame(menu_inicial, width=295, height=180, bg='white', pady=0, padx=0, relief='flat' )
frame_baixo.grid(row=1, column=0, sticky=NSEW )



app_nome =Label(frame_cima, text='CALCULADORA DE IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 16 bold'), bg='white', fg='black')
app_nome.place(x=0, y=0)


app_margin =Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 1'), bg='black', fg='black')
app_margin.place(x=0, y=35)



l_peso =Label(frame_baixo, text='insira seu peso', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg='black', fg='white')
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

e_peso =Entry(frame_baixo,width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)


l_altura =Label(frame_baixo, text='insira sua altura', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg='black', fg='white')
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)

e_altura =Entry(frame_baixo,width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)


l_resultado =Label(frame_baixo, text='---', width=5,  height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Ivy 24 bold'), bg='black', fg='white')
l_resultado.place(x=175, y=10)

l_resultado_texto =Label(frame_baixo, text='', width=37,  height=1, padx=0, pady=12, relief='flat', anchor='center', font=('Ivy 10 bold'), bg='black', fg='white')
l_resultado_texto.place(x=0, y=90)


b_calcular =Button(frame_baixo, command=Calcular, text='Calcular', width=34,  height=1, overrelief=SOLID,  relief='raised', anchor='center', font=('Ivy 10 bold'), bg='black', fg='white')
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=3, columnspan=30)





menu_inicial.mainloop() 
