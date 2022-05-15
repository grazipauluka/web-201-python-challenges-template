# web-201-python-challenges-template

### 1- Fork this repo:

You want to have your own repository for writing the solutions of all the coding challenges in the template.
Here is a general [explanation](https://docs.github.com/en/get-started/quickstart/fork-a-repo) on what is Forking and how to do it

Use the ![Fork](https://github.com/mduhagon/web-201-python-ref-resources/blob/main/Screenshot%202022-05-03%20191703.png?raw=true) button to fork this repo, this should promt something like this:

![](https://github.com/mduhagon/web-201-python-ref-resources/blob/main/Screenshot%202022-05-03%20191341.png?raw=true)

Then, you can clone your own repository to a local folder, to start making changes and running the tests!

### 2- Install pytest

From the repository root folder, you can create a virtual environment, activate it, and then install pytest there: 

For Mac / Linux:
```
python3 -m venv my_env
source my_env/bin/activate
pip install -U pytest
```

For Windows:
```
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate
pip install -U pytest
```

### 3- Running the tests

To run all tests:

From the terminal, run:
```
pytest
```

To run all tests in one test file:
```
pytest -q test_challenge_00.py
```

priorities:
1 > 6 > 2 > 4 > 5 > 3 > 7