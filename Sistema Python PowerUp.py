"""
Projeto de automação desenvolvido para automatizar o cadastro
de produtos em um sistema web utilizando Python, PyAutoGUI e Pandas.
"""



# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa

# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import pandas as pd
import time

link = ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

# abrir o navegador (chrome)
pyautogui.press("win")
time.sleep(1)
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(3)
# entrar no link

pyautogui.write(link)
time.sleep(1)
pyautogui.press("enter")

# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=599 , y=407)

time.sleep(3)

# escrever o seu email

pyautogui.write("Seu_email")
time.sleep(1)
pyautogui.press("tab")
time.sleep(2)
pyautogui.write("Sua_senha")
time.sleep(1)
pyautogui.press("tab")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)

# Passo 3: Importar a base de produtos pra cadastrar

tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    # Passo 4: Cadastrar um produto
    #Codigo
    pyautogui.click(x= 645 , y=294) #clicou no campo de codigo
    codigo = str (tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)  #escrever o codigo do produto
    pyautogui.press("tab") #pular para o proximo campo
    #marca
    marca = str (tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo
    tipo = str (tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #Categoria
    categoria = str (tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #Preço
    preco = str (tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    #Custo
    custo = str (tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #OBS
    obs = str (tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab") #Passar para o botao enviar

    pyautogui.press("enter")

    time.sleep(1)

    pyautogui.scroll(5000) #vai rolar até o topo da tela


# Passo 5: Repetir o processo de cadastro até o fim