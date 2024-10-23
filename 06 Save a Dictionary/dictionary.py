import pickle

def save_dict(dict_to_save, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)

def load_dict(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

def save_dict_no_lib(dict_to_save, file_path):
    with open(file_path, 'w') as file:
        for key, value in dict_to_save.items():
            file.write(f'{key}:{value}\n')

def load_dict_no_lib(file_path):
    recovered_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split(':')
            recovered_dict[int(key)] = value
    return recovered_dict

# commands used in solution video for reference
if __name__ == '__main__':
    test_dict = {1: 'a', 2: 'b', 3: 'c'}
    save_dict(test_dict, 'test_dict.pickle')
    recovered = load_dict('test_dict.pickle')
    print(recovered)  # {1: 'a', 2: 'b', 3: 'c'}
