# -*- coding: utf-8 -*-
# RegEx pattern for matching zip code.
# Using:
#     - us_zip = ZIP_CODE['US']
ZIP_CODE = {
    'AD': r'AD\d{3}',
    'AM': r'(37)?\d{4}',
    'AR': r'([A-HJ-NP-Z])?\d{4}([A-Z]{3})?',
    'AS': r'96799',
    'AT': r'\d{4}',
    'AU': r'\d{4}',
    'AX': r'22\d{3}',
    'AZ': r'\d{4}',
    'BA': r'\d{5}',
    'BB': r'(BB\d{5})?',
    'BD': r'\d{4}',
    'BE': r'\d{4}',
    'BG': r'\d{4}',
    'BH': r'((1[0-2]|[2-9])\d{2})?',
    'BM': r'[A-Z]{2}[ ]?[A-Z0-9]{2}',
    'BN': r'[A-Z]{2}[ ]?\d{4}',
    'BR': r'\d{5}[\-]?\d{3}',
    'BY': r'\d{6}',
    'CA': r'^[A-Z]\d[A-Z] ?\d[A-Z]\d$',
    'CC': r'6799',
    'CH': r'\d{4}',
    'CK': r'\d{4}',
    'CL': r'\d{7}',
    'CN': r'[1-9]\d{5}',
    'CR': r'\d{4,5}|\d{3}-\d{4}',
    'CS': r'\d{5}',
    'CV': r'\d{4}',
    'CX': r'6798',
    'CY': r'\d{4}',
    'CZ': r'\d{3}[ ]?\d{2}',
    'DE': r'\d{5}',
    'DK': r'\d{4}',
    'DO': r'\d{5}',
    'DZ': r'\d{5}',
    'EC': r'([A-Z]\d{4}[A-Z]|(?:[A-Z]{2})?\d{6})?',
    'EE': r'\d{5}',
    'EG': r'\d{5}',
    'ES': r'\d{5}',
    'ET': r'\d{4}',
    'FI': r'\d{5}',
    'FO': r'\d{3}',
    'FR': r'\d{2}[ ]?\d{3}',
    'GE': r'\d{4}',
    'GF': r'9[78]3\d{2}',
    'GL': r'39\d{2}',
    'GN': r'\d{3}',
    'GP': r'9[78][01]\d{2}',
    'GR': r'\d{3}[ ]?\d{2}',
    'GS': r'SIQQ 1ZZ',
    'GT': r'\d{5}',
    'GW': r'\d{4}',
    'HM': r'\d{4}',
    'HN': r'(?:\d{5})?',
    'HR': r'\d{5}',
    'HT': r'\d{4}',
    'HU': r'\d{4}',
    'ID': r'\d{5}',
    'IL': r'\d{5}',
    'IN': r'\d{6}',
    'IO': r'BBND 1ZZ',
    'IQ': r'\d{5}',
    'IS': r'\d{3}',
    'IT': r'\d{5}',
    'JO': r'\d{5}',
    'JP': r'\d{3}-\d{4}',
    'KE': r'\d{5}',
    'KG': r'\d{6}',
    'KH': r'\d{5}',
    'KR': r'\d{3}[\-]\d{3}',
    'KW': r'\d{5}',
    'KZ': r'\d{6}',
    'LA': r'\d{5}',
    'LK': r'\d{5}',
    'LR': r'\d{4}',
    'LS': r'\d{3}',
    'LT': r'\d{5}',
    'LU': r'\d{4}',
    'LV': r'\d{4}',
    'MA': r'\d{5}',
    'MC': r'980\d{2}',
    'MD': r'\d{4}',
    'ME': r'8\d{4}',
    'MG': r'\d{3}',
    'MK': r'\d{4}',
    'MN': r'\d{6}',
    'MQ': r'9[78]2\d{2}',
    'MT': r'[A-Z]{3}[ ]?\d{2,4}',
    'MU': r'(\d{3}[A-Z]{2}\d{3})?',
    'MV': r'\d{5}',
    'MX': r'\d{5}',
    'MY': r'\d{5}',
    'NC': r'988\d{2}',
    'NE': r'\d{4}',
    'NF': r'2899',
    'NG': r'(\d{6})?',
    'NI': r'((\d{4}-)?\d{3}-\d{3}(-\d{1})?)?',
    'NL': r'\d{4}[ ]?[A-Z]{2}',
    'NO': r'\d{4}',
    'NP': r'\d{5}',
    'NZ': r'\d{4}',
    'OM': r'(PC )?\d{3}',
    'PF': r'987\d{2}',
    'PG': r'\d{3}',
    'PH': r'\d{4}',
    'PK': r'\d{5}',
    'PL': r'\d{2}-\d{3}',
    'PM': r'9[78]5\d{2}',
    'PN': r'PCRN 1ZZ',
    'PR': r'00[679]\d{2}([ \-]\d{4})?',
    'PT': r'\d{4}([\-]\d{3})?',
    'PW': r'96940',
    'PY': r'\d{4}',
    'RE': r'9[78]4\d{2}',
    'RO': r'\d{6}',
    'RS': r'\d{6}',
    'RU': r'\d{6}',
    'SA': r'\d{5}',
    'SE': r'\d{3}[ ]?\d{2}',
    'SG': r'\d{6}',
    'SH': r'(ASCN|STHL) 1ZZ',
    'SI': r'\d{4}',
    'SJ': r'\d{4}',
    'SK': r'\d{3}[ ]?\d{2}',
    'SM': r'4789\d',
    'SN': r'\d{5}',
    'SO': r'\d{5}',
    'SZ': r'[HLMS]\d{3}',
    'TC': r'TKCA 1ZZ',
    'TH': r'\d{5}',
    'TJ': r'\d{6}',
    'TM': r'\d{6}',
    'TN': r'\d{4}',
    'TR': r'\d{5}',
    'TW': r'\d{3}(\d{2})?',
    'UA': r'\d{5}',
    'US': r'\d{5}([ \-]\d{4})?',
    'UY': r'\d{5}',
    'UZ': r'\d{6}',
    'VA': r'00120',
    'VE': r'\d{4}',
    'WF': r'986\d{2}',
    'XK': r'\d{5}',
    'YT': r'976\d{2}',
    'YU': r'\d{5}',
    'ZA': r'\d{4}',
    'ZM': r'\d{5}'
}

