import pyautogui #for automating the function of keyboard and mouse
from PIL import Image,ImageGrab
#from numpy import asarray
import time

#global image
'''
def Take_screenshot():
    image= ImageGrab.grab().convert('L')
    image.show()
    return image
'''

def hit(key):
    pyautogui.keyDown(key)
    return

#def draw():

def is_collide(data):

    for i in range(300, 415):
        for j in range(410, 563):
            if data[i, j] < 100: #checking for black picels cactus
                hit("down") #ducking kneeing down
                return

    for i in range(300, 415):
        for j in range(563, 650):
            if data[i, j] < 100: #checking for birds
                hit("up") #jumping
                return
    return

if __name__ == '__main__':
    print("Hey Dino game is about to start in 6 seconds ...... Get ready !!!")
    time.sleep(5)
    #hit("up")

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        is_collide(data)

        #Take_screenshot()

        '''
        data= image.load()
        if is_collide(data):
            hit("up")
        #print(asarray(image))
        for i in range(300,415):
            for j in range(600,650):
                data[i,j]=0

        #image.show()
    
        # Draw the rectangle for cactus
        for i in range(275, 325):
            for j in range(563, 650):
                data[i, j] = 0

        # Draw the rectangle for birds coming in upper portion
        for i in range(250, 300):
            for j in range(410, 563):
                data[i, j] = 171

        image.show()
        break
    '''

