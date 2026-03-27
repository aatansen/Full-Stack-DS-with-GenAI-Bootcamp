# **Context**

- [**Context**](#context)
- [**Day 23 - PyPI Package Discussion**](#day-23---pypi-package-discussion)
  - [**PyPI Package**](#pypi-package)
    - [What is a Python Package?](#what-is-a-python-package)
    - [Package Manager: `pip`](#package-manager-pip)
    - [Requirements File](#requirements-file)
    - [Virtual Environments](#virtual-environments)
    - [How a Package is Structured](#how-a-package-is-structured)
    - [Publishing a Package to PyPI](#publishing-a-package-to-pypi)
- [**Day 24 - PyPI Project Setup**](#day-24---pypi-project-setup)
- [**Day 25 - Publish to PyPI**](#day-25---publish-to-pypi)
- [**Day 34 - Documentation of Python Package**](#day-34---documentation-of-python-package)

# **Day 23 - PyPI Package Discussion**

## **PyPI Package**

- **PyPI (Python Package Index)** is the official repository where Python developers publish and share reusable Python packages.
- Website: pypi.org
- Similar idea to
  - npm for JavaScript
  - Maven Central for Java

[⬆️ Go to Context](#context)

### What is a Python Package?

- A **package** is a collection of Python modules bundled together.
- Used to:
  - Reuse code
  - Avoid writing everything from scratch
  - Share solutions with others
- Examples:
  - `requests` → HTTP requests
  - `numpy` → numerical computing
  - `django` → web framework

[⬆️ Go to Context](#context)

### Package Manager: `pip`

- `pip` is the tool used to install packages from PyPI.

- Common commands:
  - `pip install package_name`
  - `pip uninstall package_name`
  - `pip list`
  - `pip show package_name`
  - `pip install --upgrade package_name`

[⬆️ Go to Context](#context)

### Requirements File

- Used to manage dependencies `requirements.txt`

  ```txt
  django==4.2.3
  requests>=2.28
  numpy
  ```

- Installation
  - `pip install -r requirements.txt`

[⬆️ Go to Context](#context)

### Virtual Environments

- Isolate project dependencies.
- Prevent version conflicts.
  - `python -m venv venv`
  - `venv\Scripts\activate`

[⬆️ Go to Context](#context)

### How a Package is Structured

- Basic structure:

  ```txt
  mypackage/
    ├── mypackage/
    │    ├── __init__.py
    │    └── core.py
    ├── setup.py / pyproject.toml
    ├── README.md
    └── LICENSE
  ```

[⬆️ Go to Context](#context)

### Publishing a Package to PyPI

- Create account on PyPI
- Prepare package metadata
- Build distribution
- Upload using `twine`
- Modern tools
  - `setuptools`
  - `poetry`
  - `flit`

[⬆️ Go to Context](#context)

# **Day 24 - PyPI Project Setup**

- Create `.venv`
- Generate project structure by running `template.py`
- Add required packages in `requirements.txt` and `requirements-dev.txt`
- Write `setup.py` and `setup.cfg`
- Now define `pyproject.toml`
- Install `requirements-dev.txt`
- Define `logger.py` and `custom_exception.py` inside `src/ytnb-embed` path
- Write test run in `tox.ini` and create `tests/integration/test_int.py` & `tests/unit/test_unit.py` files
- Now to integrate CI/CD create `.github/workflows/ci.yml` for CI integration
- Push to github to see the github action running

[⬆️ Go to Context](#context)

# **Day 25 - Publish to PyPI**

- Add youtube embed functionality in `src/ytnb_embed/youtube.py`
- Now create [PyPI account](https://pypi.org/account/register/)
- Get API
- Setup secrete in Github Action secrete
  - [https://github.com/USER_NAME/REPO_NAME/settings/secrets/actions](https://github.com/USER_NAME/REPO_NAME/settings/secrets/actions)
  - Add `PYPI_API_TOKEN` in New repository secret
- Now in every push it will test using `tox` and in every release it will release it to the `PyPI`

> [!NOTE]
>
> - Final Project Repository --> [ytnb-embed](https://github.com/aatansen/ytnb-embed)

[⬆️ Go to Context](#context)

# **Day 34 - Documentation of Python Package**

- Make sure [mkdocs-material](https://pypi.org/project/mkdocs-material/) is install
- Create those files

  ```txt
  ytnb-embed
  ├── 📁 .github
  │   └── 📁 workflows
  │       └── ⚙️ docs.yml
  ├── 📁 docs
  │   ├── 📁 usage
  │   │   ├── 📝 advanced.md
  │   │   ├── 📝 basic.md
  │   │   └── 📝 examples.md
  │   ├── 📝 api.md
  │   ├── 📝 contributing.md
  │   ├── 📝 index.md
  │   ├── 📝 installation.md
  │   ├── 📝 license.md
  │   ├── 📝 privacy.md
  │   └── 📝 quick-start.md
  └── ⚙️ mkdocs.yml
  ```

- Project repository: [ytnb-embed](https://github.com/aatansen/ytnb-embed)
- Docs : [ytnb-embed documentation](https://aatansen.github.io/ytnb-embed/)

[⬆️ Go to Context](#context)
