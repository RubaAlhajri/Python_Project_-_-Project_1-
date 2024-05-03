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
#to add to the playlist we must use extend, and change dataframe record to a dictionary
myPlayList.extend(testadd.to_dict(orient='records'))
myPlayList.extend(testadd.to_dict(orient='records'))
myPlayList.extend(testadd.to_dict(orient='records'))
myPlayList.extend(testadd2.to_dict(orient='records'))

#to get the song you want you must use index number of that song as shown below(Note: this will show the whole song valuables).
#if you want to only print the track name of the song you just write myPlayList[0]['track_name'], where the second square brackets [] will indicate the key values of the song dictionary
print(myPlayList[0])

#This is how you iterate through the playlist and print the values of each song
for song in myPlayList:
    print('song name:', song['track_name'])



