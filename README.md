JURY ARRAY
==========



## USAGE

```python
from jury import Polynomial
from jury import Term
from jury import JuryArray
p = Polynomial(Term(1,4),Term(0.5,3),Term(0.3,2),Term(2,1),Term(2,0))
    array = JuryArray(p)
    for line in array.generate():
        print line
```
## OUTPUT
```python
[2, 2, 0.3, 0.5, 1]
[1, 0.5, 0.3, 2, 2]
[2, 0.3, 0.5, 1]
[1, 0.5, 0.3, 2]
[0.3, 0.5, 1]
[1, 0.5, 0.3]
[-0.35, -0.7]
[-0.7, -0.35]
[-0.24499999999999997]
[-0.24499999999999997]
```

## RUN TESTS
* pip install -r pip.txt
* py.test

