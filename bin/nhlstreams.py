#!/usr/bin/python3
#Ver 1.3.3.1
# This file must be in the same place as the JAR file:

#       http://www.reddit.com/r/NHLStreams/comments/2izhk1/the_vlc_fix/

#

# Edit this next line to match your VLC binary: ( \ = escape char, so double it for literal \ )

vlcbin =  "/usr/bin/vlc"

spw = 15 #Mac/Linux users: Adjust for however long you think it will take you to enter your password for sudo (time before VLC launches)

import json, urllib.request, urllib.error, urllib.parse, os, time, platform, subprocess, threading

#date = input("Enter date of game [YYYYMMDD]: ")
date = time.strftime("%Y%m%d")




if os.path.isfile(vlcbin):

    print("VLC Found!")

else:

    print("Please edit this file and fix VLC path!")

    time.sleep(5)

    os._exit(0)

pydir = os.path.dirname(os.path.abspath(__file__))

for root, dirs, files in os.walk(pydir):

    if 'FuckNeulionV1.jar' in files and not 'FuckNeulionV2.2.jar' in files:

        print("Please get version 2 of JAR")

        time.sleep(3)

        os._exit(0)

    elif 'FuckNeulionV2.2.jar' in files:

        print("Jar file found")

        break

    else:

        print("Could not find jar file in current folder. Please move it in where ever this script is located.")

        time.sleep(2)

        os._exit(0)

teams = {

                "NJD" : "devils",

                "OTT" : "senators",

                "MTL" : "canadiens",

                "TBL" : "lightning",

                "BUF" : "sabres",

                "NYI" : "islanders",

                "STL" : "blues",

                "NSH" : "predators",

                "ANA" : "ducks",

                "BOS" : "bruins",

                "VAN" : "canucks",

                "SJS" : "sharks",

                "PIT" : "penguins",

                "COL" : "avalanche",

                "CHI" : "blackhawks",

                "LAK" : "kings",

                "TOR" : "mapleleafs",

                "MIN" : "wild",

                "NYR" : "rangers",

                "PHI" : "flyers",

                "DAL" : "stars",

                "CBJ" : "bluejackets",

                "DET" : "redwings",

                "ARI" : "coyotes",

                "WSH" : "capitals",

                "WPG" : "jets",

                "CAR" : "hurricanes",

                "CGY" : "flames",

                "FLA" : "panthers",

                "EDM" : "oilers"

        }

tf = False

tf2 = False

favegame=False

startFav=False

z=0

runjar = False

os2 = platform.system()

ha="h"

t1=-1




if os2 == 'Windows':

    hdir = "C:\\Windows\\System32\\drivers\\etc\\hosts"

elif os2 == 'Linux':

    hdir = "/etc/hosts"

elif os2 == 'Darwin':

    hdir = "/private/etc/hosts"

else:

    hdir = ""

try:

    with open(hdir, "r") as hf:

        lines1 = hf.readlines()

        for l in lines1:

            li=l

            if li == '127.0.0.1 nlsk.neulion.com\n':

                tf = True

                break

            elif li == '#127.0.0.1 nlsk.neulion.com\n' or li == '# 127.0.0.1 nlsk.neulion.com\n':

                tf2 = True

                tf = True

                break

        hf.close()

        if not tf:

            if os2 == 'Windows':

                with open(hdir, "a") as hf2:

                    hf2.write("\n127.0.0.1 nlsk.neulion.com\n")

                    hf2.close()

            else:

                print("Please allow me to edit your hosts file. You won't be able to watch any games if I can't. (If prompted for password)")

                def write(hdir):

                    process = 'echo \"127.0.0.1 nlsk.neulion.com\" | sudo tee -a ' + hdir

                    subprocess.call(process,shell=True)

                t3 = threading.Thread(target=write,args=(hdir,))

                t3.start()

                t3.join()

        elif tf2:

            print("Remove the # before 127.0.0.1 nlsk.neulion.com in your host file before opening a game.")

            time.sleep(3)

            print("Exiting...")

            os._exit(0)

