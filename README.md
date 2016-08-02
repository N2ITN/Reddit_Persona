# Reddit_Persona
Reddit Persona is a python module that extracts personality insights, sentiment &amp; interests from any redditor's posts &amp; comments. redditor text is collected via reddit's python API, PRAW, Inights and machine learning is powered by [Indico.io](https://indico.io), for which a free API key is required. The API key allows for 10,000 API calls per month. A fee of $0.006 each applies to additional calls.

#Setup
Register for an API key with Indico
When importing the module for the first time, you will be prompted to enter your key.
Key is then verified and saved to disk.


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
>>> governator reddit_persona.go("GovSchwarzenegger")
>>> print governator
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

```

I have no affiliation with Indico, I just think it's a cool service for out of the box machine learning. 
While it's possible to reproduce these results using Torch, Keras, TensorFlow, etc., I believe the next step in machine learning is accessible deployment, empowering any user with the magic of this new technology. 
