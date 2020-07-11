import os
music_dir="D:\Irfan\My Music\English songs"
songs=os.listdir(music_dir)
os.startfile(os.path.join(music_dir,songs[2]))