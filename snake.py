import sys, pygame, math
from random import randint


width = 800
height = 800
borderWidth = 10
screenPadding = 50


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imageHead = pygame.image.load('snakeHead.png')
        self.imageHead = pygame.transform.scale(self.imageHead, (50, 50))
        self.imageBody = pygame.image.load('snakeBody.png')
        self.imageBody = pygame.transform.scale(self.imageBody, (50, 50))
        self.angle = 0
        self.speed = 50
        self.x = [250, 200]
        self.y = [250, 250]
        self.length = 2

    def update(self):
        if self.angle % 360 == 0:
            self.x.insert(0, self.x[0]+50)
            self.y.insert(0, self.y[0])
        if self.angle % 360 == 90:
            self.x.insert(0, self.x[0])
            self.y.insert(0, self.y[0]+50)
        if self.angle % 360 == 180:
            self.x.insert(0, self.x[0]-50)
            self.y.insert(0, self.y[0])
        if self.angle % 360 == 270:
            self.x.insert(0, self.x[0])
            self.y.insert(0, self.y[0]-50)
        self.x = self.x[:self.length]
        self.y = self.y[:self.length]

    def rotateHead(self, angle):
        self.imageHead = pygame.transform.rotate(self.imageHead, angle)

    def wrap(self):
        if self.x[0] <= 0:
            self.x[0] += width
        if self.x[0] >= width:
            self.x[0] -= width
        if self.y[0] <= 0:
            self.y[0] += height
        if self.y[0] >= height:
            self.y[0] -= height

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('apple.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.x = 0
        self.y = 0
        self.alive = 0

    def spawn(self):
        x = randint(1, (width/50)-1)*50
        y = randint(1, (height/50)-1)*50
        self.x = x
        self.y = y
        self.alive = 1


def checkCollisionApple(snake, apple):
    if snake.x[0] == apple.x and snake.y[0] == apple.y:
        return True

def checkColissionSelf(snake):
    if (snake.x[0], snake.y[0]) in zip(snake.x[1:], snake.y[1:]):
        return True
    else:
        return False

def checkColissionWall(snake):
    if snake.x[0] <= 0 or snake.y[0] <= 0 or snake.x[0] >= width-50 or snake.y[0] >= height-50:
        return True
    else:
        return False

def drawBorder():
    pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), [0, 0, width, borderWidth])
    pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), [0, 0, borderWidth, height])
    pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), [0, height, width, borderWidth])
    pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), [width, 0, borderWidth, height + borderWidth])






def main():
    pygame.init()
    pygame.font.init()
    gameoverfont = pygame.font.SysFont('Comic Sans MS', 30)
    gameovertext = gameoverfont.render('GAME OVER', False, (200, 0, 0))

    size = width+2*borderWidth + 2*screenPadding, height+2*borderWidth + 2*screenPadding
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    speed = 50

    initialVector = [0, speed]
    snake = Snake()
    snake.rotateHead(-90)

    apple = Apple()
    apple.spawn()

    while 1:



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.angle -= 90
                    snake.rotateHead(90)
                if event.key == pygame.K_RIGHT:
                    snake.angle += 90
                    snake.rotateHead(-90)

        if checkColissionSelf(snake) or checkColissionWall(snake):
            screen.fill(black)
            screen.blit(apple.image, (apple.x, apple.y))
            for i in range(snake.length):
                if i != 0:
                    screen.blit(snake.imageBody, (snake.x[i], snake.y[i]))
            screen.blit(snake.imageHead, (snake.x[0], snake.y[0]))
            screen.blit(gameovertext, (0, 0))
            pygame.display.flip()
        else:

            if checkCollisionApple(snake, apple):
                snake.length += 1
                apple.alive = 0
                apple.spawn()

            snake.update()
            snake.wrap()


            pygame.time.delay(100)

            screen.fill(black)
            pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), [screenPadding, screenPadding, width+2*borderWidth, borderWidth])
            pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), [screenPadding, screenPadding, borderWidth, height+2*borderWidth])
            pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), [screenPadding, height + borderWidth + screenPadding, width + 2*borderWidth, borderWidth])
            pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), [width+borderWidth+screenPadding, screenPadding, borderWidth, height+2*borderWidth])
            screen.blit(apple.image, (apple.x, apple.y))
            for i in range(snake.length):
                if i != 0:
                    screen.blit(snake.imageBody, (snake.x[i], snake.y[i]))
            screen.blit(snake.imageHead, (snake.x[0], snake.y[0]))
            pygame.display.flip()

if __name__ == "__main__":
    main()