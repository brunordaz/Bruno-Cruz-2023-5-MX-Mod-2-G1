from game.components.enemies.enemy_ship import EnemyShip

class EnemyHandler:
    MAX_ENEMIES = 5

    def __init__(self):
        self.enemies = []
        #self.enemies.append(EnemyShip())

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            if not enemy.is_alive:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self):
        if len(self.enemies) < self.MAX_ENEMIES:
            self.enemies.append(EnemyShip)

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
