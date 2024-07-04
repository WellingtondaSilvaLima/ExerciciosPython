from funcoes import *
from tkinter import *


janela = Tk()
janela.title('Calculathor')
janela.geometry('500x600')
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

resultado = 0
resultado_na_tela = Label(janela,
                          text=str(resultado),
                          padx=30,
                          pady=15,
                          borderwidth=2,
                          relief='solid',
                          bg="lightgrey",
                          anchor='e',
                          font=('Verdana', 12, 'italic'))
resultado_na_tela.grid(row=0, column=0, columnspan=5)


janela.mainloop()

# SDG
