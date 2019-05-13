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
    
    
    
    
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()