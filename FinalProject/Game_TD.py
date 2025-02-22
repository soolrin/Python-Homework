import pygame as pg
import math


def creating_window():
    screen = pg.display.set_mode((900, 900))
    pg.display.set_caption("Tower defense")
    pg.display.set_icon(pg.image.load("FinalProject\img\castle_2.png"))
    return screen


def read_map():
    try:
        with open("FinalProject\map.txt", "r", encoding="utf-8") as map_file:
            return [[int(char) for char in line.strip()] for line in map_file]
    except FileNotFoundError:
        print("\n\nОшибка: Нет такого файла\n\n")
        exit()
    except ValueError:
        print("\n\nОшибка: неверный формат данных в файле карты.\n\n")
        exit()


def draw_map(map_game, pixel, screen, map_data):
    # Загрузка изображений
    water = pg.image.load("FinalProject\img\earth1.jpg")
    road = pg.image.load("FinalProject\img\\road1.jpg")
    place_tower = pg.image.load("FinalProject\img\place_tower.jpg")

    # Масштабируем изображения до нужного размера (если нужно)
    water = pg.transform.scale(water, (pixel, pixel))
    road = pg.transform.scale(road, (pixel, pixel))
    place_tower = pg.transform.scale(place_tower, (pixel, pixel))

    # Отображаем элементы на карте
    for y, row in enumerate(map_game):
        for x, px in enumerate(row):
            pos = (x * pixel, y * pixel)  # Позиция элемента на экране
            if px == map_data["road"]:
                screen.blit(road, pos)
            elif px == map_data["place_tower"]:
                screen.blit(place_tower, pos)
            elif px == map_data["water"]:
                screen.blit(water, pos)


def find_path(map_game):
    # Поиск стартовой точки, которая будет первой проходимой клеткой (с значением 1)
    start = 0
    for y in range(len(map_game)):
        for x in range(len(map_game[y])):
            if map_game[y][x] == 1:
                start = (x, y)  # Сохраняем координаты стартовой точки
                break
        if start:
            break

    # Путь с начальной точки
    path = [start]
    # Множество посещенных точек (чтобы не пройти по одной точке несколько раз)
    visited = set([start])
    # Направления, в которых можно двигаться (вправо, вниз, влево, вверх)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    current = start
    # Ищем путь до тех пор, пока есть куда двигаться
    while True:
        found = False  # Флаг для проверки
        for di_x, di_y in directions:
            # Рассчитываем новые координаты для текущего направления
            next_x, next_y = current[0] + di_x, current[1] + di_y
            if 0 <= next_x < len(map_game[0]) and 0 <= next_y < len(map_game):
                # Если клетка проходимая и еще не посещена
                if map_game[next_y][next_x] == 1 and (next_x, next_y) not in visited:
                    path.append((next_x, next_y))
                    visited.add((next_x, next_y))
                    current = (next_x, next_y)
                    found = True
                    break
        if not found:
            break

    return path


def update_enemy(enemy, pixel):
    # Проверяем, достиг ли враг последней точки на пути
    if enemy["current_index"] >= len(enemy["path"]) - 1:
        return True

    # Получаем следующую цель для движения врага
    target = enemy["path"][enemy["current_index"] + 1]

    # Расчет координат точки в пикселях
    target_x = target[0] * pixel + pixel // 2  # Центральная позиция по оси X
    target_y = target[1] * pixel + pixel // 2  # Центральная позиция по оси Y

    # Расчет разницы между текущими координатами врага и точкой
    di_x = target_x - enemy["x"]
    di_y = target_y - enemy["y"]

    # Расчет расстояния между текущей позицией врага и целью
    distance = math.hypot(di_x, di_y)

    if distance <= enemy["speed"]:
        # Перемещаем врага на точку
        enemy["x"] = target_x
        enemy["y"] = target_y

        # Увеличиваем индекс пути, чтобы перейти к следующей точке
        enemy["current_index"] += 1
    else:
        # Нормализуем направление, чтобы враг двигался к цели
        direction_x = di_x / distance  # Направление по оси X
        direction_y = di_y / distance  # Направление по оси Y

        # Перемещаем врага с учетом его скорости
        enemy["x"] += direction_x * enemy["speed"]
        enemy["y"] += direction_y * enemy["speed"]

    # Если враг не достиг последней точки пути, возвращаем False
    return False


