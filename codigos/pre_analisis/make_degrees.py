import numpy as np

data_dir = "./data"
edges_list_dir = data_dir + "/edges_list"
full_net_props_dir = data_dir + "/full_net_properties"

edges = np.load(edges_list_dir + "/all_edges_byusers.npy")

users, degree_users = np.unique(edges[:, 0], return_counts=True)
movies, degree_movies = np.unique(edges[:, 1], return_counts=True)

np.save(full_net_props_dir + "/users.npy", users)
np.save(full_net_props_dir + "/movies.npy", movies)

np.save(full_net_props_dir + "/degree_users.npy", degree_users)
np.save(full_net_props_dir + "/degree_movies.npy", degree_movies)