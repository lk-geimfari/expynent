import re

import expynent

CREDIT_CARD = re.compile(expynent.CREDIT_CARD)
SLUG = re.compile(expynent.SLUG)
HEX_VALUE = re.compile(expynent.HEX_VALUE)
IP_V4 = re.compile(expynent.IP_V4)
MAC_ADDRESS = re.compile(expynent.MAC_ADDRESS)
BITCOIN_ADDRESS = re.compile(expynent.BITCOIN_ADDRESS)
YANDEX_MONEY = re.compile(expynent.YANDEX_MONEY)
LONGITUDE = re.compile(expynent.LONGITUDE)
LATITUDE = re.compile(expynent.LATITUDE)
TIME_24H_FORMAT = re.compile(expynent.TIME_24H_FORMAT)
ISO_8601_DATETIME = re.compile(expynent.ISO_8601_DATETIME)