import os

os.system("scrapy crawl TweetScraper -a query='" + + "since:2019-01-01 until:2019-02-02'")
os.system("python3 ExportingIsFUN.py")
