# click-template-cli
Leveraging click python package to create cli tool template

A sample code of using click package for running command line tool

## For general users to run the program with pip installl
```bash
pip3 install click-template-cli
click_app --name=Jason
```


## For developers to develop features or fix bugs

### Install
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
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

### After running it, deactivate the .venv
```bash
deactivate
```