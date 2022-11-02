import numpy as np
import os

data_dir = "./data"
raw_data_dir = data_dir + "/raw"
edges_list_dir = data_dir + "/edges_list"

data_files = [file_name for file_name in os.listdir(raw_data_dir) if "combined" in file_name]
save_names = [f"edges{i+1}.npy" for i in range(len(data_files))]

for index, data_file in enumerate(data_files):
    file_path = raw_data_dir + "/" + data_file
    
    with open(file_path, 'r') as file:
        movies = []
        users = []
        ratings = []

        i = 0
        for line in file:
            line = line.strip("\n")
            if ":" in line:
                movie_id = int(line.strip(":"))
                
            else:
                movies.append(movie_id)
                separated_line = line.split(",")
                users.append(int(separated_line[0]))
                ratings.append(float(separated_line[1]))
        
            if i == 0:
                print(f"first: {movie_id}")
            
            i += 1
        
        print(f"last: {movie_id}")
            
        edges = np.array([movies, users, ratings]).T
        np.save(edges_list_dir + "/" + save_names[index], edges)
        del edges
        del movies
        del users
        del ratings
