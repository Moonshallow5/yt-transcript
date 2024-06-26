from youtube_transcript_api import YouTubeTranscriptApi
output=[]


def inzz():
    x=input("Pls enter the URL for the transcript :) ")
    zz=[]
    for i in range(len(x)):
        if(i>=32):
            zz.append(x[i])
    print(zz)
    san=''.join(zz)
    return san
    
    

def final(san):


    tx=YouTubeTranscriptApi.get_transcript(san,languages=['en'])
    for i in tx:
    
        outtxt=(i['text'])
        output.append(outtxt)
        
        with open("transcript.txt","a") as j:
            j.write(outtxt+"\n")
final(inzz())
        
      