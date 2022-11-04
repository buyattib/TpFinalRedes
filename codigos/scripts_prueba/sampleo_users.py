import numpy as np
from ..funciones.use_pickle import open_pickle

data_dir = "./data"
samples_list_dir = data_dir + "/edges_list/samples"
edges_list_dir = data_dir + "/edges_list/byuser"

#En la posicion i, el grado del usuario i.
degree_users = np.load(edges_list_dir + "/bipartite_degree_users.npy")
n_users = len(degree_users)

#En la posicion k, una lista con los indices de los usuarios de grado k.
users_by_degree = open_pickle(edges_list_dir + "/users_by_degree.data")

edges_ig = np.load(edges_list_dir + "/all_edges_igraph_ids.npy")

# #Lista de grados desde 0 a k_max y lista de cuantos usuarios de cada grado hay.
all_degrees, degree_counts = np.unique(degree_users, return_counts=True)
degree_prob_density = degree_counts/n_users

#Para cada grado, sampleo una proporcion de usuarios de ese grado tal que al final tenga 1000 usuarios.
sample_size = 1120
sample_users = np.concatenate([np.random.choice(users_k, size=int(np.round(sample_size*d)), replace=False) for users_k, d in zip(users_by_degree, degree_prob_density)])

#Busco los indices de los usuarios sampleados en la lista de todos los enlaces.
sample_users_indexes = np.concatenate([np.where(edges_ig[:, 0] == user)[0] for user in sample_users])
sample_edges_ig = edges_ig[sample_users_indexes]

# np.save(samples_list_dir + "/degree_distribution_1kusers.npy", sample_edges_ig)

#Tiene 1k users, 9168k movies, 125.551 edges.
print(len(sample_edges_ig))
print(len(np.unique(sample_edges_ig[:,0])))
print(len(np.unique(sample_edges_ig[:,1])))
