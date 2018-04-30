import numpy as np


text = np.loadtxt("click-stream event.csv",delimiter=",",skiprows=1)

print(text[0])
