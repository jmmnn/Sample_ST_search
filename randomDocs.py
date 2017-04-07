
# import nltk
# from nltk.corpus import wordnet as wn
import pandas as pd
import string
import random

titles = [
'Analysis: What Xbox One Scorpio means for the future of the console wars',
'Ancient Humans Didn not Turn to Cannibalism For the Calories',
'Twitter co-founder Ev Williams is selling 30 percent of his stock for personal reasons',
'Comcast to sell unlimited mobile plans that get throttled after 20GB',
]

content = [
'Enlarge / The exploded innards on what will surely be the most powerful game console in existence... until the next one. Eurogamer / Digital Foundry · reader comments 96.',
'Humans have been eating other humans since the beginning of time, but the motivations behind this macabre practice are complex and often unclear.',
'Twitter co-founder and current board member Ev Williams is going to offload some of his Twitter stock. Williams, who was once Twitters CEO and is the companys largest individual shareholder, said Thursday that he plans to sell a “minority of my TWTR',
'Comcast today announced pricing for its forthcoming smartphone data plans and said the Xfinity Mobile service will be available as an add-on for Comcast home Internet customers before the end of June.',
]


#this is the main function
def randomDoc():
    document = {
    'Country Origin' : random.sample(['Cuba' , 'France' , 'China' , 'Russia', 'Mexico', 'United Kingdom', 'USA'],2),
    'Entity Origin' : random.sample(['United Nations' , 'European Union' , 'Ministry of Foreign Affairs' , 'Permanent Mission to the UN'],2),
    'Domain Origin' : random.sample(['gov.fr' , 'gouv.fr' , '.gov' , '.go.uk' , 'gov.cn' , '.edu' , 'edu.mx'],2),
    'Title' : random.sample(titles,1),
    'Content' : random.sample(content,1),
    'url' : 'https://unite.un.org/',
    'Language' : random.sample(['English', 'French' , 'Spanish' , 'Russian' , 'Arabic' , 'Chinese'],2),
    'Resource Type' : random.sample(['Training', 'Publications', 'Software', 'Projects', 'Regulations' , 'Patents' , 'News', 'Database'],4),
    'Resource Format' : random.sample(['Video', 'Audio', 'Website', 'Book' , 'Dataset'],2),
    'SDG Goal' : random.sample(['Poverty', 'Hunger', 'Water', 'Climate Change', 'Cities' , 'Partnerships'],3),
    'Indexed Date' : '2015-31-12'
    }
    return document
# Tests
#print (randomDoc())
#print (random.sample(['Video', 'Audio', 'Website', 'Book' , 'Dataset'], 2))

## Not used for now.
# randSentences = nltk.corpus.brown.sents()   #Brings 50k sentences