def tower_intellect(towers, enemies, bullets, time):
    for tower in towers:

        # Если с момента последнего выстрела прошло меньше времени, чем cooldown, пропускаем эту башню
        if time - tower["last_shot"] < tower["cooldown"]:
            continue

        closest = 0  # Переменная для хранения ближайшего врага
        min_dist = tower["range"]

        for enemy in enemies:
            # Расстояние от башни до врага с помощью теоремы Пифагора
            dist = math.sqrt(
                (enemy["x"] - tower["cx"]) ** 2 + (enemy["y"] - tower["cy"]) ** 2
            )
            # Если расстояние до врага меньше минимального, обновляем ближайшего врага
            if dist < min_dist:
                min_dist = dist
                closest = enemy

        if closest:
            # Вычисляем угол между башней и врагом
            angle = math.atan2(closest["y"] - tower["cy"], closest["x"] - tower["cx"])

            # Добавляем пулю в список выстреленных с заданными параметрами
            bullets.append(
                {
                    "x": tower["cx"],  # Позиция пули по X (из центра башни)
                    "y": tower["cy"],  # Позиция пули по Y (из центра башни)
                    "angle": angle,  # Угол выстрела
                    "speed": 8,  # Скорость пули
                    "damage": 0.5,  # Урон пули
                }
            )

            # Обновляем время последнего выстрела башни
            tower["last_shot"] = time


def update_bullets(bullets, enemies, coins):

    for bullet in bullets[:]:
        # Обновляем позицию пули по осям X и Y, используя скорость и угол
        bullet["x"] += math.cos(bullet["angle"]) * bullet["speed"]
        bullet["y"] += math.sin(bullet["angle"]) * bullet["speed"]

        for enemy in enemies[:]:
            # Вычисление расстояния между пулей и врагом
            di_x = enemy["x"] - bullet["x"]
            di_y = enemy["y"] - bullet["y"]
            dist = math.hypot(di_x, di_y)  # Расстояние между пулей и врагом

            # Если расстояние между пулей и врагом меньше радиуса врага, то попадание
            if dist < enemy["radius"]:
                enemy["hp"] -= bullet["damage"]  # Уменьшение HP при попадании
                if enemy["hp"] <= 0:
                    coins[0] += enemy["reward"]
                    enemies.remove(enemy)
                bullets.remove(bullet)
                break


def draw_text(screen, text, size, color, x, y):
    font = pg.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def game_over_screen(screen):
    screen.fill((0, 0, 0))
    draw_text(screen, "ПОРАЖЕНИЕ!", 74, (255, 0, 0), 450, 300)
    draw_text(screen, "Нажми для перезапуска", 36, (255, 255, 255), 450, 400)
    pg.display.flip()


def victory_screen(screen):
    screen.fill((0, 0, 0))
    draw_text(screen, "ПОБЕДА!", 74, (0, 255, 0), 450, 300)
    draw_text(screen, "Нажми для перезапуска", 36, (255, 255, 255), 450, 400)
    pg.display.flip()


def init_game():
    # Инициализация игровых параметров
    return {
        "player_hp": 20,
        "coins": [100],
        "wave": [],
        "max_wave_size": 10,
        "enemies": [],
        "towers": [],
        "bullets": [],
        "spawn_time": pg.time.get_ticks(),
        "game_state": "playing",
    }


