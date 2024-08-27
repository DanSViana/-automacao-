# importa a biblioteca de automação
# NOTE: instale a biblioteca: pip install pyautogui
import pyautogui as auto

# atrasar os comandos da biblioteca
auto.PAUSE = 0.5

auto.press('win') # abre o menu iniciar
auto.write('chrome') # digita a palavra "Chrome" ou "Firefox"
auto.press('enter') # aperta "Enter"

# tecla de atalho para maximizar tela
auto.hotkey('alt', 'space')
auto.press('x')

# acessa o site do "GitHub"
auto.write('github.com')
auto.press('enter')

# entrar na página de login do GitHub
for i in range(12):
    auto.press('tab')

auto.press('enter')

# para entrar com senha e login 
# auto.write('DanSViana')
# auto.press('tab')
# auto.write('Der!m123')
# auto.press('enter')



