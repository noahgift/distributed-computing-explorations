#!/usr/bin/env python3

from multiprocessing import Pool
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import time

def do_kmeans(n_samples):
    """KMeans clustering on generated data"""

    X,_ = make_blobs(n_samples, centers=3, n_features=10,
                random_state=0)
    kmeans = KMeans(n_clusters=3)
    t0 = time.time()
    kmeans.fit(X)
    print(f"KMeans cluster fit in {time.time()-t0}")

def run_parallel():
    """Run Everything"""

    count = 25
    processes = 13
    t0 = time.time()
    with Pool(processes) as p:
        p.map(do_kmeans, [100000 for x in range(count)])
    print(f"Performed {count} KMeans in total time: {time.time()-t0} using processes total: {processes}")

run_parallel()