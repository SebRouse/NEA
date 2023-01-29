import pygame


board=[["TWS",None,None,"DLS",None,None,None,"TWS",None,None,None,"DLS",None,None,"TWS"],
[None,"DWS",None,None,None,"TLS",None,None,None,"TLS",None,None,None,"DWS",None],
[None,None,"DWS",None,None,None,"DLS",None,"DLS",None,None,None,"DWS",None,None],
["DLS",None,None,"DWS",None,None,None,"DLS",None,None,None,"DWS",None,None,"DLS"],
[None,None,None,None,"DWS",None,None,None,None,None,"DWS",None,None,None,None],
[None,"TLS",None,None,None,"TLS",None,None,None,"TLS",None,None,None,"TLS",None],
[None,None,"DLS",None,None,None,"DLS",None,"DLS",None,None,None,"DLS",None,None],
["TWS",None,None,"DLS",None,None,None,"DWS",None,None,None,"DLS",None,None,"TWS"],
[None,None,"DLS",None,None,None,"DLS",None,"DLS",None,None,None,"DLS",None,None],
[None,"TLS",None,None,None,"TLS",None,None,None,"TLS",None,None,None,"TLS",None],
[None,None,None,None,"DWS",None,None,None,None,None,"DWS",None,None,None,None],
["DLS",None,None,"DWS",None,None,None,"DLS",None,None,None,"DWS",None,None,"DLS"],
[None,None,"DWS",None,None,None,"DLS",None,"DLS",None,None,None,"DWS",None,None],
[None,"DWS",None,None,None,"TLS",None,None,None,"TLS",None,None,None,"DWS",None],
["TWS",None,None,"DLS",None,None,None,"TWS",None,None,None,"DLS",None,None,"TWS"]]

rack=["R","A","B","G","H","Z","A"]
FPS =30
pygame.init()
screen = pygame.display.set_mode((1200,765))

movesStack =[]

pygame.display.set_caption("Scrabble - Play Scrabble")
running = True
board_tiles = [[0 for row in range(15)] for col in range(15)]
block_size = 50

buttonColourLight = (229,229,229)
buttonColourDark=(122, 122, 122)

font = pygame.font.SysFont(None, 24)
tileFont =pygame.font.SysFont(None,36)
titleFont=pygame.font.SysFont(None,48)
titleFont.set_underline(True)

UIrack=[]
for i in range(len(rack)):
    txt = tileFont.render(rack[i],True,(0,0,0))
    rec = pygame.Rect(765+40+(block_size+1)*i,300,block_size,block_size)
    UIrack.append((txt,rec))
    pygame.draw.rect(screen,buttonColourLight,rec)
    screen.blit(txt,(765+40+(block_size+1)*i+15,300+10))

rectangle_draging=False


def drawBackround():
    screen.fill((0,0,0))
    colour=(255,255,255)
    for row in range(len(board_tiles)):
        for col in range(len(board_tiles[0])):
            if board[row][col]=="TWS":
                txt = font.render("DWS",True,(0,0,0))
                colour=(40,78,96)

            elif board[row][col]=="DWS" and row != 7 and col !=7:
                colour=(49,155,118) 
                txt = font.render("DWS",True,(0,0,0))
                
            elif board[row][col]=="DLS":
                txt = font.render("DLS",True,(0,0,0))
                colour=(217,89,128)
            elif board[row][col] =="TLS":
                txt = font.render("TLS",True,(0,0,0))
                colour=(99,170,192)
            elif row==7 and col == 7:
                txt = font.render("Start",True,(0,0,0))
                colour =(249,155,69)
            else:
                txt = font.render("",True,(0,0,0))
                colour=(255,255,255)

            rect = pygame.Rect(col*(block_size+1), row*(block_size+1), block_size, block_size)

            pygame.draw.rect(screen, colour, rect)

            screen.blit(txt,((block_size+1)*col+6,(block_size+1)*row+15))

    img = font.render('Player1 Points:', True, (255,255,255))





    screen.blit(img, (765, 60))
    img=font.render('Player2 Points:',True,(255,255,255))
    screen.blit(img,(765,90))
    turn = 1
    img = titleFont.render(f"Player{turn}'s turn",True,(255,255,255))
    screen.blit(img,(865,10))


drawBackround()
clock = pygame.time.Clock()

TileDragged=None
startCoords=None


