import pygame, random


class Food:
    def __init__(self):

        self.food_pos = []

    def get_food_pos(self, field):                                         #Выбор позиции еды
        self.food_pos = random.choice(field)

    def draw_food(self, window):                                            #Отрисовка еды
        pygame.draw.circle(window, pygame.Color("Red"),
                           [self.food_pos[0], self.food_pos[1]], 5, 1)
