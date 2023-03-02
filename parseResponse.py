import webbrowser
import gettime as tm
import music as ms
import secrets

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
end = "False"

def special_instructions(response):
    if "*browser*" in response.lower():
        print("Opening browser....")
        webbrowser.get(chrome_path).open("google.com")
    if "*music leo*" in response.lower():
        ms.playPlaylist(ms.playlistLeo)
    if "*music random*" in response.lower():
        randomPlaylist = secrets.choice(ms.allPlaylists)
        ms.playPlaylist(randomPlaylist)
    if "*music stop*" in response.lower():
        ms.stopMusic()
    if "*volume half*" in response.lower():
        ms.changeVolume(50)
    if "*volume full*" in response.lower():
        ms.changeVolume(100)
    if "*time*" in response.lower():
        tm.get_time()

def clear_substrings(response):
    newResponse = response.replace("*browser*", "")
    newResponse = newResponse.replace("*Browser*", "")
    newResponse = newResponse.replace("*music leo*", "")
    newResponse = newResponse.replace("*Music Leo*", "")
    newResponse = newResponse.replace("*music Leo*", "")
    newResponse = newResponse.replace("*Music Random*", "")
    newResponse = newResponse.replace("*music random*", "")
    newResponse = newResponse.replace("*music stop*", "")
    newResponse = newResponse.replace("*Music Stop*", "")
    newResponse = newResponse.replace("*time*", "")
    newResponse = newResponse.replace("*Time*", "")
    return newResponse
'''
def check_end(response):
    if end == True:
        exit()
'''