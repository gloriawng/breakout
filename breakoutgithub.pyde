#Name: Breakout Arcade Game
#Programmer: Gloria Wang & Mark Chen
#Date: May 10, 2022
#Description: This game allows a user to play a version of Atari's Breakout Arcade Game

displayScreen = 1
gameWon = False
lives = 3
score = 0
ballX = random(1000)
ballY = 550
ballSpeedX = -2
ballSpeedY = -2

def setup():
    global logo, life, start
    size(1000, 600)
    background(0)
    textAlign(CENTER)
    logo = loadImage('breakoutlogo.gif')
    life = loadImage('lifeicon1.png')
    start = loadImage('start1.png')
    

def draw():
    background(0)    
    if displayScreen == 0:
        startScreen()    
    elif displayScreen == 2:
        endScreen()
    elif displayScreen == 1:
        gameScreen()



def startScreen():
    #Title
    image(logo, (width - logo.width) / 2, 50)
    
    #Instructions
    fill(255)
    textSize(30)
    text("Instructions & Rules", 500, 250)
    
    fill(255, 0, 0)
    textSize(15)
    text("A brick wall is at the top section of the screen, use the mouse to", 500, 300)
    text("control the paddle and hit the ball upwards. The ball will eliminate", 500, 320)
    text("the blocks and when all the blocks are gone, YOU WIN. You have 3", 500, 340)
    text("lives to do so. You lose a life if the ball goes past the paddle. Once,", 500, 360)
    text("all 3 lives are gone, YOU LOSE. The game info will be in the top left", 500, 380)
    text("and music will be in the top right. ", 500, 400)
    
    #Play button
    image(start, 425, 450)
    
    
    
def gameScreen():
    global ballX, ballY, ballSpeedX, ballSpeedY, lives, mouseX
        
    #Settings bar
    fill(160)
    rect(0, 0, 1000, 50)
    
    #Lives indicator
    if lives == 3:
        image(life, 15, 10)
        image(life, 55, 10)
        image(life, 95, 10)
    if lives == 2:
        image(life, 15, 10)
        image(life, 55, 10)     
    if lives == 1:
        image(life, 15, 10)
    
    #Score indicator
    msg = "SCORE: " + str(score)
    textSize(30)
    fill(0)
    text(msg, 210, 35)
    
    #Ball
    ballX += ballSpeedX
    ballY += ballSpeedY
    fill(120)
    ball = ellipse(ballX, ballY, 18, 18)
    
    if ballX + 9 >= width:
        ballSpeedX = -ballSpeedX
        ballX = width - 9
    elif ballX - 9 <= 0:
        ballSpeedX = -ballSpeedX
        ballX = 9
    if ballY + 9 >= height:
        ballY = height - 9
        ballSpeedX = 0
        lives -= 1 #Keeps on deleting lives until 0 // ntbf
    elif ballY - 9 <= 50:
        ballSpeedY = -ballSpeedY
        ballY = 59
        
    fill(0, 0, 255)
    paddle = rect(mouseX, 550, 160, 20) #mouseX is left most side, should be center // ntbf
    
    if mouseX < 0:
        mouseX = 0
    
    if ballY + 9 >= 550:
        if ballX >= mouseX and ballX < (mouseX + 80):
            ballSpeedY = -ballSpeedY
            ballY = 541
        if ballX >= (mouseX + 80) and ballX <= (mouseX + 160):
            ballSpeedY = -ballSpeedY
            ballSpeedX = -ballSpeedX
            ballY = 541
                
        
def endScreen():
    pass


def mouseClicked():
    global displayScreen
    if displayScreen == 0 and mouseX >= 425 and mouseX <= 575 and mouseY >= 450 and mouseY <= 525:
        displayScreen = 1
