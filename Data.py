"""  
 Name: Discord_Bot
 Date: 10/11/2019
 Description: JSON to python class to easily parse relevant data

 @Author Elias Afzalzada
 Copyright © Elias Afzalzada - All Rights Reserved
"""

class RedditData:
    def __init__(self, list):
        vars(self).update(list)

class DataExtractor:
    def __init__(self, RedditData):
        self.reddit_data = RedditData
        self.posts = list(RedditData.data.children)


    def getPosts(self):
        return list(self.posts)