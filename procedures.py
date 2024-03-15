
def get_best_tavern(data, tact):
    sub = []
    tm = []
    for q in data:
        time = data[q]["time"].strip().split(':')
        if data[q]["time"] != "":
            time = data[q]["time"].strip().split(':')
            time = (int(time[0]) * 60) + int(time[1])
        else:time = 14000
        if data[q][tact] != "":
            stat = float(data[q][tact].strip())
        else:stat = 0
        sub.append([stat/time])
        tm.append(time)
    return {"q":str(sub.index(max(sub))),"time":tm[sub.index(max(sub))]}