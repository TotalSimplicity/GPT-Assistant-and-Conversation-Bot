import webbrowser
import music as ms
import secrets

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
end = "False"

substrings_to_clear = ["*browser*", "*Browser*", "*music leo*", "*Music Leo*", "*music Leo*", "*Music Random*", "*music random*", "*music stop*", "*Music Stop*", "*time*", "*Time*"]

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
        print("Time is disabled")

def clear_substrings(response):
    
    newResponse = response
    for substring in substrings_to_clear:
        newResponse = newResponse.replace(substring, "")
    return newResponse
'''
def check_end(response):
    if end == True:
        exit()
'''