# CE1115 DSAI Project 
> Data Science Project to build a movie tagline predictor. 


## Project motivation and utility

Ever found yourself staring at a certain movie tagline and wondering what on earth the directors were thinking about when they came up with it? Yes, we too. On the other hand, we've also often been on the other end of the spectrum, struggling to come up with creative titles for our projects or succinct one-liners to encapsulate our business pitches. Enter our movie tagline predictor, a model we have built which we hope will provide some enlightenment to the many lost souls described above. We believe that this model can be transferrable to other salient applications, such as the web-link summarization we often see accompanying our everyday Google searches. 

## Installation

### Package install:
Run the following command to install the package from PyPI or conda.

`pip install DSAI_proj`

`conda install DSAI_proj`

### Editable Install:
1) Clone the repository locally and cd into it. 

2) Create a virtual/conda/pipenv environment first.

3) Depending on which type of environment you are using, run one of the following commands:

`pip install -e`

`conda develop .`

`pipenv install -e`

## Data Extraction & Cleaning

The functions in this package perform the following functions for data extraction via the TMDB API:
- Multi-threaded download of movie information via the extract_dataset_threaded function.
- Dataset splitting and segmenting via the create_splits function.
- Cleaning of the dataset has yet to be performed - TO-DO!!!

## Exploratory Data Analysis & Visualization

TO-DO!!!

## Modelling

TO-DO!!!

## Training and Evaluation

TO-DO!!!

## Results interpretation and recommendations

TO-DO!!!
