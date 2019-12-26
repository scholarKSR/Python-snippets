#! /usr/bin/env python3

#==============================WALK* FUNCTIONS=====================
"""
-------------------------------
function: walk(path)
function: walk2list(path)
function: walk4specific(path,filetype)
--------------------------------

os.walk(path)

1) GO TO NEXT ROOM:
2) CHECK FOR ARTICLES AND SUBROOMS:
3-N) IF NO ARTICLES AND SUBROOMS: COME OUT FOR STEP (1)
3-Y) IF ATRICLES FOUND: NOTE DOWN; IF SUBROOMS FOUND: NOTE DOWN
4) GO TO SUB ROOM
5) REPEAT STEP (2),(3-N),(3-Y)

THATS HOW IT WORKS.
"""
import os

def walkonly(path):
    folcount = 0
    filecount = 0
    print('walking...')
    for fol, sf, file in os.walk(path):
        folcount+=1
        #print('\n'+ 'CURRENT FOLDER: '+str(fol))
        for f in file:
            filecount+=1
            #print('\t\tFILE IN: '+str(fol)+':'+str(f))
        #for s in sf:
            #print('\tSUBFOLDER OF: '+str(fol)+':'+str(s))
        
    
    print('\nFiles : %d nos.'%filecount)
    print('Folders : %d nos.'%folcount+'\n---in complete path tree')

def walkviz(path):
    folcount = 0
    filecount = 0
    for fol, sf, file in os.walk(path):
        folcount+=1
        print('\n'+ 'CURRENT FOLDER: '+str(fol))
        for f in file:
            filecount+=1
            print('\t\tFILE IN: '+str(fol)+':'+str(f))
        for s in sf:
            print('\tSUBFOLDER OF: '+str(fol)+':'+str(s))
        
    print('\nFiles : %d nos.'%filecount)
    print('Folders : %d nos.'%folcount+'\n---in complete path tree')

def walkdot(path,fileType):
    for fol, sf, file in os.walk(path):
        #folcount+=1
        #print('\n'+ 'CURRENT FOLDER: '+str(fol))
        for f in file:
            #filecount+=1
            #print('\t\tFILE IN: '+str(fol)+':'+str(f))
            if f.endswith(fileType):
                print(str(fol)+' : '+str(f))
                #print('\n'+str(f))
        #for s in sf:
            #print('\tSUBFOLDER OF: '+str(fol)+':'+str(s))


"""
finds for matching string in filename
"""
def walksearch(path, string):
    for fol, sf, file in os.walk(path):
        #folcount+=1
        #print('\n'+ 'CURRENT FOLDER: '+str(fol))
        for f in file:
            #filecount+=1
            #print('\t\tFILE IN: '+str(fol)+':'+str(f))
            if string in f:
                print(str(fol)+' : '+str(f))
        #for s in sf:
            #print('\tSUBFOLDER OF: '+str(fol)+':'+str(s))


def walkexact(path, search):
    for fol, sf, file in os.walk(path):
        #folcount+=1
        #print('\n'+ 'CURRENT FOLDER: '+str(fol))
        for f in file:
            #filecount+=1
            #print('\t\tFILE IN: '+str(fol)+':'+str(f))
            if f == search:
                print(str(fol)+' : '+str(f))
        #for s in sf:
            #print('\tSUBFOLDER OF: '+str(fol)+':'+str(s))



    
"""
/run/user/1001/gvfs/mtp:host=%5Busb%3A002%2C004%5D
above is address of my smsung tizen
"""
#==========================================end of WALK* FUNCTIONS===============
#from ABC import *
#from walkwork import *
from path_functions import *
'''asdffffffffffffffffffffffffffc=construction'''#CONSTRUCTION--------
def walk_main(searchkey = input('---------------local system only-------- \nkey: ')):
    
    walktype_data = ['.', 's', 'a', 'v', 'f', 'work']
    path = pathinput()
    
    searchkey = keyinput()
    
    key = input('. search(s) exact(a) viz(v) ftype(f) work(new walk type) \nkey:')

    while True:
        if key not in walktype:
            print('!keyerror!')
            #print('key:'end=' ')
            key = input('key:')
            break
        
        else:
            print('walk-search...')
            if key == '.':
                walkonly(path)
                break
            if key == 'v':
                walkviz(path)
                break
            if key == 's':
                walksearch(path,searchkey)
                break
            if key == 'a':
                walkexact(path,searchkey)
                break
            if key == 'f':
                walkdot(path,searchkey)
                break
            if key == 'work':
                appopen('/home/kishore/LearnPY/walkwork.py')
                walkwork(path,searchkey)
                break
    
if __name__ == '__main__':
	walk_main()
	print('.................walk end..')