# Template of Analysis Framework [TAF]

Developpement of a pythonic Template of Analysis Framework

# Installation

## Create a virtual environment

### Option 1 -- using `conda`

To create the virtual environment configured in the file `TAF_env.yml`, one simply needs
to run:
```
conda en create -f TAF_env.yml
```
*Note: to update an existing virtual environment (if one wished to modify `TAF_env.yml`),
run*
```
conda env update --name TAF_env --file TAF_env.yml --prune
```
### Option 2 -- using python `venv`
To create a virtual environment named `TAF_env` with version 3.12 (this is an example) of
Python, run:
```
python3.12 -m venv TAF_env
```
*Careful: you have to choose the right location on your computer, because the files
associated to this virtual environment will be created at this location.*
Once the environment is created, you can enter it via:
```
source path/TAF_env/bin/activate
```
Once inside this environment, **and only once inside (!)**, run:
```
pip install --upgrade pip
python3 -m pip install -r requirements_py_venv_TAF.txt
```
to install the requirements defined in the file `requirements_py_venv_TAF.txt`

## Create an environment variable for this repository
In your `~/.bashrc` (in Unix) or `~/.bash_profile` (in MacOS) add
```
export TAF="<put the path to your local copy of this repo>"
```
*Note: to get the local path to your repository, enter `pwd` in your terminal while being
in your repo.*
*Note: the `export` keyword assumes that the shell is in BASH, it can vary if it is not (
e.g. zsh, tcsh, ...).*
*Careful: do not forget to either open a new terminal or to `source` your `bash*` file to
make this modification active.*
From now on, the location of this repo in the computer will be accessed via `${TAF}`.
