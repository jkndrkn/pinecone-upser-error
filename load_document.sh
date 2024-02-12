
#!/bin/bash

set -e

set -o allexport
source config.sh 
set +o allexport

python load_document.py 
