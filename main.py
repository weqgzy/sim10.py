import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head(20)

#pd.get_dummies(data['whoAmI'])

robot_lst = []
human_lst = []
for i in lst:
  if i == 'robot':
     robot_lst.append(1)
     human_lst.append(0)
  if i == 'human':
     robot_lst.append(0)
     human_lst.append(1)
one_hot_data = pd.DataFrame({'human': human_lst, 'robot': robot_lst})
one_hot_data.head(20)