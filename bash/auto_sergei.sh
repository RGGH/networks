#!/bin/bash   
echo "Give a directory name to create:"    
read NEW_DIR    
ORIG_DIR=$(pwd)    
[[ -d $NEW_DIR ]] && echo $NEW_DIR already exists, aborting && exit    
mkdir  $NEW_DIR    
echo "new directory made ${pwd}"
cd $NEW_DIR
poetry new app
cd app 
poetry shell
code .
