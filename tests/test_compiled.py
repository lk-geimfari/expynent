import unittest

from expynent import compiled


class CompiledPatternsTestCase(unittest.TestCase):
    def setUp(self):
        self.compiled_patterns = compiled

    def test_mac_address_pattern(self):
        mac_pattern = self.compiled_patterns.mac_address
        mac = '00:08:C7:1B:8C:02'
        self.assertTrue(mac_pattern.match(mac))

    def test_credit_card_pattern(self):
        credit_pattern = self.compiled_patterns.credit_card
        credit_card = '3519 2073 7960 3241'
        self.assertTrue(credit_pattern.match(credit_card))

        credit_card = '3519-2073-7960-3241'
        self.assertTrue(credit_pattern.match(credit_card))

        credit_card = '3519207379603241'
        self.assertTrue(credit_pattern.match(credit_card))

    def test_ip_v4_pattern(self):
        ip_v4_pattern = self.compiled_patterns.ip_v4
        ip_v4 = '209.18.181.23'
        self.assertTrue(ip_v4_pattern.match(ip_v4))

    # def test_ip_v6_pattern(self):
    #     ip_v6_pattern = self.compiled_patterns.ip_v6
    #     ip_v6 = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
    #     self.assertTrue(ip_v6_pattern.match(ip_v6))

    def test_hex_value_pattern(self):
        hex_pattern = self.compiled_patterns.hex_value
        hex_value = '#a3c113'
        self.assertTrue(hex_pattern.match(hex_value))

    def test_slug_pattern(self):
        slug_pattern = self.compiled_patterns.slug
        slug = 'greatest-slug-ever'
        self.assertTrue(slug_pattern.match(slug))

    def test_bitcoin_pattern(self):
        bitcoin_pattern = self.compiled_patterns.bitcoin
        address = '1BoatSLRHtKNngkdXEeobR76b53LETtpyT'
        self.assertTrue(bitcoin_pattern.match(address))

    def test_yandex_money_pattern(self):
        ym_pattern = self.compiled_patterns.yandex_money
        ym = '97508675463414'
        self.assertTrue(ym_pattern.match(ym))

    def test_longitude_pattern(self):
        longitude_pattern = self.compiled_patterns.longitude
        x = '112.1844026051194'
        self.assertTrue(longitude_pattern.match(x))

    def test_latitude_pattern(self):
        latitude_pattern = self.compiled_patterns.latitude
        x = '-66.4214188124611'
        self.assertTrue(latitude_pattern.match(x))