# Pattern to match Canadian postal codes
# Examples A1B 2C3, a1b 2c3, A1b2C3
CANADA_POSTAL_CODE = r'^[A-CEG-HJ-NPR-TVXYa-ceg-hj-npr-tvxy][0-9][A-CEG-HJ-NPR-TV-Za-ceg-hj-npr-tv-z] ?[0-9][A-CEG-HJ-NPR-TV-Za-ceg-hj-npr-tv-z][0-9]$'

# Pattern to match credit card.
# This will accept patterns like:
# XXXXXXXXXXXXXXXX, XXXX-XXXX XXXX-XXXX, XXXX XXXX-XXXX XXXX,
# ...or the pattern that CREDIT_CARD_STRICT matches.
CREDIT_CARD = r'^(\d{4}[-\s]?){3}\d{4}$'

# RegEx pattern for matching a credit card that must be in the form of:
# XXXXXXXXXXXX, XXXX XXXX XXXX XXXX, or XXXX-XXXX-XXXX-XXXX
CREDIT_CARD_STRICT = r'^((\d{4}){3}|(\d{4}-){3}|(\d{4}\s){3})\d{4}$'

# RegEx pattern for matching email address
EMAIL_ADDRESS = r"([A-Za-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)"

# RegEx pattern for matching IPv4 and IPv6 addresses.
IP_V4 = r"^{0}\.{0}\.{0}\.{0}$".format(r"([01]?\d{1,2}|2(5[0-5]|[0-4]\d))")

