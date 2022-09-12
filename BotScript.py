import tweepy
import time
import random
import datetime

consumer_key = ???
consumer_secret = ???

key = ???
secret = ???

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True, retry_count=10, retry_delay=5, retry_errors=set([503]))

## Defining tweet id storage commands
FILE_NAME = "last_seen.txt"

def read_last_seen(FILE_NAME):
   file_read = open(FILE_NAME, 'r')
   last_seen_id = int(file_read.read().strip())
   file_read.close()
   return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
   file_write = open(FILE_NAME, 'w')
   file_write.write(str(last_seen_id))
   file_write.close()
   return

FILE_NAME2 = "sox_wins.txt"

def total():
   file_read = open(FILE_NAME2,'r')
   win_total = int(file_read.read().strip())
   file_read.close()
   new_win_total = win_total + 1
   file_write = open(FILE_NAME2, 'w')
   file_write.write(str(new_win_total))
   file_write.close()
   return win_total

def read_wins():
   file_read = open(FILE_NAME2, 'r')
   actual_wins = int(file_read.read().strip())
   actual_wins -= 1
   file_read.close()
   return actual_wins

def loss_total():
   file_read = open("sox_losses.txt",'r')
   loss_total = int(file_read.read().strip())
   file_read.close()
   new_loss_total = loss_total + 1
   file_write = open("sox_losses.txt", 'w')
   file_write.write(str(new_loss_total))
   file_write.close()
   return loss_total

def read_losses():
   file_read = open("sox_losses.txt", 'r')
   actual_losses = int(file_read.read().strip())
   actual_losses -= 1
   file_read.close()
   return actual_losses

FILE_NAME3 = "gamedaydone.txt"
def read_done(FILE_NAME3):
   file_read = open(FILE_NAME3, 'r')
   last_done = file_read.read()
   file_read.close()
   return last_done
def store_done(FILE_NAME3):
   file_write = open(FILE_NAME3, 'w')
   file_write.write(str('Done'))
   file_write.close()
   return
def store_notdone(FILE_NAME3):
   file_write = open(FILE_NAME3, 'w')
   file_write.write(str('Not Done'))
   file_write.close()
   return

FILE_NAME4 = "series.txt"
def read_series(FILE_NAME4):
   file_read = open(FILE_NAME4, 'r')
   last_series = file_read.read()
   file_read.close()
   return last_series
def store_series_home(FILE_NAME4, opponent):
   opponentkey = 'H' + str(opponent)
   gamenum = read_series(FILE_NAME4).count(opponentkey)+1
   file_write = open(FILE_NAME4, 'w')
   file_write.write(str(opponentkey) * (gamenum))
   file_write.close()
   return
def store_series_away(FILE_NAME4, opponent):
   opponentkey = 'A' + str(opponent)
   gamenum = read_series(FILE_NAME4).count(opponentkey)+1
   file_write = open(FILE_NAME4, 'w')
   file_write.write(str(opponentkey) * (gamenum))
   file_write.close()
   return

FILE_NAME5 = "Last10.txt"


def read_last10(FILE_NAME5):
   file_read = open(FILE_NAME5, 'r')
   last10 = str(file_read.read().strip())
   file_read.close()
   return last10

def store_last10(FILE_NAME5, newlast10):
   file_write = open(FILE_NAME5, 'w')
   file_write.write(str(newlast10))
   file_write.close()
   return

