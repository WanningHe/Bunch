banana operations.
example:
```python
from Bunch import Bunch as b
if __name__ == "__main__":
    string = ")()()()()()())"
    rotated = b.brot(string)
    aligned = b.balign(string)
    print(rotated, aligned)
```
