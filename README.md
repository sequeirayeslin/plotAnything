# plotAnything
I figured out a way to plot graphs using turtle graphics

# How to plot

Import plotAnything.py:

```Python
import plotAnything as pa
```

Run this function once:

```Python
pa.plotGraph()
```

Create a function that takes in only a single argument, i.e., a float/integer as in input and returns a float/integer as the output:

```Python
def a_line(x):
  return x
```

Or use a predefined function of a similar nature:

```Python
from math import sin
```

Plot the function using plotFun. Specify a range of x values, eg. x -> (-3, 3), turn on the autoscaling feature or the entire graph may not be visible:

```Python
pa.drawFun(a_line, -3, 3, autoScaleX= True, autoScaleY= True)
```

![alt text](https://github.com/sequeirayeslin/plotAnything/blob/main/a_line.png?raw=true)
![alt text](https://github.com/sequeirayeslin/plotAnything/blob/main/sine.png?raw=true)
