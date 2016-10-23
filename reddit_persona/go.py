from reddit_persona import insights
from reddit_persona import reddit_get
# import ibm_insights
from reddit_persona import io_helper



    

def go(USERNAME,refresh = 60*60*24):

    reddit_get.user_text(USERNAME,refresh)

    try:
        indicoio.config.api_key = indicoKey.key
        indicoio.sentiment("I love writing code!")
        
        
    except Exception as e:
        io_helper.read_raw(USERNAME)

    
    insights.execute(USERNAME,refresh)
    # ibm_insights.user(USERNAME)

    fpath = io_helper.out_path(USERNAME)
    with open(fpath, 'r') as f:
        response = ' '.join( [line + ' ' for line in f]) 
    
    print(str(response))#.encode('ascii')



# TODO Add subreddits or descriptions