fullschedule = {'2022-07-01': ['2022-07-01 - Boston Red Sox (5) @ Chicago Cubs (6) (Final)'],
'2022-07-02': ['2022-07-02 - Boston Red Sox (1) @ Chicago Cubs (3) (Final)'],
'2022-07-03': ['2022-07-03 - Boston Red Sox (4) @ Chicago Cubs (2) (Final)'],
'2022-07-04': ['2022-07-04 - Tampa Bay Rays (0) @ Boston Red Sox (4) (Final)'],
'2022-07-05': ['2022-07-05 - Tampa Bay Rays (8) @ Boston Red Sox (4) (Final)'],
'2022-07-06': ['2022-07-06 - Tampa Bay Rays @ Boston Red Sox (Scheduled)'],
'2022-07-07': ['2022-07-07 - New York Yankees @ Boston Red Sox (Scheduled)'],
'2022-07-08': ['2022-07-08 - New York Yankees @ Boston Red Sox (Scheduled)'],
'2022-07-09': ['2022-07-09 - New York Yankees @ Boston Red Sox (Scheduled)'],
'2022-07-10': ['2022-07-10 - New York Yankees @ Boston Red Sox (Scheduled)'],
'2022-07-11': ['2022-07-11 - Boston Red Sox @ Tampa Bay Rays (Scheduled)'],
'2022-07-12': ['2022-07-12 - Boston Red Sox @ Tampa Bay Rays (Scheduled)'],
'2022-07-13': ['2022-07-13 - Boston Red Sox @ Tampa Bay Rays (Scheduled)'],
'2022-07-14': ['2022-07-14 - Boston Red Sox @ Tampa Bay Rays (Scheduled)'],
'2022-07-15': ['2022-07-15 - Boston Red Sox @ New York Yankees (Scheduled)'],
'2022-07-16': ['2022-07-16 - Boston Red Sox @ New York Yankees (Scheduled)'],
'2022-07-17': ['2022-07-17 - Boston Red Sox @ New York Yankees (Scheduled)'],
'2022-07-18': [''],
'2022-07-19': [''],
'2022-07-20': [''], '2022-07-21': [''],
'2022-07-22': ['2022-07-22 - Toronto Blue Jays @ Boston Red Sox (Scheduled)'],
'2022-07-23': ['2022-07-23 - Toronto Blue Jays @ Boston Red Sox (Scheduled)'],
'2022-07-24': ['2022-07-24 - Toronto Blue Jays @ Boston Red Sox (Scheduled)'],
'2022-07-25': ['2022-07-25 - Cleveland Guardians @ Boston Red Sox (Scheduled)'],
'2022-07-26': ['2022-07-26 - Cleveland Guardians @ Boston Red Sox (Scheduled)'],
'2022-07-27': ['2022-07-27 - Cleveland Guardians @ Boston Red Sox (Scheduled)'],
'2022-07-28': ['2022-07-28 - Cleveland Guardians @ Boston Red Sox (Scheduled)'],
'2022-07-29': ['2022-07-29 - Milwaukee Brewers @ Boston Red Sox (Scheduled)'],
'2022-07-30': ['2022-07-30 - Milwaukee Brewers @ Boston Red Sox (Scheduled)'],
'2022-07-31': ['2022-07-31 - Milwaukee Brewers @ Boston Red Sox (Scheduled)'],
'2022-08-01': ['2022-08-01 - Boston Red Sox @ Houston Astros (Scheduled)'],
'2022-08-02': ['2022-08-02 - Boston Red Sox @ Houston Astros (Scheduled)'],
'2022-08-03': ['2022-08-03 - Boston Red Sox @ Houston Astros (Scheduled)'],
'2022-08-04': ['2022-08-04 - Boston Red Sox @ Kansas City Royals (Scheduled)'],
'2022-08-05': ['2022-08-05 - Boston Red Sox @ Kansas City Royals (Scheduled)'],
'2022-08-06': ['2022-08-06 - Boston Red Sox @ Kansas City Royals (Scheduled)'],
'2022-08-07': ['2022-08-07 - Boston Red Sox @ Kansas City Royals (Scheduled)'],
'2022-08-08': [''],
'2022-08-09': ['2022-08-09 - Atlanta Braves @ Boston Red Sox (Scheduled)'],
'2022-08-10': ['2022-08-10 - Atlanta Braves @ Boston Red Sox (Scheduled)'],
'2022-08-11': ['2022-08-11 - Baltimore Orioles @ Boston Red Sox (Scheduled)'],
'2022-08-12': ['2022-08-12 - New York Yankees @ Boston Red Sox (Scheduled)'],
'2022-08-13': ['2022-08-13 - New York Yankees @ Boston Red Sox (Scheduled)'],
'2022-08-14': ['2022-08-14 - New York Yankees @ Boston Red Sox (Scheduled)'],
'2022-08-15': [''],
'2022-08-16': ['2022-08-16 - Boston Red Sox @ Pittsburgh Pirates (Scheduled)'],
'2022-08-17': ['2022-08-17 - Boston Red Sox @ Pittsburgh Pirates (Scheduled)'],
'2022-08-18': ['2022-08-18 - Boston Red Sox @ Pittsburgh Pirates (Scheduled)'],
'2022-08-19': ['2022-08-19 - Boston Red Sox @ Baltimore Orioles (Scheduled)'],
'2022-08-20': ['2022-08-20 - Boston Red Sox @ Baltimore Orioles (Scheduled)'],
'2022-08-21': ['2022-08-21 - Boston Red Sox @ Baltimore Orioles (Scheduled)'],
'2022-08-22': [''],
'2022-08-23': ['2022-08-23 - Toronto Blue Jays @ Boston Red Sox (Scheduled)'],
'2022-08-24': ['2022-08-24 - Toronto Blue Jays @ Boston Red Sox (Scheduled)'],
'2022-08-25': ['2022-08-25 - Toronto Blue Jays @ Boston Red Sox (Scheduled)'],
'2022-08-26': ['2022-08-26 - Tampa Bay Rays @ Boston Red Sox (Scheduled)'],
'2022-08-27': ['2022-08-27 - Tampa Bay Rays @ Boston Red Sox (Scheduled)'],
'2022-08-28': ['2022-08-28 - Tampa Bay Rays @ Boston Red Sox (Scheduled)'],
'2022-08-29': ['2022-08-29 - Boston Red Sox @ Minnesota Twins (Scheduled)'],
'2022-08-30': ['2022-08-30 - Boston Red Sox @ Minnesota Twins (Scheduled)'],
'2022-08-31': ['2022-08-31 - Boston Red Sox @ Minnesota Twins (Scheduled)'],
'2022-09-01': ['2022-09-01 - Texas Rangers @ Boston Red Sox (Scheduled)'],
'2022-09-02': ['2022-09-02 - Texas Rangers @ Boston Red Sox (Scheduled)'],
'2022-09-03': ['2022-09-03 - Texas Rangers @ Boston Red Sox (Scheduled)'],
'2022-09-04': ['2022-09-04 - Texas Rangers @ Boston Red Sox (Scheduled)'],
'2022-09-05': ['2022-09-05 - Boston Red Sox @ Tampa Bay Rays (Scheduled)'],
'2022-09-06': ['2022-09-06 - Boston Red Sox @ Tampa Bay Rays (Scheduled)'],
'2022-09-07': ['2022-09-07 - Boston Red Sox @ Tampa Bay Rays (Scheduled)'],
'2022-09-08': [''],
'2022-09-09': ['2022-09-09 - Boston Red Sox @ Baltimore Orioles (Scheduled)'],
'2022-09-10': ['2022-09-10 - Boston Red Sox @ Baltimore Orioles (Scheduled)'],
'2022-09-11': ['2022-09-11 - Boston Red Sox @ Baltimore Orioles (Scheduled)'],
'2022-09-12': [''],
'2022-09-13': ['2022-09-13 - New York Yankees @ Boston Red Sox (Scheduled)'],
'2022-09-14': ['2022-09-14 - New York Yankees @ Boston Red Sox (Scheduled)'],
'2022-09-15': [''],
'2022-09-16': ['2022-09-16 - Kansas City Royals @ Boston Red Sox (Scheduled)'],
'2022-09-17': ['2022-09-17 - Kansas City Royals @ Boston Red Sox (Scheduled)'],
'2022-09-18': ['2022-09-18 - Kansas City Royals @ Boston Red Sox (Scheduled)'],
'2022-09-19': [''],
'2022-09-20': ['2022-09-20 - Boston Red Sox @ Cincinnati Reds (Scheduled)'],
'2022-09-21': ['2022-09-21 - Boston Red Sox @ Cincinnati Reds (Scheduled)'],
'2022-09-22': ['2022-09-22 - Boston Red Sox @ New York Yankees (Scheduled)'],
'2022-09-23': ['2022-09-23 - Boston Red Sox @ New York Yankees (Scheduled)'],
'2022-09-24': ['2022-09-24 - Boston Red Sox @ New York Yankees (Scheduled)'],
'2022-09-25': ['2022-09-25 - Boston Red Sox @ New York Yankees (Scheduled)'],
'2022-09-26': ['2022-09-26 - Baltimore Orioles @ Boston Red Sox (Scheduled)'],
'2022-09-27': ['2022-09-27 - Baltimore Orioles @ Boston Red Sox (Scheduled)'],
'2022-09-28': ['2022-09-28 - Baltimore Orioles @ Boston Red Sox (Scheduled)'],
'2022-09-29': ['2022-09-29 - Baltimore Orioles @ Boston Red Sox (Scheduled)'],
'2022-09-30': ['2022-09-30 - Boston Red Sox @ Toronto Blue Jays (Scheduled)'],
'2022-10-01': ['2022-10-01 - Boston Red Sox @ Toronto Blue Jays (Scheduled)'],
'2022-10-02': ['2022-10-02 - Boston Red Sox @ Toronto Blue Jays (Scheduled)'],
'2022-10-03': ['2022-10-03 - Tampa Bay Rays @ Boston Red Sox (Scheduled)'],
'2022-10-04': ['2022-10-04 - Tampa Bay Rays @ Boston Red Sox (Scheduled)'],
'2022-10-05': ['2022-10-05 - Tampa Bay Rays @ Boston Red Sox (Scheduled)'],
'2022-10-06': [''],
'2022-10-07': [''],
'2022-10-08': [''],
'2022-10-09': [''],
'2022-10-10': [''],
'2022-10-11': [''],
'2022-10-12': [''],
'2022-10-13': [''],
'2022-10-14': [''],
'2022-10-15': [''],
'2022-10-16': [''],
'2022-10-17': [''],
'2022-10-18': [''],
'2022-10-19': [''],
'2022-10-20': [''],
'2022-10-21': [''],
'2022-10-22': [''],
'2022-10-23': [''],
'2022-10-24': [''],
'2022-10-25': [''],
'2022-10-26': [''],
'2022-10-27': [''],
'2022-10-28': [''],
'2022-10-29': [''],
'2022-10-30': [''],
'2022-10-31': ['']}

