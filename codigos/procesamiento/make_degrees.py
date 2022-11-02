import numpy as np
import igraph as ig
import json

from funciones.funcionesGenerales import make_igraph_ids

data_dir = "./data"
edges_list_dir = data_dir + "/edges_list/byuser"
data_graphs_path = data_dir + "/graphs"

edges = np.load(edges_list_dir + "/all_edges.npy")
edges_ig, types = make_igraph_ids(edges)
g_bip = ig.Graph().Bipartite(types, [])
g_bip.add_edges(edges_ig)

n_users, n_movies = np.unique(types, return_counts=True)[1]

degree_users = g_bip.degree(np.arange(n_users))
degree_movies = g_bip.degree(np.arange(n_users, n_users+n_movies))

np.save(edges_list_dir + "/bipartite_degree_users.npy", degree_users)
np.save(edges_list_dir + "/bipartite_degree_movies.npy", degree_movies)