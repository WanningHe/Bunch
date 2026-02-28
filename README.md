banana operations.\
example:
```python
from Bunch.Bunch import Bunch as b
if __name__ == "__main__":
    string = ")()()()()()())"
    rotated = b.brot(string)
    aligned = b.balign(string)
    print(rotated, aligned)
```
To install:
```command
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org git+https://github.com/WanningHe/Bunch.git
```
