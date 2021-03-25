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

## Data Extraction

The main function in this package perform the following functions for data extraction via the TMDB API:
- Multi-threaded download of movie information via the extract_dataset_threaded function.

## Exploratory Data Analysis & Visualization

Now that we have our raw dataset to work with, we begin by looking at:
- The different types of data present.
- How they might be relevant to our task.
- Their respective distributions and whether there might be class imbalances.
- Missing data and other considerations to be had later during cleaning.

## Data Cleaning and Feature Engineering 

After the EDA step, we have generated insights from the data in terms of their distribution and relevance our overall task. The functions in this package perform the following functions to clean and feature engineer the raw data:
- Drop columns which are irrelevant 
- For columns/features with missing data, how to replace missing data.
- For columns/features with json objects, unpack the json objects into new columns.
- For categorical features, ensure that they are categoized accordingly.
- For continuous features, ensure that they are normalized and standardized.
- Separate out examples with and without taglines.
- Save the dataset into separate train, valid, test and tagless csv files.

## Modelling

TO-DO!!!

## Training and Evaluation

TO-DO!!!

## Results interpretation and recommendations

TO-DO!!!
