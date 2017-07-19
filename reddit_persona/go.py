from reddit_persona import insights, io_helper, memberberry, reddit_get


def go(target, refresh=60 * 60 * 24):

    parse = target.split('/')
    USERNAME = parse[2]

    if parse[1] == 'u':
        target = 'user'
        reddit_get.user_text(user=USERNAME, refresh=refresh)
    elif parse[1] == 'r':
        target = 'sub'
        reddit_get.user_text(sub=USERNAME, refresh=refresh)

    try:
        indicoio.config.api_key = indicoKey.key
        indicoio.sentiment("I love writing code!")

    except Exception as e:
        io_helper.read_raw(USERNAME, target)

    insights.execute(USERNAME, target, refresh)

    print(memberberry.Berry.indicoResults)


# TODO Add subreddits or descriptions
