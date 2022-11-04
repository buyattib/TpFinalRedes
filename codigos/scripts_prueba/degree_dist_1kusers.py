import numpy as np
import igraph as ig

from ..funciones.funcionesGenerales import make_igraph_ids

data_dir = "./data"
samples_list_dir = data_dir + "/edges_list/samples"

edges = np.load(samples_list_dir + "/degree_distribution_1kusers.npy")

edges_ig, types = make_igraph_ids(edges)

g_bip = ig.Graph().Bipartite(types, [])
g_bip.add_edges(edges_ig)

n_users, n_movies = np.unique(types, return_counts=True)[1]

degree_users = g_bip.degree(np.arange(n_users))
degree_movies = g_bip.degree(np.arange(n_users, n_users+n_movies))

avg_degree_users = np.mean(degree_users)
avg_degree_movies = np.mean(degree_movies)

#Grado medio de usuarios 125 y de peliculas 13.
print(avg_degree_users)
print(avg_degree_movies)