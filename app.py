import webbrowser
import pyautogui
from time import sleep

# https://api.whatsapp.com/send?phone=
# API do whats
# Selecionar o contato
# Abrir o navegador
# Clicar no botão que autoriza a abertura do Aplicativo do WhatsApp
# Ativar o campo de texto
# Escrever Mensagem
# Enviar Mensagem
# Fechando o navegador para evitar o travamento do browser (evitar 1. múltiplas abas abertas)
# Pausa de 300 segundos entre cada envio à fim de evitar o bloqueio do bot

# Opção 1 (descomentar a opção desejada)
# telefones = [5548995853584, 554799558685, 5547558896584]
# Opção 2 (descomentar a opção desejada)
telefones = []
with open('fones.txt', 'r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
#
for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(1586, 295, duration=1)
    sleep(10)
    pyautogui.click(838, 1053, duration=1)
    sleep(5)
    pyautogui.typewrite('Gostaria de participar do nosso evento?(digite sim, se gostaria de participar.')
    sleep(5)
    pyautogui.press('enter')
    sleep(300)

# f'https://api.whatsapp.com/send?phone={telefone}&text={mensagem}
