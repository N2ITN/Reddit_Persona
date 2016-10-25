import indicoio
import os.path as path
import os
import sys
import reddit_persona

meta_dict = {}


def execute(USERNAME, refresh):
    if not reddit_persona.io_helper.check_time(USERNAME, refresh):
        return
    r_data = reddit_persona.io_helper.read_raw(USERNAME)

    og = sys.stdout
    fpath = reddit_persona.io_helper.out_path(USERNAME)

    def analysis(raw='', limit=5, text='', percent=True):
        global meta_dict
        # print lines if input is a list of non-dicts
        # if input is list of dicts, merge dicts and resend to analysis
        if isinstance(raw, list):
            for item in raw:
                if not isinstance(item, dict):
                    print(item)
                else:
                    create_meta_dict(item)
            analysis(meta_dict, limit, text, percent)

        # if input is dict: print k, v pairs
        # optional args for return limit and description text
        if isinstance(raw, dict):
            print(text)
            ct = 0
            for v in sorted(raw, key=raw.get, reverse=True):
                ct += 1
                if ct > limit: break
                if isinstance(raw[v], float):
                    if percent: per = r'%'
                    else: per = ''
                    print("    " + v, str(round(raw[v] * 100, 2)) + per)
                else:
                    print(v, raw[v])
            print()

    def create_meta_dict(item):
        # merge list of dicts into master dict
        global meta_dict
        meta_dict[item['text']] = item['confidence']
        return meta_dict

    rClean = ''
    for i in range(len(r_data)):
        if r_data[i - 1] == '\\':
            rClean = rClean[:-1]
            if r_data[i] != "'":
                continue

        if r_data[i] == '*':
            rClean += ' '
        else:
            rClean += r_data[i]

    r_data = rClean
    del rClean
    indicoio.config.api_key = reddit_persona.keycheck.get_key()

    # Big 5
    big5 = {
        'text': "Big 5 personality inventory matches: ",
        "payload": indicoio.personality(r_data)
    }

    # Meyers briggs
    mbti = {
        'text': "Most likely personalilty styles: ",
        "payload": indicoio.personas(r_data),
        'ct': 3,
        'percent': True
    }

    # Political
    pol = {
        'text': "Probable political alignments: ",
        "payload": indicoio.political(
            r_data, version=1)
    }
    # Sentiment
    sen = {
        'text': "Positive/Negative Sentiment: ",
        "payload": indicoio.sentiment(r_data),
        'ct': 3
    }

    # Emotion 
    emo = {
        'text': "Predominant emotions:",
        "payload": indicoio.emotion(r_data),
        'ct': 5
    }

    # Keywords
    kw = {'text': "Keywords: ", "payload": indicoio.keywords(r_data), 'ct': 5}
    # Text tags
    tt = {'text': "Text tags: ", "payload": indicoio.text_tags(r_data), 'ct': 5}
    # Place
    pla = {
        'text': "Best guess for location: ",
        'payload': indicoio.places(
            r_data, version=2),
        'ct': 3,
        'percent': True
    }

    def Karma(USERNAME):
        import praw
        import collections
        user_agent = ("N2ITN")
        r = praw.Reddit(user_agent=user_agent)
        thing_limit = 100

        user = r.get_redditor(USERNAME)
        gen = user.get_submitted(limit=thing_limit)
        karma_by_subreddit = {}
        for thing in gen:
            subreddit = thing.subreddit.display_name
            karma_by_subreddit[subreddit] = (
                karma_by_subreddit.get(subreddit, 0) + thing.score)
            kList = []

        for w in sorted(
                karma_by_subreddit, key=karma_by_subreddit.get, reverse=True):
            kList.append(str(w) + ': ' + str(karma_by_subreddit[w]))
        kList.insert(0, 'Karma by Sub')

        print("\n\t".join(kList[:10]))

    def show(results):
        # Accepts bag of dicts, or single dict
        if not isinstance(results, dict):
            for X in results:
                show(X)
        else:
            if results == pla and pla['payload'] == []:
                print("Not enough information to infer place of origin")
                print()
            else:
                i = results
                analysis(
                    raw=i.get('payload', ''),
                    limit=i.get('ct', 5),
                    text=i.get('text', ''),
                    percent=i.get('percent', True))

    with open(fpath, 'w') as outtie:
        sys.stdout = outtie
        print("Username: " + USERNAME)
        print()
        show([pla, mbti, big5, emo, kw, pol, sen, tt])
        Karma(USERNAME)
        sys.stdout = og
    return