IP_V6 = r"""^
     \s* # Leading whitespace
     # Zero-width lookaheads to reject too many quartets
     (?:
        # 6 quartets, ending IPv4 address; no wildcards
        (?:[0-9a-f]{1,4}(?::(?!:))){6}
             (?:25[0-4]|2[0-4]\d|1\d\d|[1-9]\d|\d)
        (?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}
      |
        # 0-5 quartets, wildcard, ending IPv4 address
        (?:(?:[0-9a-f]{1,4}(?::(?!:))){0,4}[0-9a-f]{1,4})?
        (?:::(?!:))
             (?:25[0-4]|2[0-4]\d|1\d\d|[1-9]\d|\d)
        (?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}
      |
        # 0-4 quartets, wildcard, 0-1 quartets, ending IPv4 address
        (?:(?:[0-9a-f]{1,4}(?::(?!:))){0,3}[0-9a-f]{1,4})?
        (?:::(?!:))
        (?:[0-9a-f]{1,4}(?::(?!:)))?
             (?:25[0-4]|2[0-4]\d|1\d\d|[1-9]\d|\d)
        (?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}
      |
        # 0-3 quartets, wildcard, 0-2 quartets, ending IPv4 address
        (?:(?:[0-9a-f]{1,4}(?::(?!:))){0,2}[0-9a-f]{1,4})?
        (?:::(?!:))
        (?:[0-9a-f]{1,4}(?::(?!:))){0,2}
             (?:25[0-4]|2[0-4]\d|1\d\d|[1-9]\d|\d)
        (?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}
      |
        # 0-2 quartets, wildcard, 0-3 quartets, ending IPv4 address
        (?:(?:[0-9a-f]{1,4}(?::(?!:))){0,1}[0-9a-f]{1,4})?
        (?:::(?!:))
        (?:[0-9a-f]{1,4}(?::(?!:))){0,3}
             (?:25[0-4]|2[0-4]\d|1\d\d|[1-9]\d|\d)
        (?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}
      |
        # 0-1 quartets, wildcard, 0-4 quartets, ending IPv4 address
        (?:[0-9a-f]{1,4}){0,1}
        (?:::(?!:))
        (?:[0-9a-f]{1,4}(?::(?!:))){0,4}
             (?:25[0-4]|2[0-4]\d|1\d\d|[1-9]\d|\d)
        (?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}
      |
        # wildcard, 0-5 quartets, ending IPv4 address
        (?:::(?!:))
        (?:[0-9a-f]{1,4}(?::(?!:))){0,5}
             (?:25[0-4]|2[0-4]\d|1\d\d|[1-9]\d|\d)
        (?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}
      |
        # 8 quartets; no wildcards
        (?:[0-9a-f]{1,4}(?::(?!:))){7}[0-9a-f]{1,4}
      |
        # 0-7 quartets, wildcard
        (?:(?:[0-9a-f]{1,4}(?::(?!:))){0,6}[0-9a-f]{1,4})?
        (?:::(?!:))
      |
        # 0-6 quartets, wildcard, 0-1 quartets
        (?:(?:[0-9a-f]{1,4}(?::(?!:))){0,5}[0-9a-f]{1,4})?
        (?:::(?!:))
        (?:[0-9a-f]{1,4})?
      |
        # 0-5 quartets, wildcard, 0-2 quartets
        (?:(?:[0-9a-f]{1,4}(?::(?!:))){0,4}[0-9a-f]{1,4})?
        (?:::(?!:))
        (?:(?:[0-9a-f]{1,4}(?::(?!:))){0,1}[0-9a-f]{1,4})?
      |
        # 0-4 quartets, wildcard, 0-3 quartets
        (?:(?:[0-9a-f]{1,4}(?::(?!:))){0,3}[0-9a-f]{1,4})?
        (?:::(?!:))
        (?:(?:[0-9a-f]{1,4}(?::(?!:))){0,2}[0-9a-f]{1,4})?
      |
        # 0-3 quartets, wildcard, 0-4 quartets
        (?:(?:[0-9a-f]{1,4}(?::(?!:))){0,2}[0-9a-f]{1,4})?
        (?:::(?!:))
        (?:(?:[0-9a-f]{1,4}(?::(?!:))){0,3}[0-9a-f]{1,4})?
      |
        # 0-2 quartets, wildcard, 0-5 quartets
        (?:(?:[0-9a-f]{1,4}(?::(?!:))){0,1}[0-9a-f]{1,4})?
        (?:::(?!:))
        (?:(?:[0-9a-f]{1,4}(?::(?!:))){0,4}[0-9a-f]{1,4})?
      |
        # 0-1 quartets, wildcard, 0-6 quartets
        (?:[0-9a-f]{1,4})?
        (?:::(?!:))
        (?:(?:[0-9a-f]{1,4}(?::(?!:))){0,5}[0-9a-f]{1,4})?
      |
        # wildcard, 0-7 quartets
        (?:::(?!:))
        (?:(?:[0-9a-f]{1,4}(?::(?!:))){0,6}[0-9a-f]{1,4})?
     )
     (?:/(?:1(?:2[0-8]|[01]\d)|\d\d?))? # optional CIDR routing prefix (0-128)
     \s* # Trailing whitespace
    $"""

