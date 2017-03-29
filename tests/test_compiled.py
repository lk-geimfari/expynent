import unittest

from expynent import compiled
from tests.ipv6_fixtures import IP_V6_DATA


class CompiledPatternsTestCase(unittest.TestCase):
    def setUp(self):
        self.compiled_patterns = compiled

    def test_mac_address_pattern(self):
        mac_pattern = self.compiled_patterns.MAC_ADDRESS
        mac = '00:08:C7:1B:8C:02'
        self.assertTrue(mac_pattern.match(mac))

    def test_credit_card_pattern(self):
        credit_strict_pattern = self.compiled_patterns.CREDIT_CARD_STRICT
        valid_pats = set((
            '3519 2073 7960 3241',
            '3519-2073-7960-3241',
            '3519207379603241',
        ))
        nonstrict_pats = set((
            '3519-2073 7960 3241',
            '3519-2073-7960 3241',
            '3519 2073-7960 3241',
            '3519 2073-7960-3241',
            '3519 2073 7960-3241',
        ))
        invalid_pats = set((
            '1234',
            '123',
            '12341234123413245',
            '1234_1234_1234_1234',
        ))
        # Test strict pattern.
        for validpat in valid_pats:
            self.assertTrue(credit_strict_pattern.match(validpat))
        # Test non-strict patern.
        credit_pattern = self.compiled_patterns.CREDIT_CARD
        for validpat in valid_pats.union(nonstrict_pats):
            self.assertTrue(credit_pattern.match(validpat))

        # Test invalid patterns for strict.
        for invalidpat in invalid_pats.union(nonstrict_pats):
            self.assertFalse(credit_strict_pattern.match(invalidpat))

        # Test invalid patterns for non-strict.
        for invalidpat in invalid_pats:
            self.assertFalse(credit_pattern.match(invalidpat))

    def test_ip_v4_pattern(self):
        ip_v4_pattern = self.compiled_patterns.IP_V4
        ip_v4 = '209.18.181.23'
        self.assertTrue(ip_v4_pattern.match(ip_v4))

    def test_ip_v6_pattern(self):
        ip_v6_pattern = self.compiled_patterns.IP_V6
        for ip_v6, result in IP_V6_DATA.items():
            if result:
                self.assertIsNotNone(ip_v6_pattern.match(ip_v6))
            else:
                self.assertIsNone(ip_v6_pattern.match(ip_v6))

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

    def test_roman_numerals(self):
        pattern = self.compiled_patterns.ROMAN_NUMERALS
        numerals = (
            'X',
            'XL',
            'L',
            'XV',
            'XX',
            'XI'
        )
        for num in numerals:
            self.assertTrue(pattern.match(num))

    def test_ethereum_address(self):
        pattern = self.compiled_patterns.ETHEREUM_ADDRESS

        valid_addresses = [
            "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe",
            "0x5ed8cee6b63b1c6afce3ad7c92f4fd7e1b8fad9f",
            "0xfac399e49f5b6867af186390270af252e683b154",
            "0x85fc71ecffb0703a650f05263a3c1b0548092f32",
            "0xd1ade25ccd3d550a7eb532ac759cac7be09c2719",
            "0xda65665fc30803cb1fb7e6d86691e20b1826dee0",
            "0xe470b1a7d2c9c5c6f03bbaa8fa20db6d404a0c32",
            "0xf4dd5c3794f1fd0cdc0327a83aa472609c806e99",
        ]
        for address in valid_addresses:
            self.assertTrue(pattern.match(address))

        invalid_addresses = [
            "0xde0B295669a9FD93d5F28D9Ec85E40f7BAe",
            "0x85fc71ecffb0703a650f05263a3c1b0548092f32ff",
            "0xd1ade25 3d550a7eb532ac759cac7be09c2719",
            "0xda6:!65fc30803cb1fb7e6d86691e20b1826dee0",
            "0xe470b1a7d2,9c5c6f03bbaa8fa20db6d404a0c32",
            "0xf4dd5c3794f1fd0cdc0327;???a472609c806e99",
        ]
        for address in invalid_addresses:
            self.assertFalse(pattern.match(address))
