import unittest

from expynent import compiled


class CompiledPatternsTestCase(unittest.TestCase):
    def setUp(self):
        self.compiled_patterns = compiled

    def test_mac_address_pattern(self):
        mac_pattern = self.compiled_patterns.MAC_ADDRESS
        mac = '00:08:C7:1B:8C:02'
        self.assertTrue(mac_pattern.match(mac))

    def test_credit_card_pattern(self):
        credit_pattern = self.compiled_patterns.CREDIT_CARD
        credit_card = '3519 2073 7960 3241'
        self.assertTrue(credit_pattern.match(credit_card))

        credit_card = '3519-2073-7960-3241'
        self.assertTrue(credit_pattern.match(credit_card))

        credit_card = '3519207379603241'
        self.assertTrue(credit_pattern.match(credit_card))

    def test_ip_v4_pattern(self):
        ip_v4_pattern = self.compiled_patterns.IP_V4
        ip_v4 = '209.18.181.23'
        self.assertTrue(ip_v4_pattern.match(ip_v4))

    # def test_ip_v6_pattern(self):
    #     ip_v6_pattern = self.compiled_patterns.ip_v6
    #     ip_v6 = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
    #     self.assertTrue(ip_v6_pattern.match(ip_v6))

    def test_hex_value_pattern(self):
        hex_pattern = self.compiled_patterns.HEX_VALUE
        hex_value = '#a3c113'
        self.assertTrue(hex_pattern.match(hex_value))

    def test_slug_pattern(self):
        slug_pattern = self.compiled_patterns.SLUG
        slug = 'greatest-slug-ever'
        self.assertTrue(slug_pattern.match(slug))

    def test_bitcoin_pattern(self):
        bitcoin_pattern = self.compiled_patterns.BITCOIN_ADDRESS
        address = '1BoatSLRHtKNngkdXEeobR76b53LETtpyT'
        self.assertTrue(bitcoin_pattern.match(address))

    def test_yandex_money_pattern(self):
        ym_pattern = self.compiled_patterns.YANDEX_MONEY
        ym = '97508675463414'
        self.assertTrue(ym_pattern.match(ym))

    def test_longitude_pattern(self):
        longitude_pattern = self.compiled_patterns.LONGITUDE
        x = '112.1844026051194'
        self.assertTrue(longitude_pattern.match(x))

    def test_latitude_pattern(self):
        latitude_pattern = self.compiled_patterns.LATITUDE
        x = '-66.4214188124611'
        self.assertTrue(latitude_pattern.match(x))

    def test_iso_8601_datetime(self):
        iso_pattern = self.compiled_patterns.ISO_8601_DATETIME
        datetime = '2014-12-05T12:30:45.123456-05:30'
        self.assertTrue(iso_pattern.match(datetime))

        _md = iso_pattern.match(datetime)
        as_dict = _md.groupdict()

        self.assertIsInstance(as_dict, dict)

        self.assertEqual('2014', as_dict['year'])
        self.assertEqual('45.123456', as_dict['sec'])
        self.assertEqual('05', as_dict['mday'])
        self.assertEqual('30', as_dict['min'])
        self.assertEqual('12', as_dict['mon'])
        self.assertEqual('12', as_dict['hour'])

    def test_time24h_format(self):
        pattern = self.compiled_patterns.TIME_24H_FORMAT
        time = '23:45'
        self.assertTrue(pattern.match(time))

        time_2 = '13:04'
        self.assertTrue(pattern.match(time_2))

        time_3 = '09:22'
        self.assertTrue(pattern.match(time_3))

    def test_isbn(self):
        pattern = self.compiled_patterns.ISBN

        isbns = [
            "ISBN-13: 978-1-56619-909-4",
            "ISBN-13: 978 5 93286 159 2",
            "978-1-56619-909-4",
            "ISBN-10: 1-56619-909-3",
            "1-56619-909-3",
            "978 1 56619 909 4",
            "1 56619 909 3",
        ]
        for isbn in isbns:
            self.assertTrue(pattern.match(isbn))