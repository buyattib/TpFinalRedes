import numpy as np
import pandas as pd

data_dir = "./data"
edges_list_dir = data_dir + "/edges_list"

data_files = [f"edges{i}.npy" for i in range(4)]
dfs = []

for index, data_file in enumerate(data_files):
    file_path = edges_list_dir + "/" + data_file
    edges_i = np.load(file_path)
    df = pd.DataFrame(edges_i, columns=["movies", "users", "rating"])
    dfs.append(df)

df = pd.concat(dfs)
complete_edges = df.to_numpy()
np.save(edges_list_dir + "/all_edges_bymovies.npy", complete_edges)