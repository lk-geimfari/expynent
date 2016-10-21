<p align="center">
  <img src="https://raw.githubusercontent.com/lk-geimfari/expynent/master/other/logo.png">
</p>

 **expynent** is a tinny library that provides RegEx patterns. This can be useful if you don't want to write regular expression manually.



#### Installation
```zsh
➜  ~ git clone https://github.com/lk-geimfari/expynent.git
➜  ~ cd expynent/
➜  ~ python setup.py install

```
or
```zsh
➜  ~  pip install expynent
```


#### Usage
Just import the pattern that you want:
```python
import re
import expynent.patterns as expas

if re.match(expas.ZIP_CODE['RU'], '43134'):
    print('match')
else:
    print('not match')
    
# Output: 'not match'

```
also you can use compiled patterns:
```python
from expynent.compiled import username

u = input('Enter username: ')

if username.match(u):
    print('valid')
else:
    print('invalid')
```


#### Contributing
Your contributions are always welcome! Please take a look at the [contribution](https://github.com/lk-geimfari/expynent/blob/master/CONTRIBUTING.md) guidelines first.


#### Licence 
[BSD 3-Clause License](https://raw.githubusercontent.com/lk-geimfari/expynent/master/LICENSE)
