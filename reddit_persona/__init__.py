""" This module uses APIs from Reddit and Indico.io to provide insights into a Redditor's personality attributes.
Warning: This is just for fun, do not take results seriously. It is an experiment in combining social media data with machine learning APIs"""
__version__ = "1.1.1"

from reddit_persona import reddit_get, io_helper, insights, keycheck
from reddit_persona.go import go
from reddit_persona.keycheck import new_key, test_key, get_key
__all__ = ['reddit_get', 'io_helper', 'insights', 'go', 'keycheck']

mpdPath = __file__
