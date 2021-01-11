# Pytest-BDD-in-VSCode

A basic project using Pytest-BDD and Cucumber in VSCode



![](https://raw.githubusercontent.com/georgecristian97/Logo/main/logo/python-logo.png)![](https://raw.githubusercontent.com/georgecristian97/Logo/main/logo/VSCode-logo.png)![](https://raw.githubusercontent.com/georgecristian97/Logo/main/logo/Anaconda-Logo.png)



Change some Windows settings:

powershell as admin:
 Set-ExecutionPolicy RemoteSigned
 

:hammer: You need:	

Anaconda prompt -> create folder -> enter it
conda install -c conda-forge pipenv
pipenv install pytest
pipenv install pytest-bdd
pipenv install gherkin-official
pipenv install selenium



VSCode Pytest BDD + Python
open folder in VSCode
ctrl + shift + p - > python: interpreter select the one from the current folder



In project folder:
Anaconda prompt - > pipenv shell
pytest-bdd generate tests/features/buscaGoogle.feature > tests/test_mySearch.py

ctrl + shift + p - > Python: Configure test - > pytest -> folder with tests



Download google chrome
Place chromedriver.exe in project folder