from input_box import Box
from button import Button
from data import animals_list, places_list
from random import choice
import pygame, sys

rows_no = 0

# ------basic setup-----
pygame.init()
screen_width = 800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('npat')
clock = pygame.time.Clock()
run = True

# -------Font setup-------
# rock_3d = 'Font/Rock3D-Regular.ttf'
island_moments = 'Font/IslandMoments-Regular.ttf'
mochiy = 'Font/MochiyPopPOne-Regular.ttf'
lena = 'Font/Lena.ttf'
audry = 'Font/Audrey-Normal.otf'
# caviar = 'Font/CaviarDreams.ttf'
# caviar_font = pygame.font.Font(caviar,30)
# audry_font = pygame.font.Font(audry,30)

font = pygame.font.Font(None, 30)
font_size = 30
pc_font = pygame.font.Font(island_moments,50)
user_font = pygame.font.Font(lena,font_size)
name_f,place_f,animal_f,thing_f = pc_font.render('Name',True,'white'), pc_font.render('Place',True,'white'), pc_font.render('Animal',True,'white'), pc_font.render('Thing',True,'white')

# -------basic ui-------
hotizontal_border = pygame.surface.Surface((screen_width,10))
hotizontal_border.fill('white')

border_surface = pygame.surface.Surface((10,screen_height))
border_surface.fill('white')
border_coordinate=[]

text_x = []
text_width = screen_width/4
box_height = screen_height/8

box_width = text_width
offset = text_width/4
offset_y = 100
boxes_coordinate = []

current_row = 0
current_column = 0

for i in range(3):
    text_x.append(text_width+i*text_width)
    border_coordinate.append((text_width+i*text_width,100))
for i in range(3):
    for j in range(6):
        if i == 1:
            boxes_coordinate.append((text_width+offset-20,box_height+j*box_height+offset_y))
        if i % 4 == 0:
            boxes_coordinate.append((offset-20,box_height+j*box_height+offset_y))
        else:
            boxes_coordinate.append((text_width+ i*text_width + offset -20,box_height+j*box_height+offset_y))

boxes = []
boxes_bottom = []
for i in range(len(boxes_coordinate)):
    boxes.append(Box(screen,boxes_coordinate[i],text_width-offset,100,text_width/2,5,'haha'))
    boxes[i].create_box()
    boxes_bottom.append(boxes[i].bottom)


# -------User input-------
user_text = []
user_fonts = []
user_text_surf = []
user_font_surf = []
font_sizes = []
active = []
a_index = []

current_y= box_height+current_row*box_height+offset_y
current_xs = []
current_x = 50

change_box = False

for i in range(len(boxes)):
    user_text.append('')
    font_sizes.append(30)
    user_fonts.append(pygame.font.Font(lena,font_sizes[i]))
    if i == 0:
        active.append(True)
    else:
        active.append(False)

dbclock = pygame.time.Clock()
DOUBLECLICKTIME = 500

def current_xy():
    for i in boxes_coordinate:
        if i[1] == current_y:
            current_xs.append(boxes_coordinate.index(i))
current_xy()

for i in user_text:
    user_text_surf.append(user_font.render(i,True,'white'))

# buttons
submit = Button('Submit',100,40, (20,50),6,screen,font)
replay = Button('Replay',100,40, (140,50),6,screen,font)


# ????
alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
'O','P','Q','R','S','T','U','V','W','X','Y','Z']
current_alphatbet = choice(alphabets)
alphabet_font = pygame.font.Font(mochiy,90)
alphabet_surf = alphabet_font.render(current_alphatbet,True,'#C8DF52')

def check_dups(list_):
    seen = set()
    dupes = []
    for x in list_:
        if x in seen:
            dupes.append(x)
        else:
            seen.add(x)
    return dupes

# things
game_over=False
score_font = pygame.font.Font(None,50)
score = 0

submit_timer = pygame.USEREVENT
submit_delay = 1000
pygame.time.set_timer(submit_timer, submit_delay)
counter = 70
original_counter = counter

def do_replay():
    global current_row,game_over,current_alphatbet,score,submit_delay,counter,original_counter
    for i in user_text:
        user_text[user_text.index(i)] = ''
    current_row = 0
    for i in boxes:
        i.color_a = pygame.Color('lightskyblue3')
        i.color_p = pygame.Color('gray15')
    for i in active:
        active[active.index(i)] = False
    game_over = False
    current_alphatbet = choice(alphabets)
    score = 0
    counter = 70
    original_counter = counter
    submit_delay = 1000
    pygame.time.set_timer(submit_timer, submit_delay)

