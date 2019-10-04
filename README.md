## Expynent - Common Regular Expression

[![Build Status](https://travis-ci.org/lk-geimfari/expynent.svg?branch=master)](https://travis-ci.org/lk-geimfari/expynent)
[![codecov](https://codecov.io/gh/lk-geimfari/expynent/branch/master/graph/badge.svg)](https://codecov.io/gh/lk-geimfari/expynent)
[![PyPI version](https://badge.fury.io/py/expynent.svg)](https://badge.fury.io/py/expynent)

**Expynent** is a tiny library that provides common regular expression patterns. This can be useful if you don't want to 
write regular expression manually. Also you can use this library as [fixture](https://docs.pytest.org/en/latest/fixture.html) for testing framework like a [py.test](https://docs.pytest.org/en/latest/).

## Installation

```
 ~  pip install expynent
```


## Usage
Just import the pattern that you want:

```python
import re
from expynent.patterns import ZIP_CODE

if re.match(ZIP_CODE['RU'], '43134'):
    print('match')
else:
    print('not match')
    
# Output: 'not match'

```
also you can use compiled patterns:
```python
from expynent.compiled import URL

url = 'http://foo.com/blah_blah_(wikipedia)_(again)'

if URL.match(url):
    print('valid')
else:
    print('invalid')
    
# Output: 'valid'
```

## Supported patterns

You can look at the list of supported patterns below:

1. `BITCOIN_ADDRESS`
2. `CREDIT_CARD`
3. `CREDIT_CARD_STRICT`
4. `EMAIL_ADDRESS`
5. `ETHEREUM_ADDRESS`
6. `FLOAT_NUMBER`
7. `HEX_VALUE`
8. `IP_V4`
9. `IP_V6`
10. `IRC`
11. `ISBN`
12. `ISO_8601_DATETIME`
13. `LATITUDE`
14. `LICENSE_PLATE`
15. `LONGITUDE`
16. `MAC_ADDRESS`
17. `PGP_FINGERPRINT`
18. `PHONE_NUMBER`
19. `ROMAN_NUMERALS`
20. `SLUG`
21. `TIME_24H_FORMAT`
22. `URL`
23. `UUID`
24. `YANDEX_MONEY`
25. `ZIP_CODE`
26. `ETHEREUM_HASH`

## Contributing
Your contributions are always welcome! Please take a look at the [contribution](https://github.com/lk-geimfari/expynent/blob/master/CONTRIBUTING.md) guidelines first.

## Attention
This is an **experimental** project and it's mean that we do not guarantee stability. We try to write tests for
all expressions, but we cannot guarantee the perfect operation of regular expressions because it is impossible to cover all cases.

## Licence 
[BSD 3-Clause License](https://raw.githubusercontent.com/lk-geimfari/expynent/master/LICENSE)
