import pyautogui,math,time
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)

def paint_circle(x,y,r):
    pyautogui.moveTo(x,y)

    print('begin')
    for i in range(0,420):
        x1 = x + r*math.cos(i*math.pi/180)
        y1 = y + r*math.sin(i*math.pi/180)
        pyautogui.moveTo(x1,y1)

paint_circle(443,561,140)


