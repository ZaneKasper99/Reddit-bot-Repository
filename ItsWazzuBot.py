# bigwordbot

import praw
from PyDictionary import PyDictionary
import enchant

# create the objects from the imported modules

# reddit api login
reddit = praw.Reddit(client_id='4nKVnOqNzvDrsA',
                     client_secret='UppV2MulfanvTu0pKlLji0VVUm8',
                     username='ItsWazzuBot',
                     password='ItsWazzuBot',
                     user_agent='Its Wazzu Bot')
                    

# the subreddits you want your bot to live on
subreddit = reddit.subreddit('cfb', 'collegebasketball')

# phrase to activate the bot
keyphrase = 'Wazzou '
keyphrase2 = 'wazzou ' 

# look for phrase and reply appropriately
for comment in subreddit.stream.comments():
    if keyphrase in comment.body or keyphrase2 in comment.body:
        word = comment.body.replace(keyphrase, '')
        try:
        	reply = 'It\'s Wazzu'
            comment.reply(reply)
            print('posted')
        except:
        	print('error')
