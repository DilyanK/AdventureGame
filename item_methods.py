import player
import map

def Use_ID(self):
    if player.current_room == map.rooms["Reception"]:
        map.rooms["Reception"].key["east"] = None
    else:
        print("no")