[VIEW ELECTION PREDICTION DASHBOARD](https://vicolas-2023-nigerian-presidential-election-pre-election-7dvl76.streamlit.app/ "Election Dashboard")

[ANALYSE YOUR SENTIMENT DATA](https://vicolas-2023-nigerian-presidential-electi-pages2-analyse-cio3tl.streamlit.app/ "Analyse Your Sentiment Data")
# 2023-Nigerian-Presidential-Election-Prediction
This project is a sentiment analysis to weigh the negative positive and neutral emotions of Nigerians towards the election

**The Data**: The data was gathered from Twitter using snscrape. A tool that allows for extracting an unlimited amount of tweets and other information from Twitter based on specific criteria, such as keywords, hashtags, or user accounts.

**Data information**: A total of 20,000 tweets, 5,000 tweets for each specific hashtag; #Obidatti, #Tinubu, #Atiku and #kwankwaso was gathered for this project. 

The data reveals that 44.2% of people are on neutral grounds regarding the elections, while 42.6% are positive and 13.2% have negative opinions. Of the 42.6% positive sentiment score, Labour Party has the highest positive score compared to the other 3 parties. The Labour Party (LP) candidate appears to be the most talked about candidate on Twitter, with a significantly higher number of mentions than any other candidate. 

**NLP data preprocessing**

The VADER (Valence Aware Dictionary and sEntiment Reasoner) was used to simplify the NLP data preprocessing steps for this sentiment analysis.
Unlike other sentiment analysis tools that require a pre-labelled dataset for training, VADER uses a pre-built lexicon that contains thousands of words and phrases with known valence that classify the text data into positive, negative and neutral opinions. Using this model does not require any training data, as it can understand the sentiment of a text containing emoticons, slang, conjunctions, capital words, punctuations and much more, can process text data quickly and efficiently without the need for extensive preprocessing and works excellently on any form of text.
