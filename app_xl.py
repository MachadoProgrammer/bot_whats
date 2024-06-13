import webbrowser
import pyautogui
from time import sleep
import openpyxl

# ENVIANDO MENSAGEM A PARTIR DE UM ARQUIVO XLSX

clientes = openpyxl.load_workbook('')  # arquivo a ser carregado
pagina_contatos = clientes['']  # selecionar a pagina

for linha in pagina_contatos.iter_rows(min_row=2, values_only=True):
    nome, telefone, mensagem = linha

    # Abrir o navegador
    link = f'https://api.whatsapp.com/send?phone={telefone}&text={mensagem}'
    webbrowser.open(link)
    sleep(15)

    # Encontrar o botao de enviar
    botao_enviar = pyautogui.locateCenterOnScreen('')  # img do botao
    sleep(5)
    x = botao_enviar[0]
    y = botao_enviar[1]
    # clicar no botao
    pyautogui.click(x, y, duration=1)
    sleep(5)

    # Fecha a aba
    pyautogui.hotkey('ctrl', 'v')
    sleep(3)
