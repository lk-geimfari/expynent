import re

import expynent

# RegEx pattern that match credit card number.
# Match:
#    - 3519 2073 7960 3241
#    - 3519-2073-7960-3241
#    - 3519207379603241
CREDIT_CARD = re.compile(expynent.CREDIT_CARD)

# RegEx pattern that match slug.
# Match:
#    - greatest-slug-ever
SLUG = re.compile(expynent.SLUG)

# RegEx pattern that match hex value.
# Match:
#    - #a3c113
HEX_VALUE = re.compile(expynent.HEX_VALUE)

# RegEx pattern that match IPv4 address.
# Match:
#    209.18.181.23
IP_V4 = re.compile(expynent.IP_V4)

# RegEx pattern that match MAC address.
# Match:
#    - 00:08:C7:1B:8C:02
MAC_ADDRESS = re.compile(expynent.MAC_ADDRESS)

# RegEx pattern that match datetime in ISO 8601 format.
# Match:
#    - 1BoatSLRHtKNngkdXEeobR76b53LETtpyT
BITCOIN_ADDRESS = re.compile(expynent.BITCOIN_ADDRESS)

# RegEx pattern that match Yandex.Money account.
# Match:
#    - 97508675463414
YANDEX_MONEY = re.compile(expynent.YANDEX_MONEY)

# RegEx pattern that match longtitude
# Match:
#    - 112.1844026051194
LONGITUDE = re.compile(expynent.LONGITUDE)

# RegEx pattern that match latitude
# Match:
#    - -66.4214188124611
LATITUDE = re.compile(expynent.LATITUDE)

# RegEx pattern that match dtime in 24 hour format
# Match:
#    - 23:45
TIME_24H_FORMAT = re.compile(expynent.TIME_24H_FORMAT)

# RegEx pattern that match datetime in ISO 8601 format.
# Match:
#    - 2014-12-05T12:30:45.123456-05:30
ISO_8601_DATETIME = re.compile(expynent.ISO_8601_DATETIME)

# RegEx pattern that match ISBN 10 and ISBN 13.
# Match:
#    - ISBN-13: 978-1-56619-909-4
#    - ISBN-13: 978 5 93286 159 2
#    - 978-1-56619-909-4
#    - ISBN-10: 1-56619-909-3
#    - 1-56619-909-3
#    - 978 1 56619 909 4
#    - 1 56619 909 3
ISBN = re.compile(expynent.ISBN)

# RegEx pattern that match binary numbers.
# Match:
#    - L
#    - XL
#    - XV
#    - XX
#    - XI
#    - etc.
ROMAN_NUMERALS = re.compile(expynent.ROMAN_NUMERALS)