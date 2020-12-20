import os
import sys, subprocess
from time import sleep
print("------------------I'm your youtube downloading sweety-------------------")

try:
    from requests import ConnectionError
except:
    module = 'requests'
    print(f"Hey sweety we are installing {module}\n\
        because this your first time\n\
        please be patient!!!")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
    from youtubesearchpython import SearchVideos

    print("we are done!!!,\nfrom now on this step will be automatically ignored!")

try:
    from youtubesearchpython import SearchVideos
except:
    module = 'youtube-search-python'
    print(f"Hey sweety we are installing {module}\n\
        because this your first time\n\
        please be patient!!!")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
    from youtubesearchpython import SearchVideos

    print("we are done!!!,\nfrom now on this step will be automatically ignored!!!\n")

try:
    import youtube_dl
except:
    module = 'youtube_dl'
    print(f"Hey sweety we are installing {module}\n\
        because this your first time\n\
        please be patient!!!")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
    import youtube_dl

    print("we are done!!!,\nfrom now on this step will be automatically ignored!!!")

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


def s(query,quality):
    try:
        search = SearchVideos(f"{query}", offset=1, mode="list", max_results=1)
        channel = search.result()[0][4]
        title = search.result()[0][3]
        link = search.result()[0][2]
    except:
        print("Network error !")
        sleep(3)
        exit()
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    output_folder = f'{desktop}/youtube_downloader/{channel}'.replace("\\", "/")
    print(f"we are downloading {title} \n to -> {output_folder}".translate(non_bmp_map))
    while True:
        try:
            global x
            x=1
            with youtube_dl.YoutubeDL({'format': f'{quality}', 'outtmpl': output_folder + '/%(title)s.%(ext)s'},
                                      ) as ydl:
                ydl.download([link])
            print(f"\n\nYour video has been downloded to {output_folder}")
            break
        except ConnectionError:
            print("\nNetwork error ! We are trying again")
        except:
            break
            


print("your default video quality is 360p\n\
	enter 1080p for 1080p\n\
        enter 720p for 720p\n\
        enter 480p for 480p\n\
        enter 360p for 360p\n\
        enter 240p for 240p\n\
        enter 144p for 144p\n\
        enter audio for audio\n")   

x=0
quality=18
def quality_query(query):
    global quality
    quality_str=query.lower().strip()
    select_dict={"1080p":137,"720p":136,"480p":135,"360p":134,"240p":133,"144p":17,"audio":140,}
    try:
        quality = select_dict[quality_str]
        print(f"\nYour are now on {quality_str}")
        x=0
    except:
        s(query,quality)
        
quality_query(input("\nEnter your search (eg: papuni) :"))



while True:
    if x!=0:
        query = input("\nNeed another video Enter your search (type exit() to exit) :")
    else:
        query = input("\nEnter your search (eg: papuni) :")        
    if query.lower().strip()== "exit()":
        exit()
    quality_query(query)
