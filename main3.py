import time
import random


class Player:
    def __init__(self, health=300, energy=300):  # constructor
        self.health = health
        self.energy = energy
        print(f'player created, health = {self.health}, energy = {self.energy}')

    def attack(self, target, damage, denergy):
        if not self.energy <= 0:
            target.health -= damage
            self.energy -= denergy

            time.sleep(2)
            print('\nplayer attacking')

            time.sleep(1)
            if target.health < 0:
                target.health = 0
            if self.energy < 0:
                self.energy = 0
            print(f'player status: {player.__dict__}')
            print(f'monster status: {monster.__dict__}')
        else:
            time.sleep(2)
            print("\nplayer out of energy")


class Monster:
    def __init__(self, health=300):
        self.health = health
        print(f'monster created, health = {self.health}')

    def attack(self, target, damage):
        target.health -= damage

        time.sleep(2)
        print('\nmonster attacking')

        time.sleep(1)
        if target.health < 0:
            target.health = 0
        print(f'player status: {player.__dict__}')
        print(f'monster status: {monster.__dict__}')


player = Player()
monster = Monster()

while not monster.health <= 0:

    if not player.health <= 0:
        player.attack(target=monster, damage=random.randint(13, 20), denergy=random.randint(15, 20))
    else:
        print('\nplayer lose')
        break

    if not monster.health <= 0:
        monster.attack(target=player, damage=random.randint(12, 20))
    else:
        pass
else:
    print('\nplayer win!!')
