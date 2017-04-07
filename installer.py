#!/usr/bin/env python

# Setting up the environment

import subprocess
import sys
import os

#List commands to execute hereself.

#Server setup
UPDATE = "sudo apt-get update"
JAVA = "sudo apt-get install default-jre"
#UNZIP = "sudo apt-get install unzip"

#######  Apps and tools

GETELASTIC = "wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.3.0.tar.gz"
UNPAKELASTIC = "tar -xvf elasticsearch-5.3.0.tar.gz"
STARTELASTIC = "elasticsearch-5.3.0/bin/elasticsearch"
GETMINICONDA = "wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh"
INSTALLMINICONDA = "bash miniconda.sh -p miniconda"

#######  Steps specific to this project
#NEW_PYTHON_ENVIRONMENT = "conda create --name STI_search pandas numpy"
GET_DOCGENERATOR = "wget https://raw.githubusercontent.com/jmmnn/Sample_ST_search/master/randomDocs.py"
GET_CONFIG = "wget https://raw.githubusercontent.com/jmmnn/Sample_ST_search/master/config.py"
GET_INJECTOR_SCRIPT = "wget https://raw.githubusercontent.com/jmmnn/Sample_ST_search/master/sti_injector.py"

#FIRST list of commands in sequence ## Uncomment these for 1st install
cmds = [
    UPDATE,
    JAVA,
    # UNZIP,
    GETELASTIC,
    UNPAKELASTIC,
    STARTELASTIC,
    GETMINICONDA,
    INSTALLMINICONDA
    ]


#SECOND list of commands in sequence ## Comment Creata_collection after the first install
cmds2 = [
    #NEW_PYTHON_ENVIRONMENT,
    GET_DOCGENERATOR,
    GET_CONFIG,
    GET_INJECTOR_SCRIPT
    ]


#THIRD list of commands in sequence
cmds3 = [

    ]

dir = os.getcwd()
print (dir)

###### Iterates over the FIRST list of commands
count=0
for cmd in cmds:
    count+=1
    print ("Running Command Number %s" % count)
    subprocess.call(cmd, shell=True)


###### Iterates over the SECOND list of commands
count2=0
for cmd in cmds2:
    count2+=1
    print ("Running Command Number %s" % count2)
    subprocess.call(cmd, shell=True)

###### Iterates over the THIRD list of commands
count3=0
for cmd in cmds3:
    count3+=1
    print ("Running Command Number %s" % count3)
    subprocess.call(cmd, shell=True)
