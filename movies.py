import os; import re; import shutil as sh
from pathlib import Path
import sys
sys.path.append(r"C:\Users\jr\Documents\programming\python")
import dir_files as d

movie_folder = r'D:\movies'
move_folder = r'D:\edited\#input'
more_than_1sub_folder = r'D:\edited\#morethan'
delete_folder = r'D:\edited\#del'

# for each file, if matches extension set to temp variable, if find size bigger, update temp var
filetypes = ['.mp4','.mkv','.avi']
def locate_movie(files):
    print('potential movie file:\n',files)
    r = (None, -1)
    for file in files:
        if Path(file).suffix in filetypes:
            print('possible movie file located:',file)
            if os.path.getsize(file) > r[1]: r = (file, os.path.getsize(file))
            print('details:',r)
    print('Movie returned :',r[0])
    return r[0]

#if contains more than 1 sub/srt file, how to find the right one
subtypes = ['.sub','.srt']
def locate_subs(files):
    print('potential sub file:\n',files)
    r = []
    for file in files:
        if Path(file).suffix in subtypes:
            print('possible sub file located:',file)
            r.append(file)
            print('details:',r)
    print('Subs returned :',r)
    return r

#rename if 1 sub to same same as movie, else prefix
def rename(movie_name,subs):
    _subs = subs[:]
    print('RENAME. movie name: ',movie_name,' subs: ',_subs)
    r = []
    def f(x):
        if len(_subs)==1:
            y = d.rename_file(x,movie_name)
            print(y)
            return y
        else:
            y = d.rename_file(x,movie_name+ ' - ' +d.get_filename_only(x))
            print(y)
            return y
    if len(_subs)>0:
        r.append(list(map(f,subs)))
    return d.unpack_list(r)


# set target folder depending on no of subs, move movie and subs there
def move(movie,subs):
    if  movie:
        target_folder = os.path.join(more_than_1sub_folder,d._file(movie).filename) if len(subs)>1 else move_folder
        print('moving....' , movie , str(subs))
        print('target folder: ', target_folder)
        d.move(movie,target_folder)
        print('done')
        if subs:
            print('subs here')
            for i in subs:
                d.move(i,target_folder)

# move folder to delete folder
def delete(folder):
    d.move(folder, delete_folder)

    
''' go thru each each dir, locate movie, locate subs in this folder or
subfolders, move them to main folder, delete subdir'''
movie_subfolders = d._file(movie_folder).dirs() #get subfolders
print('movie subfolders:\n', movie_subfolders)

for movie_subfolder in movie_subfolders:
    print('movie subfolder:\n', movie_subfolder)
    movie = locate_movie(d._file(movie_subfolder).all_files()) #get movie
    if movie:
        subs = locate_subs(d._file(movie_subfolder).all_files()) #get subs
        if subs: subs = rename(Path(movie).name, subs)
        move(movie,subs) #move movie/subs
    delete(movie_subfolder) #delete subfolder
