import sys, pygame





pygame.init()

size = width, height = 1000, 800
speed = [0, 0]
black = 0, 0, 0

velocity = 1
direction = 0

screen = pygame.display.set_mode(size)
snakesize = 50

ball = pygame.image.load("snakeHead.png")
ball = pygame.transform.scale(ball, (snakesize, snakesize))
ballrect = ball.get_rect()

while 1:

    speed = [0,0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction -= 90
                ball = pygame.transform.rotate(ball, 90)
            if event.key == pygame.K_RIGHT:
                direction += 90
                ball = pygame.transform.rotate(ball, -90)

    if direction < 0:
        direction += 360

    direction = direction % 360

    if direction == 0:
        ballrect.y -= snakesize
    if direction == 90:
        ballrect.x += snakesize
    if direction == 180:
        ballrect.y += snakesize
    if direction == 270:
        ballrect.x -= snakesize

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     if ballrect.left > 0:
    #         speed[0] = -velocity
    # if keys[pygame.K_RIGHT]:
    #     if ballrect.right < width:
    #         speed[0] = velocity
    # if keys[pygame.K_UP]:
    #     if ballrect.top > 0:
    #         speed[1] = -velocity
    # if keys[pygame.K_DOWN]:
    #     if ballrect.bottom < height:
    #         speed[1] = velocity


    if ballrect.x > width:
        ballrect.x = 0
    if ballrect.x < 0:
        ballrect.x = width
    if ballrect.y > height:
        ballrect.y = 0
    if ballrect.y < 0:
        ballrect.y = height

    pygame.time.delay(100)
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()