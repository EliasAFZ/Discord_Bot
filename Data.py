"""  
 Name: Discord_Bot
 Date: 10/11/2019
 Description: JSON to python class to easily parse relevant data

 @Author Elias Afzalzada
 Copyright © Elias Afzalzada - All Rights Reserved
"""

class RedditData:
    def __init__(self, listing):
        vars(self).update(listing)
