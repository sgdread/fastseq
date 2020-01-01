<!--

#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: nbs/index.ipynb
# command to build the docs after a change: nbdev_build_docs

-->

# Fastseq

> A way to use fastai with sequence data


This file will become your README and also the index of your documentation.

## How to use
<div class="codecell" markdown="1">
<div class="input_area" markdown="1">

```python
from fastseq.core import *
from fastseq.data.external import *
from fastai2.basics import *
```

</div>

</div>

Getting the data fastai style:
<div class="codecell" markdown="1">
<div class="input_area" markdown="1">

```python
path = untar_data(URLs.m4_daily)
path
```

</div>
<div class="output_area" markdown="1">




    Path('/home/tako/.fastai/data/m4_daily')



</div>

</div>
<div class="codecell" markdown="1">
<div class="input_area" markdown="1">

```python
# df_train = pd.read_csv(path/'train.csv')
df_test = pd.read_csv(path/'val.csv')
df_test.head()
```

</div>
<div class="output_area" markdown="1">




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>V1</th>
      <th>V2</th>
      <th>V3</th>
      <th>V4</th>
      <th>V5</th>
      <th>V6</th>
      <th>V7</th>
      <th>V8</th>
      <th>V9</th>
      <th>V10</th>
      <th>V11</th>
      <th>V12</th>
      <th>V13</th>
      <th>V14</th>
      <th>V15</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>D1</td>
      <td>2039.20</td>
      <td>2035.00</td>
      <td>2051.80</td>
      <td>2061.8</td>
      <td>2063.50</td>
      <td>2069.5</td>
      <td>2054.00</td>
      <td>2057.00</td>
      <td>2062.80</td>
      <td>2066.40</td>
      <td>2067.40</td>
      <td>2071.40</td>
      <td>2083.80</td>
      <td>2080.60</td>
    </tr>
    <tr>
      <th>1</th>
      <td>D2</td>
      <td>2986.00</td>
      <td>3001.20</td>
      <td>2975.90</td>
      <td>2996.1</td>
      <td>2981.90</td>
      <td>2985.5</td>
      <td>2975.80</td>
      <td>2956.20</td>
      <td>2964.70</td>
      <td>2989.00</td>
      <td>2991.40</td>
      <td>3024.90</td>
      <td>3070.80</td>
      <td>3076.90</td>
    </tr>
    <tr>
      <th>2</th>
      <td>D3</td>
      <td>1120.70</td>
      <td>1117.90</td>
      <td>1115.10</td>
      <td>1112.3</td>
      <td>1109.50</td>
      <td>1106.7</td>
      <td>1103.90</td>
      <td>1101.10</td>
      <td>1098.30</td>
      <td>1095.50</td>
      <td>1092.70</td>
      <td>1089.90</td>
      <td>1087.10</td>
      <td>1084.30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D4</td>
      <td>1190.00</td>
      <td>1162.00</td>
      <td>1134.00</td>
      <td>1106.0</td>
      <td>1078.00</td>
      <td>1050.0</td>
      <td>1022.00</td>
      <td>994.00</td>
      <td>966.00</td>
      <td>938.00</td>
      <td>910.00</td>
      <td>1428.00</td>
      <td>1400.00</td>
      <td>1372.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>D5</td>
      <td>5904.67</td>
      <td>5917.05</td>
      <td>5922.58</td>
      <td>5928.8</td>
      <td>5935.29</td>
      <td>6002.8</td>
      <td>6009.47</td>
      <td>6014.82</td>
      <td>6020.19</td>
      <td>6072.49</td>
      <td>6077.72</td>
      <td>6080.23</td>
      <td>6082.75</td>
      <td>6108.07</td>
    </tr>
  </tbody>
</table>
</div>



</div>

</div>
