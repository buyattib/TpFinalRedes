import numpy as np
import json
import matplotlib.pyplot as plt

data_dir = "./data"
full_net_props_dir = data_dir + "/full_net_properties"

with open(full_net_props_dir + "/bipartite_info.json", "r") as json_file:
    full_net_info = json.load(json_file)

degree_users = np.load(full_net_props_dir + "/degree_users.npy")
degree_movies = np.load(full_net_props_dir + "/degree_movies.npy")

bin_num = 100

####
bins_linear_users = np.linspace(0, full_net_info["max_degree_users"], bin_num)
bins_linear_users_center = bins_linear_users[:-1] + np.diff(bins_linear_users)/2

counts_linear_users, new_bins_linear_users = np.histogram(degree_users, bins_linear_users)
counts_linear_users_norm, new_bins_linear_users = np.histogram(degree_users, bins_linear_users, density=True)

####
bins_log_users = np.logspace(0, np.log10(full_net_info["max_degree_users"]), bin_num)
bins_log_users_center = bins_log_users[:-1] + np.diff(bins_log_users)/2

counts_log_users, new_bins_log_users = np.histogram(degree_users, bins_log_users)
counts_log_users_norm, new_bins_log_users = np.histogram(degree_users, bins_log_users, density=True)

####
bins_linear_movies = np.linspace(0, full_net_info["max_degree_movies"], bin_num)
bins_linear_movies_center = bins_linear_movies[:-1] + np.diff(bins_linear_movies)/2

counts_linear_movies, new_bins_linear_movies = np.histogram(degree_movies, bins_linear_movies)
counts_linear_movies_norm, new_bins_linear_movies = np.histogram(degree_movies, bins_linear_movies, density=True)

####
bins_log_movies = np.logspace(0, np.log10(full_net_info["max_degree_movies"]), bin_num)
bins_log_movies_center = bins_log_movies[:-1] + np.diff(bins_log_movies)/2

counts_log_movies, new_bins_log_movies = np.histogram(degree_movies, bins_log_movies)
counts_log_movies_norm, new_bins_log_movies = np.histogram(degree_movies, bins_log_movies, density=True)


fig, ax = plt.subplots(figsize=(20, 12))
ax.bar(
    bins_linear_users[:-1], 
    counts_linear_users_norm, 
    alpha=0.6, 
    align="edge", 
    edgecolor="k",
    label="", 
    width=np.diff(bins_linear_users)
);
ax.set_xscale("linear"); ax.set_yscale("linear");
ax.set_xlabel("Degree"); ax.set_ylabel("Counts")
plt.show();


# fig, ax = plt.subplots(figsize=(20, 12))
# ax.scatter(
#     bins_log_users_center, 
#     counts_log_users, 
#     alpha=0.6, 
#     edgecolor="k",
#     label="", 
# );
# ax.set_xscale("log"); ax.set_yscale("log");
# ax.set_xlabel("Degree"); ax.set_ylabel("Counts")
# ax.set_title("Users")
# plt.show();

# fig, ax = plt.subplots(figsize=(20, 12))
# ax.scatter(
#     bins_log_movies_center, 
#     counts_log_movies, 
#     alpha=0.6, 
#     edgecolor="k",
#     label="", 
# );
# ax.set_xscale("log"); ax.set_yscale("log");
# ax.set_xlabel("Degree"); ax.set_ylabel("Counts")
# ax.set_title("Movies")
# plt.show();

