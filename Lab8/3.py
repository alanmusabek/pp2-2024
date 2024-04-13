import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    drawing = True  # Indicates whether the program is in drawing mode or erasing mode
    
    while True:
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_d:
                    drawing = True  # Switch to drawing mode
                elif event.key == pygame.K_e:
                    drawing = False  # Switch to erasing mode
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and drawing:  # Only draw if in drawing mode
                    radius = min(200, radius + 1)
                elif event.button == 3 and drawing:  # Only draw if in drawing mode
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                if drawing:  # Only add points if in drawing mode
                    position = event.pos
                    points = points + [position]
                    points = points[-256:]
                else:  # If in erasing mode, remove points near the mouse cursor
                    position = event.pos
                    points = [p for p in points if (p[0] - position[0])**2 + (p[1] - position[1])**2 > radius**2]
                    
        screen.fill((0, 0, 0))
        
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
