# **Context**

- [**Context**](#context)
- [**Day 10 - Virtual Environment \& Requirements**](#day-10---virtual-environment--requirements)
  - [**Virtual Environment**](#virtual-environment)
    - [Create Conda Environment](#create-conda-environment)
    - [List and Remove Conda Environments](#list-and-remove-conda-environments)
  - [**Requirements**](#requirements)
    - [`requirements.txt` file](#requirementstxt-file)

# **Day 10 - Virtual Environment & Requirements**

## **Virtual Environment**

### Create Conda Environment

- Create an environment in current folder (`-p`) or ` -n` for conda default path

  ```sh
  conda create -p .venv
  ```

- Activate Environment

  ```sh
  conda activate ./.venv
  ```

- Install Python in Environment

  ```sh
  conda install python=3.13
  ```

- Install Packages

  ```sh
  conda install numpy pandas
  ```

- Deactivate Environment

  ```sh
  conda deactivate
  ```

[⬆️ Go to Context](#context)

### List and Remove Conda Environments

- List All Environments – Shows all conda environments

  ```sh
  conda env list
  # or
  conda info --envs
  ```

- Remove Environment by Name

  ```sh
  conda remove --name my_env --all
  ```

- Remove Environment by Path

  ```sh
  conda remove -p ./my_env --all
  ```

[⬆️ Go to Context](#context)

## **Requirements**

### `requirements.txt` file

- A plain text file listing all Python packages and versions required for a project

  ```txt
  # Example contents of requirements.txt
  numpy==1.26.0
  pandas==2.1.0
  matplotlib==3.8.0
  scikit-learn==1.3.0
  django==5.2.0
  ```

- Install Packages from `requirements.txt`

  ```sh
  pip install -r requirements.txt
  ```

- Generate `requirements.txt` from Current Environment

  ```sh
  pip freeze > requirements.txt
  ```

- Check Installed Packages

  ```sh
  pip list
  ```

[⬆️ Go to Context](#context)
