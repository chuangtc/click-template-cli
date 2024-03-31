# click_app (template-cli)

Leveraging click python package to create cli tool template

A sample code of using click package for running command line tool

## For general users to run the program with pip install

```bash
pip3 install click-app
click_app --name=Jason
```

## For developers to develop features or fix bugs on github

<https://github.com/chuangtc/click-template-cli>

### Installation for development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel poetry
pip install click
pip install -e .
pip install pytest
pytest
```

### Usage

```bash
click_app --help
click_app --name=Jason
```

```bash
pip3 install --upgrade build
python3 -m build
```

### After running it, deactivate the .venv

```bash
deactivate
```

## Packaging and uploading to PyPI

### Manual way (For the test.pypi purpose, it's ok)

<https://packaging.python.org/en/latest/tutorials/packaging-projects/>

### Github action

<https://dev.to/iamtekson/publish-package-to-pypi-and-release-new-version-using-github-actions-108k>

Some minor changes, please checkout my .github/workflows
