import pygame, random
from control_snake import Control
from snake import Snake
from food import Food
from end_game import EndGame

random.seed()
pygame.init()
all_sprites = pygame.sprite.Group()


class GameSnake:
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()

    def main(self):
        pygame.init()

        gameClock = pygame.time.Clock()

        gameClock.tick(60)

        field, x, y = [], 5, 5
        while x < 495:
            while y < 495:
                field.append([x, y])
                y += 10
            y = 5
            x += 10

        window = pygame.display.set_mode((500, 500))  # Экран
        pygame.display.set_caption('Змейка')


        control = Control()    #Создаем персонажей
        snake = Snake()
        food = Food()
        food.get_food_pos(field)

        sound1 = pygame.mixer.Sound('music\punch.wav')
        sound2 = pygame.mixer.Sound('music\st.wav')

        var_speed = 0
        end = True

        while control.done:                     #Цикл программы
            control.control()
            window.fill(pygame.Color("Black"))
            food.draw_food(window)
            snake.draw_snake(window)

            gameT = pygame.time.get_ticks()
            self.drawTime(gameT, window)
            self.drawGameScore(snake.score, window)

            if not control.fl_pause and var_speed % 10 == 0 and end:
                if snake.head in snake.body[1:]:         #Движение змеи и поглощение еды
                    end = False
                snake.move(control)
                snake.eat(food, field)
                snake.animation()
            elif control.fl_pause and end:         #Пауза
                self.pause(window)
            elif not end and snake.score != 4:                          #Проигрыш
                self.bad_end(window, sound1)
            elif snake.score == 4:               #Победа
                end = False
                self.good_end(window, field, sound2)

            var_speed += 1

            if control.ng and (not end or snake.score == 4):              #Конец или новая игра
                endgame = EndGame()
                endgame.new_game(self)
                break
            elif control.end and not end:
                control.done = False

            pygame.display.update()
            all_sprites.update()
        pygame.quit()


    def pause(self, window):  #Надпись пауза
        pausefont = pygame.font.SysFont('test_sans', 50)
        string = pausefont.render("Pause", 0, (255, 0, 0))
        window.blit(string, (200, 220))

    def bad_end(self, window, sound1):
        pausefont = pygame.font.SysFont('test_sans', 50)
        string1 = pausefont.render("You lose!", 0, (255, 0, 0))
        string2 = pausefont.render("New game? Y/N", 0, (255, 0, 0))
        window.blit(string1, (180, 200))
        window.blit(string2, (140, 260))
        sound1.play()


    def good_end(self, window, field, sound2):
        pausefont = pygame.font.SysFont('test_sans', 50)
        string1 = pausefont.render("You win!", 0, (255, 0, 0))
        string2 = pausefont.render("New game? Y/N", 0, (255, 0, 0))
        window.blit(string1, (180, 200))
        window.blit(string2, (140, 260))
        sound2.play()

    def drawTime(self, gameTime, window):
        scorefont = pygame.font.Font(None, 40)
        scoren_font = pygame.font.Font(None, 30)
        gametime = scorefont.render("Time:", 1, pygame.Color("green"))
        game_timenum = scoren_font.render(str(gameTime / 1000), 1, pygame.Color("red"))

        window.blit(gametime, (30, 10))
        window.blit(game_timenum, (105, 14))

    def drawGameScore(self, score, window):
        scorefont = pygame.font.Font(None, 40)
        scoren_font = pygame.font.Font(None, 30)
        scoremsg = scorefont.render("Score:", 1, pygame.Color("green"))
        score_msgsize = scorefont.size("Score")

        score_numb = scoren_font.render(str(score), 1, pygame.Color("red"))
        window.blit(scoremsg, (500 - score_msgsize[0] - 60, 10))
        window.blit(score_numb, (500 - 45, 14))

pygame.quit()