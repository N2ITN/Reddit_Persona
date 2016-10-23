# Reddit_Persona
Reddit Persona is a python module that extracts personality insights, sentiment &amp; interests from any redditor's posts &amp; comments. redditor text is collected via reddit's python API, PRAW, Inights and machine learning is powered by [Indico.io](https://indico.io), for which a free API key is required. The API key allows for 10,000 API calls per month. A fee of $0.006 each applies to additional calls.

#Setup
Compatible with Python 2 and 3
```python
>>>pip install reddit_persona
```



## Indico.io API key
When importing the module for the first time, you will be prompted to enter a new key, if a valid key does not exist.
The new key is then verified then saved to disk.
I have opted to include my personal API key as default. It allows up 10k calls- first come first serve!
If it breaks or runs out, its free to get your own.


```python
>>> import reddit_persona
>>> Indico API key missing/invalid
>>> 'Without this key, reddit_persona.go(USERNAME) will collect and return Redditor text only'
>>> 'To enter your indico API key, use reddit_persona.new_key( )'
>>> reddit_persona.new_key('  your key  ')
>>> 'Key validated and saved to module files. You will not need to enter it again.'
```

# Usage 
Input:

```python
>>> import reddit_persona
>>> governator = reddit_persona.go("GovSchwarzenegger")
```
View in terminal:
```python
>>> print(governator)
```
Save to txt:
```python
>>> with open('arnold.txt', 'w') as t800:
...   t800.write(governator)
```

Note: 
reddit_persona.go() can accept optional parameter 'refresh', default 1 day:
If API calls for redditor data & text analysis were created before t seconds ago, reuse existing data.

Example for making new API calls after one minute:
```python
  reddit_persona.go(username, refresh = 60)
```




Output:

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

I have no affiliation with Indico, I just like the idea of on demand machine learning APIs. 
It's possible for a motivated programmer to produce similar results using Torch, Keras, TensorFlow, etc., however I believe the next step in the unfurling of machine learning is broad access, putting the magic of machine intelligence into the hands of anyone who is interested. 
