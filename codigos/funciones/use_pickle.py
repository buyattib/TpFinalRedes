import pickle

def save_pickle(path, file):
    with open(path, "wb") as f: 
        pickle.dump(file, f)

def open_pickle(path):
    with open(path, 'rb') as f:
        file = pickle.load(f)
    
    return file
