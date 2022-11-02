import numpy as np
import pandas as pd

data_dir = "./data"
edges_list_dir = data_dir + "/edges_list"

complete_edges_path = edges_list_dir + "/all_edges_bymovies.npy"
complete_edges = np.load(complete_edges_path)

df = pd.DataFrame(complete_edges, columns=["movies", "users", "rating"])
df = df[["users", "movies", "rating"]]
df.sort_values("users", inplace=True)

edges_by_users = df.to_numpy()
np.save(edges_list_dir + "/byuser/all_edges.npy", edges_by_users)