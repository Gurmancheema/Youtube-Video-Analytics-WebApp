#1. Importing Libraries & Connecting with Youtube API
#pip install --upgrade google-api-python-client
# !pip install pywebio
# !pip install pytube
from googleapiclient.discovery import build
from pywebio.input import *
from pywebio.output import *
from pytube import extract


API_KEY = "AIzaSyBKXDp6B3S_eqMvIbmY0o6hm59Akkh20KI"
youtube = build('youtube','v3', developerKey = API_KEY)


#2. Definig a method to Extract comments of video
result = []
def get_comments(videoId):
    try:
        videoComments = youtube.commentThreads().list(
          part ='snippet,replies',
          videoId = videoId,
          maxResults= 100
          ).execute()
        if(videoComments and videoComments['items']):
            for item in videoComments['items']:
                try:
                    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                    result.append(comment)
                except:
                    pass
        else:
            return None
        return result 
    except Exception as err:
        return None


#3. Defining a method to extract stats of the video
def stats(videoid):
    video_response_stats = youtube.videos().list(
                part = 'snippet, contentDetails, statistics',
               id= videoid).execute()

    for items in video_response_stats['items']:
        
#extract stats
        viewcount = items['statistics']['viewCount']
        likeCount = items['statistics']['likeCount']
        favoriteCount = items['statistics']['favoriteCount']
        commentCount = items['statistics']['commentCount']
        description = items['snippet']['description']
        title = items['snippet']['title']
        #dislikeCount= items['statistics']['dislikeCount']
    put_text("Stats of the Video:")
    put_text("Title:",title,"\n").show()
    put_text(" View Count:",viewcount).show()
    put_text(" Like Count:",likeCount).show()
    #print(" Favourite Count:",favoriteCount) #fav count will always be zero as mentioned in website
    put_text(" Comment Count:",commentCount).show()
    put_text(" Description:",description).show()

#4. Interactive code below
user_url = input("Enter the video URL in the textfield", type ='text')
video_id=extract.video_id(user_url)
get_comments(video_id)

len_of_comments=len(result)
put_text("*************YOUTUBE VIDEO DETAILS DISPLAY WEB APP***********************")
put_text("No.of comments: ",len_of_comments)
serial_no=0
for i in result:
    serial_no =serial_no  +1
    put_text(serial_no,":",i).show()

#Displaying the stats now
stats(video_id)


       



