import pygame
import os
import sys

from Sprites import *

pygame.init()
SIZE = WI, HE = 620, 620
FPS = 60
TILE_S = 60
PLAYER = None
FIGHT = False
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Игре нужно название")
clock = pygame.time.Clock()


def load_image(name, colorkey=None):
    # Функция загрузки изображений
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        return
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


tile_images = {
    'wall': load_image('box.png'),
    'enemy': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mar.png')


def load_level(filename):
    # Функция загрузки уровня из тхт файла
    filename = "maps/" + filename
    with open(filename, "r", encoding="utf8") as mapFile:
        level_map = [line.strip() for line in mapFile]
    return list(map(lambda x: x.ljust(10, "."), level_map))


def load_map(filename="map0_0.txt"):
    # Функия загрузки уровня на экран
    board = load_level(filename)
    x, y = None, None
    global PLAYER
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == '.':
                Tile(x, y, tile_images['empty'], "empty")
            elif board[y][x] == 'E':
                Tile(x, y, tile_images['empty'], "empty")
                Enemy(x, y, tile_images['enemy'])
            elif board[y][x] == '#':
                Tile(x, y, tile_images['wall'], "wall")
            elif board[y][x] == '@':
                Tile(x, y, tile_images['empty'], "empty")
                if not PLAYER:
                    PLAYER = Player(x, y, player_image)
                else:
                    PLAYER.rect.x, PLAYER.rect.y = x, y


class FightScreen:
    pass  # Загатовка на будущее


if __name__ == '__main__':
    ex = FightScreen()
    load_map()
    running = False if not PLAYER else True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    PLAYER.move(0, -1)
                    if PLAYER.rect.y < 0:
                        PLAYER.move(0, 1)
                if event.key == pygame.K_DOWN:
                    PLAYER.move(0, 1)
                    if PLAYER.rect.y > 600:
                        PLAYER.move(0, -1)
                if event.key == pygame.K_LEFT:
                    PLAYER.move(-1, 0)
                    if PLAYER.rect.x < 0:
                        PLAYER.move(1, 0)
                if event.key == pygame.K_RIGHT:
                    PLAYER.move(1, 0)
                    if PLAYER.rect.x > 600:
                        PLAYER.move(-1, 0)
        screen.fill(pygame.Color(0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        enemy_group.update()
        player_group.draw(screen)
        if FIGHT:
            print("Ну начадся бой и что?")
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
