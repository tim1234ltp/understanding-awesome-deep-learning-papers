import os
from os.path import isfile, join
from typing import List
from gensim import corpora, models
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import pyLDAvis.gensim


def lemmatize_stemming(text):
    stemmer = SnowballStemmer("english")
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


def preprocess(text):
    result = []
    for token in simple_preprocess(text):
        if token not in STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result


def get_txt_list() -> List:
    text_list = []
    for txt in os.listdir("F:\\personal project\\ML\\raw text"):
        path = join("F:\\personal project\\ML\\raw text\\", txt)
        if isfile(path):
            text_list.append(path)
    return text_list


def concat_all_text(filenames: List):
    with open('papers.txt', 'w', encoding='utf-8', errors='ignore') as outfile:
        for fname in filenames:
            with open(fname, encoding='utf-8', errors='ignore') as infile:
                for line in infile:
                    outfile.write(line)


def get_processed_text() -> List:
    processed_text = []
    with open('papers.txt', 'r', encoding='utf-8', errors='ignore') as papers:
        for line in papers:
            processed_text.append(preprocess(line))
    return processed_text


if __name__ == "__main__":
    # concat_all_text(get_txt_list())

    processed_text = get_processed_text()
    dictionary = corpora.Dictionary(processed_text)
    dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)
    corpus = [dictionary.doc2bow(x) for x in processed_text]

    lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=3, update_every=1, chunksize=10000, passes=1)
    p = pyLDAvis.gensim.prepare(lda, corpus, dictionary, sort_topics=False)
    pyLDAvis.save_html(p, 'lda.html')

    # bring in Term Frequency - Inverse Document Frequency to see if it can help us
    tfidf_model = models.TfidfModel(corpus)
    corpus_tfidf = tfidf_model[corpus]
    lda_tfidf = models.ldamodel.LdaModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=3, update_every=1, chunksize=10000, passes=1)

    p_tfidf = pyLDAvis.gensim.prepare(lda_tfidf, corpus_tfidf, dictionary, sort_topics=False)
    pyLDAvis.save_html(p_tfidf, 'lda_tfidf.html')
