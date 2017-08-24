import re
import unittest
from expynent import patterns
from tests.ipv6_fixtures import IP_V6_DATA
from tests.ipv4_fixtures import IP_V4_DATA
from tests.url_fixtures import VALID_URLS, INVALID_URLS


class PatternsTestCase(unittest.TestCase):
    def setUp(self):
        self.patterns = patterns

    def test_zip_code_pattern(self):
        us_zip = self.patterns.ZIP_CODE['US']
        self.assertTrue(re.match(us_zip, '23414'))

    def test_email_address_code_pattern(self):
        email_example = 'something@gmail.com'
        self.assertTrue(re.match(self.patterns.EMAIL_ADDRESS, email_example))

    def test_mac_address_pattern(self):
        mac_pattern = self.patterns.MAC_ADDRESS
        mac = '00:08:C7:1B:8C:02'
        self.assertTrue(re.match(mac_pattern, mac))

    def test_credit_card_pattern(self):
        credit_strict_pattern = self.patterns.CREDIT_CARD_STRICT
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
            self.assertTrue(re.match(credit_strict_pattern, validpat))
        # Test non-strict patern.
        credit_pattern = self.patterns.CREDIT_CARD
        for validpat in valid_pats.union(nonstrict_pats):
            self.assertTrue(re.match(credit_pattern, validpat))

        # Test invalid.txt patterns for strict.
        for invalidpat in invalid_pats.union(nonstrict_pats):
            self.assertFalse(re.match(credit_strict_pattern, invalidpat))

        # Test invalid.txt patterns for non-strict.
        for invalidpat in invalid_pats:
            self.assertFalse(re.match(credit_pattern, invalidpat))

    def test_ip_v4_pattern(self):
        ip_v4_pattern = self.patterns.IP_V4
        for ip_v4, result in IP_V4_DATA.items():
            if result:
                self.assertIsNotNone(re.match(ip_v4_pattern, ip_v4, re.VERBOSE | re.IGNORECASE | re.DOTALL))
            else:
                self.assertIsNone(re.match(ip_v4_pattern, ip_v4, re.VERBOSE | re.IGNORECASE | re.DOTALL))

    def test_ip_v6_pattern(self):
        ip_v6_pattern = self.patterns.IP_V6
        for ip_v6, result in IP_V6_DATA.items():
            if result:
                self.assertIsNotNone(re.match(ip_v6_pattern, ip_v6, re.VERBOSE | re.IGNORECASE | re.DOTALL))
            else:
                self.assertIsNone(re.match(ip_v6_pattern, ip_v6, re.VERBOSE | re.IGNORECASE | re.DOTALL))

    def test_hex_value_pattern(self):
        hex_pattern = self.patterns.HEX_VALUE
        hex_value = '#a3c113'
        self.assertTrue(re.match(hex_pattern, hex_value))

    def test_slug_pattern(self):
        slug_pattern = self.patterns.SLUG
        slug = 'greatest-slug-ever'
        self.assertTrue(re.match(slug_pattern, slug))

    def test_bitcoin_address(self):
        bitcoin_pattern = self.patterns.BITCOIN_ADDRESS
        address = '1BoatSLRHtKNngkdXEeobR76b53LETtpyT'
        self.assertTrue(re.match(bitcoin_pattern, address))

    def test_yandex_money_pattern(self):
        ym_pattern = self.patterns.YANDEX_MONEY
        ym = '97508675463414'
        self.assertTrue(re.match(ym_pattern, ym))

    def test_longitude_pattern(self):
        longitude_pattern = self.patterns.LONGITUDE
        x = '112.1844026051194'
        self.assertTrue(re.match(longitude_pattern, x))

    def test_latitude_pattern(self):
        latitude_pattern = self.patterns.LATITUDE
        x = '-66.4214188124611'
        self.assertTrue(re.match(latitude_pattern, x))

    def test_us_phone_number_no_seperators(self):
        num_pattern = self.patterns.PHONE_NUMBER['US']
        num = '12345678901'
        self.assertTrue(re.match(num_pattern, num))

    def test_ni_phone_number_no_seperators(self):
        num_pattern = self.patterns.PHONE_NUMBER['NI']
        num = '88888888'
        self.assertTrue(re.match(num_pattern, num))

    def test_ni_phone_number_with_country_code(self):
        num_pattern = self.patterns.PHONE_NUMBER['NI']
        num = '+50588888888'
        self.assertTrue(re.match(num_pattern, num))

    def test_us_phone_number_no_country_code(self):
        num_pattern = self.patterns.PHONE_NUMBER['US']
        num = '2345678901'
        self.assertTrue(re.match(num_pattern, num))

    def test_us_phone_number_mixed_separator(self):
        num_pattern = self.patterns.PHONE_NUMBER['US']
        num = '1 (234) 567-8901'
        self.assertTrue(re.match(num_pattern, num))

    def test_us_phone_number_space_separator(self):
        num_pattern = self.patterns.PHONE_NUMBER['US']
        num = '1 234 567 8901'
        self.assertTrue(re.match(num_pattern, num))

    def test_us_phone_number_dash_separator(self):
        num_pattern = self.patterns.PHONE_NUMBER['US']
        num = '1-234-567-8901'
        self.assertTrue(re.match(num_pattern, num))

    def test_us_phone_number_negative(self):
        num_pattern = self.patterns.PHONE_NUMBER['US']
        invalid_num = '-567-8901'
        self.assertIsNone(re.match(num_pattern, invalid_num))

    def test_tw_phone_number_no_country_code(self):
        num_pattern = self.patterns.PHONE_NUMBER['TW']
        num = '0220152016'
        self.assertTrue(re.match(num_pattern, num))

    def test_tw_phone_number_plus(self):
        num_pattern = self.patterns.PHONE_NUMBER['TW']
        num = '+886912345678'
        self.assertTrue(re.match(num_pattern, num))

    def test_dk_phone_number(self):
        plate_pattern = self.patterns.PHONE_NUMBER['DK']

        base_numbers = [
            '12 23 45 67',
            '8765 4321',
            '12 555 666',
            '83155621'
        ]
        prefixes = [
            '', '+45', '+45 '
        ]
        for base_no in base_numbers:
            for prefix in prefixes:
                phone_no = prefix + base_no
                self.assertTrue(re.match(plate_pattern, phone_no), 'Danish phone number: ' + phone_no)

        invalid_numbers = [
            '1234567',
            '123456789',
            '1234-5678',
        ]
        for base_no in invalid_numbers:
            for prefix in prefixes:
                phone_no = prefix + base_no
                self.assertFalse(re.match(plate_pattern, phone_no), 'Invalid Danish phone number: ' + phone_no)

    def test_pl_phone_number_valid(self):
        num_pattern = self.patterns.PHONE_NUMBER['PL']

        valid_numbers = ['+48(42)2150000', '+48 422150000', '+48 (42)2150000', '+48 (42) 2150000',
                         '+48 (42) 215 00 00', '+48 (42) 215-00-00', '422150000', '(42) 2150000',
                         '(42) 215 00 00', '42 215 00 00', '2150000', '215 00 00', '215-00-00',
                         '123456789', '123 456 789', '123-456-789']

        for index, num in enumerate(valid_numbers):
            num_match = re.match(num_pattern, num)
            self.assertTrue(num_match, num)
            if index < 10:
                self.assertEqual(num_match.group('area'), '42')
                if index < 6:
                    self.assertEqual(num_match.group('country'), '+48')

    def test_pl_phone_number_invalid(self):
        num_pattern = self.patterns.PHONE_NUMBER['PL']

        invalid_numbers = ['', '123456', '123456789000']

        for num in invalid_numbers:
            self.assertIsNone(re.match(num_pattern, num))

    def test_tw_license_plate_3_plus_4(self):
        plate_pattern = self.patterns.LICENSE_PLATE['TW']
        plate = 'AMG-6363'
        self.assertTrue(re.match(plate_pattern, plate))

    def test_tw_license_plate_2_letters_plus_4(self):
        plate_pattern = self.patterns.LICENSE_PLATE['TW']
        plate = 'AR-1234'
        self.assertTrue(re.match(plate_pattern, plate))

    def test_tw_license_plate_2_digits_plus_4(self):
        plate_pattern = self.patterns.LICENSE_PLATE['TW']
        plate = '22-1234'
        self.assertTrue(re.match(plate_pattern, plate))

    def test_tw_license_plate_4_plus_2(self):
        plate_pattern = self.patterns.LICENSE_PLATE['TW']
        plate = '5230-RH'
        self.assertTrue(re.match(plate_pattern, plate))

    def test_tw_license_plate_3_plus_3(self):
        plate_pattern = self.patterns.LICENSE_PLATE['TW']
        plate = '297-MAY'
        self.assertTrue(re.match(plate_pattern, plate))

    def test_tw_license_plate_2_plus_3(self):
        plate_pattern = self.patterns.LICENSE_PLATE['TW']
        plate = 'XD-123'
        self.assertTrue(re.match(plate_pattern, plate))

    def test_tw_license_plate_3_plus_2(self):
        plate_pattern = self.patterns.LICENSE_PLATE['TW']
        plate = '666-XB'
        self.assertTrue(re.match(plate_pattern, plate))

    def test_tw_license_plate_2_plus_2(self):
        plate_pattern = self.patterns.LICENSE_PLATE['TW']
        plate = '01-SA'
        self.assertTrue(re.match(plate_pattern, plate))

    def test_time24h_format(self):
        pattern = self.patterns.TIME_24H_FORMAT
        time = '23:45'
        self.assertTrue(re.match(pattern, time))

        time_2 = '13:04'
        self.assertTrue(re.match(pattern, time_2))

        time_3 = '09:22'
        self.assertTrue(re.match(pattern, time_3))

    def test_iso_8601_datetime(self):
        pattern = self.patterns.ISO_8601_DATETIME
        datetime = '2014-12-05T12:30:45.123456-05:30'
        self.assertTrue(re.match(pattern, datetime))

    def test_isbn(self):
        pattern = self.patterns.ISBN

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
            self.assertTrue(re.match(pattern, isbn))

    def test_roman_numerals(self):
        pattern = self.patterns.ROMAN_NUMERALS
        numerals = (
            'X',
            'XL',
            'L',
            'XV',
            'XX',
            'XI'
        )
        for num in numerals:
            self.assertTrue(re.match(pattern, num))

    def test_french_license_plates(self):
        plate_pattern = self.patterns.LICENSE_PLATE['FR']
        valid_license_plates = (
            'AA-001-AA',
            'AA-555-AA',
            'AA-999-AA',
            'AA-001-AB',
            'AA-001-QQ',
            'AA-999-AZ',
            'AA-001-BA',
            'AA-999-ZZ',
            'AB-001-AA',
            'AZ-999-ZZ',
            'BA-001-AA',
            'ZZ-999-ZZ',
            '1 A 00',
            '999 Z 00',
            '1 AA 00',
            '999 PZ 00',
            '1 QA 00',
            '9999 ZZ 00',
            '11 AAA 00',
            '999 ZZZ 00'
        )

        invalid_license_plates = (
            'A-011-DC',
            'DE-23-DE',
            'DF-532-3D',
            '1E-123-FD',
            'A A 00',
            '999 4 00',
            '1 AA B0',
            '9E9 PZ 00',
            '1 44 00',
            '9999 ZZ 0G'
        )

        for plate in valid_license_plates:
            self.assertTrue(re.match(plate_pattern, plate))

        for plate in invalid_license_plates:
            self.assertIsNone(re.match(plate_pattern, plate))

    def test_ethereum_address(self):
        pattern = self.patterns.ETHEREUM_ADDRESS

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
            self.assertTrue(re.match(pattern, address))

        invalid_addresses = [
            "0xde0B295669a9FD93d5F28D9Ec85E40f7BAe",
            "0x85fc71ecffb0703a650f05263a3c1b0548092f32ff",
            "0xd1ade25 3d550a7eb532ac759cac7be09c2719",
            "0xda6:!65fc30803cb1fb7e6d86691e20b1826dee0",
            "0xe470b1a7d2,9c5c6f03bbaa8fa20db6d404a0c32",
            "0xf4dd5c3794f1fd0cdc0327;???a472609c806e99",
        ]
        for address in invalid_addresses:
            self.assertFalse(re.match(pattern, address))

    def test_uuid(self):
        pattern = self.patterns.UUID

        valid_uuids = [
            "54de7ea8-e01b-43c9-ad38-382d9e5f62ef",
            "54DE7EA8-E01B-43C9-AD38-382D9EFF62EF"
        ]
        for uuid in valid_uuids:
            self.assertTrue(re.match(pattern, uuid))

        invalid_uuids = [
            "54de7ea8-e01b-43c9-ad38-382d9e5f62",
            "54de7ea8-e01b-43c9-ad38-382d9e5f62xz"
        ]
        for uuid in invalid_uuids:
            self.assertFalse(re.match(pattern, uuid))

    def test_float_number(self):
        float_number_pattern = self.patterns.FLOAT_NUMBER

        valid_float_numbers = (
            '2'
            '15',
            '1.4',
            '1.45',
            '+1.45',
            '1.3e10',
            '5e5',
            '555e4',
            '555E4',
            '-555e4',
            '-555E4',
            '+1e7',
            '+.9',
            '-.9',
            '-3',
            '+3'
        )
        for number in valid_float_numbers:
            self.assertTrue(re.match(float_number_pattern, number))

        invalid_float_numbers = (
            '',
            'e',
            'E',
            '3e',
            '.1e',
            '1.1e',
            '3.5ee',
            '1.1e1e',
            '+e3',
            '+1e',
            '++1.1',
            '-+1.1',
            '-1e',
            '-',
            '+'
        )
        for number in invalid_float_numbers:
            self.assertIsNone(re.match(float_number_pattern, number))
