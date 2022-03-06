import pyautogui
import json
from time import sleep

pos = [(81, 246), (158, 246), (234, 246), (309, 246), (381, 246), (455, 246), (1049, 246), (1118, 246), (1194, 248), (1268, 246), (1342, 246)]
posMenu = [[(30, 120), (150, 410), (570, 240), (530, 410), (470, 550), (150, 260)], [(995, 120), (1100, 410), (1500, 240), (1500, 410), (1400, 550), (1100, 260)]] # Izquierda - Derecha
                        

with open('counter.json', 'r') as openfile:
    counter = json.load(openfile)

def showPos():
    while True:
        print(pyautogui.position())

def rechargeEnergy(side):
    if side == False:
        pyautogui.click(posMenu[1][0]) 
        sleep(3)
        pyautogui.click(posMenu[1][1]) 
        sleep(3)
        pyautogui.click(posMenu[1][2])
        sleep(3)
        pyautogui.click(posMenu[1][3]) 
        sleep(3)
        pyautogui.write("500")  
        sleep(3)
        pyautogui.click(posMenu[1][4]) 
        sleep(10)
        pyautogui.click(posMenu[1][0]) 
        sleep(3)
        pyautogui.click(posMenu[1][5]) 
        sleep(3)
        pyautogui.click(posMenu[1][0]) 
        sleep(3)
        pyautogui.click(posMenu[1][1]) 
        sleep(3)
        pyautogui.click(posMenu[1][0]) 
        sleep(3)
        pyautogui.click(posMenu[1][5]) 
        sleep(3)

    else:
        pyautogui.click(posMenu[0][0]) 
        sleep(3)
        pyautogui.click(posMenu[0][1]) 
        sleep(3)
        pyautogui.click(posMenu[0][2])
        sleep(3)
        pyautogui.click(posMenu[0][3]) 
        sleep(3)
        pyautogui.write("500")  
        sleep(3)
        pyautogui.click(posMenu[0][4]) 
        sleep(10)
        pyautogui.click(posMenu[0][0]) 
        sleep(3)
        pyautogui.click(posMenu[0][5]) 
        sleep(3)
        pyautogui.click(posMenu[0][0]) 
        sleep(3)
        pyautogui.click(posMenu[0][1]) 
        sleep(3)
        pyautogui.click(posMenu[0][0]) 
        sleep(3)
        pyautogui.click(posMenu[0][5]) 
        sleep(3)
        


def initBot():
    global counter

    while True:

        for i in range(len(pos)):
            pyautogui.click(pos[i][0], pos[i][1])
            sleep(1)

            ready = pyautogui.locateOnScreen('ready.png')
            ready2 = pyautogui.locateOnScreen('ready2.png')

            if ready is not None or ready2 is not None:

                mine = pyautogui.locateOnScreen('mine.png')

                if mine is not None:
                    pyautogui.click(mine[0], mine[1])
                    
                    sleep(8)

                    login = pyautogui.locateOnScreen('login.png')
                    if login is None:
                        login = pyautogui.locateOnScreen('logindark.png')
                
                    if login is None:
                        counter += 1
                        with open("counter.json", "w") as outfile:
                            json_object = json.dumps(counter, indent = 4)
                            outfile.write(json_object)
                    else:
                        pyautogui.click(login[0] + 30, login[1] + 30)
                        sleep(10)
                        google = pyautogui.locateOnScreen('google.png')
                        if google is not None:
                            pyautogui.click(google[0] + 10, google[1] + 10)
                        sleep(10)
                        cf = pyautogui.locateOnScreen('cf.png')
                        if cf is not None:
                            pyautogui.click(cf[0] + 10, cf[1] + 10)
                        sleep(4)
                        

                
                else:
                    print(ready, ready2)
                    if ready[0] is not None and ready[0] < 960:
                        rechargeEnergy(True)
                    elif ready[0] is not None and ready[0] > 960:
                        rechargeEnergy(False)
                    elif ready2[0] is not None and ready2[0] > 960:
                        rechargeEnergy(False)
                    elif ready2[0] is not None and ready2[0] < 960:
                        rechargeEnergy(False)

initBot() 
showPos() 