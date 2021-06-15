import random
import pygame, Pokoje, Postacie, os

class pocisk:
    def __init__(self,a,b,c,d):
        self.vx=b
        self.vy=c
        self.px=0
        self.py=0
        self.po=a
        self.pokoj=d

michu1=pygame.image.load(os.path.join('grafiki', 'michu1.png'))
michu2=pygame.image.load(os.path.join('grafiki', 'michu2.png'))

prawo1=pygame.image.load(os.path.join('grafiki', 'prawo1.png'))
prawo2=pygame.image.load(os.path.join('grafiki', 'prawo2.png'))

lewo1=pygame.image.load(os.path.join('grafiki', 'lewo1.png'))
lewo2=pygame.image.load(os.path.join('grafiki', 'lewo2.png'))

dol1=pygame.image.load(os.path.join('grafiki', 'dol1.png'))
dol2=pygame.image.load(os.path.join('grafiki', 'dol2.png'))

gora1=pygame.image.load(os.path.join('grafiki', 'gora1.png'))
gora2=pygame.image.load(os.path.join('grafiki', 'gora2.png'))

czar_d1=pygame.image.load(os.path.join('grafiki', 'czar_d1.png'))
czar_d2=pygame.image.load(os.path.join('grafiki', 'czar_d2.png'))
czar_d3=pygame.image.load(os.path.join('grafiki', 'czar_d3.png'))
czar_d4=pygame.image.load(os.path.join('grafiki', 'czar_d4.png'))

czar_g1=pygame.image.load(os.path.join('grafiki', 'czar_g1.png'))
czar_g2=pygame.image.load(os.path.join('grafiki', 'czar_g2.png'))
czar_g3=pygame.image.load(os.path.join('grafiki', 'czar_g3.png'))
czar_g4=pygame.image.load(os.path.join('grafiki', 'czar_g4.png'))

czar_p1=pygame.image.load(os.path.join('grafiki', 'czar_p1.png'))
czar_p2=pygame.image.load(os.path.join('grafiki', 'czar_p2.png'))
czar_p3=pygame.image.load(os.path.join('grafiki', 'czar_p3.png'))
czar_p4=pygame.image.load(os.path.join('grafiki', 'czar_p4.png'))

czar_l1=pygame.image.load(os.path.join('grafiki', 'czar_l1.png'))
czar_l2=pygame.image.load(os.path.join('grafiki', 'czar_l2.png'))
czar_l3=pygame.image.load(os.path.join('grafiki', 'czar_l3.png'))
czar_l4=pygame.image.load(os.path.join('grafiki', 'czar_l4.png'))

michu_lw1=pygame.image.load(os.path.join('grafiki', 'michu_lw1.png'))
michu_lw2=pygame.image.load(os.path.join('grafiki', 'michu_lw2.png'))
michu_lw3=pygame.image.load(os.path.join('grafiki', 'michu_lw3.png'))

michu_pw1=pygame.image.load(os.path.join('grafiki', 'michu_pw1.png'))
michu_pw2=pygame.image.load(os.path.join('grafiki', 'michu_pw2.png'))
michu_pw3=pygame.image.load(os.path.join('grafiki', 'michu_pw3.png'))

michu_gw1=pygame.image.load(os.path.join('grafiki', 'michu_gw1.png'))
michu_gw2=pygame.image.load(os.path.join('grafiki', 'michu_gw2.png'))
michu_gw3=pygame.image.load(os.path.join('grafiki', 'michu_gw3.png'))

michu_dw1=pygame.image.load(os.path.join('grafiki', 'michu_dw1.png'))
michu_dw2=pygame.image.load(os.path.join('grafiki', 'michu_dw2.png'))
michu_dw3=pygame.image.load(os.path.join('grafiki', 'michu_dw3.png'))

clock = pygame.time.Clock()

pocisk_graf=pygame.image.load(os.path.join('grafiki', 'pocisk.png'))

pygame.font.init()
czcionka_retro=pygame.font.Font('ARCADECLASSIC.TTF',36)
czcionka_retro1=pygame.font.Font('ARCADECLASSIC.TTF',72)

