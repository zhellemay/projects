import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VIOLET = (127, 0, 255)
PINK1 = (219, 119, 141)
PINK2 = (255, 56, 152)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader Game by Pulla and Suarez")

player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
bullet_img = pygame.image.load("bullet.png")
boss_img = pygame.image.load("boss.png")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)


class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = BLACK

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, PINK1)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect.topleft)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


class Player:
    def __init__(self):
        self.image = pygame.transform.scale(player_img, (50, 50))
        self.x = WIDTH // 2 - 25
        self.y = HEIGHT - 70
        self.speed = 5
        self.health = 50

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - 50:
            self.x += self.speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        health_text = font.render(f"Player HP: {self.health}", True, PINK2)
        screen.blit(health_text, (10, 40))

    def take_damage(self):
        self.health -= 1


class Enemy:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(enemy_img, (40, 40))
        self.x = x
        self.y = y
        self.speed = 3
        self.direction = 1

    def move(self):
        self.x += self.speed * self.direction
        if self.x >= WIDTH - 40 or self.x <= 0:
            self.direction *= -1
            self.y += 40

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Bullet:
    def __init__(self, x, y, speed=-7):
        self.image = pygame.transform.scale(bullet_img, (10, 20))
        self.x = x + 20
        self.y = y
        self.speed = speed
        self.active = True

    def move(self):
        self.y += self.speed
        if self.y < 0 or self.y > HEIGHT:
            self.active = False

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Boss:
    def __init__(self):
        self.image = pygame.transform.scale(boss_img, (100, 100))
        self.x = WIDTH // 2 - 50
        self.y = 50
        self.speed = 2
        self.health = 100
        self.direction = 1
        self.bullets = []

    def move(self):
        self.x += self.speed * self.direction
        if self.x >= WIDTH - 100 or self.x <= 0:
            self.direction *= -1

    def fire(self):
        if random.randint(1, 15) == 1:
            self.bullets.append(Bullet(self.x + 45, self.y + 90, speed=5))

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        health_text = font.render(f"Boss HP: {self.health}", True, WHITE)
        screen.blit(health_text, (WIDTH - 220, 10))

    def take_damage(self):
        self.health -= 1


class SpaceInvaders:
    def __init__(self):
        self.player = Player()
        self.enemies = [Enemy(random.randint(50, WIDTH - 50), random.randint(50, 200)) for _ in range(5)]
        self.bullets = []
        self.enemy_count = 0
        self.boss = None
        self.running = True
        self.start_game = False
        self.start_button = Button(WIDTH // 2 - 50, HEIGHT // 2 + 50, 100, 50, "Start")

    def run(self):
        while self.running:
            screen.fill(BLACK)

            if not self.start_game:
                self.show_welcome_screen()
            else:
                self.handle_events()
                self.update()
                self.draw()

                if self.boss and self.boss.health <= 0:
                    self.display_message("WOW! YOU WIN!!", f"Total Points: {self.enemy_count}")
                    self.running = False

                if self.player.health <= 0:
                    self.display_message("GAME OVER!!", f"Total Points: {self.enemy_count}")
                    self.running = False

            pygame.display.update()
            clock.tick(60)

    def show_welcome_screen(self):
        screen.fill(PINK1)
        welcome_text = font.render("Welcome to Space Invader Game!", True, BLACK)
        screen.blit(welcome_text, (WIDTH // 2 - 200, HEIGHT // 2 - 100))
        self.start_button.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.is_clicked(event.pos):
                    self.start_game = True

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move("left")
        if keys[pygame.K_RIGHT]:
            self.player.move("right")
        if keys[pygame.K_SPACE]:
            self.bullets.append(Bullet(self.player.x, self.player.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        for enemy in self.enemies:
            enemy.move()

        for bullet in self.bullets:
            bullet.move()

        self.bullets = [b for b in self.bullets if b.active]
        for bullet in self.bullets:
            for enemy in self.enemies:
                if enemy.x < bullet.x < enemy.x + 40 and enemy.y < bullet.y < enemy.y + 40:
                    self.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    self.enemy_count += 1
                    self.enemies.append(Enemy(random.randint(50, WIDTH - 50), random.randint(50, 200)))
                    break

        if self.enemy_count >= 30:
            if not self.boss:
                self.boss = Boss()

            self.boss.move()
            self.boss.fire()

            for bullet in self.boss.bullets[:]:
                bullet.move()

                if (
                        self.player.x < bullet.x < self.player.x + 50
                        and self.player.y < bullet.y > self.player.y + 50
                ):
                    self.player.take_damage()
                    self.boss.bullets.remove(bullet)

                if bullet.y > HEIGHT:
                    self.boss.bullets.remove(bullet)

            for bullet in self.bullets:
                if self.boss.x < bullet.x < self.boss.x + 100 and self.boss.y < bullet.y < self.boss.y + 100:
                    self.boss.take_damage()
                    self.bullets.remove(bullet)

    def draw(self):
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()
        for bullet in self.bullets:
            bullet.draw()

        if self.boss:
            self.boss.draw()
            for bullet in self.boss.bullets:
                bullet.draw()

        score_text = font.render(f"Enemies Defeated: {self.enemy_count}", True, PINK2)
        screen.blit(score_text, (10,10))

    def display_message(self, message, subtext):
        screen.fill(PINK1)
        text = font.render(message, True, VIOLET)
        subtext = font.render(subtext, True, WHITE)
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
        screen.blit(subtext, (WIDTH // 2 - 100, HEIGHT // 2 + 20))
        pygame.display.update()
        pygame.time.delay(3000)

if __name__ == "__main__":
    game = SpaceInvaders()
    game.run()

    pygame.quit()