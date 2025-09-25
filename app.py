import pyautogui
import time

# Defina o tempo de espera entre os cliques (em segundos)
intervalo = 180 #3 minutos

try:
    while True:
        #Obtém a posilção atual do mause
        x, y = pyautogui.position()
    
        # Clica na posição atual
        pyautogui.click(x, y)
        print(f"Clique realizado na posição ({x}, {y})")

        # Esperar o intervalo
        time.sleep(intervalo)
except KeyboardInterrupt:
    print("Auto clique interrompido pelo usuário")