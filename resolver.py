from screen_graber import crop_image, get_text, screen_grab, get_resolution
import bot_controller, json

positions_path = "positions.json"
f = open(positions_path)
positions = json.load(f)
f.close()

def check(): #pro řešení popups
    res = get_resolution()
    print("check nesrovnalostí" )
    for warn in positions["warnings"]:
        warn = positions["warnings"][warn]
        if warn["text"] == get_text(crop_image(screen_grab(),tuple((warn['frame'][0]* res[0],warn['frame'][1]* res[1],warn['frame'][2]* res[0],warn['frame'][3]* res[1])))):
            bot_controller.click(warn["button"]['width'] * res[0], warn["button"]['height']* res[1])
            break