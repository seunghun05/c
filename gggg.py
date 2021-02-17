import pygame

pygame.init()

screen = pygame.display.set_mode((500,200))
pygame.display.set_caption('Hello pygameeeee!')

BLACK=(0,0,0); WHITE=(255,255,255); RED=(255,0,0); GREEN=(0,255,0)

class Circle:

    def __init__(self, x, y, r):
        self.x = x;
        self.y = y;
        self.r = r;

    def drawing(self):
        pygame.draw.circle(screen,GREEN,(self.x,self.y),self.r,0)

c1=Circle(250,100,30)

screen.fill(WHITE)
pygame.display.update()
while True:
    

 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            
            
            if event.key == pygame.K_RIGHT:
                
                c1.x+=5
                c1.drawing()
       
            if event.key == pygame.K_LEFT:
                
                c1.x-=5
                c1.drawing()
       
            if event.key == pygame.K_UP:
                c1.y-=5
                c1.drawing()
        
            if event.key == pygame.K_DOWN:
                c1.y+=5
                c1.drawing()
    pygame.display.update()


    pygame.display.update()
