import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500,400
movement_speed=5
font_size=72

pygame.init()

background_image = pygame.transform.scale(pygame.image.load('bg.jpeg'),(SCREEN_WIDTH, SCREEN_HEIGHT))

font=pygame.font.SysFont("Time New Roman", font_size)