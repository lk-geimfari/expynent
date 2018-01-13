from expynent import compiled
from tests.ipv6_fixtures import IP_V6_DATA
from tests.url_fixtures import *


class TestCompiledPatterns:

    def test_mac_address_pattern(self):
        mac_pattern = compiled.MAC_ADDRESS
        mac = '00:08:C7:1B:8C:02'
        assert mac_pattern.match(mac)

    def test_credit_card_pattern(self):
        credit_strict_pattern = compiled.CREDIT_CARD_STRICT
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
            assert credit_strict_pattern.match(validpat)
        # Test non-strict patern.
        credit_pattern = compiled.CREDIT_CARD
        for validpat in valid_pats.union(nonstrict_pats):
            assert credit_pattern.match(validpat)

        # Test invalid.txt patterns for strict.
        for invalidpat in invalid_pats.union(nonstrict_pats):
            assert not credit_strict_pattern.match(invalidpat)

        # Test invalid.txt patterns for non-strict.
        for invalidpat in invalid_pats:
            assert not credit_pattern.match(invalidpat)

    def test_ip_v4_pattern(self):
        ip_v4_pattern = compiled.IP_V4
        ip_v4 = '209.18.181.23'
        assert ip_v4_pattern.match(ip_v4)

    def test_ip_v6_pattern(self):
        ip_v6_pattern = compiled.IP_V6
        for ip_v6, result in IP_V6_DATA.items():
            if result:
                assert ip_v6_pattern.match(ip_v6) is not None
            else:
                assert ip_v6_pattern.match(ip_v6) is None

    def test_hex_value_pattern(self):
        hex_pattern = compiled.HEX_VALUE
        hex_value = '#a3c113'
        assert hex_pattern.match(hex_value)

    def test_slug_pattern(self):
        slug_pattern = compiled.SLUG
        slug = 'greatest-slug-ever'
        assert slug_pattern.match(slug)

    def test_bitcoin_pattern(self):
        bitcoin_pattern = compiled.BITCOIN_ADDRESS
        address = '1BoatSLRHtKNngkdXEeobR76b53LETtpyT'
        assert bitcoin_pattern.match(address)

    def test_yandex_money_pattern(self):
        ym_pattern = compiled.YANDEX_MONEY
        ym = '97508675463414'
        assert ym_pattern.match(ym)

    def test_longitude_pattern(self):
        longitude_pattern = compiled.LONGITUDE
        x = '112.1844026051194'
        assert longitude_pattern.match(x)

    def test_latitude_pattern(self):
        latitude_pattern = compiled.LATITUDE
        x = '-66.4214188124611'
        assert latitude_pattern.match(x)

    def test_iso_8601_datetime(self):
        iso_pattern = compiled.ISO_8601_DATETIME
        datetime = '2014-12-05T12:30:45.123456-05:30'
        assert iso_pattern.match(datetime)

        _md = iso_pattern.match(datetime)
        as_dict = _md.groupdict()

        assert isinstance(as_dict, dict)

        assert '2014' == as_dict['year']
        assert '45.123456' == as_dict['sec']
        assert '05' == as_dict['mday']
        assert '30' == as_dict['min']
        assert '12' == as_dict['mon']
        assert '12' == as_dict['hour']

    def test_time24h_format(self):
        pattern = compiled.TIME_24H_FORMAT
        time = '23:45'
        assert pattern.match(time)

        time_2 = '13:04'
        assert pattern.match(time_2)

        time_3 = '09:22'
        assert pattern.match(time_3)

    def test_isbn(self):
        pattern = compiled.ISBN

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
            assert pattern.match(isbn)

    def test_roman_numerals(self):
        pattern = compiled.ROMAN_NUMERALS
        numerals = (
            'X',
            'XL',
            'L',
            'XV',
            'XX',
            'XI'
        )
        for num in numerals:
            assert pattern.match(num)

    def test_url(self):
        pattern = compiled.URL

        for url in VALID_URLS:
            assert pattern.match(url)

        for invalid_url in INVALID_URLS:
            assert not pattern.match(invalid_url)

    def test_ethereum_address(self):
        pattern = compiled.ETHEREUM_ADDRESS

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
            assert pattern.match(address)

        invalid_addresses = [
            "0xde0B295669a9FD93d5F28D9Ec85E40f7BAe",
            "0x85fc71ecffb0703a650f05263a3c1b0548092f32ff",
            "0xd1ade25 3d550a7eb532ac759cac7be09c2719",
            "0xda6:!65fc30803cb1fb7e6d86691e20b1826dee0",
            "0xe470b1a7d2,9c5c6f03bbaa8fa20db6d404a0c32",
            "0xf4dd5c3794f1fd0cdc0327;???a472609c806e99",
        ]
        for address in invalid_addresses:
            assert not pattern.match(address)

    def test_uuid(self):
        pattern = compiled.UUID

        valid_uuids = [
            "54de7ea8-e01b-43c9-ad38-382d9e5f62ef",
            "54DE7EA8-E01B-43C9-AD38-382D9EFF62EF"
        ]
        for uuid in valid_uuids:
            assert pattern.match(uuid)

        invalid_uuids = [
            "54de7ea8-e01b-43c9-ad38-382d9e5f62",
            "54de7ea8-e01b-43c9-ad38-382d9e5f62xz"
        ]
        for uuid in invalid_uuids:
            assert not pattern.match(uuid)

    def test_float_number(self):
        pattern = compiled.FLOAT_NUMBER

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
            assert pattern.match(number)

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
            assert pattern.match(number) is None

    def test_pesel(self):
        pattern = compiled.PESEL

        assert pattern.match('44051401458')

        invalid_pesels = ['44751401458', '4475140145', '447514014580']
        for pesel in invalid_pesels:
            assert not pattern.match(pesel)