stadiums = {'Arizona Diamondbacks': 'Chase Field',
'Atlanta Braves': 'Truist Park',
'Baltimore Orioles': 'Oriole Park at Camden Yards',
'Boston Red Sox': 'Fenway Park',
'Chicago White Sox': 'Guaranteed Rate Field',
'Chicago Cubs': 'Wrigley Field',
'Cincinnati Reds': 'Great American Ball Park',
'Cleveland Guardians': 'Progressive Field',
'Colorado Rockies': 'Coors Field',
'Detroit Tigers': 'Comerica Park',
'Houston Astros': 'Minute Maid Park',
'Kansas City Royals': 'Kauffman Stadium',
'Los Angeles Angels': 'Angel Stadium',
'Los Angeles Dodgers': 'Dodger Stadium',
'Miami Marlins': 'LoadDepot Park',
'Milwaukee Brewers': 'American Family Field',
'Minnesota Twins': 'Target Field',
'New York Yankees': 'Yankee Stadium',
'New York Mets': 'Citi Field',
'Oakland Athletics': 'RingCentral Coliseum',
'Philadelphia Phillies': 'Citizens Bank Park',
'Pittsburgh Pirates': 'PNC Park',
'San Diego Padres': 'Petco Park',
'San Francisco Giants': 'Oracle Park',
'Seattle Mariners': 'T-Mobile Park',
'St. Louis Cardinals': 'Busch Stadium',
'Tampa Bay Rays': 'Tropicana Field',
'Texas Rangers': 'Globe Life Field',
'Toronto Blue Jays': 'Rogers Centre',
'Washington Nationals': 'Nationals Park'}

