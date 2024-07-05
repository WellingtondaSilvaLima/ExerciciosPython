from funcoes import *
from tkinter import *


# Configuração da tela
janela = Tk()
janela.title('Calculathor')
janela.geometry('494x600')
janela.resizable(False, False)

# Display
resultado = 0
resultado_na_tela = Label(janela,
                          text=str(resultado),
                          padx=30,
                          pady=15,
                          borderwidth=2,
                          relief=GROOVE,
                          bg="lightgrey",
                          anchor='e',
                          font=('Verdana', 12, 'italic'),
                          width=43)
resultado_na_tela.grid(row=0, column=0, columnspan=6,)

## Teclas
# Fórmulas #
class Botao:
  def __init__(self, texto:str, linha:int, coluna:int) -> None:
    self.texto = texto
    self.linha = linha
    self.coluna = coluna

  def cria_botao(self):
    btn_generico = Button(janela,
                          text=self.texto,
                          padx=10,
                          pady=10,
                          bd=2,
                          font=('Verdana', 10),
                          relief=GROOVE)
    btn_generico.grid(row=self.linha, column=self.coluna, sticky='nsew')


btn_seno = Botao('Sin', 1, 0)
btn_seno.cria_botao()

btn_cosseno = Botao('Cos', 1, 1)
btn_cosseno.cria_botao()

btn_tangente = Botao('Tan', 1, 2)
btn_tangente.cria_botao()

btn_raiz_nesima = Botao('x^n', 1, 3)
btn_raiz_nesima.cria_botao()

btn_raiz_quadrada = Botao('x^2', 1, 4)
btn_raiz_quadrada.cria_botao()


janela.mainloop()

# SDG
