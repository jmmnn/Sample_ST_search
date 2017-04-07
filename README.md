# Build a simple demo of the STI Search

# Obtain an ubuntu server and ssh to it

#Get the installer script:
  wget https://github.com/jmmnn/Sample_ST_search/blob/master/installer.py

#Run it:
  python installer.py

##Activating the python environment
  source activate STI_search

##Additional modules
  pip install elasticsearch

##Trigger the generation of documents
  python sti_injector.py

##View your documents in a browser:
  http://localhost:9200/_search?pretty=true&q=*:*
  or
  curl 'http://localhost:9200/_search?pretty=true&q=*:*'


<!-- #installing Miniconda

  wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh

  bash miniconda.sh -p miniconda

##Creating a new conda environment
  conda create --name Sample_ST_search pandas numpy

##Activating it
source activate STI_search

##Additional modules
  pip install elasticsearch_dsl

#start a python interactive session
  $ import nltk
  $ nltk.download('brown') -->