def NextGame():
   '''Finds game info for Sox next game on an off day'''
    today = datetime.date.today()
    dateformat =  str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2)
    game = fullschedule[dateformat]
    while game == ['']:
        dateformat1 = str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day + 1).zfill(2)
        game = fullschedule[dateformat1]
        if game != ['']:
            break
    return game[0]

def GameDay():
   '''Tweets out game info on a gameday'''
    datetimeshit = datetime.datetime.now()
    str1 = str(datetimeshit).split(' ')
    time = str1[1]
    str2 = time.split(':')
    hour = int(str2[0])
    donequery = read_done(FILE_NAME3)
    if hour < 11:
        store_notdone(FILE_NAME3)
    elif hour >= 11 and donequery == 'Not Done':
        today = datetime.date.today()
        dateformat =  str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2)
        summary = fullschedule[dateformat][0]
        if summary == '':
            # nextgame = NextGame()
            # gamedate = nextgame.split('-')
            # month = gamedate[1]
            # day = gamedate[2]
            # year = gamedate[0]
            # fulldate = month +"/"+day+"/"+year
            # summary = nextgame
            # summary1 = summary.split(" @ ")
            # summary2 = summary1[1].replace(' (Scheduled)', '')
            # summary3 = summary1[0].split(' - ')
            # summary1[1] = summary2
            # summary1[0] = summary3[1]
            # if summary1[0] == "Boston Red Sox":
            #     opponent = summary1[1] #AWAY GAME
            #     stadium = stadiums[opponent]
            # else:
            #     opponent = summary1[0] #HOME GAME
            #     stadium = "Fenway Park"
            # api.update_status("The Sox are off today.../n/nDon't worry! We'll be listening to The Standells in no time!/n/nTheir next game is on " + fulldate + " against the " + opponent + " at " + stadium + "./n/n#RedSox #DirtyWater")
            # print("Game Day Tweet Posted: Off Day")
            store_done(FILE_NAME3)
        else:
            summary1 = summary.split(" @ ")
            summary2 = summary1[1].replace(' (Scheduled)', '')
            summary3 = summary1[0].split(' - ')
            summary1[1] = summary2
            summary1[0] = summary3[1]
            if summary1[0] == "Boston Red Sox":
                opponent = summary1[1] #AWAY GAME
                stadium = stadiums[opponent]
                store_series_away(FILE_NAME4, opponent)
                series = read_series(FILE_NAME4)
                if series.count('A' + opponent) == 1:
                    api.update_status("It's a great day for a ballgame.\n\nNew series, and the Red Sox are on the road as they take on the " + opponent + " at " + stadium + " in the opener.\n\n#RedSox #DirtyWater")
                elif series.count('A' + opponent) == 2:
                    api.update_status("It's a great day for a ballgame.\n\nThe series rolls on, and the Red Sox are locked and loaded for game 2 at " + stadium + " against the " + opponent + ".\n\n#RedSox #DirtyWater")
                elif series.count('A' + opponent) == 3:
                    api.update_status("It's a great day for a ballgame.\n\nGame 3 is coming up, as the Red Sox are back at " + stadium + " playing the " + opponent + ".\n\n#RedSox #DirtyWater")
                elif series.count('A' + opponent) == 4:
                    api.update_status("It's a great day for a ballgame.\n\nBoston Red Sox. " + opponent + " Game 4 at " + stadium + ".\n\n#RedSox #DirtyWater")
                print("Game Day Tweet Posted: Away Game")
            else:
                opponent = summary1[0] #HOME GAME
                stadium = "Fenway Park"
                store_series_home(FILE_NAME4, opponent)
                series = read_series(FILE_NAME4)
                if series.count('H' + opponent) == 1:
                    api.update_status("It's a great day for a ballgame.\n\nAlways a good day for a fresh start at home. The Red Sox open their series against the " + opponent + " in America's Most Beloved Ball Park, " + stadium + ".\n\n#RedSox #DirtyWater")
                elif series.count('H' + opponent) == 2:
                    api.update_status("It's a great day for a ballgame.\n\nThe series rolls on, and the Red Sox are locked and loaded for game 2 at " + stadium + " against the " + opponent + ".\n\n#RedSox #DirtyWater")
                elif series.count('H' + opponent) == 3:
                    api.update_status("It's a great day for a ballgame.\n\nGame 3 is coming up against the " + opponent + " as the Red Sox continue their homestand at " + stadium + ".\n\n#RedSox #DirtyWater")
                elif series.count('H' + opponent) == 4:
                    api.update_status("It's a great day for a ballgame.\n\nBoston Red Sox. " + opponent + " Game 4 at " + stadium + ".\n\n#RedSox #DirtyWater")
                print("Game Day Tweet Posted: Home Game")
            store_done(FILE_NAME3)

