# RegEx pattern for matching zip code.
# Using:
#     - us_zip = ZIP_CODE['US']
ZIP_CODE = {
    'AD': 'AD\d{3}',
    'AM': '(37)?\d{4}',
    'AR': '([A-HJ-NP-Z])?\d{4}([A-Z]{3})?',
    'AS': '96799',
    'AT': '\d{4}',
    'AU': '\d{4}',
    'AX': '22\d{3}',
    'AZ': '\d{4}',
    'BA': '\d{5}',
    'BB': '(BB\d{5})?',
    'BD': '\d{4}',
    'BE': '\d{4}',
    'BG': '\d{4}',
    'BH': '((1[0-2]|[2-9])\d{2})?',
    'BM': '[A-Z]{2}[ ]?[A-Z0-9]{2}',
    'BN': '[A-Z]{2}[ ]?\d{4}',
    'BR': '\d{5}[\-]?\d{3}',
    'BY': '\d{6}',
    'CA': '^[A-Z]\d[A-Z] ?\d[A-Z]\d$',
    'CC': '6799',
    'CH': '\d{4}',
    'CK': '\d{4}',
    'CL': '\d{7}',
    'CN': '[1-9]\d{5}',
    'CR': '\d{4,5}|\d{3}-\d{4}',
    'CS': '\d{5}',
    'CV': '\d{4}',
    'CX': '6798',
    'CY': '\d{4}',
    'CZ': '\d{3}[ ]?\d{2}',
    'DE': '\d{5}',
    'DK': '\d{4}',
    'DO': '\d{5}',
    'DZ': '\d{5}',
    'EC': '([A-Z]\d{4}[A-Z]|(?:[A-Z]{2})?\d{6})?',
    'EE': '\d{5}',
    'EG': '\d{5}',
    'ES': '\d{5}',
    'ET': '\d{4}',
    'FI': '\d{5}',
    'FO': '\d{3}',
    'FR': '\d{2}[ ]?\d{3}',
    'GE': '\d{4}',
    'GF': '9[78]3\d{2}',
    'GL': '39\d{2}',
    'GN': '\d{3}',
    'GP': '9[78][01]\d{2}',
    'GR': '\d{3}[ ]?\d{2}',
    'GS': 'SIQQ 1ZZ',
    'GT': '\d{5}',
    'GW': '\d{4}',
    'HM': '\d{4}',
    'HN': '(?:\d{5})?',
    'HR': '\d{5}',
    'HT': '\d{4}',
    'HU': '\d{4}',
    'ID': '\d{5}',
    'IL': '\d{5}',
    'IN': '\d{6}',
    'IO': 'BBND 1ZZ',
    'IQ': '\d{5}',
    'IS': '\d{3}',
    'IT': '\d{5}',
    'JO': '\d{5}',
    'JP': '\d{3}-\d{4}',
    'KE': '\d{5}',
    'KG': '\d{6}',
    'KH': '\d{5}',
    'KR': '\d{3}[\-]\d{3}',
    'KW': '\d{5}',
    'KZ': '\d{6}',
    'LA': '\d{5}',
    'LK': '\d{5}',
    'LR': '\d{4}',
    'LS': '\d{3}',
    'LT': '\d{5}',
    'LU': '\d{4}',
    'LV': '\d{4}',
    'MA': '\d{5}',
    'MC': '980\d{2}',
    'MD': '\d{4}',
    'ME': '8\d{4}',
    'MG': '\d{3}',
    'MK': '\d{4}',
    'MN': '\d{6}',
    'MQ': '9[78]2\d{2}',
    'MT': '[A-Z]{3}[ ]?\d{2,4}',
    'MU': '(\d{3}[A-Z]{2}\d{3})?',
    'MV': '\d{5}',
    'MX': '\d{5}',
    'MY': '\d{5}',
    'NC': '988\d{2}',
    'NE': '\d{4}',
    'NF': '2899',
    'NG': '(\d{6})?',
    'NI': '((\d{4}-)?\d{3}-\d{3}(-\d{1})?)?',
    'NL': '\d{4}[ ]?[A-Z]{2}',
    'NO': '\d{4}',
    'NP': '\d{5}',
    'NZ': '\d{4}',
    'OM': '(PC )?\d{3}',
    'PF': '987\d{2}',
    'PG': '\d{3}',
    'PH': '\d{4}',
    'PK': '\d{5}',
    'PL': '\d{2}-\d{3}',
    'PM': '9[78]5\d{2}',
    'PN': 'PCRN 1ZZ',
    'PR': '00[679]\d{2}([ \-]\d{4})?',
    'PT': '\d{4}([\-]\d{3})?',
    'PW': '96940',
    'PY': '\d{4}',
    'RE': '9[78]4\d{2}',
    'RO': '\d{6}',
    'RS': '\d{6}',
    'RU': '\d{6}',
    'SA': '\d{5}',
    'SE': '\d{3}[ ]?\d{2}',
    'SG': '\d{6}',
    'SH': '(ASCN|STHL) 1ZZ',
    'SI': '\d{4}',
    'SJ': '\d{4}',
    'SK': '\d{3}[ ]?\d{2}',
    'SM': '4789\d',
    'SN': '\d{5}',
    'SO': '\d{5}',
    'SZ': '[HLMS]\d{3}',
    'TC': 'TKCA 1ZZ',
    'TH': '\d{5}',
    'TJ': '\d{6}',
    'TM': '\d{6}',
    'TN': '\d{4}',
    'TR': '\d{5}',
    'TW': '\d{3}(\d{2})?',
    'UA': '\d{5}',
    'US': '\d{5}([ \-]\d{4})?',
    'UY': '\d{5}',
    'UZ': '\d{6}',
    'VA': '00120',
    'VE': '\d{4}',
    'WF': '986\d{2}',
    'XK': '\d{5}',
    'YT': '976\d{2}',
    'YU': '\d{5}',
    'ZA': '\d{4}',
    'ZM': '\d{5}'
}

