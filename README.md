# DVC Project 
Lab assignment for the the Social Computing course. This project is aimed to create a reproducible DVC pipeline from the notebook 
[Clustering of smartphone sensor data for Human Activity Detection](https://github.com/herrfz/dataanalysis/blob/master/week4/clustering_example.ipynb) using the
[Samsung Dataset](https://data.world/uci/human-activity-recognition).

For each record in the dataset it is provided: 
- Triaxial acceleration from the accelerometer (total acceleration) and the estimated body acceleration.
- Triaxial Angular velocity from the gyroscope. 
- A 561-feature vector with time and frequency domain variables. 
- Its activity label. 
- An identifier of the subject who carried out the experiment.

## Setup
1. Download the repository and move to the folder

```
git clone https://github.com/luke2212/SocialComputing-Project
cd SocialComputing-Project
```
2. Create a virtual environment and install the dependancies as listed in `requirements.txt`. This project has been run on Ubuntu 20.04 with a conda environment

```
conda create -n venv
conda activate venv
```
  or if you are using Windows, you can create the virtual environment by using `virtualvenv`

```
virtualenv -p /usr/bin/python3.7 venv
source venv/bin/activate
```
 Then install the dependancies.
 
 `pip install -r src/requirements.txt`

## Run
To launch the tool, from the terminal execute `dvc pull` to download the dataset.
Then execute the following command to reproduce the pipeline:

`dvc repro --force`

## Examples
Run the command `dvc dag` to show the pipeline graph:

```
                      +--------------------------+                    
                      | data/samsungData.csv.dvc |                    
                      +--------------------------+                    
                    *****        *       ***    *****                 
                ****            *           *        ****             
             ***               *             **          ***          
+--------------+       +-------------+       +-----+       +--------+ 
| tBodyAccMean |       | tBodyAccMax |       | SVD |       | Kmeans | 
+--------------+       +-------------+       +-----+       +--------+ 
```

## Resource & Libraries
* [Pandas](https://pandas.pydata.org/docs/) - open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
* [Scipy](https://docs.scipy.org/doc/scipy/reference/) - open-source software for mathematics, science, and engineering.
* [Matplotlib](https://matplotlib.org/3.3.3/contents.html) - library for creating static, animated, and interactive visualizations in Python.

## Authors
* [Luca Musti](https://github.com/luke2212)