def DirtyWater():
   '''Tweets when the Sox win or lose'''
   tweets = api.home_timeline(since_id = read_last_seen(FILE_NAME))
   for tweet in reversed(tweets):
      if 'FINAL' in tweet.text:
         if '#DirtyWater' in tweet.text:
            print(str(tweet.id) + ' - ' + tweet.text)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            Last10 = read_last10(FILE_NAME5)
            list = [char for char in Last10]
            list.append(list.pop(0))
            latest = 'W'
            list[len(list)-1] = latest
            newLast10 = ''.join(list)
            store_last10(FILE_NAME5, newLast10)
            emojis = ['\U0001F525' if i == 'W' else '\U0000274C' for i in list]
            fortweet = ''.join(emojis)
            wintweet = api.update_status("YOUR 2022 RED SOX HAVE NOTCHED WIN #" + str(total()) + "\n\nYOU ALREADY KNOW WHAT TIME IT IS\n\n#RedSox #DirtyWater\n\nhttps://open.spotify.com/track/3NINDFPIYnyT26cWWRomOQ")
            reply = "Red Sox last 10 games after win #" + str(read_wins()) + "\n\n" + fortweet
            api.update_status(status = reply, in_reply_to_status_id = wintweet.id , auto_populate_reply_metadata=True)
            store_last_seen(FILE_NAME, tweet.id)
         elif '#DirtyWater' not in tweet.text:
            print(str(tweet.id) + ' - ' + tweet.text)
            api.create_favorite(tweet.id)
            losses = loss_total()
            games_to_500 = int(losses) - read_wins()
            Last10 = read_last10(FILE_NAME5)
            list = [char for char in Last10]
            list.append(list.pop(0))
            latest = 'L'
            list[len(list)-1] = latest
            newLast10 = ''.join(list)
            store_last10(FILE_NAME5, newLast10)
            emojis = ['\U0001F525' if i == 'W' else '\U0000274C' for i in list]
            fortweet = ''.join(emojis)
            store_last_seen(FILE_NAME, tweet.id)
            if games_to_500 > 0:
               losstweet = api.update_status("Tough loss for the boys. That makes " + str(losses) + " on the year.\n\nThe 2022 Red Sox are now " + str(games_to_500) + " games under 0.500.\n\n#RedSox")
            elif games_to_500 < 0:
               losstweet = api.update_status("Tough loss for the boys. That makes " + str(losses) + " on the year.\n\nThe 2022 Red Sox are now only " + str(abs(games_to_500)) + " games over 0.500.\n\n#RedSox")
            else:
               losstweet = api.update_status("Tough loss for the boys. That makes " + str(losses) + " on the year.\n\nThe 2022 Red Sox are now a 0.500 ballclub.\n\n#RedSox")
            reply = "Red Sox last 10 games after loss #" + str(read_losses()) + "\n\n" + fortweet
            api.update_status(status = reply, in_reply_to_status_id = losstweet.id , auto_populate_reply_metadata=True)

