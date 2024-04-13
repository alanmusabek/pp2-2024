import pygame

pygame.init()
screen = pygame.display.set_mode((1980, 720))
pygame.display.set_caption("Clock")
image = pygame.image.load('./images/mickeyclock3.jpeg')
image = pygame.transform.scale(image, (600,400))
right_arm = pygame.image.load('./images/mickeyclock(1).png')
right_arm = pygame.transform.scale(right_arm, (600,400))
left_arm = pygame.image.load('./images/mickeyclock.png')
left_arm = pygame.transform.scale(left_arm, (600,400))

angle_1 = 0
def blitRotate(surf, image, pos, originPos, angle):

    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)

def blitRotate2(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)
    pygame.draw.rect(surf, (255, 0, 0), new_rect, 2)

try:
    left_arm = pygame.image.load('./images/mickeyclock.png')
    right_arm = pygame.image.load('./images/mickeyclock(1).png')
    image = pygame.image.load('./images/mickeyclock3.jpeg')
except:
    text = pygame.font.SysFont('Times New Roman', 50).render('image', False, (255, 255, 0))
    left_arm = pygame.Surface((text.get_width()+1, text.get_height()+1))
    right_arm = pygame.Surface((text.get_width()+1, text.get_height()+1))
    image = pygame.Surface((text.get_width()+1, text.get_height()+1))
    pygame.draw.rect(image, (0, 0, 255), (1, 1, *text.get_size()))
    image.blit(text, (1, 1))
    right_arm.blit(text, (1, 1))
    left_arm.blit(text, (1, 1))
w, h = right_arm.get_size()
w_1, h_1 = left_arm.get_size()
w_2, h_2 = image.get_size()

angle = 0
done = False

while True:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pos = (screen.get_width()/2, screen.get_height()/2)
    
    angle_1 -= 1/100
    blitRotate(screen, image, pos, (w_2/2, h_2/2), 0)
    blitRotate(screen, right_arm, pos, (w/2, h/2), angle)
    blitRotate(screen, left_arm, pos, (w_1/2, h_1/2), angle_1)
    #blitRotate2(screen, image, pos, angle)
    angle -= 1
    pygame.display.update()