def do_submit():
    global current_y, score,current_alphatbet, current_row,game_over,counter,original_counter
    for i in boxes_coordinate:
        if i[1] == current_y:
            word = user_text[boxes_coordinate.index(i)]
            if i[0] == 230:
                dup_ans = check_dups(user_text)
                if ((word.lower() in places_list) and (word[0].lower() == current_alphatbet.lower())and (word.lower() not in dup_ans)):
                    boxes[boxes_coordinate.index(i)].color_p = 'green'
                    score += 10

                else:
                    boxes[boxes_coordinate.index(i)].color_p = 'red'
            elif i[0] == 430:
                dup_ans = check_dups(user_text)
                if ((word.lower() in animals_list) and (word[0].lower() == current_alphatbet.lower()) and (word.lower() not in dup_ans)):
                    boxes[boxes_coordinate.index(i)].color_p = 'green'
                    score += 10
                else:
                    boxes[boxes_coordinate.index(i)].color_p = 'red'
            else:
                dup_ans = check_dups(user_text)
                if ((len(word)>2)and(word.lower()!= '') and (word.lower() not in dup_ans) and (set(word.lower()) != ' ') and (word[0].lower() == current_alphatbet.lower())):
                    score += 10
                    boxes[boxes_coordinate.index(i)].color_p = 'green'
                else:
                    boxes[boxes_coordinate.index(i)].color_p = 'red'


    for i in active:
        if i:
            active[active.index(i)] = False
    if current_row != 5:
        current_row +=1
        if current_row % 2 == 0:
            counter = original_counter
            counter -= 20
            original_counter = counter
        else:
            counter = original_counter
        current_y= box_height+current_row*box_height+offset_y
        for i in current_xs:
            active[i] = False
        current_xs.clear()
        current_xy()
        active[current_xs[0]] = True
        current_alphatbet = choice(alphabets)
    else:
        game_over = True

# main loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == submit_timer:
            if not game_over:
                counter -= 1
            else:
                counter = 0
            if counter <= 0:
                do_submit()
                

        if event.type == pygame.MOUSEBUTTONDOWN:
            if dbclock.tick() < DOUBLECLICKTIME:
                for i in boxes:
                    if i.box_rect.y == current_y:
                        if i.box_rect.collidepoint(event.pos):
                            active[boxes.index(i)] = True
                            
                        else:
                            active[boxes.index(i)] = False

        if event.type == pygame.KEYDOWN:
            if event.key != pygame.K_RETURN:
                for i in active:
                        if i:
                            if event.key == pygame.K_BACKSPACE:
                                user_text[active.index(i)] = user_text[active.index(i)][:-1]
                                if font_sizes[active.index(i)] < 30:
                                    font_sizes[active.index(i)] += 1
                                    user_fonts[active.index(i)] = pygame.font.Font(lena,font_sizes[active.index(i)])
                                    
                            elif not len(user_text[active.index(i)]) >= 100:
                                user_text[active.index(i)] += event.unicode

            if event.key ==  pygame.K_RETURN:

                for i in active:
                    for j in current_xs:
                        if i:
                            if change_box:
                                if ((active.index(i) == j) and (current_xs.index(j) != 3)):
                                    ab = current_xs[current_xs.index(j)+1]
                                    active[ab] = True
                                    active[j] = False
                                    change_box = False
                        else:
                            change_box = True
    if game_over:
        current_y = 0
        for i in active:
            active[active.index(i)]=False
    else:
        current_y= box_height+current_row*box_height+offset_y

    screen.fill((0,0,0))

    # border
    screen.blit(hotizontal_border, (0,0))
    screen.blit(hotizontal_border, (0,100))
    screen.blit(hotizontal_border, (0,200))

    screen.blit(border_surface,(0,0))
    screen.blit(border_surface,border_coordinate[0])
    screen.blit(border_surface,border_coordinate[1])
    screen.blit(border_surface,border_coordinate[2])
    screen.blit(border_surface,(screen_width-10,0))

    # font
    screen.blit(name_f,(text_width/2-name_f.get_width()/2,150-name_f.get_height()/2))
    screen.blit(place_f,(text_x[0]+text_width/2-name_f.get_width()/2,150-name_f.get_height()/2))
    screen.blit(animal_f,(text_x[1]+text_width/2-name_f.get_width()/2,150-name_f.get_height()/2))
    screen.blit(thing_f,(text_x[2]+text_width/2-name_f.get_width()/2,150-name_f.get_height()/2))

    # User Input
    for surf in user_text_surf:
        temp = user_text_surf.index(surf)
        surf = user_fonts[user_text_surf.index(surf)].render(user_text[user_text_surf.index(surf)],True,'white')
        screen.blit(surf,(boxes_coordinate[temp][0]+10,boxes_coordinate[temp][1]+35))

        if surf.get_width() > text_width-offset-10:
            font_sizes[temp]-=1
            user_fonts[temp] = pygame.font.Font(lena,font_sizes[temp])

    # Buttons
    submit.draw()
    submitted = submit.check_click()

    replay.draw()
    replay_click = replay.check_click()

    if replay_click:
        do_replay()

    if submitted:
        do_submit()

    # Things
    alphabet_surf = alphabet_font.render(current_alphatbet,True,'#C8DF52')
    screen.blit(alphabet_surf,(screen_width/2-alphabet_surf.get_width()/2,-20))
    
    score_surf = score_font.render(f'Score: {score}', True, 'white')
    screen.blit(score_surf,(590,10))

    timer_surf = score_font.render(f'Time left: {counter}',True,'white')
    screen.blit(timer_surf,(590,60))

    # Boxes
    for i in boxes:
        i.draw1()
        i.update()
        if i.bottom > max(boxes_bottom):
            boxes_bottom.append(i.bottom)

        if active[boxes.index(i)]:
            i.color = i.color_a
        else:
            i.color = i.color_p

    pygame.display.flip()
    clock.tick(60)