czest_strzalow=500
strzaly=0
szerokosc=1000
wysokosc=1000
ekran = pygame.display.set_mode((szerokosc,wysokosc))
pokoje = [Pokoje.pokoj(0,0)]
wrogowie = []
postac = Postacie.bohater()
postac.x=240
postac.y=240
czy_istnieje_pokoj=0
czy_nacisnienty=0
uderzanie=0
czas_uderzania=100
abc=0
pociski=1
projectiles=[]
punkty=0
postac.zycie=200

licznik_krokow=0
czest_krokow=100

pygame.mixer.init()
krok1 = pygame.mixer.Sound(os.path.join('sfx', 'krok_prawy.wav'))
krok2 = pygame.mixer.Sound(os.path.join('sfx', 'krok_lewy.wav'))
miecz = pygame.mixer.Sound(os.path.join('sfx', 'miecz.wav'))
strzal = pygame.mixer.Sound(os.path.join('sfx', 'strzal.wav'))

while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if uderzanie==0:
                    uderzanie=1

    keys=pygame.key.get_pressed()

    if uderzanie>=1:
        uderzanie+=1
    uderzanie%=czas_uderzania


    if keys[pygame.K_LEFT] and (pokoje[postac.pokoj].kolizja(postac.x-1,postac.y)==0) and abc==0:
        postac.x-=1
        postac.pozycja=1
        czy_nacisnienty=1

    if keys[pygame.K_RIGHT] and (pokoje[postac.pokoj].kolizja(postac.x+1,postac.y)==0) and abc==0:
        postac.x+=1
        postac.pozycja=2
        czy_nacisnienty=1

    if keys[pygame.K_DOWN] and (pokoje[postac.pokoj].kolizja(postac.x,postac.y+1)==0) and abc==0:
        postac.y+=1
        postac.pozycja=3
        czy_nacisnienty=1

    if keys[pygame.K_UP] and (pokoje[postac.pokoj].kolizja(postac.x,postac.y-1)==0) and abc==0:
        postac.y-=1
        postac.pozycja=4
        czy_nacisnienty=1

    ekran.fill((0,0,0))
    if czy_nacisnienty==0:
        postac.pozycja=0
    
    czy_nacisnienty=0

    for x in pokoje:
        x.rzut(pokoje[postac.pokoj].lokacjaX,pokoje[postac.pokoj].lokacjaY)
    
        

    "gorne wyjscie"

    if postac.x>144 and postac.x<292 and postac.y==0:
        for x in pokoje:
            if x.lokacjaX==pokoje[postac.pokoj].lokacjaX and x.lokacjaY==pokoje[postac.pokoj].lokacjaY+1:
                postac.pokoj=pokoje.index(x)
                czy_istnieje_pokoj=1
                postac.y=431
                
                break

        if czy_istnieje_pokoj==0:
            pokoje.append(Pokoje.pokoj(pokoje[postac.pokoj].lokacjaX,pokoje[postac.pokoj].lokacjaY+1))
            postac.pokoj=len(pokoje)-1
            postac.y=431
            for x in range(random.randrange(7)):
                wrogowie.append(Postacie.wrog(len(pokoje)-1,random.choice(pokoje[-1].podloga),random.randrange(czest_strzalow)))
           

        czy_istnieje_pokoj=0

    "dolne wyjscie"

    if postac.x>144 and postac.x<292 and postac.y==432:
        for x in pokoje:
            if x.lokacjaX==pokoje[postac.pokoj].lokacjaX and x.lokacjaY==pokoje[postac.pokoj].lokacjaY-1:
                postac.pokoj=pokoje.index(x)
                czy_istnieje_pokoj=1
                postac.y=0
                
                break

        if czy_istnieje_pokoj==0:
            pokoje.append(Pokoje.pokoj(pokoje[postac.pokoj].lokacjaX,pokoje[postac.pokoj].lokacjaY-1))
            postac.pokoj=len(pokoje)-1
            postac.y=0
            for x in range(random.randrange(7)):
                wrogowie.append(Postacie.wrog(len(pokoje)-1,random.choice(pokoje[-1].podloga),random.randrange(czest_strzalow)))
                
           

        czy_istnieje_pokoj=0

        "prawe wyjscie"

    if postac.y>144 and postac.y<292 and postac.x==432:
        for x in pokoje:
            if x.lokacjaX==pokoje[postac.pokoj].lokacjaX+1 and x.lokacjaY==pokoje[postac.pokoj].lokacjaY:
                postac.pokoj=pokoje.index(x)
                czy_istnieje_pokoj=1
                postac.x=0
                
                break

        if czy_istnieje_pokoj==0:
            pokoje.append(Pokoje.pokoj(pokoje[postac.pokoj].lokacjaX+1,pokoje[postac.pokoj].lokacjaY))
            postac.pokoj=len(pokoje)-1
            postac.x=0
            for x in range(random.randrange(7)):
                wrogowie.append(Postacie.wrog(len(pokoje)-1,random.choice(pokoje[-1].podloga),random.randrange(czest_strzalow)))
           

        czy_istnieje_pokoj=0

        "lewe wyjscie"

    if postac.y>144 and postac.y<292 and postac.x==-1:
        for x in pokoje:
            if x.lokacjaX==pokoje[postac.pokoj].lokacjaX-1 and x.lokacjaY==pokoje[postac.pokoj].lokacjaY:
                postac.pokoj=pokoje.index(x)
                czy_istnieje_pokoj=1
                postac.x=431
                break

        if czy_istnieje_pokoj==0:
            pokoje.append(Pokoje.pokoj(pokoje[postac.pokoj].lokacjaX-1,pokoje[postac.pokoj].lokacjaY))
            postac.pokoj=len(pokoje)-1
            postac.x=431

            for x in range(random.randrange(3)):
                wrogowie.append(Postacie.wrog(len(pokoje)-1,random.choice(pokoje[-1].podloga),random.randrange(czest_strzalow)))
           

        czy_istnieje_pokoj=0
    licznik_krokow=licznik_krokow%czest_krokow
    licznik_krokow+=1

    strzaly%=czest_strzalow
    strzaly+=1

    for x in wrogowie:

        if x.zycie<=0:
            x.martwy=1

        if x.martwy == 0:

            if (postac.x-x.polozenie.left+24)**2+(postac.y-x.polozenie.top+24)**2<=2304 and uderzanie!=0 and x.pokoj==postac.pokoj:
                abc=1
                if uderzanie<=5:
                    miecz.play()


                if postac.x-x.polozenie.left>=postac.y-x.polozenie.top and postac.x-x.polozenie.left>(postac.y-x.polozenie.top)*-1:

                    if uderzanie < czas_uderzania/3:
                        ekran.blit(michu_pw1,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))

                    if uderzanie < czas_uderzania*2/3 and uderzanie >=czas_uderzania/3:
                        ekran.blit(michu_pw2,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))

                    if uderzanie >= czas_uderzania*2/3:
                        ekran.blit(michu_pw3,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))

                    if uderzanie == czas_uderzania-2:
                        x.zycie-=34
                        punkty+=25



                if postac.x-x.polozenie.left<=(postac.y-x.polozenie.top) and (postac.x-x.polozenie.left)*-1>postac.y-x.polozenie.top:

                    if uderzanie < czas_uderzania/3:
                        ekran.blit(michu_lw1,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))

                    if uderzanie < czas_uderzania*2/3 and uderzanie >=czas_uderzania/3:
                        ekran.blit(michu_lw2,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))

                    if uderzanie >= czas_uderzania*2/3:
                        ekran.blit(michu_lw3,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))

                    if uderzanie == czas_uderzania-2:
                        x.zycie-=34
                        punkty+=25

                    



                if postac.x-x.polozenie.left<=(postac.y-x.polozenie.top)*-1 and postac.x-x.polozenie.left>(postac.y-x.polozenie.top):

                    if uderzanie < czas_uderzania/3:
                        ekran.blit(michu_dw1,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))

                    if uderzanie < czas_uderzania*2/3 and uderzanie >=czas_uderzania/3:
                        ekran.blit(michu_dw2,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))

                    if uderzanie >= czas_uderzania*2/3:
                        ekran.blit(michu_dw3,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))
                    
                    if uderzanie == czas_uderzania-2:
                        x.zycie-=34
                        punkty+=25



                if (postac.x-x.polozenie.left)*-1<=postac.y-x.polozenie.top and postac.x-x.polozenie.left<postac.y-x.polozenie.top:

                    if uderzanie < czas_uderzania/3:
                        ekran.blit(michu_gw1,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))

                    if uderzanie < czas_uderzania*2/3 and uderzanie >=czas_uderzania/3:
                        ekran.blit(michu_gw2,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))

                    if uderzanie >= czas_uderzania*2/3:
                        ekran.blit(michu_gw3,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))
                    
                    if uderzanie == czas_uderzania-2:
                        x.zycie-=34
                        punkty+=25

                

            if x.pokoj==postac.pokoj:

                "na prawo od czarodzieja"
                if (strzaly+x.strzal)%czest_strzalow==int(czest_strzalow*3/4):
                    strzal.play()

                if postac.x-x.polozenie.left>=postac.y-x.polozenie.top and postac.x-x.polozenie.left>(postac.y-x.polozenie.top)*-1:

                    if (strzaly+x.strzal)%czest_strzalow>=0 and (strzaly+x.strzal)%czest_strzalow<czest_strzalow/4:
                        ekran.blit(czar_p1,x.polozenie.move((-pokoje[postac.pokoj].lokacjaX+pokoje[x.pokoj].lokacjaX)*480+240,(pokoje[postac.pokoj].lokacjaY-pokoje[x.pokoj].lokacjaY)*480+240))

                    if (strzaly+x.strzal)%czest_strzalow>=czest_strzalow/4 and (strzaly+x.strzal)%czest_strzalow<czest_strzalow*2/4:
                        ekran.blit(czar_p2,x.polozenie.move((-pokoje[postac.pokoj].lokacjaX+pokoje[x.pokoj].lokacjaX)*480+240,(pokoje[postac.pokoj].lokacjaY-pokoje[x.pokoj].lokacjaY)*480+240))

                    if (strzaly+x.strzal)%czest_strzalow>=czest_strzalow*2/4 and (strzaly+x.strzal)%czest_strzalow<czest_strzalow*3/4:
                        ekran.blit(czar_p3,x.polozenie.move((-pokoje[postac.pokoj].lokacjaX+pokoje[x.pokoj].lokacjaX)*480+240,(pokoje[postac.pokoj].lokacjaY-pokoje[x.pokoj].lokacjaY)*480+240))
                    
                    if (strzaly+x.strzal)%czest_strzalow>=czest_strzalow*3/4 and (strzaly+x.strzal)%czest_strzalow<czest_strzalow:
                        ekran.blit(czar_p4,x.polozenie.move((-pokoje[postac.pokoj].lokacjaX+pokoje[x.pokoj].lokacjaX)*480+240,(pokoje[postac.pokoj].lokacjaY-pokoje[x.pokoj].lokacjaY)*480+240))


                    


                    

                "od góry czarodzieja"

                if postac.x-x.polozenie.left<=(postac.y-x.polozenie.top)*-1 and postac.x-x.polozenie.left>(postac.y-x.polozenie.top):

                    if (strzaly+x.strzal)%czest_strzalow>=0 and (strzaly+x.strzal)%czest_strzalow<czest_strzalow/4:
                        ekran.blit(czar_g1,x.polozenie.move((-pokoje[postac.pokoj].lokacjaX+pokoje[x.pokoj].lokacjaX)*480+240,(pokoje[postac.pokoj].lokacjaY-pokoje[x.pokoj].lokacjaY)*480+240))

                    if (strzaly+x.strzal)%czest_strzalow>=czest_strzalow/4 and (strzaly+x.strzal)%czest_strzalow<czest_strzalow*2/4:
                        ekran.blit(czar_g2,x.polozenie.move((-pokoje[postac.pokoj].lokacjaX+pokoje[x.pokoj].lokacjaX)*480+240,(pokoje[postac.pokoj].lokacjaY-pokoje[x.pokoj].lokacjaY)*480+240))

                    if (strzaly+x.strzal)%czest_strzalow>=czest_strzalow*2/4 and (strzaly+x.strzal)%czest_strzalow<czest_strzalow*3/4:
                        ekran.blit(czar_g3,x.polozenie.move((-pokoje[postac.pokoj].lokacjaX+pokoje[x.pokoj].lokacjaX)*480+240,(pokoje[postac.pokoj].lokacjaY-pokoje[x.pokoj].lokacjaY)*480+240))
                    
                    if (strzaly+x.strzal)%czest_strzalow>=czest_strzalow*3/4 and (strzaly+x.strzal)%czest_strzalow<czest_strzalow:
                        ekran.blit(czar_g4,x.polozenie.move((-pokoje[postac.pokoj].lokacjaX+pokoje[x.pokoj].lokacjaX)*480+240,(pokoje[postac.pokoj].lokacjaY-pokoje[x.pokoj].lokacjaY)*480+240))


                        
                
                "od lewej czarodzieja"

                if postac.x-x.polozenie.left<=(postac.y-x.polozenie.top) and (postac.x-x.polozenie.left)*-1>postac.y-x.polozenie.top:

                    if (strzaly+x.strzal)%czest_strzalow>=0 and (strzaly+x.strzal)%czest_strzalow<czest_strzalow/4:
                        ekran.blit(czar_l1,x.polozenie.move((-pokoje[postac.pokoj].lokacjaX+pokoje[x.pokoj].lokacjaX)*480+240,(pokoje[postac.pokoj].lokacjaY-pokoje[x.pokoj].lokacjaY)*480+240))

                    if (strzaly+x.strzal)%czest_strzalow>=czest_strzalow/4 and (strzaly+x.strzal)%czest_strzalow<czest_strzalow*2/4:
                        ekran.blit(czar_l2,x.polozenie.move((-pokoje[postac.pokoj].lokacjaX+pokoje[x.pokoj].lokacjaX)*480+240,(pokoje[postac.pokoj].lokacjaY-pokoje[x.pokoj].lokacjaY)*480+240))

                    if (strzaly+x.strzal)%czest_strzalow>=czest_strzalow*2/4 and (strzaly+x.strzal)%czest_strzalow<czest_strzalow*3/4:
                        ekran.blit(czar_l3,x.polozenie.move((-pokoje[postac.pokoj].lokacjaX+pokoje[x.pokoj].lokacjaX)*480+240,(pokoje[postac.pokoj].lokacjaY-pokoje[x.pokoj].lokacjaY)*480+240))
                    
                    if (strzaly+x.strzal)%czest_strzalow>=czest_strzalow*3/4 and (strzaly+x.strzal)%czest_strzalow<czest_strzalow:
                        ekran.blit(czar_l4,x.polozenie.move((-pokoje[postac.pokoj].lokacjaX+pokoje[x.pokoj].lokacjaX)*480+240,(pokoje[postac.pokoj].lokacjaY-pokoje[x.pokoj].lokacjaY)*480+240))

                "od dołu czarodzieja"

                if (postac.x-x.polozenie.left)*-1<=postac.y-x.polozenie.top and postac.x-x.polozenie.left<postac.y-x.polozenie.top:

                    if (strzaly+x.strzal)%czest_strzalow>=0 and (strzaly+x.strzal)%czest_strzalow<czest_strzalow/4:
                       ekran.blit(czar_d1,x.polozenie.move((-pokoje[postac.pokoj].lokacjaX+pokoje[x.pokoj].lokacjaX)*480+240,(pokoje[postac.pokoj].lokacjaY-pokoje[x.pokoj].lokacjaY)*480+240))

                    if (strzaly+x.strzal)%czest_strzalow>=czest_strzalow/4 and (strzaly+x.strzal)%czest_strzalow<czest_strzalow*2/4:
                        ekran.blit(czar_d2,x.polozenie.move((-pokoje[postac.pokoj].lokacjaX+pokoje[x.pokoj].lokacjaX)*480+240,(pokoje[postac.pokoj].lokacjaY-pokoje[x.pokoj].lokacjaY)*480+240))

                    if (strzaly+x.strzal)%czest_strzalow>=czest_strzalow*2/4 and (strzaly+x.strzal)%czest_strzalow<czest_strzalow*3/4:
                        ekran.blit(czar_d3,x.polozenie.move((-pokoje[postac.pokoj].lokacjaX+pokoje[x.pokoj].lokacjaX)*480+240,(pokoje[postac.pokoj].lokacjaY-pokoje[x.pokoj].lokacjaY)*480+240))
                    
                    if (strzaly+x.strzal)%czest_strzalow>=czest_strzalow*3/4 and (strzaly+x.strzal)%czest_strzalow<czest_strzalow:
                        ekran.blit(czar_d4,x.polozenie.move((-pokoje[postac.pokoj].lokacjaX+pokoje[x.pokoj].lokacjaX)*480+240,(pokoje[postac.pokoj].lokacjaY-pokoje[x.pokoj].lokacjaY)*480+240))

                if (strzaly+x.strzal)%czest_strzalow==czest_strzalow-120 and pociski==1:
                    projectiles.append(pocisk(x.polozenie.copy(),(postac.x-x.polozenie.left+24)/100,(postac.y-x.polozenie.top+24)/100,x.pokoj))
            
            else:
                ekran.blit(czar_d1,x.polozenie.move((-pokoje[postac.pokoj].lokacjaX+pokoje[x.pokoj].lokacjaX)*480+240,(pokoje[postac.pokoj].lokacjaY-pokoje[x.pokoj].lokacjaY)*480+240))
    
    if uderzanie==0 or abc==0:
        if (pokoje[postac.pokoj].kolizja(postac.x,postac.y)==0):

                if licznik_krokow<czest_krokow/2:  
                    if postac.pozycja!=0 and licznik_krokow==1:
                        krok1.play()
                    if postac.pozycja==0:
                        ekran.blit(michu1,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))
                    if postac.pozycja==1:
                        ekran.blit(lewo1,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))
                    if postac.pozycja==2:
                        ekran.blit(prawo1,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))
                    if postac.pozycja==3:
                        ekran.blit(dol1,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))
                    if postac.pozycja==4:
                        ekran.blit(gora1,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))

                else:
                    if postac.pozycja!=0 and licznik_krokow == 50:
                        krok2.play()
                    if postac.pozycja==0:
                        ekran.blit(michu2,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))
                    if postac.pozycja==1:
                        ekran.blit(lewo2,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))
                    if postac.pozycja==2:
                        ekran.blit(prawo2,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))
                    if postac.pozycja==3:
                        ekran.blit(dol2,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))
                    if postac.pozycja==4:
                        ekran.blit(gora2,(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240))
        else:
            pygame.draw.rect(ekran,(0,255,0),(postac.x+szerokosc/2-240,postac.y+wysokosc/2-240,48,48),0)
        abc=0
    for x in projectiles:
        ekran.blit(pocisk_graf,x.po.move((-pokoje[postac.pokoj].lokacjaX+pokoje[x.pokoj].lokacjaX)*480+240+x.px,(pokoje[postac.pokoj].lokacjaY-pokoje[x.pokoj].lokacjaY)*480+240+x.py))
        x.px+=x.vx
        x.py+=x.vy
        if pokoje[x.pokoj].kolizja(x.po.left+x.px,x.po.top+x.py):
            projectiles.remove(x)
        if (postac.x-x.po.left-x.px+24)**2+(postac.y-x.po.top-x.py+24)**2<=500:
            projectiles.remove(x)
            postac.zycie-=25

    ekran.blit(czcionka_retro.render("HP " + str(postac.zycie), 0, (255,255,255)),(20,20))
    ekran.blit(czcionka_retro.render("PUNKTY " + str(punkty), 0, (255,255,255)),(20,50))

    if postac.zycie<=0:
        ekran.fill((0,0,0))
        ekran.blit(czcionka_retro1.render("GAME OVER", 0, (255,255,255)),(szerokosc/2-155,wysokosc/2-30))
        pygame.mixer.quit()




            


    clock.tick(120)
    pygame.display.flip()
