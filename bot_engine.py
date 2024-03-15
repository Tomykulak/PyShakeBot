#bude hlavním programem bota
import time
import webbrowser
import bot_controller
import decorator_procedure


#proc_status drží procedury které se provedli True / neprovedli False
proc_status = {"login":True,"daily_bonus":True,"tavern":True}

def start(server):
    run_game(server)
    bot_controller.wait(1) ##load
    #TODO
    while any(proc_status):
        for proc in proc_status:
            bot_controller.wait(0.5)
            proc_status[proc] = decorator_procedure.do_procedure(proc)
                   
                   
def run_game(server):
    webbrowser.open_new('https://' + server + '.sfgame.net/')
    bot_controller.wait(5)
    bot_controller.press('f11') #enter fullScreen mode