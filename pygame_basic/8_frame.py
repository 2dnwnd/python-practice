import pygame
########################################################################
# # 기본 초기화 (반드시 필요)
pygame.init() 

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정 (게임 이름 창에다가)
pygame.display.set_caption('Nado Game')

# FPS
clock = pygame.time.Clock()
########################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)

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

    pygame.display.update()
  
# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기


# pygame 종료
pygame.quit()