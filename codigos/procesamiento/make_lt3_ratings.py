import numpy as np

data_dir = "./data"
edges_list_dir = data_dir + "/edges_list/byuser"

edges = np.load(edges_list_dir + "/all_edges.npy")
lt3 = edges[edges[:,2] < 3][:,:2]
np.save(edges_list_dir + "/lt3.npy", lt3)