pygame.display.update()
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            ###drag and drop##
            for i in range(len(UIrack)):
                txt,rectangle=UIrack[i]


                

                if rectangle.collidepoint(event.pos):
                    
                    TileDragged =i
                    rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle.x - mouse_x
                    offset_y = rectangle.y - mouse_y

                    startCoords = (rectangle.x,rectangle.y)



            ####Undo button###
            if (883+200)>=mousePos[0]>=883 and (440+50)>= mousePos[1]>=440 :
                if len(movesStack) != 0:
                    rectangle,endCoords,startCoords = movesStack.pop()
                    rectangle.x = startCoords[0]
                    rectangle.y = startCoords[1]


            ####next turn button#####
            if (883+200)>=mousePos[0]>=883 and (380+50)>= mousePos[1]>=380:
                rack=["B","Z","R","H","U","T","S"]
                UIrack=[]
                for i in range(len(rack)):
                    txt = tileFont.render(rack[i],True,(0,0,0))
                    rec = pygame.Rect(765+40+(block_size+1)*i,300,block_size,block_size)
                    UIrack.append((txt,rec))
            

                
                


        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                txt,rectangle=UIrack[TileDragged]
                mouse_x, mouse_y = event.pos
                rectangle.x = mouse_x + offset_x
                rectangle.y = mouse_y + offset_y  
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if rectangle_draging:
            
                txt,rectangle=UIrack[TileDragged]
                mouse_x, mouse_y = event.pos
                if  (mouse_y + offset_y)//(block_size+1)*(block_size+1) <0 :
                    ycoord=0
                elif (mouse_y + offset_y)//(block_size+1)*(block_size+1) >=15*(block_size+1):
                    ycoord = 15*(block_size+1)
                else:
                    ycoord = (mouse_y + offset_y)//(block_size+1)*(block_size+1) 
                
                if (mouse_x + offset_x)//(block_size+1)*(block_size+1) <0:
                    xcoord =0
                else:
                    xcoord=(mouse_x + offset_x)//(block_size+1)*(block_size+1)


                if 765-block_size>=(mouse_x + offset_x)//(block_size+1)*(block_size+1)>=0:
                    rectangle.x = xcoord
                    rectangle.y = ycoord
                else:
                    rectangle.x =765+40+(block_size+1)*TileDragged
                    rectangle.y = 300

                movesStack.append((rectangle,(rectangle.x,rectangle.y),(startCoords)))

                
    
            rectangle_draging = False      

    drawBackround()
        

    for i in range(len(UIrack)):
        txt,rectangle=UIrack[i]
        
        pygame.draw.rect(screen,buttonColourLight,rectangle)
        screen.blit(txt,(rectangle.x+15,rectangle.y+10))



    clock.tick(FPS)







    mousePos=pygame.mouse.get_pos()

    ###Next Turn Button###
    if (883+200)>=mousePos[0]>=883 and (380+50)>= mousePos[1]>=380:
        pygame.draw.rect(screen,buttonColourDark,[883,380,200, 50])
    else:
        pygame.draw.rect(screen,buttonColourLight,[883,380,200, 50])
    txt =font.render('Next Turn',True,(0,0,0))
    screen.blit(txt,(945,397))

    ###Undo Button###
    if (883+200)>=mousePos[0]>=883 and (440+50)>= mousePos[1]>=440:
        pygame.draw.rect(screen,buttonColourDark,[883,440,200, 50])
    else:
        pygame.draw.rect(screen,buttonColourLight,[883,440,200, 50])
    txt = font.render("Undo",True,(0,0,0))
    screen.blit(txt,(960,457))



    ###Pass Turn Button###
    if (883+200)>=mousePos[0]>=883 and (500+50)>= mousePos[1]>=500:
        pygame.draw.rect(screen,buttonColourDark,[883,500,200, 50])
    else:
        pygame.draw.rect(screen,buttonColourLight,[883,500,200, 50])
    txt = font.render("Pass",True,(0,0,0))
    screen.blit(txt,(960,517))


    ###Save Game and Exit Button####
    if (883+200)>=mousePos[0]>=883 and (700+50)>= mousePos[1]>=700:
        pygame.draw.rect(screen,buttonColourDark,[883,700,200, 50])
    else:
        pygame.draw.rect(screen,buttonColourLight,[883,700,200, 50])
    txt= font.render("Save Game & Exit",True,(0,0,0))
    screen.blit(txt,(913,717))





    pygame.display.update()