import numpy as np
import igraph as ig
import json

data_dir = "./data"
edges_list_dir = data_dir + "/edges_list/byuser"
data_graphs_path = data_dir + "/graphs"

#Cargo todos los enlaces
edges = np.load(edges_list_dir + "/all_edges.npy")

n_users = np.unique(edges[:,0]).shape[0]
n_movies = np.unique(edges[:,1]).shape[0]
n_edges = edges.shape[0]
density = (n_users * n_movies) / n_edges

ratings, ratings_counts = np.unique(edges[:,2], return_counts=True)
n_gt3 = np.sum(ratings_counts[2:])
n_lt3 = np.sum(ratings_counts[:2])

degree_users = np.load(edges_list_dir + "bipartite_degree_users.npy")
degree_movies = np.load(edges_list_dir + "bipartite_degree_movies.npy")

avg_degree_users = np.mean(degree_users)
max_degree_users = np.max(degree_users)
min_degree_users = np.min(degree_users)

avg_degree_movies = np.mean(degree_movies)
max_degree_movies = np.max(degree_movies)
min_degree_movies = np.min(degree_movies)

full_net_info = {
    "n_users": n_users,
    "n_movies": n_movies,
    "n_edges": n_edges,
    "n_gt3": int(n_gt3),
    "n_lt3": int(n_lt3),
    "avg_degree_users": float(avg_degree_users),
    "max_degree_users": int(max_degree_users),
    "min_degree_users": int(min_degree_users),
    "avg_degree_movies": float(avg_degree_movies),
    "max_degree_movies": int(max_degree_movies),
    "min_degree_movies": int(min_degree_movies),
}

with open(data_dir + "/bipartite_info.json", "w") as json_file:
    json.dump(full_net_info, json_file)

