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

# Load similarity matrices
similarity_handmade = np.genfromtxt('similarities/handmade.csv', delimiter=';', skip_header=1)
similarity_handmade = np.delete(similarity_handmade, 0, axis=1) # Delete row headers
similarity_word2vec = np.genfromtxt('similarities/word2vec.csv', delimiter=';')

# Clustering
model_handmade = AgglomerativeClustering(n_clusters=N_CLUSTERS, connectivity=similarity_handmade)
labels_handmade = model_handmade.fit_predict(X=similarity_handmade)
print_clusters(labels_handmade, 'handmade')
model_word2vec = AgglomerativeClustering(n_clusters=N_CLUSTERS, connectivity=similarity_word2vec)
labels_word2vec = model_handmade.fit_predict(X=similarity_word2vec)
print_clusters(labels_word2vec, 'Word2Vec')

# Adjusted Rand Score
rand_word2vec = adjusted_rand_score(labels_handmade, labels_word2vec)
print('Adjusted Rand Score for Word2Vec: ' + str(rand_word2vec))