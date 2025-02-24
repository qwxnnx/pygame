import pygame

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Game')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
bg = pygame.image.load('images/bg2.jpg')



walk_right = [
    pygame.image.load('images/wrr.png'),
    pygame.image.load('images/wrr1.png'),
    pygame.image.load('images/wrr2.png'),
    pygame.image.load('images/wrr3.png'),
]
walk_left = [
    pygame.image.load('images/wll.png'),
    pygame.image.load('images/wll1.png'),
    pygame.image.load('images/wll2.png'),
    pygame.image.load('images/wll3.png'),
]


ghost = pygame.image.load('images/gh.png')


ghost_list = []

player_anim_count = 0
bg_x = 0

player_speed = 7
player_x = 150
player_y = 415

is_jump = False
jump_count = 10

bg_sound = pygame.mixer.Sound('bg.mp3')
bg_sound.play()


ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 5000)

label = pygame.font.Font('fonts/mont.ttf', 60)
lose_label = label.render('YOU LOST', False, (193, 196,199))
re_label = label.render('Restart', False, (193, 196,199))
re_label_rect = re_label.get_rect(topleft=(300, 300))

gameplay = True

running = True
while running:
    screen.blit(bg,(bg_x, 0))
    screen.blit(bg,(bg_x + 800, 0))
    
    if gameplay:
    
    
       player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
    
       if ghost_list:
            for (i, el) in enumerate(ghost_list):
                screen.blit(ghost, el)
                el.x -= 10

                if el.x < -20:
                    ghost_list.pop(i)

                if player_rect.colliderect(el):
                   gameplay = False

       keys = pygame.key.get_pressed()
       if keys[pygame.K_LEFT]:
          screen.blit(walk_left[player_anim_count],(player_x, player_y))
       else:
          screen.blit(walk_right[player_anim_count],(player_x, player_y))

       if keys[pygame.K_LEFT] and player_x > 90:
           player_x -= player_speed
       elif keys[pygame.K_RIGHT] and player_x < 650:
           player_x += player_speed     

       if not is_jump:
           if keys[pygame.K_SPACE]:
               is_jump = True
       else:
           if jump_count >= -10:
               if jump_count > 0:
                 player_y -= (jump_count ** 2) / 2
               else:
                   player_y += (jump_count ** 2) / 2
               jump_count -= 1
           else:
               is_jump = False
               jump_count = 10        


       if player_anim_count == 3:
           player_anim_count = 0
       else:
           player_anim_count += 1
    
       bg_x -= 2
       if bg_x == -800:
           bg_x = 0

    else:
        screen.fill((33, 33, 78))
        screen.blit(lose_label, (260, 150)) 
        screen.blit(re_label, re_label_rect)  


        mouse = pygame.mouse.get_pos()
        if re_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            ghost_list.clear()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list.append(ghost.get_rect(topleft=(820, 430)))
             
    clock.tick(10)        
           