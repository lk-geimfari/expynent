import re
import unittest

from expynent import patterns


class PatternsTestCase(unittest.TestCase):
    def setUp(self):
        self.patterns = patterns

    def test_zip_code_pattern(self):
        us_zip = self.patterns.ZIP_CODE['US']
        self.assertTrue(re.match(us_zip, '23414'))

    def test_email_pattern(self):
        email_pattern = self.patterns.EMAIL
        email = 'someuser@example.com'
        self.assertTrue(re.match(email_pattern, email))

    def test_file_extension_pattern(self):
        ext = 'py'
        ext_pattern = self.patterns.file_extension(ext)
        filename = 'somd_e46-6f_f3343hd2s.py'
        self.assertTrue(re.match(ext_pattern, filename))

    def test_username_pattern(self):
        username_pattern = self.patterns.USERNAME
        username = 'john_snow9821'
        self.assertTrue(username_pattern, username)

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

    def test_url_pattern(self):
        url_pattern = self.patterns.URL
        url = 'https://github.com/lk-geimfari/expynent'
        self.assertTrue(re.match(url_pattern, url))

    def test_password(self):
        pass_pattern = self.patterns.password()
        password = 'some.pa$$w0rd_d'
        self.assertTrue(pass_pattern, password)
