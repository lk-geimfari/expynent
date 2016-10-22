import re
import unittest

from expynent import (
    compiled,
    patterns
)


class PatternsTestCase(unittest.TestCase):
    def setUp(self):
        self.patterns = patterns

    def test_zip_code_pattern(self):
        us_zip = self.patterns.ZIP_CODE['US']
        self.assertTrue(re.match(us_zip, '23414'))

    def test_file_extension_pattern(self):
        ext = 'py'
        ext_pattern = self.patterns.file_extension(ext)
        filename = 'somd_e46-6f_f3343hd2s.py'
        self.assertTrue(re.match(ext_pattern, filename))

    def test_username_pattern(self):
        username_pattern = self.patterns.USERNAME
        username = 'john_snow9821'
        self.assertTrue(re.match(username_pattern, username))

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

    def test_ip_v6_pattern(self):
        ip_v6_pattern = self.patterns.IP_V6
        ip_v6 = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
        self.assertTrue(re.match(ip_v6_pattern, ip_v6))

    def test_url_pattern(self):
        url_pattern = self.patterns.URL
        url = 'https://github.com/lk-geimfari/expynent'
        self.assertTrue(re.match(url_pattern, url))

    def test_password(self):
        pass_pattern = self.patterns.password()
        password = 'some.pa$$w0rd_d'
        self.assertTrue(re.match(pass_pattern, password))

    def test_domain_pattern(self):
        domain_pattern = self.patterns.DOMAIN
        domain = 'example.com'
        self.assertTrue(re.match(domain_pattern, domain))

    def test_uppercase_pattern(self):
        uppercase_pattern = self.patterns.UPPERCASE
        upper_str = 'UPPER'
        self.assertTrue(re.match(uppercase_pattern, upper_str))

    def test_hex_value_pattern(self):
        hex_pattern = self.patterns.HEX_VALUE
        hex_value = '#a3c113'
        self.assertTrue(re.match(hex_pattern, hex_value))

    def test_slug_pattern(self):
        slug_pattern = self.patterns.SLUG
        slug = 'greatest-slug-ever'
        self.assertTrue(re.match(slug_pattern, slug))

    def test_html_tag_pattern(self):
        html_tag_pattern = self.patterns.HTML_TAG
        htm_tag = '<br></br>'
        self.assertTrue(re.match(html_tag_pattern, htm_tag))

    def test_html_js_tag_pattern(self):
        html_js_tag_pattern = self.patterns.HTML_JS_TAG
        html_js_tag = '<IMG onmouseover="window.close()">'
        self.assertTrue(re.match(html_js_tag_pattern, html_js_tag))

    def test_year_pattern(self):
        year_pattern = self.patterns.YEAR
        year = '2016'
        self.assertTrue(re.match(year_pattern, year))

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


class CompiledPatternsTestCase(unittest.TestCase):
    def setUp(self):
        self.compiled_patterns = compiled

    def test_username_pattern(self):
        username_pattern = self.compiled_patterns.username
        username = 'john_snow9821'
        self.assertTrue(username_pattern.match(username))

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

    def test_ip_v6_pattern(self):
        ip_v6_pattern = self.compiled_patterns.ip_v6
        ip_v6 = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
        self.assertTrue(ip_v6_pattern.match(ip_v6))

    def test_url_pattern(self):
        url_pattern = self.compiled_patterns.url
        url = 'https://github.com/lk-geimfari/expynent'
        self.assertTrue(url_pattern.match(url))

    def test_domain_pattern(self):
        domain_pattern = self.compiled_patterns.domain
        domain = 'example.com'
        self.assertTrue(domain_pattern.match(domain))

    def test_uppercase_pattern(self):
        uppercase_pattern = self.compiled_patterns.uppercase
        upper_str = 'UPPER'
        self.assertTrue(uppercase_pattern.match(upper_str))

    def test_hex_value_pattern(self):
        hex_pattern = self.compiled_patterns.hex_value
        hex_value = '#a3c113'
        self.assertTrue(hex_pattern.match(hex_value))

    def test_slug_pattern(self):
        slug_pattern = self.compiled_patterns.slug
        slug = 'greatest-slug-ever'
        self.assertTrue(slug_pattern.match(slug))

    def test_html_tag_pattern(self):
        html_tag_pattern = self.compiled_patterns.html_tag
        htm_tag = '<br></br>'
        self.assertTrue(html_tag_pattern.match(htm_tag))

    def test_html_js_tag_pattern(self):
        html_js_tag_pattern = self.compiled_patterns.html_js_tag
        html_js_tag = '<IMG onmouseover="window.close()">'
        self.assertTrue(html_js_tag_pattern.match(html_js_tag))

    def test_year_pattern(self):
        year_pattern = self.compiled_patterns.year
        year = '2016'
        self.assertTrue(year_pattern.match(year))

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
