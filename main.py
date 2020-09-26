# pip install os
import os

import time

start = time.time()




# creat the folder if it dos not exists
def creatIFnotEXIST(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folder,files):
    for file in files :
        os.replace(file,f"{folder}/{file}")


if __name__ == "__main__":
    

    files = os.listdir()
    files.remove('main.py')
    # print(files)

    creatIFnotEXIST('Images')
    creatIFnotEXIST('Docs')
    creatIFnotEXIST('Media')
    creatIFnotEXIST('Anonymous')

    # # https://www.journaldev.com/32081/get-file-extension-in-python
    # pathlib.Path(file).suffix.lower()
    imgExt = ['.png','.jpg','.svg','.raw','.gif','.heif']
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExt ]
    # print(images)
    print("Total Images Found {}".format(len(images)))

    docExt = ['.txt','.docx','.txt','.pdf','.ppt']
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExt ]
    # print(docs)
    print("Total Docs Found {}".format(len(docs)))

    mediaExt = ['.mp4','.mp3','.flv','.vlc']
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExt ]
    # print(medias)
    print("Total Media Found {}".format(len(medias)))


    anonymous = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        # https://stackoverflow.com/questions/51920023/python-path-is-file-evaluates-symlink-as-a-file
        # pathlib.Path().is_file
        if (ext not in imgExt) and (ext not in docExt) and (ext not in mediaExt) and os.path.isfile(file) :
            anonymous.append(file)
    # print(anonymous)        

    # for image in images :
    #     os.replace(image,f"Images/{image}")
    # for doc in docs :
    #     os.replace(doc,f"Docs/{doc}")
    # for media in medias :
    #     os.replace(media,f"Media/{media}")
    # for Anonym in Anonymous :
    #     os.replace(Anonym,f"Anonymous/{Anonym}")
        
    move("Images",images)
    move("Docs",docs)
    move("Media",medias)
    move("Anonymous",anonymous)

    end = time.time()

    print("Total Cleared Files {}  in {:.3f}".format((len(docs)+len(images)+len(medias)+len(anonymous)),(end - start)))


