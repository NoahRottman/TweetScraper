import textblob
import sys
from textblob import TextBlob
import os
import pandas as pd
import numpy as np


#path = os.getcwd()
#file_name = os.path.join(path, "tweet/data.csv")
#print(file_name)

os.chdir("Data/tweet")

colnames = ['number', 'ID', 'datetime', 'has_media', 'is_reply', 'is_retweet', 'medias', 'x', 'y', 'z', 'text', 'w', 's', 't']
data = pd.read_csv("data.csv", names=colnames)
text = data.text.tolist()
date = data.datetime.tolist()
text_and_date = np.column_stack((text, date))
score = []
subjectivity = []
avg = 0
cnt = 0
pos = 0
neg = 0
neutral = 0
for i in range(len(text)):
    polar = TextBlob(text[i]).sentiment.polarity
    score.append(polar)
    subject = TextBlob(text[i]).sentiment.subjectivity
    subjectivity.append(subject)
    avg += polar
    cnt += 1
    if polar > 0:
        pos += 1
    elif polar == 0:
        neutral+=1
    else:
        neg += 1
    #print(text[i], ": ", temp)

date_text_score = np.column_stack((date, text, score, subjectivity))
np.savetxt(sys.stdout, date_text_score, fmt='%s')
avge = avg/cnt
print("Average: ", avge)
print("Positive: ", pos)
print("neutral", neutral)
print("Negative: ", neg)

