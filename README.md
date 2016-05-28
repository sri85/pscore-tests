# pscore-tests
Tests for Gousto Healthy Recipes
###Introduction
This repository contains the tests for [Gousto  Recipes page](https://www.gousto.co.uk/this-weeks-recipes). These tests are based on shareable page object model based framework called [pscore](https://pypi.python.org/pypi/pscore/0.4.8) . 
pscore stands for Python Selenium Core. These tests use page object model and the model is installed as an dependency before the tests are run  , this allows engineers to share the models across organization, the model for these tests can be found [here](https://github.com/sri85/pscore-model)
### Pre-Requisities
These instructions are for the tests to run on OsX machine
 1. Python 2.7
 2. Brew package manager for MAC
 3. Python package manager Pip,installation instructions can be found [here](http://docs.python-guide.org/en/latest/starting/install/osx) 
 4. Virtualenv wrapper for managing python dependencies , the instructions to install virtualenv can be found [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenvironments-ref)
These steps needs to be completed before proceeding to the test execution.
 5. Git
 6. Chrome Browser

### Preparing the environment for test execution.
 1. Clone this repo using `git clone https://github.com/sri85/pscore-tests.git`
 2. Navigate to the folder and create a virtualenv to install the dependencies using the command `virtualenv venv` where `venv` stands for name of the virtual environment. 
 3. The dependencies for the tests are listed in `requirements.txt` which can be installed using `pip install -r requirements.txt`, this will install `nose2` and the page object model `gousto_model` in the virtual environment.
 4. Activate the virtualenvironment using the command `source venv/bin/activate`

### Running the tests
 1. The tests use `nose2` as a test runner so in order to run the tests use the command `nose2 -c nose2.cfg`. This would run all the tests in the `tests` folder.(Currently there is only one file `test_recipe_page.py`)
 2. Let us say if you want to target specific tests then you could use `tags` for the same `nose2 -c nose2.cfg -A tags="<name of the tag>"`, you could find the name of the tag in the `tests/test_recipe_page.py` where the tags are defined as `@tagger("name of the tag")`
 3. These tests would run in a chrome browser.
 
### FAQ's
 1. Since the tests are run in chrome browser which requires `chromedriver` binary to be present in the `HOME` directory with executable permissions. Most of the times if the framework should download the chromedriver binary onto your machine and palce it in the `HOME` folder . If it fails for some reason , Grab the zip file from [here](http://chromedriver.storage.googleapis.com/index.html?path=2.21/) and extract the binary and place it in `HOME` directory and give it executable permissions using `chmod +x <path to the chromedriver>`.
 
If any issues , feel free to contact me :) 
 

