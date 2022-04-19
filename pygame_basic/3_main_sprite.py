import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Nado Game')

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

# 이벤트 루프 (키보드나 마우스 입력이 있어야 창이 안꺼짐)
running = True
while running:
    for event in pygame.event.get(): # 이벤트가 발생했는지
        if event.type == pygame.QUIT: # 창닫기 눌렀을때
            running = False

    screen.blit(background, (0,0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 화면을 계속 그리기

# pygame 종료
pygame.quit()