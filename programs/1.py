import pygame
pygame.init()



def enter(x1, y1, x2, y2, a1, b1, a2, b2):   #Проверка попадания стрелы в цель
    if x1 > x2 - a1 and x1 < x2 + a2 and y1 > y2 - b1 and y1 < y2 + b2:
        return 1
    return 0

a, b = [1], [1]
if a == b:
    print('of')
window = pygame.display.set_mode((500, 500))  # Экран

screen = pygame.Surface((500, 500))

player = pygame.Surface((40, 40))

tar = pygame.Surface((40, 40))

arrow = pygame.Surface((20, 60))

count = 0
myfont = pygame.font.SysFont('test_sans', 25)

x_p, y_p = 0, 0

x_t, y_t = 0, 460

x_a, y_a = 1000, 1000

strike = False
right = True
done = False

while done == False:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_UP: #Движение игрока
            y_p -= 1
        if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
            y_p += 1
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            x_p += 1
        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            x_p -= 1
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:  #Выпуск стрелы
            if strike == False:
                x_a, y_a = x_p + 20, y_p + 40
                strike = True

    if strike:  #Полет стрелы
        y_a += 0.5
        if y_a > 460:
            strike = False
            x_a, y_a = 1000, 1000

    if enter(x_a, y_a, x_t, y_t, 20, 60, 40, 40):
        count += 1
        strike = False
        x_a, y_a = 1000, 1000

    if right:
        x_t += 0.5
        if x_t > 460:
            x_t -= 0.5
            right = False
    else:
        x_t -= 0.5
        if x_t < 0:
            x_t += 0.5
            right = True

    string = myfont.render("Очков: " + str(count), 0, (255, 0, 0))
    screen.fill((0, 255, 0))
    screen.blit(string, (410, 430))
    screen.blit(player, (x_p, y_p))
    screen.blit(tar, (x_t, y_t))
    screen.blit(arrow, (x_a, y_a))
    window.blit(screen, (0, 0))
    pygame.display.update()

pygame.quit()