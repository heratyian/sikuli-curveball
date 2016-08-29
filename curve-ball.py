running = True
GAME_SITE = "http://www.curveball-game.com/"
GAME_REGION = Region()

Env.MoveMouseDelay = 0.05
Env.ObserveScanRate = 0.05
Env.DelayBeforeMouseDown = 0.05

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.TAB, KeyModifier.CTRL, runHotkey)

def open_chrome_to_website(site):
    App.open("Google Chrome.app")
    wait(5)
    paste(site)
    type(Key.ENTER)
    wait("1472447096601.png", 10)
    region_object = find("1472447096601.png")
    #print(region_object.getX())
    global GAME_REGION
    GAME_REGION = region_object

    

def start_game():
    click("1472447127229.png")
    mouse_spot = Env.getMouseLocation()
    print(mouse_spot.getX())
    print(mouse_spot.getY())
    wait(5)
    print(GAME_REGION)


    
open_chrome_to_website(GAME_SITE)
start_game()

global GAME_REGION

while running:
    region_object = find(Pattern("1472500373233.png").similar(0.30))
    
    ball = Pattern("1472494780504.png").similar(0.55)
    
    if region_object.find(ball): # might take up to 1 sec
        firstLoc = region_object.find(ball)
        clickLoc = firstLoc.nearby(100).find(ball) # should be very fast
        if click(clickLoc): # good chance to hit it
            mouse_spot = Env.getMouseLocation()
            hover(Location(mouse_spot.getX(), mouse_spot.getY()+80))
    
    
    
    
    
    
    










    
    