except:

    print("Hosts file can't be found. Please edit manually. See directions on how to run me as admin. If already edited, ignore me.")

while True:

    r = urllib.request.urlopen("http://live.nhl.com/GameData/SeasonSchedule-20142015.json")

    h = r.read()

    d = json.loads(h.decode())




	

	

    try:

        l = []

        lines = open("fav.txt","r")

        for li in lines:

            l.append(li)

        lines.close()

        

        fav = l[0].strip()

        if fav == "NONE":

            fav = None

        try:

            favbitrate = int(l[1].strip())

        except:
            if l[1].strip()=="ipad":
                favbitrate='ipad'
            else:
                favbitrate = None

        cdn = l[2]

           

			

            #print "Favourite loaded. {} at {} bitrate.".format(fav,favbitrate)

    except:

        while True:

            c = input("It seems you don't have a favorite team.\nWould you like to set one now? [Y/N] ")

            if c.lower()[:1] == "y" or c.lower()[:1] == "n":

                if c.lower()[:1] == "y":

                    while True:

                            teamlist = ""

                            for team in teams:

                                if len(teamlist) > 2:

                                    teamlist += ", "

                                teamlist += team

                            teamlist += " or None"

                            print(teamlist)

                            c = input("Which one is your favorite? ")

                            fav = c.upper()

                            if fav in teams or fav == 'NONE':

                                print("Okay, {} is now your favorite team.".format(fav))

                                break

                    while True:

                        bitrates = ["1600","3000","4500", "5000", "ipad", "none"]

                        c = input("What is your preferred bitrate? {} ".format(bitrates))

                        if c in bitrates:

                            favbitrate = c

                            with open("fav.txt","w") as f:

                                f.write(fav + "\n" + str(favbitrate))

                            break

                        else:

                            print("Sorry, that is not a valid bitrate. You may select 'none' to not set a bitrate.")

                            

                    while True:

                            cdns = ["cdnak","cdnllnwnl","cdnl3nl"]

                            c = input("What is your preferred CDN? {} ".format(cdns))

                            if c in cdns:

                                    cdn = c

                                    with open("fav.txt","a") as f:

                                            f.write("\n" + cdn)

                                    break

                            else:

                                print("Sorry, that is not a valid CDN. l = L")

                    break

                elif  c.lower()[:1] == "n":

                    cdn = "cdnak"

                    fav = None

                    favbitrate = None

                    break







            

    games = []

    for entry in d:

        if entry['est'][:8] == date:

            games.append({"id":str(entry['id'])[-4:],"id2":str(entry['id'])[-6:],"id3":str(entry['id']),"home":entry['h'],"away":entry['a'], "time":str(entry['est'])[-8:]})

    if not games:

        print("I couldn't find any games for that date. Sorry.")
        time.sleep(5)
        os._exit(0)

    

    gamelist = ""

    favGame = 0

    from datetime import datetime, timedelta as td

    from datetime import tzinfo

    for (i,game) in enumerate(games):

        t = game['time']

        t = datetime.strptime(t, "%H:%M:%S")

        t=t.strftime("%I:%M %p")

        gamelist += "{}: {} at {} {}".format(i+1,game['away'],game['home'],t)

        

        if fav == game['away'] or fav == game['home']:

            gamelist += "**"

            if fav == game['away']:

                ha = "away"

            else:

                ha="home"

            if not startFav:

                favGame = i+1

         

        gamelist += "\n"





    if favGame > 0:

        if z ==0:

            favegame=True

            z=int(z)+1

            cin=favGame

            startFav=True

    else:

        startFav = False

        z=int(z)+1



    if not startFav and z > 0:

        print(gamelist)

        cin = input("Which game would you like to start (#) (q to quit)? ")

        if cin.lower()[:1] == "q":

            if runjar==True:

                if os2 == 'Windows':

                    subprocess.call("TASKKILL /F /PID {pid} /T >NUL".format(pid=t1.pid),shell=True)

                elif os2 == 'Darwin':

                    subprocess.Popen("sudo kill {pid}".format(pid=t1.pid),shell=True)

                else:

                    subprocess.Popen('sudo killall sudo',shell=True)

            os._exit(0)

    try:

        if int(cin) <= 0 or int(cin) > i+1:

            print("Please select a number between 1 and {}".format(i+1))

            time.sleep(2)

            continue

        gameid = games[int(cin)-1]['id']

        gameid2 = games[int(cin)-1]['id2'][:2]

        gid  = games[int(cin)-1]['id3']



    except:

        print("Please select a number between 1 and {}".format(i+1))

        time.sleep(2)

        continue



    url = "http://smb.cdnak.neulion.com/fs/nhl/mobile/feed_new/data/streams/2014/ipad/{}_{}.json".format(gameid2, gameid)

    

    try:

        r = urllib.request.urlopen(url)

        h = r.read()

        d = json.loads(h.decode())



        home = d['gameStreams']['ipad']['home']['live']['bitrate0']

        away = d['gameStreams']['ipad']['away']['live']['bitrate0']

        if favegame:

            cin = input("{} is playing today. Start it? [Y/N] ".format(fav))

            if cin.lower()[:1] == "y":

                cin = favGame

                gid = games[cin-1]['id3']

                favegame=False

            else:

                startFav=False

                favegame=False

                continue

    except:

        if favegame:

            favegame=False

            startFav=False

            continue

        else:

            print("It appears that game hasn't started yet. Sorry.")
            time.sleep(5)
            continue



    if not home or not away:

        print("I couldn't find any streams for this game. Sorry.")
        time.sleep(5)
        continue



    if "mp4" in home or "mp4" in away:

        print("It appears that game has ended already, or hasn't started. Sorry.")
        time.sleep(5)
        continue



    if favbitrate is not None:
        bitrates = favbitrate

    else:
        print(favbitrate)
        bitrates = [1600,3000,4500, 5000, "ipad"]



    urls = [home,away]

    urllist = []

    i = 0

    urlstring = ""

    for url in urls:

        url = url[:-9]
        if favbitrate is None:
            for bitrate in bitrates:



                if startFav == True and fav is not None and teams[fav] not in url:

                    continue



                i += 1

                string = "{}{}.m3u8".format(url,bitrate)
                string = string.replace('cdnak', cdn.strip())
                urllist.append(string)

                urlstring += "{}: {}\n".format(i,string)

        else:
            if startFav == True and fav is not None and teams[fav] not in url:

                continue

            

            i += 1

            string = "{}{}.m3u8".format(url,bitrates)
            string = string.replace('cdnak', cdn.strip())
            urllist.append(string)

            urlstring += "{}: {}\n".format(i,string)



    #~ print urllist



    if len(urllist) > 1 and not startFav:

        while True:

            print("Here are the URLs I found for this game:")

            print(urlstring)

            urlnum = input("Choose a stream (#): ")

            try:

                if int(urlnum) < 1 or int(urlnum) > i+1:

                    print("Please select a number between 1 and {}".format(i))

                    time.sleep(2)

                    continue

                url = str(urllist[int(urlnum)-1])

                if i == 12:

                    if int(urlnum) <7:

                        ha = "home"

                    else:

                        ha = "away"

                else:

                    if int(urlnum) == 1:



                        ha = "home"

                    else:

                        ha = "away"

                break

            except:

                print("Please select a number between 1 and {}".format(i))

                time.sleep(2)

                continue

    else:

        url = urllist[0]







    yn = 'n'
    count=0

    if os2 == 'Windows':

        def run_vlc(url):

            process = '"' + vlcbin + '" ' + url + ' :http-user-agent=\"PS4 libhttp/1.76 (PlayStation 4)\" :http-continuous :http-reconnect'

            subprocess.call(process,shell=True)

            return



        if not runjar:
            while yn.lower()[:1] == 'n' and count<5:
                t1 = subprocess.Popen('java -jar FuckNeulionV2.2.jar '+gid+' '+ha,shell=True)

                time.sleep(5)
                yn = input("Did you get HOUSTON...? [Y/N] ")
                count=int(count)+1
            if count == 5:
                print("The jar isn't working now. Wait a couple minutes and try again.")
                time.sleep(5)
                continue

            runjar=True

        t2 = threading.Thread(target=run_vlc,args=(url,))

        t2.start()

        print("Starting VLC...")

        time.sleep(5)

        yn = input("Start another game? [Y/N] ")

        if yn.lower()[:1] == "y":
            t2.join()

            subprocess.call("TASKKILL /F /PID {pid} /T >NUL".format(pid=t1.pid),shell=True)

            runjar=False

            continue

        else:

            t2.join()

            break

    elif os2 == 'Darwin':

       def run_vlc(url):

            process = '"' + vlcbin + '" -q :http-continuous :http-reconnect ' + url + ' 2> /dev/null'  #+ ' :http-user-agent=\"iTunesAppleTV/4.1\"'

            subprocess.call(process,shell=True)

            return

       if not runjar:
            t1 = subprocess.Popen('sudo java -jar FuckNeulionV2.2.jar '+gid+' '+ha,shell=True)
            time.sleep(int(spw))
            while yn.lower()[:1] == 'n' and count<5:
                if count > 0:
                    t1 = subprocess.Popen('sudo java -jar FuckNeulionV2.2.jar '+gid+' '+ha,shell=True)
                    time.sleep(5)
                yn = input("Did you get HOUSTON...? [Y/N] ")
                
                count=int(count)+1
            if count == 5:
                print("The jar isn't working now. Wait a couple minutes and try again.")
                time.sleep(5)
                continue

            runjar=True



       

       t2 = threading.Thread(target=run_vlc,args=(url,))

       t2.start()

       print("Starting VLC...")

       time.sleep(5)

       yn = input("Start another game? ONE GAME AT A TIME! [Y/N] ")

       if yn.lower()[:1] == "y":
            t2.join()

            subprocess.Popen("sudo kill {pid}".format(pid=t1.pid),shell=True)

            runjar=False

            continue

       else:

            t2.join()

            break

    else:

       def run_vlc(url2):
            print(url2)
            process = '"' + vlcbin + '" -q :http-continuous :http-reconnect ' + url2 + ' 2> /dev/null'# + ' :http-user-agent=\"iTunesAppleTV/4.1\"'

            subprocess.call(process,shell=True)

            return

       if not runjar:

            t1 = subprocess.Popen('sudo java -jar FuckNeulionV2.2.jar '+gid+' '+ha,shell=True)
            time.sleep(int(spw))
            while yn.lower()[:1] == 'n' and count<5:
                if count > 0:
                    t1 = subprocess.Popen('sudo java -jar FuckNeulionV2.2.jar '+gid+' '+ha,shell=True)
                    time.sleep(5)
                yn = input("Did you get HOUSTON...? [Y/N] ")
                
                count=int(count)+1
            if count == 5:
                print("The jar isn't working now. Wait a couple minutes and try again.")
                time.sleep(5)
                continue

            runjar=True



       t2 = threading.Thread(target=run_vlc,args=(url,))

       t2.start()

       print("Starting VLC...")

       time.sleep(5)

       yn = input("Start another game? ONE GAME AT A TIME! [Y/N] ")

       if yn.lower()[:1] == "y":
            t2.join()
            subprocess.Popen('sudo killall sudo',shell=True)

            runjar=False

            continue

       else:

            t2.join()

            break

            

if runjar==True:

    if os2 == 'Windows':

        subprocess.call("TASKKILL /F /PID {pid} /T >NUL".format(pid=t1.pid),shell=True)

    elif os2 == 'Darwin':

        subprocess.Popen("sudo kill {pid}".format(pid=t1.pid),shell=True)

    else:

        subprocess.Popen('sudo killall sudo',shell=True)
