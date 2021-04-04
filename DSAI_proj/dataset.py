# AUTOGENERATED! DO NOT EDIT! File to edit: 03_dataset.ipynb (unless otherwise specified).

__all__ = ['MovieDataset', 'Tokenize', 'RandomResizeCrop', 'ToTensor', 'NormalizeStandardize', 'Compose']

# Internal Cell
from torch.utils.data import Dataset
from torchvision import transforms
from transformers import DistilBertTokenizer
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import pandas as pd
import os
import torch

# Cell

class MovieDataset(Dataset):

    def __init__(self,
                 poster_img_dir: str,
                 backdrop_img_dir: str,
                 ds_type: str,
                 transforms: list):
        super(MovieDataset, self).__init__()
        self.ds_type = ds_type
        self.poster_path, self.backdrop_path = poster_img_dir, backdrop_img_dir
        self.transforms = transforms
        assert self.ds_type in ['train', 'valid', 'test'], "Dataset type provided is invalid."
        self.df = pd.read_csv(f"{self.ds_type}.csv")
        print(f"{self.ds_type} dataset created!")

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx: int) -> dict:
        """
        Returns a dict of 5 items:
        Poster Image, BackDrop Image, MetaData, Title+overview, label
        """
        poster_img_path = os.path.join(self.poster_path, f"{self.df.iloc[idx]['id']}.jpg")
        backdrop_img_path = os.path.join(self.backdrop_path, f"{self.df.iloc[idx]['id']}.jpg")

        poster_img_array = Image.open(poster_img_path).convert('RGB')
        backdrop_img_array = Image.open(backdrop_img_path).convert('RGB')
        text_inputs = f"{self.df.iloc[idx]['title']}[SEP]{self.df.iloc[idx]['overview']}"
        label = self.df.iloc[idx]['tagline']
        meta = self.df.iloc[0].drop(labels=['overview', 'title', 'tagline', 'id']).to_numpy(dtype=np.float32)

        sample = {"poster_img" : poster_img_array,
                  "backdrop_img" : backdrop_img_array,
                  "text_inputs" : text_inputs,
                  "meta" : meta,
                  "labels" : label}

        sample = self.transforms(sample)
        return sample

# Cell

# Tokenize concatenates the title and overview into a single example
class Tokenize(object):

    def __init__(self, tokenizer, max_length: int):
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __call__(self, x: dict) -> dict:
        x['labels'] = self.tokenizer(x['labels'], return_tensors='pt', max_length=self.max_length, padding='max_length')
        x['text_inputs'] = self.tokenizer(x['text_inputs'], return_tensors='pt', max_length=self.max_length, padding='max_length')
        return x

# Cell

# Resize the images to a fixed size for batching
class RandomResizeCrop(object):

    def __init__(self, width: int, height: int, method: int):
        self.width, self.height = width, height
        self.method = method

    def __call__(self, x: dict) -> dict:
        resize = transforms.RandomResizedCrop((self.height, self.width), interpolation=self.method)
        x['poster_img'] = np.array(resize(x['poster_img']))
        x['backdrop_img'] = np.array(resize(x['backdrop_img']))
        return x

# Cell

# ToTensor converts the numpy array to a torch Tensor of the same data type
class ToTensor(object):

    def __call__(self, x: dict) -> dict:
        x['poster_img'] = np.transpose(x['poster_img'], axes=(2, 0, 1))
        x['backdrop_img'] = np.transpose(x['backdrop_img'], axes=(2, 0, 1))
        x = {k : torch.Tensor(v) if isinstance(v, np.ndarray) else v for k, v in x.items()}
        return x

# Cell

# NormalizeStandardize scales images to between 0 and 1 before subtracting mean and dividing by std
class NormalizeStandardize(object):

    def __init__(self, mean: list, std: list):
        nc = len(mean)
        self.mean = torch.Tensor(mean).view(nc, 1, 1)
        self.std = torch.Tensor(std).view(nc, 1, 1)

    def __call__(self, x: dict) -> dict:
        poster_norm = torch.true_divide(x['poster_img'], 255.)
        backdrop_norm = torch.true_divide(x['backdrop_img'], 255.)
        x['poster_img'] = (poster_norm - self.mean) / self.std
        x['backdrop_img'] = (backdrop_norm - self.mean) / self.std
        return x

# Cell

class Compose(object):

    def __init__(self, tfms: list):
        self.tfms = tfms

    def __call__(self, x: dict) -> dict:
        for tfm in self.tfms:
            x = tfm(x)
        return x