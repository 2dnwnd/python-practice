import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Nado Game')

# FPS
clock = pygame.time.Clock()

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
to_y = 0

# 이동 속도
character_speed = 0.5

# 이벤트 루프 (키보드나 마우스 입력이 있어야 창이 안꺼짐)
running = True
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정

    # print('fps :',clock.get_fps())
    for event in pygame.event.get(): # 이벤트가 발생했는지
        if event.type == pygame.QUIT: # 창닫기 눌렀을때
            running = False

        if event.type == pygame.KEYDOWN: # 키가 눌리면
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: # 키보드를 누르지않을때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0   

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 캐릭터가 벽에 나가지 않도록 제한
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    screen.blit(background, (0,0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 화면을 계속 그리기

# pygame 종료
pygame.quit()