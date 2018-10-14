import re
from expynent import patterns
from tests.ipv6_fixtures import IP_V6_DATA
from tests.ipv4_fixtures import IP_V4_DATA


def test_zip_code_pattern():
    us_zip = patterns.ZIP_CODE['US']
    assert re.match(us_zip, '23414')


def test_email_address_pattern():
    email_pattern = patterns.EMAIL_ADDRESS
    valid_emails = (
        'very.common@example.com',
        'Indeed@Strange.COM',
        'user.name+tag+sorting@example.com'
    )
    invalid_emails = (
        'Abc.example.com',
        'A@b@c@example.com',
        'john.doe@example..com'
    )

    for valid_email in valid_emails:
        assert re.match(email_pattern, valid_email)

    for invalid_email in invalid_emails:
        assert not re.match(email_pattern, invalid_email)


def test_mac_address_pattern():
    mac_pattern = patterns.MAC_ADDRESS
    mac = '00:08:C7:1B:8C:02'
    assert re.match(mac_pattern, mac)


def test_credit_card_pattern():
    credit_strict_pattern = patterns.CREDIT_CARD_STRICT
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
        assert re.match(credit_strict_pattern, validpat)
    # Test non-strict pattern.
    credit_pattern = patterns.CREDIT_CARD
    for validpat in valid_pats.union(nonstrict_pats):
        assert re.match(credit_pattern, validpat)

    # Test invalid.txt patterns for strict.
    for invalidpat in invalid_pats.union(nonstrict_pats):
        assert not re.match(credit_strict_pattern, invalidpat)

    # Test invalid.txt patterns for non-strict.
    for invalidpat in invalid_pats:
        assert not re.match(credit_pattern, invalidpat)


def test_ip_v4_pattern():
    ip_v4_pattern = patterns.IP_V4
    for ip_v4, result in IP_V4_DATA.items():
        if result:
            assert re.match(ip_v4_pattern, ip_v4,
                            re.VERBOSE | re.IGNORECASE | re.DOTALL) is not None
        else:
            assert re.match(ip_v4_pattern, ip_v4,
                            re.VERBOSE | re.IGNORECASE | re.DOTALL) is None


def test_ip_v6_pattern():
    ip_v6_pattern = patterns.IP_V6
    for ip_v6, result in IP_V6_DATA.items():
        if result:
            assert re.match(ip_v6_pattern, ip_v6,
                            re.VERBOSE | re.IGNORECASE | re.DOTALL) is not None
        else:
            assert re.match(ip_v6_pattern, ip_v6,
                            re.VERBOSE | re.IGNORECASE | re.DOTALL) is None


def test_hex_value_pattern():
    hex_pattern = patterns.HEX_VALUE
    hex_value = '#a3c113'
    assert re.match(hex_pattern, hex_value)


def test_slug_pattern():
    slug_pattern = patterns.SLUG
    slug = 'greatest-slug-ever'
    assert re.match(slug_pattern, slug)


def test_bitcoin_address():
    bitcoin_pattern = patterns.BITCOIN_ADDRESS
    address = '1BoatSLRHtKNngkdXEeobR76b53LETtpyT'
    assert re.match(bitcoin_pattern, address)


def test_yandex_money_pattern():
    ym_pattern = patterns.YANDEX_MONEY
    ym = '97508675463414'
    assert re.match(ym_pattern, ym)


def test_longitude_pattern():
    longitude_pattern = patterns.LONGITUDE
    x = '112.1844026051194'
    assert re.match(longitude_pattern, x)


def test_latitude_pattern():
    latitude_pattern = patterns.LATITUDE
    x = '-66.4214188124611'
    assert re.match(latitude_pattern, x)


def test_us_phone_number_no_seperators():
    num_pattern = patterns.PHONE_NUMBER['US']
    num = '12345678901'
    assert re.match(num_pattern, num)


def test_ni_phone_number_no_seperators():
    num_pattern = patterns.PHONE_NUMBER['NI']
    num = '88888888'
    assert re.match(num_pattern, num)


def test_ni_phone_number_with_country_code():
    num_pattern = patterns.PHONE_NUMBER['NI']
    num = '+50588888888'
    assert re.match(num_pattern, num)


def test_us_phone_number_no_country_code():
    num_pattern = patterns.PHONE_NUMBER['US']
    num = '2345678901'
    assert re.match(num_pattern, num)


def test_us_phone_number_mixed_separator():
    num_pattern = patterns.PHONE_NUMBER['US']
    num = '1 (234) 567-8901'
    assert re.match(num_pattern, num)


def test_us_phone_number_space_separator():
    num_pattern = patterns.PHONE_NUMBER['US']
    num = '1 234 567 8901'
    assert re.match(num_pattern, num)


def test_us_phone_number_dash_separator():
    num_pattern = patterns.PHONE_NUMBER['US']
    num = '1-234-567-8901'
    assert re.match(num_pattern, num)


