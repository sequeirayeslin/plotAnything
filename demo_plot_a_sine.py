
import plotAnything as pa
from math import sin, pi

pa.drawGraph()

f = 2
A = 2
sin_2_Hz = lambda x: A * sin(2*pi*f*x)

pa.drawFun(sin_2_Hz, -2, 2, autoScaleX= True, autoScaleY= True)
input()