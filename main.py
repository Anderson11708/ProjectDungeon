#project dungeon
import pygame
import Player
import Health
import Wall
import Floor
import Enemy




def runGame ():
    # game setup
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    player = Player.Player ()
    clock = pygame.time.Clock()
    clock.tick(60)
    delta_time = 0
    corner = [0,5,0,5]
    corner_y = [0,0,4,4]
    #floor = Floor.Floor (0,0)

    # Loads the sprites
    groups = {"wall": pygame.sprite.Group(),"floor" : pygame.sprite.Group(), "health" : pygame.sprite.Group(),"enemies": pygame.sprite.Group()}

    groups["wall"].add(Wall.generate_walls(50,0,14,1,1,0)) #top wall
    groups["wall"].add(Wall.generate_walls(50,550,14,1,1,4)) #bottom wall
    groups["wall"].add(Wall.generate_walls(0,50,1,10,0,0)) #left wall
    groups["wall"].add(Wall.generate_walls(750,50,1,10,5,0)) #right wall


    for i in range(4) :
        if i < 2 :
            groups["wall"].add(Wall.generate_walls((i%2)*750,0,1,1,corner[i],corner_y[i]))
        else :
            groups["wall"].add(Wall.generate_walls((i%2)*750,550,1,1,corner[i],corner_y[i]))

    # generating the floor, health potion and enemy
    groups["floor"].add(Floor.generate_floor(50, 50, 14, 10, 2, 2))
    groups["health"].add(Health.Health(100, 100))
    groups["enemies"].add(Enemy.Enemy(400,400))

    # game loop
    running = True
    while running:
        # Making actions based off keys clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.set_yspeed(-300)
                elif event.key == pygame.K_s:
                    player.set_yspeed(300)
                elif event.key == pygame.K_a:
                    player.set_xspeed(-300)
                elif event.key == pygame.K_d:
                    player.set_xspeed(300)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    if player.get_yspeed() < 0 :
                        player.set_yspeed(0)
                elif event.key == pygame.K_s:
                    if player.get_yspeed() > 0 :
                        player.set_yspeed(0)
                elif event.key == pygame.K_a:
                    if player.get_xspeed() < 0 :
                        player.set_xspeed(0)
                elif event.key == pygame.K_d:
                    if player.get_xspeed() > 0 :
                        player.set_xspeed(0)
        # setting the time of the game
        delta_time = clock.tick(144)/1000
        player.update(delta_time,groups)
        # updating each group
        for group in groups.values():
            for i in group:
                i.update(delta_time,groups)
        window.fill((0,0,0))
        # drawing the spites
        for group in groups.values():
            for i in group :
                i.draw(window)
        # updates the screen
        player.draw(window)
        pygame.display.flip()

runGame()

