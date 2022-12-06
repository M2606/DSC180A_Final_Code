# DSC180A_Capstone Code Repo

This repo contains our code files for my Quarter 1 Capstone Project. The code files are placed in different directories for ease of utilization. The aim of this project was to identify cis-expression Quantitative Loci (cis-eQTL) on chromosome 22 of the human genome. The code files here generate p-values, correlations and standard errors for all genes (or the test gene) on chromosome 22 to help in identification and analysis of the cis-eQTLs.

The driver code is in the run.py file. It contains the code to load all the required data and generate the required statistics that our various analyses have been performed on. 

The code is intended to be run in a docker container with image id specified in the submission.json file. The command to run the file is also present in the submission.json file. 

When the script is run with the 'test' argument, the code is run on the test data which is a subset of the data that we have performed our analysis on. 

Running the run.py file, calls the etl.py and generate_stats.py code files present in the src directory that load the required data and generate the desired statistics.

The config directory contains the paths for all the data as well as a parameter that determines on which population the stats will be gathered for.

Successful execution of the run.py file should result in a csv file in the root directory with the desired stats.

