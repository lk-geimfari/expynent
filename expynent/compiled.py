import re

import expynent

username = re.compile(expynent.USERNAME)
uppercase = re.compile(expynent.UPPERCASE)
credit_card = re.compile(expynent.CREDIT_CARD)
url = re.compile(expynent.URL)
slug = re.compile(expynent.SLUG)
domain = re.compile(expynent.DOMAIN)
hex_value = re.compile(expynent.HEX_VALUE)
ip_v4 = re.compile(expynent.IP_V4)
ip_v6 = re.compile(expynent.IP_V6)
mac_address = re.compile(expynent.MAC_ADDRESS)
year = re.compile(expynent.YEAR)
html_tag = re.compile(expynent.HTML_TAG)
html_js_tag = re.compile(expynent.HTML_JS_TAG)
bitcoin = re.compile(expynent.BITCOIN_ADDRESS)
yandex_money = re.compile(expynent.YANDEX_MONEY)
longitude = re.compile(expynent.LONGITUDE)
latitude = re.compile(expynent.LATITUDE)
