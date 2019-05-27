#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [800, 800]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

reineblanche = pygame.image.load('PION BLANC/REINE BLANCHE.png').convert()
reineblanche = pygame.transform.smoothscale(reineblanche, [100,100])
reineblanche.set_colorkey([181, 230, 29])  

R = pygame.image.load('PION BLANC/ROI BLANC.png').convert()
R = pygame.transform.smoothscale(R, [100,100])
R.set_colorkey([181, 230, 29])  

F = pygame.image.load('PION BLANC/FOU BLANC.png').convert()
F = pygame.transform.smoothscale(F, [100,100])
F.set_colorkey([181, 230, 29])  

C = pygame.image.load('PION BLANC/CHEVAL BLANC.png').convert()
C = pygame.transform.smoothscale(C, [100,100])
C.set_colorkey([181, 230, 29])  

T = pygame.image.load('PION BLANC/TOUR BLANCHE.png').convert()
T = pygame.transform.smoothscale(T, [100,100])
T.set_colorkey([181, 230, 29])

reineblancheN = pygame.image.load('PION NOIR/REINE NOIR.png').convert()
reineblancheN = pygame.transform.smoothscale(reineblancheN, [100,100])
reineblancheN.set_colorkey([181, 230, 29])

RN = pygame.image.load('PION NOIR/ROI NOIR.png').convert()
RN = pygame.transform.smoothscale(RN, [100,100])
RN.set_colorkey([181, 230, 29])  
               
FN = pygame.image.load('PION NOIR/FOU NOIR.png').convert()
FN = pygame.transform.smoothscale(FN, [100,100])
FN.set_colorkey([181, 230, 29])  
               
CN = pygame.image.load('PION NOIR/CHEVAL NOIR.png').convert()
CN = pygame.transform.smoothscale(CN, [100,100])
CN.set_colorkey([181, 230, 29])  
               
TN = pygame.image.load('PION NOIR/TOUR NOIR.png').convert()
TN = pygame.transform.smoothscale(TN, [100,100])
TN.set_colorkey([181, 230, 29])

# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK

    # DESSIN
    ecran.fill(BLANC)
    
    #Sol
    
    pygame.draw.rect(ecran, NOIR, [0,0, 100,100])
    pygame.draw.rect(ecran, NOIR, [200,0, 100,100])
    pygame.draw.rect(ecran, NOIR, [400,0, 100,100])
    pygame.draw.rect(ecran, NOIR, [600,0, 100,100])
    pygame.draw.rect(ecran, NOIR, [0,200, 100,100])
    pygame.draw.rect(ecran, NOIR, [200,200, 100,100])
    pygame.draw.rect(ecran, NOIR, [400,200, 100,100])
    pygame.draw.rect(ecran, NOIR, [600,200, 100,100]) 
    pygame.draw.rect(ecran, NOIR, [0,400, 100,100])
    pygame.draw.rect(ecran, NOIR, [200,400, 100,100])
    pygame.draw.rect(ecran, NOIR, [400,400, 100,100])
    pygame.draw.rect(ecran, NOIR, [600,400, 100,100])     
    pygame.draw.rect(ecran, NOIR, [0,600, 100,100])
    pygame.draw.rect(ecran, NOIR, [200,600, 100,100])
    pygame.draw.rect(ecran, NOIR, [400,600, 100,100])
    pygame.draw.rect(ecran, NOIR, [600,600, 100,100])      
    
    pygame.draw.rect(ecran, NOIR, [100,100, 100,100])
    pygame.draw.rect(ecran, NOIR, [300,100, 100,100])
    pygame.draw.rect(ecran, NOIR, [500,100, 100,100])
    pygame.draw.rect(ecran, NOIR, [700,100, 100,100])    
    pygame.draw.rect(ecran, NOIR, [100,300, 100,100])
    pygame.draw.rect(ecran, NOIR, [300,300, 100,100])
    pygame.draw.rect(ecran, NOIR, [500,300, 100,100])
    pygame.draw.rect(ecran, NOIR, [700,300, 100,100])    
    pygame.draw.rect(ecran, NOIR, [100,500, 100,100])
    pygame.draw.rect(ecran, NOIR, [300,500, 100,100])
    pygame.draw.rect(ecran, NOIR, [500,500, 100,100])
    pygame.draw.rect(ecran, NOIR, [700,500, 100,100])    
    pygame.draw.rect(ecran, NOIR, [100,700, 100,100])
    pygame.draw.rect(ecran, NOIR, [300,700, 100,100])
    pygame.draw.rect(ecran, NOIR, [500,700, 100,100])
    pygame.draw.rect(ecran, NOIR, [700,700, 100,100])    
    
    #pion
    
    ecran.blit(reineblanche, [300, 0])    
    ecran.blit(R, [400, 0])
    ecran.blit(F, [200, 0])
    ecran.blit(F, [500, 0])
    ecran.blit(C, [100, 0])
    ecran.blit(C, [600, 0])
    ecran.blit(T, [0, 0])
    ecran.blit(T, [700, 0])
    
    ecran.blit(reineblancheN, [400, 700])
    ecran.blit(RN, [300, 700])
    ecran.blit(FN, [200, 700])
    ecran.blit(FN, [500, 700])
    ecran.blit(CN, [100, 700])
    ecran.blit(CN, [600, 700])
    ecran.blit(TN, [0, 700])
    ecran.blit(TN, [700, 700])    
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()