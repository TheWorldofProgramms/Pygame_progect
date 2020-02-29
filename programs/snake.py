import pygame

class Snake:
    def __init__(self):

        self.head = [45, 45]
        self.body = [[45, 45], [35, 45], [25, 45]]
        self.score = 0

    def move(self, control):
        #Движение змеи в зависимости от направления
        if control.flag_direction == 'Right':
            self.head[0] += 10
            if self.head[0] > 500:
                self.head[0] = -5
        elif control.flag_direction == 'Left':
            self.head[0] -= 10
            if self.head[0] < -10:
                self.head[0] = 495
        elif control.flag_direction == 'Up':
            self.head[1] -= 10
            if self.head[1] < -10:
                self.head[1] = 495
        elif control.flag_direction == 'Down':
            self.head[1] += 10
            if self.head[1] > 500:
                self.head[1] = -5

    def animation(self):
        #Создаем новую голову и удаляем хвост
        self.body.insert(0, list(self.head))
        self.body.pop()


    def draw_snake(self, window):
        #Прорисовка змеи
        for segment in self.body:
            pygame.draw.rect(window, pygame.Color("Green"),
                         pygame.Rect(segment[0], segment[1], 9, 9))

    def eat(self, food, field):    #Поглощение еды
        if self.head == food.food_pos:
            self.body.append(food.food_pos)
            food.get_food_pos(field)
            self.score += 2