def test_us_phone_number_negative():
    num_pattern = patterns.PHONE_NUMBER['US']
    invalid_num = '-567-8901'
    assert re.match(num_pattern, invalid_num) is None


def test_gr_phone_number_with_country_code():
    num_pattern = patterns.PHONE_NUMBER['GR']
    num = '+302101234567'
    assert re.match(num_pattern, num)


def test_gr_phone_number_no_country_code():
    num_pattern = patterns.PHONE_NUMBER['GR']
    num = '2101234567'
    assert re.match(num_pattern, num)


def test_gr_phone_number_space_separator():
    num_pattern = patterns.PHONE_NUMBER['GR']
    num = '+30 2101234567'
    assert re.match(num_pattern, num)


def test_gr_phone_number_negative():
    num_pattern = patterns.PHONE_NUMBER['GR']
    invalid_num = '+303'
    assert re.match(num_pattern, invalid_num) is None


def test_tw_phone_number_no_country_code():
    num_pattern = patterns.PHONE_NUMBER['TW']
    num = '0220152016'
    assert re.match(num_pattern, num)


def test_tw_phone_number_plus():
    num_pattern = patterns.PHONE_NUMBER['TW']
    num = '+886912345678'
    assert re.match(num_pattern, num)


def test_dk_phone_number():
    plate_pattern = patterns.PHONE_NUMBER['DK']

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
            assert re.match(plate_pattern, phone_no), \
                'Danish phone number: {}'.format(phone_no)

    invalid_numbers = [
        '1234567',
        '123456789',
        '1234-5678',
    ]
    for base_no in invalid_numbers:
        for prefix in prefixes:
            phone_no = prefix + base_no
            assert not re.match(plate_pattern, phone_no), \
                'Invalid Danish phone number: {}'.format(phone_no)


def test_pl_phone_number_valid():
    num_pattern = patterns.PHONE_NUMBER['PL']

    valid_numbers = ['+48(42)2150000', '+48 422150000', '+48 (42)2150000',
                     '+48 (42) 2150000', '+48 (42) 215 00 00',
                     '+48 (42) 215-00-00', '422150000', '(42) 2150000',
                     '(42) 215 00 00', '42 215 00 00', '2150000', '215 00 00',
                     '215-00-00', '123456789', '123 456 789', '123-456-789']

    for index, num in enumerate(valid_numbers):
        num_match = re.match(num_pattern, num)
        assert num_match, num
        if index < 10:
            assert num_match.group('area') == '42'
            if index < 6:
                assert num_match.group('country') == '+48'


def test_pl_phone_number_invalid():
    num_pattern = patterns.PHONE_NUMBER['PL']

    invalid_numbers = ['', '123456', '123456789000']

    for num in invalid_numbers:
        assert re.match(num_pattern, num) is None


def test_bd_phone_number_valid():
    num_pattern = patterns.PHONE_NUMBER['BD']

    valid_numbers = ['01924547181', "+8801924547181", "+88 016 24547181",
                     "+88-017-24547181"]

    for phone_no in valid_numbers:
        assert re.match(num_pattern, phone_no), \
            'Bangladeshi phone number: {}'.format(phone_no)


def test_ru_phone_number_valid():
    num_pattern = patterns.PHONE_NUMBER['RU']

    valid_numbers = ['+74951234567', '84951234567', '74951234567',
                     '+7 495 123 45 67', '8(926)123-45-67', '123-45-67',
                     '9261234567', '74951234567', '(495)1234567',
                     '(495) 123 45 67', '84951234567', '8-495-123-45-67',
                     '8 499 1234 234', '8 499 12 12 888', '8 499 12 555 12',
                     '8 499 123 8 123']
    for number in valid_numbers:
        num_match = re.match(num_pattern, number)
        assert num_match, number


def test_ru_phone_number_invalid():
    num_pattern = patterns.PHONE_NUMBER['RU']

    invalid_numbers = ['', '+7492323', '2323', '74951234567899']

    for number in invalid_numbers:
        assert re.match(num_pattern, number) is None


def test_ua_phone_number_valid():
    num_pattern = patterns.PHONE_NUMBER['UA']

    valid_numbers = ['+380631234567', '+38-(073)-123-45-67', '083 123 45 67',
                     '+380 (93) 123-4567', '0671234567', '0 97 123 4 123',
                     '38 096 123 45 67', '8(096)123-4567', '+38 (093) 1234567',
                     '38(096)123-45-67', '8 098 1221 567', '38(098)12-12-345',
                     '8-067-123 45-67']

    for number in valid_numbers:
        num_match = re.match(num_pattern, number)
        assert num_match, number


def test_ua_phone_number_invalid():
    num_pattern = patterns.PHONE_NUMBER['UA']

    invalid_numbers = ['', '+38063123', '0800', '38063123456789', '097123#456',
                       '+8(097)1234567']

    for number in invalid_numbers:
        assert re.match(num_pattern, number) is None


