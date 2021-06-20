INITIAL_TEXT = 'Beginning of Test!'
NONMATCHING_CODE = 'Example of non-matching code: '
MATCHING_CODE = 'Example of matching code: '
FINAL_TEXT = 'End of Test!'

ZIP_CODE_DATA = {
    "AD":{
        "Matching Zip Code": """
        {INITIAL_TEXT}
        {MATCHING_CODE}AD290
        {FINAL_TEXT}""",
        "Non-Matching Zip Code": """
        {INITIAL_TEXT}
        {NONMATCHING_CODE}AD922 ::: 344 ::: AD2345 ::: AD 123
        {FINAL_TEXT}""",
        "Expected Outcomes":["AD290"],
    },
    "AM":{
        "Matching Zip Code": """
        {INITIAL_TEXT}
        {MATCHING_CODE}371234 ::: 0123
        {FINAL_TEXT}""",
        "Non-Matching Zip Code": """
        {INITIAL_TEXT}
        {NONMATCHING_CODE}37 7234 ::: 471234 ::: 5100 ::: 37123 ::: A123
        {FINAL_TEXT}""",
        "Expected Outcomes":["371234", "0123"],
    },
    "AR":{
        "Matching Zip Code": """
        {INITIAL_TEXT}
        {MATCHING_CODE}C1473GTH
        {FINAL_TEXT}""",
        "Non-Matching Zip Code": """
        {INITIAL_TEXT}
        {NONMATCHING_CODE}C1414 ::: 1414 ::: I1414 ::: I1414GRT ::: C14145BTH ::: C14145BT ::: C134BTH
        {FINAL_TEXT}""",
        "Expected Outcomes":["C1473GTH"],
    },
    "AS":{
        "Matching Zip Code": """
        {INITIAL_TEXT}
        {MATCHING_CODE}96799
        {FINAL_TEXT}""",
        "Non-Matching Zip Code": """
        {INITIAL_TEXT}
        {NONMATCHING_CODE}96798 ::: 967 ::: 967 99
        {FINAL_TEXT}""",
        "Expected Outcomes":["96799"],
    },
    "AT":{
        "Matching Zip Code": """
        {INITIAL_TEXT}
        {MATCHING_CODE}9782
        {FINAL_TEXT}""",
        "Non-Matching Zip Code": """
        {INITIAL_TEXT}
        {NONMATCHING_CODE}0782 ::: 978 ::: 97 82
        {FINAL_TEXT}""",
        "Expected Outcomes":["9782"],
    },
    "AX":{
        "Matching Zip Code": """
        {INITIAL_TEXT}
        {MATCHING_CODE}22140
        {FINAL_TEXT}""",
        "Non-Matching Zip Code": """
        {INITIAL_TEXT}
        {NONMATCHING_CODE}22040 ::: 23140 ::: 22 140
        {FINAL_TEXT}""",
        "Expected Outcomes":["22140"],
    },
    "BB":{
        "Matching Zip Code": """
        {INITIAL_TEXT}
        {MATCHING_CODE}BB11002
        {FINAL_TEXT}""",
        "Non-Matching Zip Code": """
        {INITIAL_TEXT}
        {NONMATCHING_CODE}17002 ::: BB 17002 ::: BB1700 ::: BB37002
        {FINAL_TEXT}""",
        "Expected Outcomes":["BB11002"],
    },
    "BH":{
        "Matching Zip Code": """
        {INITIAL_TEXT}
        {MATCHING_CODE}1032 ::: 454
        {FINAL_TEXT}""",
        "Non-Matching Zip Code": """
        {INITIAL_TEXT}
        {NONMATCHING_CODE}4032 ::: 154 ::: 24
        {FINAL_TEXT}""",
        "Expected Outcomes":["1032", "454"],
    },
    "BM":{
        "Matching Zip Code": """
        {INITIAL_TEXT}
        {MATCHING_CODE}CR 01 ::: GE 01 ::: GE CX ::: GE 01 :: CR01 ::: GECX
        {FINAL_TEXT}""",
        "Non-Matching Zip Code": """
        {INITIAL_TEXT}
        {NONMATCHING_CODE}AB 01 ::: CR 012 ::: AB01 ::: GECY
        {FINAL_TEXT}""",
        "Expected Outcomes":["CR 01", "GE 01", "GE CX", "GE 01", "CR01", "GECX"],
    },
    "BN":{
        "Matching Zip Code": """
        {INITIAL_TEXT}
        {MATCHING_CODE}KF4138 ::: PD1151 ::: PB1751 ::: BS8211
        {FINAL_TEXT}""",
        "Non-Matching Zip Code": """
        {INITIAL_TEXT}
        {NONMATCHING_CODE}KF5138 ::: PD4151 ::: PB3751 ::: BS7211
        {FINAL_TEXT}""",
        "Expected Outcomes":["KF4138", "PD1151", "PB1751", "BS8211"],
    },
    "BR":{
        "Matching Zip Code": """
        {INITIAL_TEXT}
        {MATCHING_CODE}09999-999 
        {FINAL_TEXT}""",
        "Non-Matching Zip Code": """
        {INITIAL_TEXT}
        {NONMATCHING_CODE}A09999-999 ::: A9999-999
        {FINAL_TEXT}""",
        "Expected Outcomes":["09999-999"],
    },
    "DE":{
        "Matching Zip Code": """
        {INITIAL_TEXT}
        {MATCHING_CODE}W-1000 ::: O-1030 ::: 04357
        {FINAL_TEXT}""",
        "Non-Matching Zip Code": """
        {INITIAL_TEXT}
        {NONMATCHING_CODE}W-0300 ::: O-0430 ::: 143572 ::: A04357
        {FINAL_TEXT}""",
        "Expected Outcomes":["W-1000", "O-1030", "04357"],
    },
    "EC":{
        "Matching Zip Code": """
        {INITIAL_TEXT}
        {MATCHING_CODE}200151 ::: A1234B ::: CR200151
        {FINAL_TEXT}""",
        "Non-Matching Zip Code": """
        {INITIAL_TEXT}
        {NONMATCHING_CODE}2001517::: A12345B ::: CR2001513 ::: A 1234 B
        {FINAL_TEXT}""",
        "Expected Outcomes":["200151", "A1234B", "CR200151"],
    },
    "GF":{
        "Matching Zip Code": """
        {INITIAL_TEXT}
        {MATCHING_CODE}97389 CEDEX ::: 97300 ::: 97391 CEDEX2 ::: 97389CEDEX ::: 97389CEDEX2 ::: 97386 CEDEX 2
        {FINAL_TEXT}""",
        "Non-Matching Zip Code": """
        {INITIAL_TEXT}
        {NONMATCHING_CODE}97389CDEX::: 87300 ::: 973001 ::: 97389CDEX2
        {FINAL_TEXT}""",
        "Expected Outcomes":["97389 CEDEX", "97300", "97391 CEDEX2", "97389CEDEX", "97389CEDEX2", "97386 CEDEX 2"],
    },
}