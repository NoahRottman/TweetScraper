import os


import sys

            #for line in sys.stdin:
line = "horrible"
os.system("scrapy crawl TweetScraper -a query='" + line + " since:2019-01-01 until:2019-02-02'")
os.system("python3 ExportingIsFUN.py")
os.system("python3 sentiment.py")

