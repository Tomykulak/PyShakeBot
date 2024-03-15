from screen_graber import crop_image, get_color_pixel, screen_grab, get_resolution
import bot_controller
from resolver import check
from procedures import get_best_tavern
from bot_controller import click, wait
from screen_graber import get_resolution, get_text, crop_image
import json

positions_path = "positions.json"
f = open(positions_path)
positions = json.load(f)
f.close()
#TODO get config 
tact = "xp" #just for now
def do_procedure(key):

    procedures = {} #-tady jsou uloženy všechny procedury které máme
    
    def proc(proc_fn): #tady se to nahází do dictu ze kterýho to pak pustíš když chceš
        procedures[proc_fn.__name__] = proc_fn #funkce v py jsou jenom objekty takže mají __name__
    
    @proc
    def login():
        res = get_resolution()
        character = positions['login']['character'].copy()
        click(character['width']* res[0], character['height'] * res[1]) # kliknuti pro login postavy
        return False
        
    @proc
    def daily_bonus():
        wait(2)
        print("Zacatek daily loginu\n")
        res = get_resolution()
        daily_btn = positions['daily_bonus']['button'].copy()
        daily_header = positions['daily_bonus']['header']['frame'].copy()
        frame = (daily_header[0]*res[0],daily_header[1]*res[1],daily_header[2]*res[0],daily_header[3]*res[1])
        daily_bonus_text = (get_text(crop_image(screen_grab(),frame)))
        daily_bonus_text.strip()
        daily_counter = 0
        daily_array = ['D','A','I','L','Y','B','O','N','U','S']
    #prohleda tesseract text v daily bonusu
        for letter in daily_bonus_text:
            if letter in daily_array and daily_counter <= 6:
                daily_counter += 1
                daily_array.remove(letter)
        print("[", daily_counter, "] Daily bonus counter")
        if daily_counter > 6:
            click(daily_btn['width']* res[0], daily_btn['height'] * res[1])
        else:
            print("Nenasel jsem daily")
        return True
    @proc
    def tavern():
        check()
        res = get_resolution()
        tavern_menu_btn = positions['menu']['tavern'].copy()
        bot_controller.click(tavern_menu_btn['width'] * res[0], tavern_menu_btn['height']* res[1])
        #TODO GET thirst val
    #hledání npc
        active_npc = None
        npcs = positions['tavern']['npc'].copy()
        for npc in npcs:
            npc = npcs[npc].copy()
            if npc['color'] is not None:
                if npc['color']  == get_color_pixel(npc['width'] * res[0], npc['height'] * res[1]):
                    active_npc = npc.copy()
                    break
                else: print( get_color_pixel(npc['width'] * res[0], npc['height'] * res[1]) + "//////" + npc['color'])
    #npc nalezen
        if active_npc is not None:
            bot_controller.click(active_npc['width'] * res[0], active_npc['height']* res[1])
    #choose Quest
            tavern_q_nav = positions['tavern']['quest_nav'].copy()
            q_stats = {}
            for q in tavern_q_nav:
                wait(0.1)
                count = q
                q = tavern_q_nav[q].copy()
                quest = positions['tavern']['quest'].copy()
                bot_controller.click(q['width'] * res[0], q['height']* res[1])
    #získání quest stats
                q_stats[count] = {
                    "gold":get_text(crop_image(screen_grab(),tuple((quest['gold'][0]* res[0],quest['gold'][1]* res[1],quest['gold'][2]* res[0],quest['gold'][3]* res[1])))),
                    "xp":get_text(crop_image(screen_grab(),tuple((quest['xp'][0]* res[0],quest['xp'][1]* res[1],quest['xp'][2]* res[0],quest['xp'][3]* res[1])))),
                    "time":get_text(crop_image(screen_grab(),tuple((quest['time'][0]* res[0],quest['time'][1]* res[1],quest['time'][2]* res[0],quest['time'][3]* res[1])))),
                    }
            best = get_best_tavern(q_stats, tact) #provede přepočet a vybere nejlepší hospodu
            best_time = best["time"]
            best_q = best["q"]
            bot_controller.click(tavern_q_nav[best_q]['width'] * res[0], tavern_q_nav[best_q]['height']* res[1])
            bot_controller.click(positions['tavern']["accept_quest"]['width'] * res[0], positions['tavern']["accept_quest"]['height']* res[1])
            #return {False,best["time"]}
            wait(int(best_time) + 1)
    #čekání na splnění úkolu
            for i in range(3):
                wait(0.5)
                bot_controller.click(positions['tavern']["fight"]['skip_ok_button']['width'] * res[0], positions['tavern']["fight"]['skip_ok_button']['height']* res[1])
            check()
            return False
        else:
            raise Exception('NPC nenalezen')
    
    @proc
    def arena():
        print("Vyberu nejlepší arenu" )
        #TODO
        return True
    @proc
    def dungeon():
        print("Vyberu nejlepší úkol dungeon" )
        #TODO
        return True
    
    procedures[key]()
    