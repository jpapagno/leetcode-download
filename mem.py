import pickle
import model
import os

directory = 'downloads/pickles'

    # Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# File path
def save_object(model):

    file_path = os.path.join(directory, model.title + '.pickle')
    try:
        with open(file_path, "wb") as f:
            pickle.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)

def load_object(num_title):
    try:
        with open(num_title + '.pickle', "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)