def test_tw_license_plate_3_plus_4():
    plate_pattern = patterns.LICENSE_PLATE['TW']
    plate = 'AMG-6363'
    assert re.match(plate_pattern, plate)


def test_tw_license_plate_2_letters_plus_4():
    plate_pattern = patterns.LICENSE_PLATE['TW']
    plate = 'AR-1234'
    assert re.match(plate_pattern, plate)


def test_tw_license_plate_2_digits_plus_4():
    plate_pattern = patterns.LICENSE_PLATE['TW']
    plate = '22-1234'
    assert re.match(plate_pattern, plate)


def test_tw_license_plate_4_plus_2():
    plate_pattern = patterns.LICENSE_PLATE['TW']
    plate = '5230-RH'
    assert re.match(plate_pattern, plate)


def test_tw_license_plate_3_plus_3():
    plate_pattern = patterns.LICENSE_PLATE['TW']
    plate = '297-MAY'
    assert re.match(plate_pattern, plate)


def test_tw_license_plate_2_plus_3():
    plate_pattern = patterns.LICENSE_PLATE['TW']
    plate = 'XD-123'
    assert re.match(plate_pattern, plate)


def test_tw_license_plate_3_plus_2():
    plate_pattern = patterns.LICENSE_PLATE['TW']
    plate = '666-XB'
    assert re.match(plate_pattern, plate)


def test_tw_license_plate_2_plus_2():
    plate_pattern = patterns.LICENSE_PLATE['TW']
    plate = '01-SA'
    assert re.match(plate_pattern, plate)


def test_gr_license_plate_greek_chars():
    plate_pattern = patterns.LICENSE_PLATE['GR']

    valid_plates = [
        'ABE-1234',
        'AAA-1212',
        'ΑΒΕ-1212'
    ]
    invalid_plates = [
        'ABE-12',
        'AB-1212',
        'ABE 1234',
        'ABEE=121212',
        'ΑΒΕ--1212'
    ]
    assert all(re.match(plate_pattern, plate) for plate in valid_plates)
    assert all(not re.match(plate_pattern, plate) for plate in invalid_plates)


def test_time24h_format():
    pattern = patterns.TIME_24H_FORMAT
    time = '23:45'
    assert re.match(pattern, time)

    time_2 = '13:04'
    assert re.match(pattern, time_2)

    time_3 = '09:22'
    assert re.match(pattern, time_3)


def test_iso_8601_datetime():
    pattern = patterns.ISO_8601_DATETIME
    datetime = '2014-12-05T12:30:45.123456-05:30'
    assert re.match(pattern, datetime)


def test_isbn():
    pattern = patterns.ISBN

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
        assert re.match(pattern, isbn)


def test_roman_numerals():
    pattern = patterns.ROMAN_NUMERALS
    numerals = (
        'X',
        'XL',
        'L',
        'XV',
        'XX',
        'XI'
    )
    for num in numerals:
        assert re.match(pattern, num)


def test_french_license_plates():
    plate_pattern = patterns.LICENSE_PLATE['FR']
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
        assert re.match(plate_pattern, plate)

    for plate in invalid_license_plates:
        assert re.match(plate_pattern, plate) is None


def test_ethereum_address():
    pattern = patterns.ETHEREUM_ADDRESS

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
        assert re.match(pattern, address)

    invalid_addresses = [
        "0xde0B295669a9FD93d5F28D9Ec85E40f7BAe",
        "0x85fc71ecffb0703a650f05263a3c1b0548092f32ff",
        "0xd1ade25 3d550a7eb532ac759cac7be09c2719",
        "0xda6:!65fc30803cb1fb7e6d86691e20b1826dee0",
        "0xe470b1a7d2,9c5c6f03bbaa8fa20db6d404a0c32",
        "0xf4dd5c3794f1fd0cdc0327;???a472609c806e99",
    ]
    for address in invalid_addresses:
        assert not re.match(pattern, address)


def test_uuid():
    pattern = patterns.UUID

    valid_uuids = [
        "54de7ea8-e01b-43c9-ad38-382d9e5f62ef",
        "54DE7EA8-E01B-43C9-AD38-382D9EFF62EF"
    ]
    for uuid in valid_uuids:
        assert re.match(pattern, uuid)

    invalid_uuids = [
        "54de7ea8-e01b-43c9-ad38-382d9e5f62",
        "54de7ea8-e01b-43c9-ad38-382d9e5f62xz"
    ]
    for uuid in invalid_uuids:
        assert not re.match(pattern, uuid)


def test_float_number():
    float_number_pattern = patterns.FLOAT_NUMBER

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
        assert re.match(float_number_pattern, number)

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
        assert re.match(float_number_pattern, number) is None


def test_pesel():
    pesel_pattern = patterns.PESEL

    assert re.match(pesel_pattern, '44051401458')

    invalid_pesels = ['44751401458', '4475140145', '447514014580']
    for pesel in invalid_pesels:
        assert not re.match(pesel_pattern, pesel)
