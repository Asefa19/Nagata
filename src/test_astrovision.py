import kagglehub
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Download latest version
#path = kagglehub.dataset_download("emirhanai/planets-and-moons-dataset-ai-in-space")

path = "../../PlanetsAndMoons"

print("Path: ", path)

import os


path = "../../PlanetsAndMoons"
    
def get_directories_list(path):
    if path is None:
        path = os.getcwd()
    return [entry for entry in os.listdir(path) if os.path.isdir(os.path.join(path, entry))]

def list_objects():
    dir_list = get_directories_list("../../PlanetsAndMoons")
    return dir_list
    
print(list_objects())


# def get_directories_list(path):
#   """
#     Returns a list of directories in the given path.
#     If path is not provided, it defaults to the current working directory.
#   """
#   if path is None:
#       path = os.getcwd()
#   return [entry for entry in os.listdir(path) if os.path.isdir(os.path.join(path, entry))]

# # Example usage:
# directories = get_directories_list(path)
# print(directories)



# train_datagen = ImageDataGenerator(
#     featurewise_center=True,
#     samplewise_center=False,
#     featurewise_std_normalization=True,
#     samplewise_std_normalization=False,
#     zca_whitening=False,
#     zca_epsilon=1e-06,
#     rotation_range=0,
#     width_shift_range=0.0,
#     height_shift_range=0.0,
#     brightness_range=None,
#     shear_range=0.0,
#     zoom_range=0.0,
#     channel_shift_range=0.0,
#     fill_mode='nearest',
#     cval=0.0,
#     horizontal_flip=False,
#     vertical_flip=False,
#     rescale=1.0/255.0,
#     preprocessing_function=None,
#     data_format=None,
#     dtype=None,
#     validation_split=0.2)
# train_generator = train_datagen.flow_from_directory("../../PlanetsAndMoons", target_size=(256, 256),
#                                                     batch_size=128,
#                                                     class_mode='categorical',
#                                                     interpolation="lanczos",
#                                                     subset="training")