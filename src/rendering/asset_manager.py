import os
import pygame
import random

class AssetManager:
    def __init__(self):
        self.file_dictionary = {}
        self.cloud_dictionary = {}
        self.fillDict("assets", self.file_dictionary)
        self.fillDict("assets/Clouds", self.cloud_dictionary)

    def file_names(self, path):
        return os.listdir(path)

    def fillDict(self, path, dict):
        file_names = self.file_names(path)
        for file in file_names:
            if file.endswith(".png"):
                full_path = os.path.join(path, file)
                name  = os.path.splitext(file)[0]
                dict[name] = pygame.image.load(full_path).convert_alpha()

    def get_image(self, name):
        return self.file_dictionary[name]

    def get_cloud(self):
        return random.choice(list(self.cloud_dictionary.values()))