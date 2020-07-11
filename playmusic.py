import os
music_dir="D:\\Irfan\\My Music\\English songs"
print(os.listdir("D:\\Irfan\\My Music\\English songs"))
songs=os.listdir(music_dir)
song=input("Which song would you like to listen?:")
if "right now" in song:
    os.startfile(os.path.join(music_dir,songs[0]))
if "baby" in song:
    os.startfile(os.path.join(music_dir,songs[1]))
if "let me love you" in song:
    os.startfile(os.path.join(music_dir,songs[2]))