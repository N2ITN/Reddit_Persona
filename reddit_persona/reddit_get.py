from os.path import join, dirname
from os import path, getcwd
from pprint import pprint
import collections
import praw
from reddit_persona import io_helper
import json


class reddit:

    def __init__(self, name, target):
        self.name = name
        self.target = target
        base_dir = path.join(getcwd(), path.dirname(__file__))
        creds = json.load(open(base_dir + '/' + 'reddit_creds.json'))
        self.user_agent = praw.Reddit(**creds)

    def get_user(self):
        redditor = praw.models.Redditor(self.user_agent, self.name)

        def comments():
            return [c.body.split('\n', 1)[0] for i, c in enumerate(redditor.comments.top(limit=100))]

        def submissions():
            return [
                '\n\t'.join([c.title, c.selftext])
                for i, c in enumerate(redditor.submissions.top(limit=100))
            ]

        return '\n\t'.join(comments() + submissions())

    '''
    TODO Update subreddit analyis for new API
    Outdated version below (should be quick fix, new api is streamlined)
    '''

    # def get_sub(self):
    #     sub_data = self.user_agent.get_subreddit(self.name)
    #     top_posts = sub_data.get_top_from_year()

    #     def sub_comments():
    #         for post in top_posts:
    #             yield post
    #             for comment in post.comments:
    #                 if type(comment) != praw.objects.MoreComments:
    #                     yield comment

    #     y = list(sub_comments())
    #     self.reddit_data = ' '.join([str(d) for d in y]).encode('utf-8')


def report(username, target):

    payload = reddit(username, target).get_user()

    assert len(payload) > 1, "Error - Data not retrieved"
    return str(payload)


def user_text(refresh=False, user=False, sub=False):

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
