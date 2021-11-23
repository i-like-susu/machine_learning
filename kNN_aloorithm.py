from collections import Counter
import matplotlib.pyplot as plt
from math import sqrt
import numpy as np

seed = np.random.seed(10)
sample = np.random.random(60).reshape(-1, 2)

label = np.random.randint(0, 2, 30)

target = [0.5, 0.5]
distance = [sqrt(np.sum((target - i) ** 2)) for i in sample]

nearest = np.argsort(distance)
top = [label[i] for i in nearest[:6]]

counter = Counter(top)
print(counter.most_common(1)[0][0])