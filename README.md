# Reddit_Persona
Reddit Persona is a python module that extracts personality insights, sentiment &amp; interests from a user account. Support for subreddit analysis not working due to `praw` update v3--> v5, fix incoming ).

Text is collected via reddit's python API, `praw`, and NLP is powered by the indico.io API.

## Setup

```command 
pip install reddit_persona
```

## Usage 



Shell
```command
python -m reddit_persona /u/GovSchwarzenegger
```


Python 
```python
import reddit_persona
governator = reddit_persona.go("/u/GovSchwarzenegger")
print(governator)
#Save to txt
with open('arnold.txt', 'w') as t800:
   t800.write(governator)
```

Requests, especially for subreddits, can take a while. This is due primarily to the reddit API.
To save on time, this module avoids recreating API calls, by caching recent results. If a call is rerun with a day, results will read from the cache.

In python mode, ```reddit_persona.go()``` accepts the optional parameter 'refresh' to customize data refresh time, in seconds.
For a one minute refresh on new queries:
```python
  reddit_persona.go(username, refresh = 60)
```


### Output

Analysis output is printed to stdout. The raw reddit text and the analysis text are saved in 'reddit_persona/usr/' as username.txt and username_raw.txt respectively


```
Username: GovSchwarzenegger

  Best guess for location:
        New York 84.6%

  Most likely personalilty styles:
        protagonist 11.43%
        campaigner 10.5%
        consul 9.43%

  Big 5 personality inventory matches:
        agreeableness 65.27%
        extraversion 58.4%
        openness 52.75%
        conscientiousness 46.41%

  Predominant emotions:
        sadness 46.53%
        anger 18.8%
        fear 15.34%

  Keywords:
        fantastic 25.45%
        guys 22.51%
        studio 21.57%
        Todd 19.25%
        ride 17.67%

  Probable political alignments:
        Green 40.25%
        Conservative 25.48%
        Liberal 18.22%
        Libertarian 16.05%

  Text tags:
        fitness 48.58%
        personal 41.43%
        startups_and_entrepreneurship 5.99%
        relationships 0.59%
        film 0.4%
        
  Karma by Sub:
        Fitness: 24744
        videos: 22509
        IAmA: 13212
        movies: 11113
        bodybuilding: 6258
        pics: 694
        politics: 672
        AskReddit: 640
        ArnoldSchwarzenegger: 486
```
### Note: Indico.io API key
I have opted to include my personal API key as default. It allows up 10k calls- first come first serve!
If it breaks or runs out, its free to get your own.

Overwite key:
```python
reddit_persona.new_key('your key')
```
The new key is then verified then saved to disk.


### Thoughts
I have no affiliation with Indico, I just like the idea of on demand machine learning APIs. 
It's possible for a motivated programmer to produce similar results using Torch, Keras, TensorFlow, etc., however I believe the next step in the unfurling of machine learning is broad access, putting the magic of machine intelligence into the hands of anyone who is interested. 
