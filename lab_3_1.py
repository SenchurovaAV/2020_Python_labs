import turtle as tt
from random import *

running = True
def stopRun(a,b) -> None:
    global running
    print("test")
    running = False
    
tt.onclick(stopRun)

while running:
    tt.forward(randint(1, 50))
    tt.left(randint(-180, 180))