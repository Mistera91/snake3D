def setup():
    global map, keys, cam
    fullScreen(P3D)
    rectMode(CENTER)
    class map:
        sizeX     = width
        sizeY     = height
        sizeZ     = width
    
    class cam:
        eyeX       = map.sizeX / 2.0
        eyeY       = map.sizeY / 2.0
        eyeZ       = map.sizeZ / 2.0
        lookingAtX = 0
        lookingAtY = 0
        lookingAtZ = 0
        xAxisIsUp  = 0
        yAxisIsUp  = 1
        zAxisIsUp  = 0
        yaw        = 0
        pitch      = 90

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
    if keys.LEFT_ARROW and not keys.RIGHT_ARROW:
        cam.yaw = (cam.yaw - 1) % 360
    if keys.RIGHT_ARROW and not keys.LEFT_ARROW:
        cam.yaw = (cam.yaw + 1) % 360
    if keys.UP_ARROW and not keys.DOWN_ARROW:
        cam.pitch = constrain(cam.pitch - 1, 1, 179)
    if keys.DOWN_ARROW and not keys.UP_ARROW:
        cam.pitch = constrain(cam.pitch + 1, 1, 179)
    background(0)
    cam.lookingAtX = cam.eyeX + width * sin(radians(cam.pitch)) * cos(radians(cam.yaw))
    cam.lookingAtY = cam.eyeY - height * cos(radians(cam.pitch))
    cam.lookingAtZ = cam.eyeZ + width * sin(radians(cam.pitch)) * sin(radians(cam.yaw))
    camera(
    cam.eyeX      , cam.eyeY      , cam.eyeZ      ,
    cam.lookingAtX, cam.lookingAtY, cam.lookingAtZ,
    cam.xAxisIsUp , cam.yAxisIsUp , cam.zAxisIsUp )
    #spotLight(255, 255, 255, map.sizeX / 2.0, map.sizeY / 2.0, map.sizeZ / 2.0, 0, 1, -0.5, TAU, 0)
    translate(map.sizeX / 2.0, map.sizeY / 2.0, map.sizeZ / 2.0)
    pushMatrix() # Global matrix
    pushMatrix() # Negative X wall matrix
    translate(- map.sizeX / 2.0, 0, 0)
    fill( 50,  25,  25)
    box(0, map.sizeY, map.sizeZ)
    popMatrix() # End of negative X wall matrix
    
    pushMatrix() # Positive X wall matrix
    translate(map.sizeX / 2.0, 0, 0)
    fill(100,  50,  50)
    box(0, map.sizeY, map.sizeZ)
    fill(255)
    textSize(36)
    rotateY(- HALF_PI)
    text("Yaw : " + str(cam.yaw) + ", Pitch : " + str(cam.pitch), 0, 0, map.sizeX / 4)
    popMatrix() # End of positive X wall matrix
    
    pushMatrix() # Positive Y wall matrix
    translate(0, map.sizeY / 2.0, 0)
    fill( 50, 100,  50)
    box(map.sizeX, 0, map.sizeZ)
    popMatrix() # End of positive Y wall matrix
    
    pushMatrix() # Negative Y wall matrix
    translate(0, - map.sizeY / 2.0, 0)
    fill( 25,  50,  25)
    box(map.sizeX, 0, map.sizeZ)
    popMatrix() # End of negative Y wall matrix
    
    pushMatrix() # Positive Z wall matrix
    translate(0, 0, map.sizeZ / 2.0)
    fill( 50,  50, 100)
    box(map.sizeX, map.sizeY, 0)
    popMatrix() # End of negative Y wall matrix
    
    pushMatrix() # Negative Z wall matrix
    translate(0, 0, -map.sizeZ / 2.0)
    fill( 25,  25,  50)
    box(map.sizeX, map.sizeY, 0)
    popMatrix() # End of negative Y wall matrix


    popMatrix() # End of global matrix