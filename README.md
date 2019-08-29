# RoofNet

This repository contains code for the RoofNet project that will be submitted to the AI for climate change NeurIPS workshop. 

# Installation

This codebase is setup as a python module. To install, first create a conda environment or virtual env. 
Then clone the roofnet directory and `cd` into it. Once you do that, you can install the `roofnet` package by running:

```
pip install -e . 
```

This will install roofnet locally on your system. The `-e` option means 
that local changes in roofnet will be registered by your system so that you can edits roofnet at your leisure.

Launch a python shell and run `import roofnet` now to make sure this is working. If you receive a module not found error, 
try adding `roofnet` to your path in `.bashrc` and then run `source ~/.bashrc`. The path in your `.bashrc` file 
should look something like this:

`export PYTHONPATH=/home/misha/downloads/roofnet:$PYTHONPATH`

### Other packages

You will also need to install the following packages:

```
pandas
numpy
matplotlib
torch
torchvision
pillow
seaborn
```

And maybe some others that are not on this list.

# Preprocessing and Loading Data

Before running any scripts, you will need to download the roof data first. Here are the two datasets:

* Small dataset ~200Mb https://drive.google.com/open?id=1JB5H2Q85OZJWAoR_3HGIurdndJFBiP3Q
* Large dataset ~11GB https://drive.google.com/file/d/1VhQtCYomwsBKsYAVKabelzjPjfD9EwX5/view?usp=sharing

I suggest that you use the small dataset while developing and the large dataset once you're ready to launch a full experiment.


The `Data Analysis` notebook in the `notebooks` directory shows you how to preprocess and load data. There are two main
processes here:

1. Loading the images from the folders and converting them to a numpy object (this also compresses and crops all of the images).
The final `npy` object should be much smaller than the original data file. E.g. the 200MB file was compressed to 1.3MB for me.

2. Creating a:
* torch dataset (`class ImageDataset`) - this is the torch dataset object that defines how to retrieve one data point 
* torch sampler (`class TripletBuildingSampler`) - this class randomly samples a triplet of images `img_ref,img_positive,img_negative`.
* torch loader (`class Loader`) - this loads data from the dataset using the sampler

# Algorithms

TODO!
