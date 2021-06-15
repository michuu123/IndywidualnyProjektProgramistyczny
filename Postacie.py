import pygame, Pokoje as p

ekran = pygame.display.set_mode((1000,1000))

class bohater:
    def __init__(self):
        self.pokoj=0
        self.zycie=300
        self.pozycja=0
        self.x=240
        self.y=240
    def rzut(self):
        p.draw.rect(ekran,(255,255,0),(self.x,self.y,48,48),0)

class wrog:
    def __init__(self,a,b,c):
        self.pokoj=a
        self.zycie=100
        self.polozenie=b
        self.strzal=c
        self.martwy=0

    def rzut(self):
        p.draw.rect(ekran,(255,255,0),(self.x,self.y,48,48),0)


if __name__ == "__main__":
    import pygame
    print("elo")
    x = p.pokoj()
    y = p.pokoj()
    z = p.pokoj()
    z1 = p.pokoj()
    print("rozmiar x - " + str(x.rozmiar_x))
    print("rozmiar y - " + str(x.rozmiar_y))
    print("pozycja x - " + str(x.pozycja_x))
    print("pozycja y - " + str(x.pozycja_y))
    print(x.bok2x)
    print(x.bok2y)
    X=5
    Y=5

    

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            X-=1
        if keys[pygame.K_RIGHT]:
            X+=1
        if keys[pygame.K_DOWN]:
            Y+=1
        if keys[pygame.K_UP]:
            Y-=1
        ekran.fill((0,0,0))
        x.kolizja(1,3)
        x.rzut()
        if x.kolizja(X,Y) == 0:
            pygame.draw.rect(ekran,(0,255,0),(X,Y,48,48),0)
        else:
            pygame.draw.rect(ekran,(255,0,0),(X,Y,48,48),0)
        pygame.display.flip()