import pygame, random

size = width, height = 400, 300
screen = pygame.display.set_mode(size)
# Создаем второй холст
screen2 = pygame.Surface(screen.get_size())
clock = pygame.time.Clock()

running = True
balls = list()
v = 100
fps = 60
radius = 10

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            balls.append([color, list(event.pos)])

    i = 0
    while i < len(balls):
        ball = balls[i]
        if ball[1][1] >= height - radius:
            balls.remove(ball)
            pygame.draw.circle(screen2, ball[0], (ball[1][0], int(ball[1][1])), radius)
        else:
            i += 1

    screen.fill(pygame.Color('black'))
    screen.blit(screen2, (0, 0))

    for ball in balls:
        pygame.draw.circle(screen, ball[0], (ball[1][0], int(ball[1][1])), radius)
        ball[1][1] += v / fps

    clock.tick(fps)
    pygame.display.flip()

pygame.quit()
