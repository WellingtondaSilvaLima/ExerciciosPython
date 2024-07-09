from funcoes import *
from tkinter import *


# Configuração da tela
janela = Tk()
janela.title('Calculathor')
janela.geometry('494x282')
janela.resizable(False, False)

# Display
resultado_na_tela = Label(janela,
                          text='0',
                          padx=30,
                          pady=15,
                          borderwidth=2,
                          relief=GROOVE,
                          bg="lightgrey",
                          anchor='e',
                          font=('Verdana', 12, 'italic'),
                          width=43)
resultado_na_tela.grid(row=0, column=0, columnspan=5,)

## Teclas
# Fórmulas #
class Botao:
  def __init__(self, texto:str, linha:int, coluna:int) -> None:
    self.texto = texto
    self.linha = linha
    self.coluna = coluna

  def cria_botao(self, comando, mescla=False):
    btn_generico = Button(janela,
                          text=self.texto,
                          padx=10,
                          pady=10,
                          bd=2,
                          font=('Verdana', 10),
                          relief=GROOVE,
                          command=comando)
    self.__mescla_linhas(btn_generico, mescla)

  def __mescla_linhas(self, btn_para_mesclar, mescla:bool):  
    if mescla == False:
      btn_para_mesclar.grid(row=self.linha, column=self.coluna, sticky='nsew')
    else:
      btn_para_mesclar.grid(row=self.linha, column=self.coluna, sticky='nsew', rowspan=2)


btn_seno = Botao('Sin', 1, 0)
btn_seno.cria_botao(lambda: seno(resultado_na_tela))

btn_cosseno = Botao('Cos', 1, 1)
btn_cosseno.cria_botao(lambda: cosseno(resultado_na_tela))

btn_tangente = Botao('Tan', 1, 2)
btn_tangente.cria_botao(lambda: tangente(resultado_na_tela))

btn_raiz_nesima = Botao('x^1/n', 1, 3)
btn_raiz_nesima.cria_botao(lambda: raiz_nesima(resultado_na_tela))

btn_raiz_quadrada = Botao('x^1/2', 2, 4)
btn_raiz_quadrada.cria_botao(lambda: raiz_quadrada(resultado_na_tela))

btn_limpar = Botao('C', 1, 4)
btn_limpar.cria_botao(lambda: limpa_visor(resultado_na_tela))

btn_potencia = Botao('x^n', 3, 4)
btn_potencia.cria_botao(lambda: exponenciacao(resultado_na_tela))

btn_sete = Botao('7', 2, 0)
btn_sete.cria_botao(lambda: mostra_numeros(7, resultado_na_tela))

btn_oito = Botao('8', 2, 1)
btn_oito.cria_botao(lambda: mostra_numeros(8, resultado_na_tela))

btn_nove = Botao('9', 2, 2)
btn_nove.cria_botao(lambda: mostra_numeros(9, resultado_na_tela))

btn_divisao = Botao('/', 2, 3)
btn_divisao.cria_botao(lambda: divisao(resultado_na_tela))

btn_multiplicacao = Botao('*', 3, 3)
btn_multiplicacao.cria_botao(lambda: multiplicacao(resultado_na_tela))

btn_quatro = Botao('4', 3, 0)
btn_quatro.cria_botao(lambda: mostra_numeros(4, resultado_na_tela))

btn_cinco = Botao('5', 3, 1)
btn_cinco.cria_botao(lambda: mostra_numeros(5, resultado_na_tela))

btn_seis = Botao('6', 3, 2)
btn_seis.cria_botao(lambda: mostra_numeros(6, resultado_na_tela))

btn_subtracao = Botao('-', 4, 3)
btn_subtracao.cria_botao(lambda: subtracao(resultado_na_tela))

btn_um = Botao('1', 4, 0)
btn_um.cria_botao(lambda: mostra_numeros(1, resultado_na_tela))

btn_dois = Botao('2', 4, 1)
btn_dois.cria_botao(lambda: mostra_numeros(2, resultado_na_tela))

btn_tres = Botao('3', 4, 2)
btn_tres.cria_botao(lambda: mostra_numeros(3, resultado_na_tela))

btn_soma = Botao('+', 5, 3)
btn_soma.cria_botao(lambda: soma(resultado_na_tela))

btn_igual = Botao('=', 4, 4)
btn_igual.cria_botao(lambda: igual(), True)

btn_ponto = Botao('.', 5, 0)
btn_ponto.cria_botao(lambda: mostra_ponto('.', resultado_na_tela))

btn_zero = Botao('0', 5, 1)
btn_zero.cria_botao(lambda: mostra_numeros(0, resultado_na_tela))

btn_virgula = Botao('+/-', 5, 2)
btn_virgula.cria_botao(lambda: mudar_sinal(resultado_na_tela))



janela.mainloop()

# SDG
