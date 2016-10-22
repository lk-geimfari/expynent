import re

import expynent

credit_card = re.compile(expynent.CREDIT_CARD)
slug = re.compile(expynent.SLUG)
hex_value = re.compile(expynent.HEX_VALUE)
ip_v4 = re.compile(expynent.IP_V4)
ip_v6 = re.compile(expynent.IP_V6)
mac_address = re.compile(expynent.MAC_ADDRESS)
bitcoin = re.compile(expynent.BITCOIN_ADDRESS)
yandex_money = re.compile(expynent.YANDEX_MONEY)
longitude = re.compile(expynent.LONGITUDE)
latitude = re.compile(expynent.LATITUDE)
