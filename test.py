import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
bgColor = (51, 153, 255)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

#pygame.display.update() 

gameExit = False

while not gameExit:
  for event in pygame.event.get():
    #print(event)
    if event.type == pygame.QUIT:
      gameExit = True
    
  gameDisplay.fill(bgColor)
  pygame.display.update()

pygame.quit()
quit()

