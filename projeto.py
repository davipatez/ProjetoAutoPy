# O projeto sera desenvolvido aqui

#eNVIO DE MENSAGEM AUTOMATICA PARA UM GRUPO DE PESSOAS NO WHATSAPP

import pyautogui
import time

pyautogui.PAUSE = 1.5

pyautogui.press('win')
pyautogui.write('Chorme')
pyautogui.press('enter')
pyautogui.click(x=894, y=638)
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')
time.sleep(10)
pyautogui.click(x=241, y=268)


pyautogui.write('Dipo', interval=0.30)
pyautogui.press('enter')
pyautogui.write('Salve meu caro amigo, se vc recebeu essa mensagem, voce foi selecionado pra receber essa mensagem como um teste de um simples bot em python que eu to fazendo. Acredite, eu nem toquei no teclado pra te mandar isso. Eh isso ai, meu bom, te amo e tmj safado <3', interval=0.30)
pyautogui.press('enter')

# pyautogui.click(x=241, y=268)
# pyautogui.write('Nome')
# pyautogui.press('enter')
# pyautogui.write('MENSAGEM')
# pyautogui.press('enter')

# pyautogui.click(x=241, y=268)
# pyautogui.write('Nome')
# pyautogui.press('enter')
# pyautogui.write('MENSAGEM')
# pyautogui.press('enter')


