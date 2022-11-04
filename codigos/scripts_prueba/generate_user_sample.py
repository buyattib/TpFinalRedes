import numpy as np
import json
from ..funciones.use_pickle import open_pickle

data_dir = "./data"
samples_list_dir = data_dir + "/samples"
full_net_props_dir = data_dir + "/full_net_properties"
edges_list_dir = data_dir + "/edges_list"

with open(full_net_props_dir + "/bipartite_info.json", "r") as json_file:
    full_net_info = json.load(json_file)

users = np.load(full_net_props_dir + "/users.npy")
degree_users = np.load(full_net_props_dir + "/degree_users.npy")
users_by_degree = open_pickle(full_net_props_dir + "/users_by_degree.data")

edges = np.load(edges_list_dir + "/all_edges_byusers.npy")
edges_gt3 = np.load(edges_list_dir + "/gt3_byusers.npy")
edges_lt3 = np.load(edges_list_dir + "/lt3_byusers.npy")

users_gt3 = np.unique(edges_gt3[:,0])
users_lt3 = np.unique(edges_lt3[:,0])

max_degree = 1500
reduced_users_indexes = np.where(degree_users < max_degree)[0]
reduced_users = users[reduced_users_indexes]

reduced_degree_users = degree_users[reduced_users_indexes]
n_users_reduced = len(reduced_users)

reduced_gt3_users = np.intersect1d(users_gt3, reduced_users)
reduced_lt3_users = np.intersect1d(users_lt3, reduced_users)

# n_users_reduced_gt3 = len(reduced_gt3_users)
# n_users_reduced_lt3 = len(reduced_lt3_users)

# degree_distribution = np.array([len(users_degree_k)/n_users_reduced for users_degree_k in users_by_degree[:max_degree]])
# gt3_degree_distribution = np.array([len(np.intersect1d(users_degree_k, reduced_gt3_users))/n_users_reduced_gt3 for users_degree_k in users_by_degree[:max_degree]])
# lt3_degree_distribution = np.array([len(np.intersect1d(users_degree_k, reduced_lt3_users))/n_users_reduced_lt3 for users_degree_k in users_by_degree[:max_degree]])

# pre_sample_size = 5618
# pre_sample_size_gt3 = 5620
# pre_sample_size_lt3 = 5652

# sample_users = np.concatenate([np.random.choice(users_k, size=int(pre_sample_size*d), replace=False) for users_k, d in zip(users_by_degree[:max_degree], degree_distribution)])
# sample_users_gt3 = np.concatenate([np.random.choice(np.intersect1d(users_k, reduced_gt3_users), size=int(pre_sample_size_gt3*d), replace=False) for users_k, d in zip(users_by_degree[:max_degree], gt3_degree_distribution)])
# sample_users_lt3 = np.concatenate([np.random.choice(np.intersect1d(users_k, reduced_lt3_users), size=int(pre_sample_size_lt3*d), replace=False) for users_k, d in zip(users_by_degree[:max_degree], lt3_degree_distribution)])

# sample_size = len(sample_users)
# sample_size_gt3 = len(sample_users_gt3)
# sample_size_lt3 = len(sample_users_lt3)

# print(sample_size)
# print(sample_size_gt3)
# print(sample_size_lt3)

# sample_edges_indexes = np.concatenate([np.where(edges[:,0] == u)[0] for u in sample_users])
# sample_edges = edges[sample_edges_indexes]

# sample_edges_indexes_gt3 = np.concatenate([np.where(edges_gt3[:,0] == u)[0] for u in sample_users_gt3])
# sample_edges_gt3 = edges_gt3[sample_edges_indexes_gt3]

# sample_edges_indexes_lt3 = np.concatenate([np.where(edges_lt3[:,0] == u)[0] for u in sample_users_lt3])
# sample_edges_lt3 = edges_lt3[sample_edges_indexes_lt3]

# sample_users_degrees = np.array([degree_users[np.where(users == u)[0]] for u in sample_users])
# sample_degrees, sample_degrees_distribution = np.unique(sample_users_degrees, return_counts=True)
# sample_degrees_distribution = sample_degrees_distribution/sample_size


# import matplotlib.pyplot as plt

# plt.plot(degree_distribution)
# plt.show()

# plt.plot(gt3_degree_distribution)
# plt.show()

# plt.plot(lt3_degree_distribution)
# plt.show()


# plt.plot(sample_degrees_distribution)
# plt.show()