def handle_events(game_state, towers, map_game, coins, pixel, restart_game):
    # Получаем текущую позицию курсора мыши
    mouse_pos = pg.mouse.get_pos()

    # Перевод координат мыши в координаты клетки сетки
    grid_x = (mouse_pos[0] // pixel) * pixel
    grid_y = (mouse_pos[1] // pixel) * pixel

    # Обрабатываем все события, которые происходят в игре
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            return False  # False, чтобы завершить выполнение функции

        if event.type == pg.MOUSEBUTTONDOWN:
            if game_state == "playing":
                # Проверяем, что у игрока достаточно монет (не меньше 50),
                # клетка на карте "place tower" (значение 2), и на выбранной клетке нет башни
                if (
                    coins[0] >= 50
                    and map_game[grid_y // pixel][grid_x // pixel] == 2
                    and not any(t["x"] == grid_x and t["y"] == grid_y for t in towers)
                ):
                    # Добавляем новую башню в список towers с координатами и параметрами
                    towers.append(
                        {
                            "x": grid_x,  # Координата по оси X
                            "y": grid_y,  # Координата по оси Y
                            "cx": grid_x + pixel // 2,  # Центр по X
                            "cy": grid_y + pixel // 2,  # Центр по Y
                            "range": 150,  # Радиус действия башни
                            "cooldown": 1000,  # Время перезарядки (в миллисекундах)
                            "last_shot": 0,  # Время последнего выстрела (для отслеживания перезарядки)
                        }
                    )
                    coins[0] -= 50  # Снимаем 50 монет с игрока для строительства башни
            else:
                restart_game()  # Вызываем функцию рестарта игры

    # Возвращаем True, чтобы продолжить выполнение игры
    return True


def spawn_enemies(game_state, path, pixel, enemies, wave, max_wave_size, spawn_time):
    if game_state != "playing":
        return spawn_time

    # Получаем текущее время в миллисекундах с начала работы программы
    current_time = pg.time.get_ticks()

    # Если прошло больше 3000 миллисекунд с последнего спауна врага и количество врагов в текущей волне
    # меньше максимального размера волны, спавним нового врага
    if current_time - spawn_time > 3000 and len(wave) < max_wave_size:
        enemies.append(
            {
                "path": path,  # Путь, по которому враг будет двигаться
                "current_index": 0,  # Индекс текущей точки пути
                "x": path[0][0] * pixel + pixel // 2,  # Начальная позиция по оси X
                "y": path[0][1] * pixel + pixel // 2,  # Начальная позиция по оси Y
                "speed": 2,  # Скорость врага
                "hp": 4,  # Текущее количество здоровья врага
                "max_hp": 4,  # Максимальное количество здоровья
                "radius": pixel // 2 - 2,  # Радиус врага (определяет его размер)
                "reward": 10,  # Награда за уничтожение этого врага
            }
        )

        wave.append(1)
        # Возвращаем текущее время для использования при следующем проверке спауна
        return current_time

    # Если спавн не произошел, возвращаем время последнего спауна без изменений
    return spawn_time


def update_game_state(player_hp, wave, max_wave_size, enemies):
    if player_hp <= 0:
        return "game_over"
    if len(wave) >= max_wave_size and len(enemies) == 0 and player_hp > 0:
        return "victory"
    return "playing"


def draw_interface(screen, player_hp, coins):
    draw_text(screen, f"HP: {player_hp}", 36, (255, 255, 255), 100, 30)
    draw_text(screen, f"Coins: {coins[0]}", 36, (255, 215, 0), 800, 30)


def draw_towers(screen, towers, pixel):
    for tower in towers:
        tower_img = pg.image.load("FinalProject\img\\tower.png")
        tower_img = pg.transform.scale(tower_img, (pixel, pixel))
        screen.blit(tower_img, (tower["cx"] - pixel // 2, tower["cy"] - pixel // 2))


def draw_bullets(screen, bullets):
    for bullet in bullets:
        pg.draw.circle(screen, (255, 255, 0), (int(bullet["x"]), int(bullet["y"])), 5)


def draw_enemies(screen, enemies, pixel):
    for enemy in enemies:
        monster = pg.image.load("FinalProject\img\monster.png")
        monster = pg.transform.scale(monster, (pixel, pixel))
        screen.blit(monster, (enemy["x"] - pixel // 2, enemy["y"] - pixel // 2))

        # Полоска HP
        hp_width = 40
        hp_height = 6
        border = 1
        hp_x = enemy["x"] - hp_width // 2
        hp_y = enemy["y"] - enemy["radius"] - 15
        pg.draw.rect(
            screen,
            (50, 50, 50),
            (
                hp_x - border,
                hp_y - border,
                hp_width + 2 * border,
                hp_height + 2 * border,
            ),
        )
        current_hp_width = (enemy["hp"] / enemy["max_hp"]) * hp_width
        pg.draw.rect(screen, (200, 0, 0), (hp_x, hp_y, hp_width, hp_height))
        pg.draw.rect(screen, (0, 200, 0), (hp_x, hp_y, current_hp_width, hp_height))


def main():
    pg.init()
    # Размер пикселя карты
    pixel = 60
    map_data = {"water": 0, "road": 1, "place_tower": 2}
    # Создание окна для игры
    screen = creating_window()
    # Контроль времени (тики)
    clock = pg.time.Clock()

    # Инициализация данных игры
    game_data = init_game()
    player_hp = game_data["player_hp"]
    coins = game_data["coins"]
    wave = game_data["wave"]
    max_wave_size = game_data["max_wave_size"]
    enemies = game_data["enemies"]
    towers = game_data["towers"]
    bullets = game_data["bullets"]
    spawn_time = game_data["spawn_time"]
    game_state = game_data["game_state"]

    def restart_game():
        # Обновление всех данных игры при перезапуске
        nonlocal game_data, player_hp, coins, wave, enemies, towers, bullets, spawn_time, game_state
        game_data = init_game()
        player_hp = game_data["player_hp"]
        coins = game_data["coins"]
        wave = game_data["wave"]
        enemies = game_data["enemies"]
        towers = game_data["towers"]
        bullets = game_data["bullets"]
        spawn_time = game_data["spawn_time"]
        game_state = game_data["game_state"]

    while True:
        # Игровой цикл, когда игра в процессе
        if game_state == "playing":
            dt = clock.tick(60)  # Ограничение на 60 fps
            current_time = pg.time.get_ticks()  # Время с начала игры

            # Чтение карты и нахождение пути
            map_game = read_map()
            path = find_path(map_game)

            # Отрисовка карты игры
            draw_map(map_game, pixel, screen, map_data)

            # Обновление состояния игры: спаун врагов, волны и т.д.
            spawn_time = spawn_enemies(
                game_state, path, pixel, enemies, wave, max_wave_size, spawn_time
            )
            game_state = update_game_state(player_hp, wave, max_wave_size, enemies)

            # Обработка врагов
            for enemy in enemies[:]:
                if update_enemy(enemy, pixel):
                    player_hp -= 5  # Потеря жизни игроком
                    enemies.remove(enemy)  # Удаление врага

            # Логика башен и снарядов
            tower_intellect(towers, enemies, bullets, current_time)
            update_bullets(bullets, enemies, coins)  # Обновление состояния снарядов

            # Отрисовка врагов, башен, снарядов и интерфейса на экране
            draw_enemies(screen, enemies, pixel)
            draw_towers(screen, towers, pixel)
            draw_bullets(screen, bullets)
            draw_interface(screen, player_hp, coins)

            pg.display.flip()  # Обновление экрана

        else:  # Если игра завершена, обработка экрана завершения
            if game_state == "game_over":
                game_over_screen(screen)  # Экран с сообщением о проигрыше
            else:
                victory_screen(screen)  # Экран с сообщением о победе

        # Обработка событий
        if not handle_events(game_state, towers, map_game, coins, pixel, restart_game):
            return


main()
