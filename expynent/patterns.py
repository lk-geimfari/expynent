# -*- coding: utf-8 -*-
# RegEx pattern for matching zip code.
# Using:
#     - us_zip = ZIP_CODE['US']
ZIP_CODE = {
    'AD': r'\bAD[1-7]\d{2}\b',
    'AM': r'(\b(37)\d{4}\b)|(\b[0-4]{1,1}\d{3}\b)',
    'AR': r'(?!\b[IO])(\b[A-Z]?\d{4,4}[A-Z]{3,3}\b)',
    'AS': r'\b96799\b',
    'AT': r'\b[1-9]\d{3}\b',
    'AU': r'\b\d{4}\b',
    'AX': r'\b22[1-9]\d{2}\b',
    'AZ': r'\b[0-8]\d{3}\b',
    'BA': r'\b[7-8]\d{4}\b',
    'BB': r'(\bBB(01|02|03|04|05|06|07|08|10|11)\d{3})\b',
    'BD': r'\b\d{4}\b',
    'BE': r'\b[1-9]\d{3}\b',
    'BG': r'\b\d{4}\b',
    'BH': r'\b((1[0-2]|[2-9])\d{2})\b',
    'BM': r'\b(CR|DD|DV|FL|HM|HS|MA|PG|SN|SB|WK)[ ]?[0-2][0-9]\b|\bGE[ ]?(CX|[0-2][0-9])\b',
    'BN': r'\b((PE|T[F,H]|B[B,C,D]|K[B,F])[1-4]|(T[C,H,A,G,B]|P[C,A,D]|B[T,G,H,J,E]|K[C,E,A])[1-3]|(KG|PB|T[D,E]|B[L,N,U,F,A,M])[1-2]|(BP1|K[H,D]1|BS8))\d{3}\b',
    'BR': r'\b\d{5}[\-]?\d{3}\b',
    'BY': r'\b(224|225|210|211|246|247|230|231|220|223|212|213)\d{3}\b',
    'CA': r'\b([A-CEGHJ-NPR-TVXY]\d[A-Z])[ ]?\d[A-Z]\d$\b',
    'CC': r'\b6799\b',
    'CH': r'\b[1-468]\d{3}\b|\b([57][0-7]|9[0-6])\d{2}\b',
    'CK': r'\b\d{4}\b',
    'CL': r'\b\d{7}\b',
    'CN': r'\b[0-9]\d{5}\b',
    'CR': r'\d{4,5}|\d{3}-\d{4}',#Is this a right format?
    'CS': r'\b\d{5}\b',
    'CV': r'\b[1-9]\d{3}\b',
    'CX': r'\b6798\b',
    'CY': r'\b[1-9]\d{3}\b',
    'CZ': r'\b\d{3}[ ]?\d{2}\b',
    'DE': r'\b(W|O)-[1-9]\d{3}\b|\b\d{5}\b',
    'DK': r'\b[1-9]\d{3}\b',
    'DO': r'\b\d{5}\b',
    'DZ': r'\b\d{5}\b',
    'EC': r'\b[A-Z]\d{4}[A-Z]\b|\b(?:[A-Z]{2})?\d{6}\b',
    'EE': r'\b[0-4]\d{4}\b',
    'EG': r'\b[1-8]\d{4}\b',
    'ES': r'\b([0-4]\d|5[0-2])\d{4}\b',
    'ET': r'\b[1-7]\d{4}\b',
    'FI': r'\b\d{5}\b',
    'FO': r'\b(FO[- ])?[1-9]\d{2}\b',
    'FR': r'\b\d{2}[ ]?\d{3}\b',
    'GE': r'\b\d{4}\b',
    'GF': r'(\b9[78]3\d{2}[ ]CEDEX[ ]?\d?\b)|(?![ ]CEDEX)(\b9[78]3\d{2}CEDEX\d?\b)|(\b9[78]3\d{2}\b)',
    'GL': r'\b39\d{2}\b',
    'GN': r'\b\d{3}\b',
    'GP': r'\b9[78][01]\d{2}\b',
    'GR': r'\b[1-8]\d{2}[ ]?\d{2}\b',
    'GS': r'\bSIQQ 1ZZ\b',
    'GT': r'\b[0-2]\d{4}\b',
    'GW': r'\b\d{4}\b',
    'HM': r'\b\d{4}\b',
    'HN': r'\b[1-5]\d{4}\b',
    'HR': r'\b(10|20|21|22|23|31|32|33|34|35|40|42|43|44|47|48|49|51|52|53)\d{3}\b',
    'HT': r'\b\d{4}\b',
    'HU': r'\b[1-9]\d{3}\b',
    'ID': r'\b[1-9]\d{4}\b',
    'IL': r'\b[1-9]\d{4}\b',
    'IN': r'\b[1-9]\d{5}\b',
    'IO': r'\bBBND 1ZZ\b',
    'IQ': r'\b(52|64|34|41|62|56|32|42|10|51|44|36|46|58|54)\d{3}\b',
    'IS': r'\b[1-9]\d{2}\b',
    'IT': r'\b\d{5}\b',
    'JO': r'\b[1-7]\d{4}\b',
    'JP': r'\b\d{3}-\d{4}\b',
    'KE': r'\b\d{5}\b',
    'KG': r'\b\d{6}\b',
    'KH': r'\b\d{5}\b',
    'KR': r'\b\d{3}[\-]\d{3}\b',
    'KW': r'\b\d{5}\b',
    'KZ': r'\b\d{6}\b',
    'LA': r'\b\d{5}\b',
    'LK': r'\b\d{5}\b',
    'LR': r'\b\d{4}\b',
    'LS': r'\b\d{3}\b',
    'LT': r'\b\d{5}\b',
    'LU': r'\b\d{4}\b',
    'LV': r'\b\d{4}\b',
    'MA': r'\b\d{5}\b',
    'MC': r'\b980\d{2}\b',
    'MD': r'\b\d{4}\b',
    'ME': r'\b8\d{4}\b',
    'MG': r'\b\d{3}\b',
    'MK': r'\b\d{4}\b',
    'MN': r'\b\d{6}\b',
    'MQ': r'\b9[78]2\d{2}\b',
    'MT': r'\b[A-Z]{3}[ ]?\d{2,4}\b',
    'MU': r'\b(\d{3}[A-Z]{2}\d{3})?\b',
    'MV': r'\b\d{5}\b',
    'MX': r'\b\d{5}\b',
    'MY': r'\b\d{5}\b',
    'NC': r'\b988\d{2}\b',
    'NE': r'\b\d{4}\b',
    'NF': r'\b2899\b',
    'NG': r'\b(\d{6})?\b',
    'NI': r'\b((\d{4}-)?\d{3}-\d{3}(-\d{1})?)?\b',
    'NL': r'\b\d{4}[ ]?[A-Z]{2}\b',
    'NO': r'\b\d{4}\b',
    'NP': r'\b\d{5}\b',
    'NZ': r'\b\d{4}\b',
    'OM': r'\b(PC )?\d{3}\b',
    'PF': r'\b987\d{2}\b',
    'PG': r'\b\d{3}\b',
    'PH': r'\b\d{4}\b',
    'PK': r'\b\d{5}\b',
    'PL': r'\b\d{2}-\d{3}\b',
    'PM': r'\b9[78]5\d{2}\b',
    'PN': r'\bPCRN 1ZZ\b',
    'PR': r'\b00[679]\d{2}([ \-]\d{4})?\b',
    'PT': r'\b\d{4}([\-]\d{3})?\b',
    'PW': r'\b96940\b',
    'PY': r'\b\d{4}\b',
    'RE': r'\b9[78]4\d{2}\b',
    'RO': r'\b\d{6}\b',
    'RS': r'\b\d{6}\b',
    'RU': r'\b\d{6}\b',
    'SA': r'\b\d{5}\b',
    'SE': r'\b\d{3}[ ]?\d{2}\b',
    'SG': r'\b\d{6}\b',
    'SH': r'\b(ASCN|STHL) 1ZZ\b',
    'SI': r'\b\d{4}\b',
    'SJ': r'\b\d{4}\b',
    'SK': r'\b\d{3}[ ]?\d{2}\b',
    'SM': r'\b4789\d\b',
    'SN': r'\b\d{5}\b',
    'SO': r'\b\d{5}\b',
    'SZ': r'\b[HLMS]\d{3}\b',
    'TC': r'\bTKCA 1ZZ\b',
    'TH': r'\b\d{5}\b',
    'TJ': r'\b\d{6}\b',
    'TM': r'\b\d{6}\b',
    'TN': r'\b\d{4}\b',
    'TR': r'\b\d{5}\b',
    'TW': r'\b\d{3}(\d{2})?\b',
    'UA': r'\b\d{5}\b',
    'US': r'\b\d{5}([ \-]\d{4})?\b',
    'UY': r'\b\d{5}\b',
    'UZ': r'\b\d{6}\b',
    'VA': r'\b00120\b',
    'VE': r'\b\d{4}\b',
    'WF': r'\b986\d{2}\b',
    'XK': r'\b\d{5}\b',
    'YT': r'\b976\d{2}\b',
    'YU': r'\b\d{5}\b',
    'ZA': r'\b\d{4}\b',
    'ZM': r'\b\d{5}\b'
}

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
    'BD': r'^(?:\+?88)?[\s -]?01[\s -]?[13-9][\s -]?\d{8}$',
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
    'GR': r'(^[ABEZHIKMNOPTYXΑΒΕΖΗΙΚΜΝΟΡΤΥΧ]{3}-\d{4})',
    # Regex pattern to match German license plates
    'DE': r'(^[A-Z]{1,3}-[A-Z]{1,2}-[1-9][0-9]{0,3}[H,E]{0,1}$)',
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