def HomeRun():
   '''Tweets when the Sox hit a home run'''
   tweets = api.home_timeline(since_id = read_last_seen(FILE_NAME))
   for tweet in reversed(tweets):
      if '- Boston' in tweet.text:
         print(str(tweet.id) + ' - ' + tweet.text)
         api.create_favorite(tweet.id)
         str1 = str(tweet.text).rpartition(')')[0]
         str2 = str(tweet.text).rpartition('(')[0] + "("
         number = str1.replace(str2,'')
         video = ' ' + str(tweet.text).rpartition(') ')[2]
         value = random.randint(1,33)
         if value == 1:
             api.update_status("Imagine not hitting a bomb today...\n\nCould not be " + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + ".\n\nThat's home run #" + number + " in 2022 for " + str(tweet.text).split()[0] + '.\n\n#RedSox #DirtyWater' + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 2:
             api.update_status("Launch it. Watch it. Flip it.\n\n" + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " just hit an absolute piss missile for home run #" + number + " in 2022." + "\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 3:
             api.update_status("Damnit... that was our only baseball...\n\n" + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " just launched the ball my mom got me for Christmas into orbit, notching home run #" + number + " in 2022." + "\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 4:
             api.update_status("DING DONG. BALL'S GONE. SEEYA LATER.\n\n" + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " ejecto seato'd that ball out of the yard, #" + number + " in 2022 for him." + "\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 5:
             api.update_status("I don't think I've ever seen a ball get punished more than that before.\n\n" + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " spanked that ball for its bad behavior, #" + number + " in 2022 for him." + "\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 6:
             api.update_status("GOODBYE BASEBALL. THAT ONE AIN'T COMIN BACK.\n\n" + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " sent that ball to its room without dinner, marking #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 7:
             api.update_status("That one's gonna be a souvenir!\n\n You'll probably see it on eBay after the game titled \"" + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " 2022 home run #" + number + "\"\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 8:
             api.update_status("I haven't seen something leave that quickly since my last Tinder date when she found out I had the Sox game on my phone under the table.\n\n" + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " got that ball out in a hurry, launching #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 9:
             api.update_status("Now you see it... now you don't. That ball disappeared.\n\n" + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " just did his best magic act, misdirecting #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 10:
             api.update_status("That ball just got absolutely obliterated. Not a single atom remains.\n\n" + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " left no trace of home run #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 11:
             api.update_status("We're still waiting for that one to come down. It defies all laws of physics.\n\n" + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " may have reached exit velocity on home run #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 12:
             api.update_status("And boom goes the dynamite.\n\n" + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " knocked that one out the yard, marking #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 13:
             api.update_status("I love it when a plan comes together. Seems like " + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " feels the name way.\n\n He just bopped out #" + number + " in 2022, exactly like I wanted him to :)\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 14:
             api.update_status("Honestly thinking about deploying The Standells just for that bomb.\n\n" + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " is making me quesiton the rules of Red Sox Twitter, en route to #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 15:
             api.update_status("I am a literal string of Python code and that home run was so disrespectful it even hurt MY feelings.\n\n" + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " has no regard for human life, launching #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 16:
             api.update_status("I mean this is just getting ridiculous. Why do people still pitch to him? When will they learn?\n\n" + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " has no choice but to continue launching nukes, reaching #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 17:
             api.update_status(str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " dip me lightly into a pool of barbecue sauce and call me a chicken nugget.\n\nThat home run had me feeling some type of way, as " + str(tweet.text).split()[0] + " smacks #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 18:
             api.update_status("Common " + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " W.\n\n That home run marks dub #" + number + " in 2022 for him. What else do you expect. It's habitual.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 19:
             api.update_status("I am genuinely about to legally change my name to " + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + "\n\nMaybe that way I'll be hitting home run #" + number + " in 2022 like him.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 20:
             api.update_status(str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " put me in a rocket ship and launch me to Neptune.\n\nThere's simply no other realitic reaction to " + str(tweet.text).split()[0] + " smacking #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 21:
             api.update_status(str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " introduce me to a nice woman from Serbia whom I can wed and have a wonderful life with.\n\nThat home run had me planning my future, as " + str(tweet.text).split()[0] + " smacks #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 22:
             api.update_status(str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " upload my consciousness to a neural network so I can live within this tweet forever.\n\nI am now a sentient tweet, as " + str(tweet.text).split()[0] + " smacks #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 23:
             api.update_status(str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " enroll me into a 4-year degree program in mashology so I can hit one like you.\n\nOne day I'll catch up to his totals, as " + str(tweet.text).split()[0] + " graduates #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 24:
             api.update_status(str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " teleport me onto an alien spaceship and take me on a tour of the known universe.\n\nThat home run had me feeling cosmic, as " + str(tweet.text).split()[0] + " smacks #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 25:
             api.update_status(str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + ".\n\nThat's it. That's the tweet.\n\n" + str(tweet.text).split()[0] + " bops #" + number + " in 2022 outta the yard.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 26:
             api.update_status(str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " put me into a juicer and blend me into a delicious cocktail in the Cask N' Flagon.\n\nThis is my destiny, as " + str(tweet.text).split()[0] + " juices #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 27:
             api.update_status(str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " pick me up at 7:00 pm in a rented tuxedo and take me to Junior Prom.\n\nTonight will be a night to remember, as " + str(tweet.text).split()[0] + " smacks #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 28:
             api.update_status(str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " throw me off the top of the Green Monster and watch me glide like a flying squirrel.\n\nThat home run gave me new abilities, as " + str(tweet.text).split()[0] + " smacks #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 29:
             api.update_status(str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " come into my room at midnight, tuck me in, and make sure that I'm sleeping soundly.\n\nThat home run felt like home, as " + str(tweet.text).split()[0] + " smacks #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 30:
             api.update_status(str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " cram my entire body into the little pouch the umpire keeps the extra baseballs in.\n\nThat home run was something else, as " + str(tweet.text).split()[0] + " smacks #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 31:
             api.update_status(str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " hit me with a comically oversized cartoon hammer.\n\nThat home run had me wacky, zany, and borderline silly, as " + str(tweet.text).split()[0] + " smacks #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 32:
             api.update_status(str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " dunk my head into an industrial sized cotton candy maker and give me a pink strawberry hairdo.\n\nThat home run had me feeling tasty, as " + str(tweet.text).split()[0] + " smacks #" + number + " in 2022.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)
         elif value == 33:
             api.update_status("I can confirm that " + str(tweet.text).split()[0] + ' ' + str(tweet.text).split()[1] + " has now been appointed to a dukeship in Botswana.\n\nI guess they saw his home run and were extremely impressed. I can't blame them. That's #" + number +  "in 2022 for him.\n\n#RedSox #DirtyWater" + video)
             store_last_seen(FILE_NAME, tweet.id)

def ShitTalk():
   '''Tweets when the Sox' opponent hits a home run'''
    tweets = api.home_timeline(since_id = read_last_seen(FILE_NAME))
    today = datetime.date.today()
    dateformat =  str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2)
    summary = fullschedule[dateformat][0]
    if summary == '':
        today = datetime.date.today() - datetime.timedelta(days = 1)
        dateformat =  str(today.year) + "-" + str(today.month).zfill(2) + "-" + str(today.day).zfill(2)
        summary = fullschedule[dateformat][0]
    summary1 = summary.split(" @ ")
    summary2 = summary1[1].replace(' (Scheduled)', '')
    summary3 = summary1[0].split(' - ')
    summary1[1] = summary2
    summary1[0] = summary3[1]
    if summary1[0] == "Boston Red Sox":
        opponent = summary1[1] #AWAY GAME
    else:
        opponent = summary1[0] #HOME GAME
    for tweet in reversed(tweets):
        if "- " + opponent in tweet.text:
            print(str(tweet.id) + ' - ' + tweet.text)
            print(today)
            video = ' ' + str(tweet.text).rpartition(') ')[2]
            value = random.randint(1,13)
            print("~~~~~~~~~~~~~~~~~~~~~~\nDeploying some fuego shit talk. Fuck these guys.\n~~~~~~~~~~~~~~~~~~~~~~")
            if value == 1:
                api.update_status(status = "We do not care." + video)
            if value == 2:
                api.update_status(status = "\U0001F971" + video)
            if value == 3:
                api.update_status(status = "Not even impressed tbh." + video)
            if value == 4:
                api.update_status(status = "We literally let him have that one because we felt bad. Sources confirm." + video)
            if value == 5:
                api.update_status(status = "I could've hit that one farther if we're being honest." + video)
            if value == 6:
                api.update_status(status = "Wow! What a swing! \U0001F610" + video)
            if value == 7:
                api.update_status(status = "Could be worse." + video)
            if value == 8:
                api.update_status(status = "Wall scraper." + video)
            if value == 9:
                api.update_status(status = "Literally should've been a ground rule double. We all saw it." + video)
            if value == 10:
                api.update_status(status = "Actually strategically worse for the team to hit a home run there. Thiis guys a bozo." + video)
            if value == 11:
                api.update_status(status = "Never seen a less impressive home run swing in my life." + video)
            if value == 12:
                api.update_status(status = "All part of the plan. Not concerned in the slightest." + video)
            if value == 13:
                api.update_status(status = "Genuinely who cares." + video)
            store_last_seen(FILE_NAME, tweet.id)

def Starting():
   '''Tweets out the Red Sox starting line-up on gameday'''
    tweets = api.home_timeline(since_id = read_last_seen(FILE_NAME))
    for tweet in reversed(tweets):
        if "BOS Lineup" in tweet.text:
            if "New BOS Lineup" in tweet.text:
                print(str(tweet.id) + ' - ' + tweet.text)
                store_last_seen(FILE_NAME, tweet.id)
                date = datetime.date.today()
                day = str(date.day)
                mo = str(date.month)
                year = str(date.year)
                lu = str(tweet.text).split(', ')
                leadoff = lu[0].replace("New BOS Lineup: ", '')
                lu[0] = leadoff
                lineup = '\n'.join(lu)
                api.update_status("\U0001F6A8LINEUP CHANGE\U0001F6A8\n\nNew Lineup for your " + year + " Boston Red Sox: " + mo + "/" + day + "/" + year + "\n\n" + lineup + "\n\n#RedSox #DirtyWater #MediasRojas")
            else:
                print(str(tweet.id) + ' - ' + tweet.text)
                store_last_seen(FILE_NAME, tweet.id)
                date = datetime.date.today()
                day = str(date.day)
                mo = str(date.month)
                year = str(date.year)
                lu = str(tweet.text).split(', ')
                leadoff = lu[0].replace("BOS Lineup: ", '')
                lu[0] = leadoff
                lineup = '\n'.join(lu)
                api.update_status("Starting Lineup for your " + year + " Boston Red Sox: " + mo + "/" + day + "/" + year + "\n\n" + lineup + "\n\n#RedSox #DirtyWater #MediasRojas")

def Draft():
   '''Tweets out each Sox draft pick'''
    def format(tweet):
        today = datetime.date.today()
        year = str(today.year)
        split = tweet.split(' ')
        words = len(split)
        lastname = split[words-3].replace('.', '')
        firstname = split[words-4]
        position = split[words-5]
        round = split[0]
        overall = split[1].replace('(', '').replace('):', '')
        schoollist = split[4:words-5]
        school = ' '.join(schoollist)
        return year + " MLB Draft\nRound " + round + " (#" + overall + ' overall):\n\nBoston Red Sox select ' + position + ' ' + firstname + ' ' + lastname + ' out of ' + school + '.\n\n#MLBDraft #RedSox #DirtyWater'
    picks = api.user_timeline(user_id = 602004183, since_id = read_last_seen(FILE_NAME))
    for pick in reversed(picks):
        if "@RedSox" in pick.text:
            api.create_favorite(pick.id)
            status = format(str(pick.text))
            api.update_status(status)
            store_last_seen(FILE_NAME, pick.id)

while True:
   '''Runs each command indefinitely'''
   GameDay()
   DirtyWater()
   HomeRun()
   ShitTalk()
   Starting()
   #Draft()
   time.sleep(60)
