import modules.rpc as rpc
import modules.api as api
import time
import sys

def get_platform(platform=sys.platform):
    if platform == "win32":
        import modules.WinClient as ss
        return ss.Client()
    else:
        import modules.MacClient as ss
        return ss.Client()
        
print('//--------------------------------------------------------------------//')
print('//                                                                    //')
print('//       Created by Brooke (Chaottiic#001)                            //')
print('//                                                                    //')
print('//                                                                    //')
print('//       Website - https://chaottiic.com                              //')
print('//                                                                    //')
print('//       Discord - https://chaottiic.com/discord                      //')
print('//                                                                    //')
print('//                                                                    //')
print('//--------------------------------------------------------------------//')
print(' ')
print(' ')
rpc_obj = rpc.DiscordIpcClient.for_platform("608727865202180121")
if api.getSetting("DEBUG"):
    print('[LOGS] Connected to Discords RP API Successfully')
time.sleep(5)
start_time = int(round(time.time() * 1000))
old_ign = old_game= ""
while True:
    try:
        chrome = get_platform()
        if chrome == "None" or chrome == None:
            game = "Nothing :("
            icon = "1"
        else:
            if chrome == "home":
                game = "Nothing :("
                icon = "1"
            else:
                game = api.getGameName(chrome)
                icon = api.getIcon(game)
        ign = api.getSetting("IGN")
        if ign != old_ign:
            if api.getSetting("DEBUG"):
                print(f'[LOGS] Updated IGN from "{old_ign}" to "{ign}"')
            old_ign = ign 
        if game != old_game:
            if api.getSetting("DEBUG"):
                print(f'[LOGS] Updated game from "{old_game}" to "{game}"')
            old_game = game 

        activity = {
                "state": f"IGN - {ign}",
                "details": f"Playing {game}",
                "timestamps": {
                    "start": start_time
                },
                "assets": {
                    "large_text": api.getSetting("WEBSITE"),
                    "large_image": icon
                }
            }
        rpc_obj.set_activity(activity)
        if api.getSetting("DEBUG"):
                print('[LOGS] Successfully updated')
        time.sleep(25)
    except Exception as e:
        if api.getSetting("DEBUG"):
                print(f'[LOGS] {e}')