# Pattern to match credit card.
# This will accept patterns like:
# XXXXXXXXXXXXXXXX, XXXX-XXXX XXXX-XXXX, XXXX XXXX-XXXX XXXX,
# ...or the pattern that CREDIT_CARD_STRICT matches.
CREDIT_CARD = '^(\d{4}[-\s]?){3}\d{4}$'

# RegEx pattern for matching a credit card that must be in the form of:
# XXXXXXXXXXXX, XXXX XXXX XXXX XXXX, or XXXX-XXXX-XXXX-XXXX
CREDIT_CARD_STRICT = '^((\d{4}){3}|(\d{4}-){3}|(\d{4}\s){3})\d{4}$'

# RegEx pattern for matching email address
EMAIL_ADDRESS = "([A-Za-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"

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
    'NI': '(\+?505)?\d{8}',
    'DK': r'^(?:\+45)?(\s*\d){8}$',
    # RegeEx pattern to match Polish phone numbers (both geographic and mobile ones)
    'PL': r'^(?P<country>\+?48)?\W*\(?(?P<area>\d{2})?\)?\W*'
          r'(?P<phone>\d{3}(?:\W*(?:\d{2}|\d{3})){2})$'
}

# List of RegEx patterns for license plates
LICENSE_PLATE = {
    # Regex pattern to match Taiwanese license plates
    'TW': r'(^[A-Z0-9]{2,3}-\d{2,4}$)|(^\d{2,3}-[A-Z0-9]{2,3}$)|(^\d{4}-[A-Z0-9]{2}$)|',
    # Regex pattern to match French license plates
    'FR': r'(^[A-Z]{2}-\d{3}-[A-Z]{2}$)|(^\d{1,4}\s[A-Z]{1,3}\s\d{2}$)'
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
