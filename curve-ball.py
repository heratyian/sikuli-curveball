BROWSER = "Google Chrome.app"

running = True
GAME_SITE = "http://www.curveball-game.com/"

# time taken for mouse movement to a target location 
# Setting it to 0 will switch off any animation
Settings.MoveMouseDelay = 0
# number of times actual search operations are performed per second
Settings.ObserveScanRate = 100
#Settings.DelayBeforeMouseDown = 0

# end script
def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.TAB, KeyModifier.CTRL, runHotkey)

def open_chrome_to_website(site):
    App.open(BROWSER)
    wait(5)
    paste(site)
    type(Key.ENTER)
    wait("1472447096601.png", 10)

   
def start_game():
    click("1472447127229.png")
    wait(5)


open_chrome_to_website(GAME_SITE)
start_game()
region_object = find(Pattern("1472500373233.png").similar(0.30))

while running:
    ball = Pattern("1472504579127.png").similar(0.49)  
    try:
        click(region_object.find(ball))
    except:
        click()
            
    
    
    










    
    
