import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import project_functions

location = "C:\\Users\\pc\\Desktop\\컴퓨터프로그래밍\\프로젝트\\"

project_functions.data_processing(location)
project_functions.data_generation(location)
project_functions.print_graph(location, 'gulim')