# RegEx pattern for matching MAC-address.
MAC_ADDRESS = r'^([0-9A-Fa-f]{2}[:-]){5}' \
              r'([0-9A-Fa-f]{2})$'

# RegEx pattern for matching a HEX value ie. #a3c113
HEX_VALUE = r'^#?([a-f0-9]{6}|[a-f0-9]{3})$'

# RegEx pattern that matches a SLUG ie. greatest-SLUG-ever
SLUG = r'^[a-z0-9-]+$'

BITCOIN_ADDRESS = r'(?<![a-km-zA-HJ-NP-Z0-9])[13]' \
                  r'[a-km-zA-HJ-NP-Z0-9]{26,33}(?![a-km-zA-HJ-NP-Z0-9])'

# RegEx pattern to match Y.Money.
YANDEX_MONEY = r"\d{14}"

# RegEx pattern to match LATITUDE.
LATITUDE = r'^(\+|-)?(?:90(?:(?:\.0{1,14})?)|(?:[0-9]|' \
           r'[1-8][0-9])(?:(?:\.[0-9]{1,14})?))$'

# RegEx pattern to match LONGITUDE.
LONGITUDE = r'^(\+|-)?(?:180(?:(?:\.0{1,14})?)|(?:[0-9]|[1-9]' \
            r'[0-9]|1[0-7][0-9])(?:(?:\.[0-9]{1,14})?))$'

# RegEx pattern to match IRC user strings
IRC = r'(\S*)!(\S*)@(\S*)'

# List of RegEx patterns for phone numbers by country
PHONE_NUMBER = {
    # RegEx pattern to match Bangladeshi phone number (mobile ones)
    'BD': r'^(?:\+?88)?[\s -]?01[\s -]?[15-9][\s -]?\d{8}$',
    # RegEx pattern to match French phone numbers (with & without country code)
    'FR': r'^(?:\+33|0)\d{9}$',
    # RegEx pattern to match Indian Phone numbers
    'IN': r'\d{10}',
    # RegEx pattern to match phone number from Greece
    'GR': r'(?:\+?30)? ?\d{10}',
    # Regex pattern to match phone numbers from the United States
    'US': r'(?P<countrycode>1?)[\s\(-]{0,2}(?P<areadcode>\d{3})[\s\)-]{0,2}'
          r'(?P<phoneline0>\d{3})[\s-]?(?P<phoneline1>\d{4})',
    # RegEx pattern to match Spanish phone numbers
    'ES': r'^(?:\+34|0)\d{9}$',
    # RegEx pattern to match Taiwan phone numbers
    'TW': r'^(?:\+886|0)((?:9\d{8})|(?:[2-8]\d{7,8}))$',
    'NI': r'(\+?505)?\d{8}',
    'DK': r'^(?:\+45)?(\s*\d){8}$',
    # RegeEx pattern to match Polish phone numbers (both geographic and mobile ones)
    'PL': r'^(?P<country>\+?48)?\W*\(?(?P<area>\d{2})?\)?\W*'
          r'(?P<phone>\d{3}(?:\W*(?:\d{2}|\d{3})){2})$',
    # RegEx pattern to match Russian phone numbers
    'RU': r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',
    # RegEx pattern to match Ukrainian phone numbers
    'UA': r'^(\+3|3)?8?([\- ])?\(?0[\(\- ]{0,2}\d{2}[\)\- ]{0,2}(\d{2,3}[\- ]?\d{1,2}[\- ]?\d{2,3})$'
}

# List of RegEx patterns for license plates
LICENSE_PLATE = {
    # Regex pattern to match Taiwanese license plates
    'TW': r'(^[A-Z0-9]{2,3}-\d{2,4}$)|(^\d{2,3}-[A-Z0-9]{2,3}$)|(^\d{4}-[A-Z0-9]{2}$)|',
    # Regex pattern to match French license plates
    'FR': r'(^[A-Z]{2}-\d{3}-[A-Z]{2}$)|(^\d{1,4}\s[A-Z]{1,3}\s\d{2}$)',
    # Regex pattern to match Greek license plates
    'GR': r'(^[ABEZHIKMNOPTYXΑΒΕΖΗΙΚΜΝΟΡΤΥΧ]{3}-\d{4})'
}

# RegEx pattern for matching 24 hour time format.
# Example: 23:00
TIME_24H_FORMAT = r'(24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])'

