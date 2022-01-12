import pygame

SIZE = (660, 660)


# Класс отрисовки поля боя
class FightScreen:
    def __init__(self):
        self.screen = pygame.Surface(SIZE)

    def draw(self, Enemys, Enemys_Hp, Heroes, Heroes_Hp, cur, cur_m, choosing=False):
        print(cur_m)
        # Отрисовка поля боя
        self.screen.fill(pygame.Color(50))
        font = pygame.font.Font(None, 25)

        fight_bg = pygame.transform.scale(pygame.image.load('Images/fight_background.png'), (660, 560))
        self.screen.blit(fight_bg, fight_bg.get_rect(bottomright=(660, 560)))

        text = font.render("A Атака", True, (255, 100, 125))
        pygame.draw.rect(self.screen, (75, 75, 75), (0, 560, 150, 25), 5)
        self.screen.blit(text, (10, 560))
        text = font.render("S Умение", True, (155, 155, 255))
        pygame.draw.rect(self.screen, (75, 75, 75), (0, 585, 150, 25), 5)
        self.screen.blit(text, (10, 585))
        text = font.render("D Зацита", True, (50, 55, 255))
        pygame.draw.rect(self.screen, (75, 75, 75), (0, 610, 150, 25), 5)
        self.screen.blit(text, (10, 610))
        text = font.render("F Предметы", True, (255, 255, 100))
        pygame.draw.rect(self.screen, (75, 75, 75), (0, 635, 150, 25), 5)
        self.screen.blit(text, (10, 635))
        if not choosing:
            text = font.render("Дантэ", True, (255, 0, 0))
            pygame.draw.rect(self.screen, (75, 75, 75), (150, 560, 510, 25), 5)
            self.screen.blit(text, (160, 560))
            text = font.render("Левап", True, (155, 0, 155))
            pygame.draw.rect(self.screen, (75, 75, 75), (150, 585, 510, 25), 5)
            self.screen.blit(text, (160, 585))
            text = font.render("Ашадия", True, (255, 255, 100))
            pygame.draw.rect(self.screen, (75, 75, 75), (150, 610, 510, 25), 5)
            self.screen.blit(text, (160, 610))
            text = font.render("Лилиан", True, (100, 255, 255))
            pygame.draw.rect(self.screen, (75, 75, 75), (150, 635, 510, 25), 5)
            self.screen.blit(text, (160, 635))

            text = font.render("ОЗ", True, (0, 255, 0))
            self.screen.blit(text, (320, 560))
            self.screen.blit(text, (320, 585))
            self.screen.blit(text, (320, 610))
            self.screen.blit(text, (320, 635))
        else:
            text = font.render("Выберите противника", True, (255, 0, 0))
            self.screen.blit(text, (260, 560))
            s = [f'{i + 1} ' + Enemys[i][0] + f' {Enemys_Hp[i] if Enemys_Hp[i] > 0 else 0}'
                 for i in range(len(Enemys))]
            n = 0
            cnt = 0
            for i in range(1, len(s) + 1):
                text = font.render(", ".join(s[n:i]), True, (255, 0, 0))
                if text.get_width() > 500:
                    text = font.render(", ".join(s[n:i - 1]), True, (255, 0, 0))
                    self.screen.blit(text, (160, 585 + 25 * cnt))
                    cnt += 1
                    n = i - 1
            text = font.render(", ".join(s[n:i]), True, (255, 0, 0))
            self.screen.blit(text, (160, 585 + 25 * cnt))
            text = font.render(f"Текущая цель: противник номер {cur + 1}", True, (255, 0, 0))
            self.screen.blit(text, (160, 635))
            pygame.draw.rect(self.screen, (75, 75, 75), (150, 560, 510, 100), 5)

        for i in range(len(Enemys)):
            if Enemys_Hp[i] > 0:
                cof = 120 if i % 2 else 20
                pygame.draw.rect(self.screen, (255, 75, 75), (cof, 95 * i + 80, 95, 95))
        for i in range(4):
            cof = 500 if i % 2 else 400
            pygame.draw.rect(self.screen, (75, 155, 255), (cof, 80 * i + 120, 95, 95))
        if cur_m in Heroes:
            i = Heroes.index(cur_m)
            cof = 500 if i % 2 else 400
            y = 80 * i + 120
            Points = [(cof + 19, y - 40), (cof + 48, y), (cof + 76, y - 40)]
            pygame.draw.polygon(self.screen, (255, 255, 0), Points)
        else:
            i = Enemys.index(cur_m)
            cof = 120 if i % 2 else 20
            y = 95 * i + 80
            Points = [(cof + 19, y - 40), (cof + 48, y), (cof + 76, y - 40)]
            pygame.draw.polygon(self.screen, (255, 255, 0), Points)
        if choosing:
            return
        for i in range(len(Heroes_Hp)):
            text = font.render(f"{Heroes_Hp[i]}/{Heroes[i][1]}", True, (0, 255, 0))
            self.screen.blit(text, (360, 560 + 25 * i))
