def setup():
    global map, keys, cam, apple, snake
    fullScreen(P3D)
    textAlign(CENTER, CENTER)
    textMode(SHAPE)
    rectMode(CENTER)
    class snake:
        speed = width / 200
        size  = width / 40
        snake = [[0, 0, 0]] * 100
        color = 100, 200, 100

    class map:
        sizeX      = width
        sizeY      = height
        sizeZ      = width
        frameCount = 0
        announcedText         = ""
        announcedTextFrames   = 0

    class apple:
        X             = random(-map.sizeX / 2, map.sizeX / 2)
        Y             = random(-map.sizeY / 2, map.sizeY / 2)
        Z             = random(-map.sizeZ / 2, map.sizeZ / 2)
        color         = 200,  50,  50
        size          = width / 50
        eatHitboxSize = 3 * size 
        touched       = False
    
    class cam:
        eyeX           = map.sizeX / 2.0 + snake.size
        eyeY           = map.sizeY / 2.0
        eyeZ           = map.sizeZ / 2.0
        lookingAtX     = 0
        lookingAtY     = 0
        lookingAtZ     = 0
        xAxisIsUp      = 0
        yAxisIsUp      = 1
        zAxisIsUp      = 0
        yaw            = 0
        pitch          = 90
        sensivityYaw   = 3
        sensivityPitch = 2
        fov            = 180 # FOV (field of view) in degres, converted later on to radians
        aspectRatio    = width / float(height)
        nearClipPlane  = 1
        farClipPlane   = map.sizeX * 1.414213562

    class keys:
        Z           = False
        Q           = False
        S           = False
        D           = False
        
        UP_ARROW    = False
        LEFT_ARROW  = False
        DOWN_ARROW  = False
        RIGHT_ARROW = False
        
        F           = False
        INFERIOR    = False
        
def keyPressed():
    if keyCode == 60:
        keys.INFERIOR = True
    if keyCode == 70:
        keys.F = True
    if keyCode == 90:
        keys.Z = True
    if keyCode == 81:
        keys.Q = True
    if keyCode == 83:
        keys.S = True
    if keyCode == 68:
        keys.D = True
    if keyCode == 38:
        keys.UP_ARROW = True
    if keyCode == 37:
        keys.LEFT_ARROW = True
    if keyCode == 40:
        keys.DOWN_ARROW = True
    if keyCode == 39:
        keys.RIGHT_ARROW = True 
    
def keyReleased():
    if keyCode == 60:
        keys.INFERIOR = False
    if keyCode == 70:
        keys.F = False
    if keyCode == 90:
        keys.Z = False
    if keyCode == 81:
        keys.Q = False
    if keyCode == 83:
        keys.S = False
    if keyCode == 68:
        keys.D = False
    if keyCode == 38:
        keys.UP_ARROW = False
    if keyCode == 37:
        keys.LEFT_ARROW = False
    if keyCode == 40:
        keys.DOWN_ARROW = False
    if keyCode == 39:
        keys.RIGHT_ARROW = False

