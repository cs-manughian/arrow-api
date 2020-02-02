import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *

import numpy as np
np.random.seed(2018)

import nltk
nltk.download('wordnet')

"""
 Tokenization — Split the text into sentences and the sentences into words. 
    Lowercase the words and remove punctuation.
"""
def tokenize(text):
    # TODO
    raise NotImplementedError

"""
 Lemmatized — words in third person are changed to first person 
    and verbs in past and future tenses are changed into present

 Stemming — words are reduced to their root form

 — Words that have fewer than 3 characters are removed
 — All stopwords are removed
"""
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result

def lemmatize_stemming(text):
    stemmer = SnowballStemmer('english') # Choose a language
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


"""
 Reference:
  Topic Modeling and LDA material
  https://towardsdatascience.com/topic-modeling-and-latent-dirichlet-allocation-in-python-9bf156893c24
"""