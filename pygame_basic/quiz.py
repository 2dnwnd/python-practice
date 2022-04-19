import pygame
########################################################################
# # 기본 초기화 (반드시 필요)
pygame.init() 

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정 (게임 이름 창에다가)
pygame.display.set_caption('DDong Game')

# FPS
clock = pygame.time.Clock()
########################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)

# 배경 이미지 불러오기
background = pygame.image.load('C:/Users/dnwnd/OneDrive/바탕 화면/PythonWorkspace/pygame_basic/background.png')

# 캐릭터 불러오기
character = pygame.image.load('C:/Users/dnwnd/OneDrive/바탕 화면/PythonWorkspace/pygame_basic/character.png')
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
# 캐릭터 처음 위치 조정
character_x_pos = (screen_width - character_width) / 2 
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0

# 이동 속도
character_speed = 5
enemy_speed = 5

# 적 enemy 캐릭터
from random import *
enemy = pygame.image.load('C:/Users/dnwnd/OneDrive/바탕 화면/PythonWorkspace/pygame_basic/enemy.png')
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randrange(0,410)
enemy_y_pos = 0


# 이벤트 루프 (키보드나 마우스 입력이 있어야 창이 안꺼짐)
running = True
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 이벤트가 발생했는지
        if event.type == pygame.QUIT: # 창닫기 눌렀을때
            running = False

        if event.type == pygame.KEYDOWN: # 키가 눌리면
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP: # 키보드를 누르지않을때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
        
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x
    # 캐릭터가 벽에 나가지 않도록 제한
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = randrange(0,410)

    # 4. 충동 처리
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print('충돌했어요')
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    pygame.display.update() # 화면을 계속 그리기

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기

# pygame 종료
pygame.quit()