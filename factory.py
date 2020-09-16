from enum import Enum

class EnemyType:
    MINION = 'MINION'
    FIGHTER = 'FIGHTER'
    BOSS = 'BOSS'

class Enemy:
    def __init__(self, enemy_type, hp, power):
        self.type = enemy_type
        self.hp = hp
        self.power = power

    def __repr__(self):
        return f'{self.type}(hp={self.hp}, power={self.power})'

    def take_damage(self, damage: int) -> None:
        self.hp -= damage


class Boss(Enemy):
    def __init__(self):
        super().__init__(EnemyType.BOSS, 100, 100)

class Fighter(Enemy):
    def __init__(self):
        super().__init__(EnemyType.FIGHTER, 50,50)

class Minion(Enemy):
    def __init__(self):
        super().__init__(EnemyType.MINION, 10,10)

class EnemyFactory:
    def get(self, type: EnemyType) -> Enemy:
        if type == EnemyType.BOSS:
            return Boss()
        elif type == EnemyType.FIGHTER:
            return Fighter()
        elif type == EnemyType.MINION:
            return Minion()
        

if __name__ == '__main__':
    enemy_factory = EnemyFactory()

    minion = enemy_factory.get(EnemyType.MINION)
    boss = enemy_factory.get(EnemyType.BOSS)
    
    print(minion)
    print(boss)
    
    