# RegEx pattern for matching datetime in ISO 8601 format.
ISO_8601_DATETIME = r'^(?P<full>((?P<year>\d{4})([/-]?(?P<mon>(0[1-9])|' \
                    r'(1[012]))([/-]?(?P<mday>(0[1-9])|' \
                    r'([12]\d)|(3[01])))?)?(?:T(?P<hour>([01][0-9])|' \
                    r'(?:2[0123]))(\:?(?P<min>[0-5][0-9])(\:?(?P<sec>[0-5][0-9]' \
                    r'([\,\.]\d{1,10})?))?)?(?:Z|([\-+](?:([01][0-9])' \
                    r'|(?:2[0123]))(\:?(?:[0-5][0-9]))?))?)?))$'

# RegEx pattern that match ISBN 10 and ISBN 13.
# Match:
#    - ISBN-13: 978-1-56619-909-4
#    - ISBN-13: 978 5 93286 159 2
#    - 978-1-56619-909-4
#    - ISBN-10: 1-56619-909-3
#    - 1-56619-909-3
#    - 978 1 56619 909 4
#    - 1 56619 909 3
ISBN = "^(?:ISBN(?:-1[03])?:? )?(?=[-0-9 ]{17}$|[-0-9X ]" \
       "{13}$|[0-9X]{10}$)(?:97[89][- ]?)?[0-9]{1,5}[- ]" \
       "?(?:[0-9]+[- ]?){2}[0-9X]$"

# RegEx pattern that matches roman numerals.
# Match:
#    - L
#    - XL
#    - XV
#    - XX
#    - XI
#    - etc.
ROMAN_NUMERALS = r'^(?=[MDCLXVI])M*(C[MD]|D?C*)(X[CL]|L?X*)(I[XV]|V?I*)$'

# http:// or https://
# domain
# localhost
# ipv4
# ipv6
# optional port
# This is regular expression from Django Web Framework
URL = r'^(?:http|ftp)s?://' \
      r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' \
      r'localhost|' \
      r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' \
      r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' \
      r'(?::\d+)?' \
      r'(?:/?|[/?]\S+)$'

# RegEx pattern that matches Ethereum address starts with 0x
# Match:
#    - 0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe
#    - 0x5ed8cee6b63b1c6afce3ad7c92f4fd7e1b8fad9f
#    - 0xfac399e49f5b6867af186390270af252e683b154
#    - 0x85fc71ecffb0703a650f05263a3c1b0548092f32
ETHEREUM_ADDRESS = r'^0x([a-zA-Z0-9]{40})$'

# RegEx pattern that matches Ethereum KECCAK-based hashes starting with 0x
# Match:
#    - 0x9b4554f8580afa24f03909efcf7a5e1e8da8ebdb7cbcd902f815aaf74381c4fe
#    - 0x9e3f46eae1f804c954ea5347af8307ec8163b3676580e0c7c524be702682a0ed
#    - 0x197d8129eeddf563e785b1593f7a476f04b3b01675fd80d7a85de554e38dbfa6
#    - 0x715c00c9d3f41a6fb936ea6d005794c7115419267247a31904b94f395e96d4ac
ETHEREUM_HASH = r'^0x([a-zA-Z0-9]{64})$'

# RegEx pattern that matches UUID's.
# Match:
#    - 54de7ea8-e01b-43c9-ad38-382d9e5f62ef
#    - 54DE7EA8-E01B-43C9-AD38-382D9EFF62EF
UUID = r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'

# RegEx pattern that matches float numbers
# Match:
#    - 1.1
#    - 3.1e10
#    - 1.2e+10
#    - 1.2e-10
#    - -1.2e-10
#    - 5.1E10
FLOAT_NUMBER = r'^[+-]?((\d\d*\.?\d*)|(\.\d+))([Ee][+-]?\d+)?$'

# RegEx pattern to match PESEL
PESEL = r'^(?P<birthdate>\d{2}[890-3]\d[0-3]\d)(\d{4})(?P<checksum>\d)$'

# ReGex pattern to match PGP fingerprint
# Match:
# FA05 36C5 8CEB B951 13EF 405A 4AB5 9C00 1B09 1337
# FA0536C58CEBB95113EF405A4AB59C001B091337
PGP_FINGERPRINT = r'^([a-fA-F0-9]{40})|(([a-fA-F0-9]{4}\ ){9}[a-fA-F0-9]{4})$'
