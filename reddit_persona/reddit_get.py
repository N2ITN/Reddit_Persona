import simplejson as json
from os.path import join, dirname
from os import path
from pprint import pprint
import collections
import praw
from reddit_persona import io_helper


class reddit:
	def __init__(self,user):
		self.user = user
		try:
			self.reddit_pull(user)
		except:
			#  "Could not pull data."
			exit()

	def reddit_pull(self, user):
		user_agent = 'whatever'
		r = praw.Reddit(user_agent=user_agent)
		me = r.get_redditor(self.user)
		s = me.get_submitted()
		s_flat = praw.helpers.flatten_tree(s)
		s_raw = ''
		for s in s_flat:
			s_raw += s.title + " " + s.selftext
		c = me.get_comments()
		c_flat = praw.helpers.flatten_tree(c)
		c_raw = ''
		for f in c_flat:
			c_raw += f.body + " "
		self.reddit_data = u''.join(c_raw + " " + s_raw).encode('utf-8')

def report(username):
	account = reddit(username)
	payload = account.reddit_data
	assert len(payload) > 1, "Error - Data not retrieved"
	return payload


def user_text(accountname,refresh):
	u = accountname + '_raw.txt'
	memoize = path.join(io_helper.usr_path, u)
	if io_helper.check_time(accountname,refresh):
		with  open(memoize,'w') as r_data:
			r_data.write(report(accountname))
		

