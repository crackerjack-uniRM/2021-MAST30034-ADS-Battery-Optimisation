# Battery Optimisation Project (BOP) Dev Environment Setup

To run the project without any unexpected error, please use the following commands to build any one of environments below to setup a virtual environment.

After install a virtual environment, please install dependencies using requirements.txt.

**For MacOS/Linux User**: choose either methods

**For Windows User**: prefer choose anaconda/miniconda

## Anaconda / Miniconda

**Auto Environment Setup**

To create a conda environment automatically, please run `install.py` script. 

**Manual Environment Setup**

A `environment.yml` is generated under path `./conda/`, please check the file existence, if exist, please run 

```bash
conda env create -f environment.yml
```

OR install conda environment from a spec-file:

```bash
conda install --name bop --file spec-file
```

To activate the conda envrionment, run `conda activate bop`.

Please make sure that there is no duplicated environment name.

## Virtual Envrionment

To run the virutal envrionment setup script, please run `install.py`. 

To activate the virtual environment, please run `source /venv-bop/bin/activate`

NOTE: a shell may block this command, for example, fish shell will require user add this virtual env to config.fish. 

And this virtual env setup is highly depends on the current python version that you have. Therefore, the team strongly 
recommand using anaconda / miniconda instead.
