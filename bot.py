import pyautogui
import json
from time import sleep

pos = [(81, 246), (158, 246), (234, 246), (309, 246), (381, 246)]
posMenu = [[(30, 120), (150, 410), (570, 240), (530, 410), (470, 550), (150, 260)], [(995, 120), (1100, 410), (1500, 240), (1500, 410), (1400, 550), (1100, 260)]] # Izquierda - Derecha
                        

with open('counter.json', 'r') as openfile:
    counter = json.load(openfile)

def showPos():
    while True:
        print(pyautogui.position())

def rechargeEnergy(side):
    print("hols")
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

    try:
        while True:

            
            for i in range(len(pos)):

                login = pyautogui.locateOnScreen('login.png')
                if login is None:
                    login = pyautogui.locateOnScreen('logindark.png')
            
                else:
                    pyautogui.click(login[0], login[1])
                    sleep(10)
                    if i < 6:
                        pyautogui.click(426, 220)
                    else:
                        pyautogui.click(1384, 220)
                    sleep(10)
                    if i < 6:
                        pyautogui.click(255, 25)
                    else:
                        pyautogui.click(1214, 25)
                    sleep(4)

                retry = pyautogui.locateOnScreen("retry.png")
                if retry is not None:
                    pyautogui.click(retry[0] + 30, retry[1] + 30)
                    sleep(5)

                pyautogui.click(pos[i][0], pos[i][1])
                sleep(1)

                ready = pyautogui.locateOnScreen('ready.png')
                ready2 = pyautogui.locateOnScreen('ready2.png')

                if ready is not None or ready2 is not None:

                    mine = pyautogui.locateOnScreen('mine.png')
                    print("Si")

                    if mine is not None:
                        print("no")
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
                            pyautogui.click(login[0], login[1])
                            sleep(10)
                            if i < 6:
                                pyautogui.click(426, 220)
                            else:
                                pyautogui.click(1384, 220)
                            sleep(10)
                            if i < 6:
                                pyautogui.click(255, 25)
                            else:
                                pyautogui.click(1214, 25)
                            sleep(4)
                                    

                    
                    else:
                        if ready[0] is not None:
                            if ready[0] < 960:
                                rechargeEnergy(True)
                            elif ready[0] > 960:
                                print("aca")
                                rechargeEnergy(False)

                        elif ready2[0] is not None:
                            if ready2[0] > 960:
                                rechargeEnergy(False)
                            elif ready2[0] < 960:
                                rechargeEnergy(True)
    except Exception as e:
        print(e)
        initBot()

initBot()