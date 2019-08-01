# User manual

## How to use *test_py.py*
1. Copy __*test_py*__ to your work place where your python file located
2. Open terminal and go to your work place 
3. Type **_pipenv shell --three_** to set your own eviroment. If you aleady doneit one time before, just type **_pipenv shell_**
4. Type **_pipenv install pytest_** to install pytest
5. Open __*test_py*__ file and **import** your py file as main

```
import unittest
import python_basic as main

class MyTest(unittest.TestCase):
    def test_waypoint1(self):
        name = '        world             '
        self.assertEqual(main.hello(name),"Hello world!")
    def test_waypoint2(self):
        a = 3
        b = 4

```
My py file name python_basic.py, so I type **_import python_basic as main_**
 
6. Type **_pytest_** to run the test

### Note: All your function must be the same name with the functions which was already noted in README.md file


##### Update date 1/08/2019

