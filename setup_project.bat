eval $(conda shell.bash hook)
conda env create -f environment.yml 
source activate fundpy-test-3-final-env
git init 
pre-commit install 


