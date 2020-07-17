import datetime
from collections import OrderedDict

import confuse
import yaml

from order_history_generator.generator import *

file = open('config.yaml')

config = yaml.load(file, Loader=yaml.FullLoader)

p = config[ZONES]['RED'][PERCENT_OF_TOTAL_ORDERS]
t = config[TOTAL_ORDERS]

print(int(p * t))

list = [1,2,3]
list[0] = 2
print(list)