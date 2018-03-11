import csv

import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.cluster import adjusted_rand_score

N_CLUSTERS = 6

def create_word2vec_similarity():
    # Import in function because it's rather slow, and this function is at most called once
    from gensim.models import Word2Vec
    from gensim.models.keyedvectors import KeyedVectors
    # Load Google's pre-trained Word2Vec model
    model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

    # Headers
    with open('similarities/handmade.csv', 'r') as f:
        d_reader = csv.DictReader(f, delimiter=';')
        headers = d_reader.fieldnames
        headers.pop(0)

    n = len(headers)
    similarity_word2vec = np.zeros((n, n))
    # Create matrix
    for i in range(n):
        for j in range(n):
            print(headers[i], headers[j])
            similarity_word2vec[i, j] =  model.similarity(headers[i], headers[j])

    print(similarity_word2vec)
    np.savetxt('similarities/word2vec.csv', similarity_word2vec, delimiter=';')

def create_lsa_lda_similarity():
    # Import in function because it's rather slow, and this function is at most called once
    from scipy.spatial.distance import cosine
    from sklearn.datasets import fetch_20newsgroups
    from sklearn.decomposition import NMF, LatentDirichletAllocation
    from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

    # fetch data
    dataset = fetch_20newsgroups(shuffle=True, random_state=1, remove=('headers', 'footers', 'quotes'))
    documents = dataset.data
    num_features = 2000 # most frequent N words included

    # Headers
    with open('similarities/handmade.csv', 'r') as f:
        d_reader = csv.DictReader(f, delimiter=';')
        headers = d_reader.fieldnames
        headers.pop(0)

    # Non-negative Matrix Factorization (NMF) uses TF-IDF
    tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=num_features, stop_words='english')
    tfidf = tfidf_vectorizer.fit_transform(documents)
    tfidf_feature_names = tfidf_vectorizer.get_feature_names()

    # LDA uses raw term counts because it is a probabilistic graphical model
    tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=num_features, stop_words='english')
    tf = tf_vectorizer.fit_transform(documents)
    tf_feature_names = tf_vectorizer.get_feature_names()

    def create_similarity(model, feature_names, name):
        body_vectors = {}
        for body_part in headers:
            body_vectors[body_part] = []
        for topic_idx, topic in enumerate(model.components_):
            for i in topic.argsort():
                if feature_names[i] in headers:
                    body_vectors[feature_names[i]].append(topic[i])
        n = len(headers)
        similarity = np.zeros((n, n))
        # Create matrix
        for i in range(n):
            for j in range(n):
                if len(body_vectors[headers[i]]) == len(body_vectors[headers[j]]):
                    similarity[i, j] = cosine(body_vectors[headers[i]], body_vectors[headers[j]])
                else:
                    similarity[i, j] = 0 # NaN
        similarity = np.nan_to_num(similarity)
        np.savetxt('similarities/' + name + '.csv', similarity, delimiter=';')

    no_topics = 6
    # Run NMF
    nmf = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)
    # Run LDA
    lda = LatentDirichletAllocation(n_components=no_topics, max_iter=5, learning_method='online', learning_offset=50.,random_state=0).fit(tf)

    create_similarity(nmf, tfidf_feature_names, 'lsa')
    create_similarity(lda, tf_feature_names, 'lda')

def print_clusters(labels, name=''):
    # Label names
    with open('similarities/handmade.csv', 'r') as f:
        d_reader = csv.DictReader(f, delimiter=';')
        headers = d_reader.fieldnames
        headers.pop(0)

    results = []
    for i in range(len(headers)):
        results.append((headers[i], labels[i]))

    if name:
        print('Results for ' + name + ':')
    for i in range(N_CLUSTERS):
        cluster = ''
        for result in results:
            if result[1] == i:
                cluster += result[0] + ', '
        cluster = cluster [:-2]
        print('Cluster ' + str(i) + ': ' + cluster)


# Create similarity matrices (slow)
# create_word2vec_similarity()
# create_lsa_lda_similarity()

# Load similarity matrices
similarity_handmade = np.genfromtxt('similarities/handmade.csv', delimiter=';', skip_header=1)
similarity_handmade = np.delete(similarity_handmade, 0, axis=1) # Delete row headers
similarity_word2vec = np.genfromtxt('similarities/word2vec.csv', delimiter=';')
similarity_lsa = np.genfromtxt('similarities/lsa.csv', delimiter=';')
similarity_lda = np.genfromtxt('similarities/lda.csv', delimiter=';')

# Clustering
model_handmade = AgglomerativeClustering(n_clusters=N_CLUSTERS, connectivity=similarity_handmade)
labels_handmade = model_handmade.fit_predict(X=similarity_handmade)
print_clusters(labels_handmade, 'handmade')
model_word2vec = AgglomerativeClustering(n_clusters=N_CLUSTERS, connectivity=similarity_word2vec)
labels_word2vec = model_handmade.fit_predict(X=similarity_word2vec)
print_clusters(labels_word2vec, 'Word2Vec')
model_lsa = AgglomerativeClustering(n_clusters=N_CLUSTERS, connectivity=similarity_lsa)
labels_lsa = model_handmade.fit_predict(X=similarity_lsa)
print_clusters(labels_lsa, 'LSA')
model_lda = AgglomerativeClustering(n_clusters=N_CLUSTERS, connectivity=similarity_lda)
labels_lda = model_handmade.fit_predict(X=similarity_lda)
print_clusters(labels_lda, 'LDA')

# Adjusted Rand Score
rand_word2vec = adjusted_rand_score(labels_handmade, labels_word2vec)
print('Adjusted Rand Score for Word2Vec: ' + str(rand_word2vec))
rand_lsa = adjusted_rand_score(labels_handmade, labels_lsa)
print('Adjusted Rand Score for LSA: ' + str(rand_lsa))
rand_lda = adjusted_rand_score(labels_handmade, labels_lda)
print('Adjusted Rand Score for LDA: ' + str(rand_lda))