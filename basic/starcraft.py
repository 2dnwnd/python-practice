from random import *

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print('{} 유닛이 생성되었습니다.'.format(name))

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 마린
class Marine(AttackUnit):
    def __init__(self):
        super().__init__('마린', 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print('{} : 스팀팩을 사용합니다. (HP 10감소)'.format(self.name))
        else:
            print('{} : 체력이 부족하여 스팀팩을 사용할 수 없습니다.'.format(self.name))

class Tank(AttackUnit):
    seize_developed = False
    
    def __init__(self):
        super().__init__('탱크', 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        if self.seize_mode == False:
            print('{} : 시즈모드로 전환합니다.'.format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print('{} : 시즈모드로 해제합니다.'.format(self.name))
            self.damage /= 2
            self.seize_mode = False

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        super().__init__('레이스', 80, 20, 5)
        self.clocked = False
    
    def clocking(self):
        if self.clocked == True:
            print('{} : 클로킹 모드를 해제합니다.'.format(self.name))
            self.clocked = False
        else:
            print('{} : 클로킹 모드로 전환합니다.'.format(self.name))
            self.clocked = True

# 게임 시작
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

# 게임 종료
def game_over():
    print("Player : gg") # good game
    print("[Player] 님이 게임에서 퇴장하셨습니다.")


game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move('1시')

Tank.seize_developed = True
print('탱크 시즈모드 개발 완료')

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack('1시')

for unit in attack_units:
    unit.damaged(randint(5,21))
    
game_over()