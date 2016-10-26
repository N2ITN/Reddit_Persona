import simplejson as json
from os.path import join, dirname
from os import path
from pprint import pprint
import collections
import praw
from reddit_persona import io_helper


class reddit:

    def __init__(self, name, target):

        # try:
        self.name = name
        self.target = target
        self.reddit_pull(name)

        # except Exception as e:
        #     print (e)
        #     print('No result for', self.target)
        #     exit()

    def reddit_pull(self, name):
        ua = 'N2ITN'
        self.user_agent = praw.Reddit(user_agent=ua)
        if self.target == 'user':
            self.get_user()
        elif self.target == 'sub':
            self.get_sub()

    def get_user(self):

        user_data = self.user_agent.get_redditor(self.name)
        submitted = user_data.get_submitted()
        submitted_flat = praw.helpers.flatten_tree(submitted)
        submitted_text = ' '.join(
            [' '.join([s.title, s.selftext]) for s in submitted_flat])

        comments = user_data.get_comments()
        comments_flat = praw.helpers.flatten_tree(comments)
        comments_text = ' '.join([c.body for c in comments_flat])

        self.reddit_data = ' '.join(
            [comments_text, submitted_text]).encode('utf-8')

    def get_sub(self):
        sub_data = self.user_agent.get_subreddit(self.name)
        top_posts = sub_data.get_top_from_year()

        def sub_comments():
            for post in top_posts:
                yield post
                for comment in post.comments:
                    if type(comment) != praw.objects.MoreComments:
                        yield comment

        y = list(sub_comments())
        self.reddit_data = ' '.join([str(d) for d in y]).encode('utf-8')


def report(username, target):
    account = reddit(username, target)
    payload = account.reddit_data
    assert len(payload) > 1, "Error - Data not retrieved"
    return str(payload)


def user_text(refresh, user=False, sub=False):

    if user:
        accountname = user
        target = 'user'
    elif sub:
        accountname = sub
        target = 'sub'
    u = accountname + '_raw.txt'

    memoize = path.join(io_helper.usr_path, target, u)

    with open(memoize, 'w') as r_data:
        nameOut = report(accountname, target)
        r_data.write(nameOut)
