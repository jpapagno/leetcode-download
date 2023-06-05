import pickle
import os


# Create the directory if it doesn't exist
# if not os.path.exists(directory):
#     os.makedirs(directory)

# File path
def save_object(model):
    directory = 'downloads/pickles'
    file_path = os.path.join(directory, model.title + '.pickle')
    try:
        with open(file_path, "wb") as f:
            pickle.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        raise ValueError("Error during pickling object (Possibly unsupported):", ex)

def load_object(title):
    # directory = 'downloads/pickles'
    # file_path = os.path.join(directory, title + '.pickle')
    try:
        with open(title + '.pickle', "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        raise ValueError("Error during unpickling object (Possibly unsupported):", ex)