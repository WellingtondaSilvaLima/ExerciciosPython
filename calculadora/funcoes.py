from math import sqrt, sin, cos, tan
from tkinter import Label


def soma(valor1=0, valor2=0):
  return valor1 + valor2

def subtracao(valor1=0, valor2=0):
  return valor1 - valor2

def multiplicacao(valor1=0, valor2=0):
  return valor1 * valor2

def divisao(valor1=0, valor2=1):
  return valor1 / valor2

def exponenciacao(valor=0, expoente=1):
  return valor**expoente

def raiz_quadrada(valor=1):
  return sqrt(valor)

def raiz_nesima(valor=0, indice=1):
  return valor ** (1/indice)

def seno(valor=0):
  return sin(valor)

def cosseno(valor=0):
  return cos(valor)

def tangente(valor=0):
  return tan(valor)

def mudar_sinal(valor=1):
  return -(valor)

def limpa_visor(visor:Label):
  visor.config(text='0')

def mostra_numeros(numero:int, visor:Label):
  match str(numero):
    case '0':
      texto_atual = visor.cget('text')
      if texto_atual == '0':
        visor['text'] = '0'
      else:
        texto_novo = texto_atual + '0'
        visor['text'] = texto_novo
    case '1':
      texto_atual = visor.cget('text')
      if texto_atual == '0':
        visor['text'] = '1'
      else:
        texto_novo = texto_atual + '1'
        visor['text'] = texto_novo
    case '2':
      texto_atual = visor.cget('text')
      if texto_atual == '0':
        visor['text'] = '2'
      else:
        texto_novo = texto_atual + '2'
        visor['text'] = texto_novo
    case '3':
      texto_atual = visor.cget('text')
      if texto_atual == '0':
        visor['text'] = '3'
      else:
        texto_novo = texto_atual + '3'
        visor['text'] = texto_novo
    case '4':
      texto_atual = visor.cget('text')
      if texto_atual == '0':
        visor['text'] = '4'
      else:
        texto_novo = texto_atual + '4'
        visor['text'] = texto_novo
    case '5':
      texto_atual = visor.cget('text')
      if texto_atual == '0':
        visor['text'] = '5'
      else:
        texto_novo = texto_atual + '5'
        visor['text'] = texto_novo
    case '6':
      texto_atual = visor.cget('text')
      if texto_atual == '0':
        visor['text'] = '6'
      else:
        texto_novo = texto_atual + '6'
        visor['text'] = texto_novo
    case '7':
      texto_atual = visor.cget('text')
      if texto_atual == '0':
        visor['text'] = '7'
      else:
        texto_novo = texto_atual + '7'
        visor['text'] = texto_novo
    case '8':
      texto_atual = visor.cget('text')
      if texto_atual == '0':
        visor['text'] = '8'
      else:
        texto_novo = texto_atual + '8'
        visor['text'] = texto_novo
    case '9':
      texto_atual = visor.cget('text')
      if texto_atual == '0':
        visor['text'] = '9'
      else:
        texto_novo = texto_atual + '9'
        visor['text'] = texto_novo
    case _:
      visor['text'] = 'Error'

def igual():
  pass

def ponto_para_virgula():
  pass

def virgula_para_ponto():
  pass


# SDG