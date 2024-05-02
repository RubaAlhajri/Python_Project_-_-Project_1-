import pandas as pd

def serachByname(name, musicList):
    for song in musicList:
        if song['track_name'] == name:
            return song
    
    return None

def maxKey(musicList, keyname):
    maxKey = {}
    for song in musicList:
        key = song.get(keyname)

        if key:
            maxKey[key] =maxKey.get(key, 0) + 1
    
    return max(maxKey, key = maxKey.get)

#===========================================================

musicLib = pd.read_csv('tcc_ceds_music.csv')

testadd = musicLib[musicLib['track_name'] == 'let her cry']
testadd2 = musicLib[musicLib['track_name'] == 'the way you look tonight']


myPlayList = []
#to add to the play list we must use extend, and change dataframe record to a dictionary
myPlayList.extend(testadd.to_dict(orient='records'))
myPlayList.extend(testadd.to_dict(orient='records'))
myPlayList.extend(testadd.to_dict(orient='records'))
myPlayList.extend(testadd2.to_dict(orient='records'))

print(myPlayList[0])
for song in myPlayList:
    print('song name:', song['track_name'])



