# Build a simple demo of the STI Search

# Obtain an ubuntu server and ssh to it


#installing Miniconda

  wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh

  bash miniconda.sh -p miniconda

##Creating a new conda environment
  conda create --name Sample_ST_search pandas numpy

##Activating it
source activate Sample_ST_search

##Additional modules
  pip install elasticsearch_dsl

#start a python interactive session
  $ import nltk
  $ nltk.download('brown')
