import numpy as np

data_dir = "./data"
samples_list_dir = data_dir + "/samples"
edges_list_dir = data_dir + "/edges_list"

def take_sample(edges, sample_size, max_degree=1500):
    users, degree_users = np.unique(edges[:,0], return_counts=True)
    reduced_users_indexes = np.where(degree_users < max_degree)[0]
    reduced_users = users[reduced_users_indexes]
    sample_users = np.random.choice(reduced_users, size=sample_size, replace=False)
    sample_edges_indexes = np.concatenate([np.where(edges[:,0] == u)[0] for u in sample_users])
    sample_edges = edges[sample_edges_indexes]
    return sample_edges, reduced_users

edges_gt3 = np.load(edges_list_dir + "/gt3_byusers.npy")
edges_lt3 = np.load(edges_list_dir + "/lt3_byusers.npy")

sample_edges_gt3 = take_sample(edges_gt3, sample_size=5000)
sample_edges_lt3 = take_sample(edges_lt3, sample_size=5000)

np.save(samples_list_dir + "/gt3_edges_sample.npy", sample_edges_gt3)
np.save(samples_list_dir + "/lt3_edges_sample.npy", sample_edges_lt3)
