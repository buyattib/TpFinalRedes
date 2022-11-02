import numpy as np

def make_igraph_ids(edges):
    #A los nodos les damos el atributo name que va a ser el id original, distinto al id que usa igraph (es la enumeracion eso).
    users_igraph_names = np.unique(edges[:,0])
    movies_igraph_names = np.unique(edges[:,1])
    
    n_users = len(users_igraph_names)
    n_movies = len(movies_igraph_names)

    #Enumeracion desde 0 hasta el total.
    users_igraph_ids = np.arange(n_users)
    movies_igraph_ids = np.arange(n_users, n_users+n_movies)

    #Tipos para el grafo bipartito: los users son 0's y las movies son 1's.
    types = np.concatenate([np.full(shape=n_users, fill_value=0), np.full(shape=n_movies, fill_value=1)])

    #Mapeo entre el enumerado (id igraph) y los nombres (ids originales)
    users_id_name_map = {name: id for name, id in zip(users_igraph_names, users_igraph_ids)}
    movies_id_name_map = {name: id for name, id in zip(movies_igraph_names, movies_igraph_ids)}

    #Armo los arrays de edges pero con los ids de igraph
    edges_users_igraph = np.array([users_id_name_map[name] for name in edges[:,0]])
    edges_movies_igraph = np.array([movies_id_name_map[name] for name in edges[:,1]])

    #Ahora los users van de 0 a n_users y las movies van de n_users a n_users+n_movies
    edges_ids = np.array([edges_users_igraph, edges_movies_igraph]).T

    return edges_ids, types