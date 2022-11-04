import numpy as np
from ..funciones.use_pickle import save_pickle

data_dir = "./data"
full_net_props_dir = data_dir + "/full_net_properties"

users = np.load(full_net_props_dir + "/users.npy")
degree_users = np.load(full_net_props_dir + "/degree_users.npy")
all_degrees = np.unique(degree_users)

#En la posicion k, una lista con los usuarios de grado k.
users_by_degree = [users[np.where(degree_users == k)[0]] for k in all_degrees]

save_pickle(full_net_props_dir + "/users_by_degree.data", users_by_degree)