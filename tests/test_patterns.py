import re
import unittest
from expynent import patterns


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
        credit_pattern = self.patterns.CREDIT_CARD
        credit_card = '3519 2073 7960 3241'
        self.assertTrue(re.match(credit_pattern, credit_card))

        credit_card = '3519-2073-7960-3241'
        self.assertTrue(re.match(credit_pattern, credit_card))

        credit_card = '3519207379603241'
        self.assertTrue(re.match(credit_pattern, credit_card))

    def test_ip_v4_pattern(self):
        ip_v4_pattern = self.patterns.IP_V4
        ip_v4 = '209.18.181.23'
        self.assertTrue(re.match(ip_v4_pattern, ip_v4))

    # def test_ip_v6_pattern(self):
    #     ip_v6_pattern = self.patterns.IP_V6
    #     ip_v6 = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
    #     self.assertTrue(re.match(ip_v6_pattern, ip_v6))

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
