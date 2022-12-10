from turtle import right
from unittest import result
import pygame
res=[]
def addTrailingZeros():
    i=len(res)
    while(i<8):
        res.append(0)
        i+=1
def decimalToBinary(num):
    """This function converts decimal number
    to binary and prints it"""
    if num > 1:
        decimalToBinary(num // 2)
    res.append(num%2)
    


arrlntgh=41
experiment=20
black = (0, 0, 0)
white = (255, 255, 255)
rule=int(input('Enter a rule number: '))
decimalToBinary(rule)
res.reverse()
addTrailingZeros()
WIDTH = 25
HEIGHT = 25
MARGIN = 1
grid = []
checkarr=[[0,0,0],[1,0,0],[0,1,0],[1,1,0],[0,0,1],[1,0,1],[0,1,1],[1,1,1]]
curntPosArr=[]

def checkstatus(l):
    for i in range(8):
        if checkarr[i] == l:
            return res[i]


for row in range(experiment):
    grid.append([])
    for column in range(arrlntgh):
        grid[row].append(0) 
pygame.init()
window_size = [WIDTH*arrlntgh+arrlntgh, experiment*HEIGHT+experiment]
scr = pygame.display.set_mode(window_size)
pygame.display.set_caption(f"Rule {rule}")
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get(): 
        keys=pygame.key.get_pressed()
        if event.type == pygame.QUIT: 
            done = True 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            if row != 0 :
                break
            grid[row][column] = 1
        elif event.type == pygame.KEYUP:
            for j in range (experiment-1):
                tmp=[]
                for i in range (arrlntgh):
                    curntPosArr=[]
                    lft = (i-1+arrlntgh)%arrlntgh
                    rgt=(i+1+arrlntgh)%arrlntgh
                    curntPosArr.append(grid[j][rgt])
                    curntPosArr.append(grid[j][i])
                    curntPosArr.append(grid[j][lft])
                    tmp.append(checkstatus(curntPosArr))
                grid[j+1]=tmp

    scr.fill(black)
    for row in range(experiment):
        for column in range(arrlntgh):
            color = white
            if grid[row][column] == 1:
                color = black
            pygame.draw.rect(scr,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
        
        
    clock.tick(50)
    pygame.display.flip()
pygame.quit()