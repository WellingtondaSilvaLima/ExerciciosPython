from math import sqrt, sin, cos, tan, radians
from tkinter import Label

operadores = ['+', '-', '*', '/', '^', '^1/']

def soma(visor:Label):
  global operadores
  valor_1 = visor.cget('text')
  if valor_1[-1] == '+' or valor_1[-1] in operadores:
    novo_valor = valor_1 + ''
    visor['text'] = f'{novo_valor}'
  else:
    novo_valor = valor_1 + '+'
    visor['text'] = f'{novo_valor}'
    

def subtracao(visor:Label):
  global operadores
  valor_1 = visor.cget('text')
  if valor_1[-1] == '-' or valor_1[-1] in operadores:
    novo_valor = valor_1 + ''
    visor['text'] = f'{novo_valor}'
  else:
    novo_valor = valor_1 + '-'
    visor['text'] = f'{novo_valor}'

def multiplicacao(visor:Label):
  global operadores
  valor_1 = visor.cget('text')
  if valor_1[-1] == '*' or valor_1[-1] in operadores:
    novo_valor = valor_1 + ''
    visor['text'] = f'{novo_valor}'
  else:
    novo_valor = valor_1 + '*'
    visor['text'] = f'{novo_valor}'

def divisao(visor:Label):
  global operadores
  valor_1 = visor.cget('text')
  if valor_1[-1] == '/' or valor_1[-1] in operadores:
    novo_valor = valor_1 + ''
    visor['text'] = f'{novo_valor}'
  else:
    novo_valor = valor_1 + '/'
    visor['text'] = f'{novo_valor}'

def exponenciacao(visor:Label):
  global operadores
  valor_1 = visor.cget('text')
  if valor_1[-1] == '^' or valor_1[-1] in operadores:
    novo_valor = valor_1 + ''
    visor['text'] = f'{novo_valor}'
  else:
    novo_valor = valor_1 + '^'
    visor['text'] = f'{novo_valor}'

def raiz_quadrada(visor:Label):
  try:
    valor = visor.cget('text')
    numero = float(valor)
    resultado = sqrt(numero)
    visor['text'] = f'{resultado}'
  except ValueError:
    pass

def raiz_nesima(visor:Label):
  global operadores
  valor_1 = visor.cget('text')
  if valor_1[-1] == '^1/' or valor_1[-1] in operadores:
    novo_valor = valor_1 + ''
    visor['text'] = f'{novo_valor}'
  else:
    novo_valor = valor_1 + '^1/'
    visor['text'] = f'{novo_valor}'

def seno(visor:Label):
  try:
    valor = visor.cget('text')
    numero = float(valor)
    numero = radians(numero)
    resultado = sin(numero)
    visor['text'] = f'{resultado}'
  except ValueError:
    pass

def cosseno(visor:Label):
  try:
    valor = visor.cget('text')
    numero = float(valor)
    numero = radians(numero)
    resultado = cos(numero)
    visor['text'] = f'{resultado}'
  except ValueError:
    pass

def tangente(visor:Label):
  try:
    valor = visor.cget('text')
    numero = float(valor)
    numero = radians(numero)
    resultado = tan(numero)
    visor['text'] = f'{resultado}'
  except ValueError:
    pass

def mudar_sinal(visor:Label):
  try:
    valor = visor.cget('text')
    numero = float(valor)
    resultado = -numero
    visor['text'] = f'{resultado}'
  except ValueError:
    pass

def limpa_visor(visor:Label):
  texto = visor.cget('text')
  if len(texto) <= 1:
    visor.config(text='0')
  else:
    visor.config(text=f'{texto[:-1]}')

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

def mostra_ponto(ponto:str, visor:Label):
  texto_atual = visor.cget('text')
  if '.' in texto_atual:
    texto_novo = texto_atual + ''
    visor['text'] = texto_novo
  else:
    texto_novo = texto_atual + ponto
    visor['text'] = texto_novo

def igual():
  pass

# SDG