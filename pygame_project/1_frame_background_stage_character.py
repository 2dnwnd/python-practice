import pygame
import os
########################################################################
# # 기본 초기화 (반드시 필요)
pygame.init() 

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정 (게임 이름 창에다가)
pygame.display.set_caption('Nado Pang')

# FPS
clock = pygame.time.Clock()
########################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치를 반환
image_path = os.path.join(current_path, 'images') # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, 'background.png'))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, 'stage.png'))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, 'character.png'))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
charachter_x_pos = (screen_width-character_width) / 2
charachter_y_pos = screen_height -character_height - stage_height

# 이벤트 루프 (키보드나 마우스 입력이 있어야 창이 안꺼짐)
running = True
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정

    # print('fps :',clock.get_fps())
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    # 3. 게임 캐릭터 위치 정의

    # 4. 충동 처리

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(stage, (0,screen_height-stage_height))
    screen.blit(character, (charachter_x_pos,charachter_y_pos))

    pygame.display.update()

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기

# pygame 종료
pygame.quit()