def draw():
    background(0)
    map.announcedTextFrames -= 1
    map.frameCount          += 1
    if keys.LEFT_ARROW and not keys.RIGHT_ARROW:
        cam.yaw = (cam.yaw - 3) % 360
    if keys.RIGHT_ARROW and not keys.LEFT_ARROW:
        cam.yaw = (cam.yaw + 3) % 360
    if keys.UP_ARROW and not keys.DOWN_ARROW:
        cam.pitch = constrain(cam.pitch - 2, 1, 179)
    if keys.DOWN_ARROW and not keys.UP_ARROW:
        cam.pitch = constrain(cam.pitch + 2, 1, 179)
    cam.lookingAtX = cam.eyeX + snake.speed * 10 * sin(radians(cam.pitch)) * cos(radians(cam.yaw))
    cam.lookingAtY = cam.eyeY - snake.speed * 10 * cos(radians(cam.pitch))
    cam.lookingAtZ = cam.eyeZ + snake.speed * 10 * sin(radians(cam.pitch)) * sin(radians(cam.yaw))
    if not keys.S:
        cam.eyeX = cam.eyeX + snake.speed * sin(radians(cam.pitch)) * cos(radians(cam.yaw))
        cam.eyeY = cam.eyeY - snake.speed * cos(radians(cam.pitch))
        cam.eyeZ = cam.eyeZ + snake.speed * sin(radians(cam.pitch)) * sin(radians(cam.yaw))
    cam.eyeX %= map.sizeX
    cam.eyeY %= map.sizeY
    cam.eyeZ %= map.sizeZ
    camera(cam.eyeX      , cam.eyeY      , cam.eyeZ      ,
           cam.lookingAtX, cam.lookingAtY, cam.lookingAtZ,
           cam.xAxisIsUp , cam.yAxisIsUp , cam.zAxisIsUp )
    perspective(PI / (360.0 / float(cam.fov)), cam.aspectRatio, cam.nearClipPlane, cam.farClipPlane)
    if  abs(cam.eyeX - map.sizeX / 2- apple.X) - apple.eatHitboxSize < 0\
    and abs(cam.eyeY - map.sizeY / 2- apple.Y) - apple.eatHitboxSize < 0\
    and abs(cam.eyeZ - map.sizeZ / 2- apple.Z) - apple.eatHitboxSize < 0: # Eating apple
        for i in range(50):
            snake.snake.insert(0, (snake.snake[0]))
        apple.X = random(-map.sizeX / 2, map.sizeX / 2)
        apple.Y = random(-map.sizeY / 2, map.sizeY / 2)
        apple.Z = random(-map.sizeZ / 2, map.sizeZ / 2)
    if frameCount % 5 == 0:
        for index in range(len(snake.snake)):
            if index == len(snake.snake) - 1:
                snake.snake[index] = [cam.eyeX - map.sizeX / 2, cam.eyeY - map.sizeY / 2, cam.eyeZ - map.sizeZ / 2]
            else:
                snake.snake[index] = snake.snake[index + 1]
    # Rendering part
    ambientLight( 63,  63,  63)
    pointLight(255, 255, 255, map.sizeX / 2.0, map.sizeY / 8, map.sizeZ / 2.0)
    translate(map.sizeX / 2.0, map.sizeY / 2.0, map.sizeZ / 2.0)
    strokeWeight(5)
    stroke(255)
    pushMatrix() # Global matrix
    pushMatrix() # Negative X wall matrix
    translate(- map.sizeX / 2.0, 0, 0)
    fill(100,  50,  50)
    box(0, map.sizeY, map.sizeZ)
    popMatrix() # End of negative X wall matrix
    
    pushMatrix() # Positive X wall matrix
    translate(map.sizeX / 2.0, 0, 0)
    fill(200, 100, 100)
    box(0, map.sizeY, map.sizeZ)
    if map.announcedTextFrames > 0:
        fill(255)
        textSize(36)
        rotateY(- HALF_PI)
        text(map.announcedText, 0, 0, map.sizeX / 4)
    popMatrix() # End of positive X wall matrix
    
    pushMatrix() # Positive Y wall matrix
    translate(0, map.sizeY / 2.0, 0)
    fill(100, 200, 100)
    box(map.sizeX, 0, map.sizeZ)
    popMatrix() # End of positive Y wall matrix
    
    pushMatrix() # Negative Y wall matrix
    translate(0, - map.sizeY / 2.0, 0)
    fill( 50, 100,  50)
    box(map.sizeX, 0, map.sizeZ)
    popMatrix() # End of negative Y wall matrix
    
    pushMatrix() # Positive Z wall matrix
    translate(0, 0, map.sizeZ / 2.0)
    fill(100, 100, 200)
    box(map.sizeX, map.sizeY, 0)
    popMatrix() # End of negative Y wall matrix
    
    pushMatrix() # Negative Z wall matrix
    translate(0, 0, -map.sizeZ / 2.0)
    fill( 50,  50, 100)
    box(map.sizeX, map.sizeY, 0)
    popMatrix() # End of negative Y wall matrix

    pushMatrix() # Apple matrix
    translate(apple.X, apple.Y, apple.Z)
    noStroke()
    fill(apple.color[0], apple.color[1], apple.color[2])
    sphere(apple.size)
    popMatrix() # End of apple matrix
    
    pushMatrix() # Snake matrix
    fill(snake.color[0], snake.color[1], snake.color[2])
    for ball in range(len(snake.snake) - 5):
        if abs(cam.eyeX - map.sizeX / 2.0 - snake.snake[ball][0]) - snake.size < 0 and\
           abs(cam.eyeY - map.sizeY / 2.0 - snake.snake[ball][1]) - snake.size < 0 and\
           abs(cam.eyeZ - map.sizeZ / 2.0 - snake.snake[ball][2]) - snake.size < 0    :
            map.announcedTextFrames = 120
            map.announcedText       = "You died with " + str(len(snake.snake)) + " score"
            cam.eyeX                = map.sizeX / 2.0 + snake.size
            cam.eyeY                = map.sizeY / 2.0
            cam.eyeZ                = map.sizeZ / 2.0
            cam.lookingAtX          = 0
            cam.lookingAtY          = 0
            cam.lookingAtZ          = 0
            cam.yaw                 = 0
            cam.pitch               = 90
            map.frameCount          = 0
            snake.snake             = [[0, 0, 0]] * 100
            break
        pushMatrix()
        translate(snake.snake[ball][0], snake.snake[ball][1], snake.snake[ball][2])
        sphere(snake.size)
        popMatrix()
    popMatrix() # End of snake matrix

    popMatrix() # End of global matrix