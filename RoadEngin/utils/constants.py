# Conversions

CONV_LU = {
    'DSU_1': 1,
    'DSU_2': 2,
    'DSU_3': 3,
    'PA_1': 4,
    'PA_2': 5,
    'PA_3': 6,
    'S_1': 4,
    'S_2': 5,
    'S_3': 6,
    'FPAV': 7,
    'TRR': 8,
    'CUN': 9,
    'VEG': 10,
    'JP': 11,
    'RV': 12,
    'TS_1': 13,
    'P_AFR': 14,
    'OND_1': 15,
    'OND_2': 16,
    'OND_3': 17,
    'AB_1': 18,
    'AB_2': 19,
    'AB_3': 20,
    'AFA_1': 21,
    'AFA_2': 22,
    'HUN_1': 23,
    'HUN_2': 24,
    'AHU_1': 25,
    'AHU_2': 26,
    'AHU_3': 27,
    'PINT': 28,
    'SU': 29,
    'SOM': 30,
    'LV': 31,
    'MNF': 32,
    'MNQ': 33,
    'RM': 34,
    'CV_2': 35,
    'CV_3': 36,
    'SUM': 37,
    'EX_1': 38,
    'EX_2': 39,
    'DB_1': 40,
    'DB_2': 41,
    'DB_3': 42,
    'PLF_1': 43,
    'PLF_2': 44,
    'PLF_3': 45,
    'MISC': 46,
    'LD': 47,
    'FCL_0': 48,
    'FBD_1': 49,
    'FBD_2': 50,
    'FBD_3': 51,
    'FBD_S': 52,
    'FCL_1': 53,
    'FCL_2': 54,
    'FCL_3': 55,
    'FCL_S': 56,
    'FCT_0': 57,
    'FCT_1': 58,
    'FCT_2': 59,
    'FCT_3': 60,
    'FCT_S': 61,
    'FJT_S': 62,
    'FJL_S': 63,
    'FJL_1': 64,
    'FJL_2': 65,
    'FJL_3': 66,
    'FJT_1': 67,
    'FJT_2': 68,
    'FJT_3': 69,
    'FL_1': 70,
    'FL_2': 71,
    'FL_3': 72,
    'FL_S': 73,
    'FT_1': 74,
    'FT_2': 75,
    'FT_3': 76,
    'FT_S': 77,
    'FR_1': 78,
    'FR_2': 79,
    'FR_3': 80,
    'FR_S': 81,
    'FR_1_POL': 78,
    'FR_2_POL': 79,
    'FR_3_POL': 80,
    'FR_S_POL': 81,
    'FB_1': 82,
    'FB_2': 83,
    'FB_3': 84,
    'FB_S': 85,
    'PC_1': 86,
    'PC_2': 87,
    'PC_3': 88,
    'PC_S': 89,
    'PC_1_POL': 86,
    'PC_2_POL': 87,
    'PC_3_POL': 88,
    'PC_S_POL': 89,
    'FML_1': 90,
    'FML_2': 91,
    'FML_3': 92,
    'DC_1': 93,
    'DC_2': 94,
    'DC_3': 95,
    'P_RIG': 96,
    'P_RIG1 ': 97,
    'ALC': 98,
    'ALC_1': 99,
    'ALC_2': 100,
    'ALC_3': 101,
    'CAR': 102,
    'P_ART': 103,
    'PCH_1': 104,
    'PCH_2': 105,
    'PCH_3': 106,
    'BCH_1': 107,
    'BCH_2': 108,
    'BCH_3': 109
}

CONV_LU_INV = {
    1: 'DSU_1',
    2: 'DSU_2',
    3: 'DSU_3',
    4: 'PA_1',
    5: 'PA_2',
    6: 'PA_3',
    7: 'FPAV',
    8: 'TRR',
    9: 'CUN',
    10: 'VEG',
    11: 'JP',
    12: 'RV',
    13: 'TS_1',
    14: 'P_AFR',
    15: 'OND_1',
    16: 'OND_2',
    17: 'OND_3',
    18: 'AB_1',
    19: 'AB_2',
    20: 'AB_3',
    21: 'AFA_1',
    22: 'AFA_2',
    23: 'HUN_1',
    24: 'HUN_2',
    25: 'AHU_1',
    26: 'AHU_2',
    27: 'AHU_3',
    28: 'PINT',
    29: 'SU',
    30: 'SOM',
    31: 'LV',
    32: 'MNF',
    33: 'MNQ',
    34: 'RM',
    35: 'CV_2',
    36: 'CV_3',
    37: 'SUM',
    38: 'EX_1',
    39: 'EX_2',
    40: 'DB_1',
    41: 'DB_2',
    42: 'DB_3',
    43: 'PLF_1',
    44: 'PLF_2',
    45: 'PLF_3',
    46: 'MISC',
    47: 'LD',
    48: 'FCL_0',
    49: 'FBD_1',
    50: 'FBD_2',
    51: 'FBD_3',
    52: 'FBD_S',
    53: 'FCL_1',
    54: 'FCL_2',
    55: 'FCL_3',
    56: 'FCL_S',
    57: 'FCT_0',
    58: 'FCT_1',
    59: 'FCT_2',
    60: 'FCT_3',
    61: 'FCT_S',
    62: 'FT_S',
    63: 'FL_S',
    64: 'FL_1',
    65: 'FL_2',
    66: 'FL_3',
    67: 'FT_1',
    68: 'FT_2',
    69: 'FT_3',
    # 62: 'FJT_S',
    # 63: 'FJL_S',
    # 64: 'FJL_1',
    # 65: 'FJL_2',
    # 66: 'FJL_3',
    # 67: 'FJT_1',
    # 68: 'FJT_2',
    # 69: 'FJT_3',
    70: 'FL_1',
    71: 'FL_2',
    72: 'FL_3',
    73: 'FL_S',
    74: 'FT_1',
    75: 'FT_2',
    76: 'FT_3',
    77: 'FT_S',
    78: 'FR_1',
    79: 'FR_2',
    80: 'FR_3',
    81: 'FR_S',
    82: 'FB_1',
    83: 'FB_2',
    84: 'FB_3',
    85: 'FB_S',
    86: 'PC_1',
    87: 'PC_2',
    88: 'PC_3',
    89: 'PC_S',
    90: 'FML_1',
    91: 'FML_2',
    92: 'FML_3',
    93: 'DC_1',
    94: 'DC_2',
    95: 'DC_3',
    96: 'P_RIG',
    97: 'P_RIG',
    98: 'ALC_1',
    99: 'ALC_1',
    100: 'ALC_2',
    101: 'ALC_3',
    102: 'CAR',
    103: 'P_ART',
    104: 'PCH_1',
    105: 'PCH_2',
    106: 'PCH_3',
    107: 'BCH_1',
    108: 'BCH_2',
    109: 'BCH_3'
}

ENGIN2VIZIR = {
    'FR_S': 'FLF_1',
    'FR_1': 'FLF_2',
    'FR_2': 'FLF_3',
    'FR_3': 'PC_1',
    'FB_1': 'FCT_1',
    'FB_2': 'FCT_2',
    'FB_3': 'FCT_3',
    'FB_S': 'FCT_S',
    'PC_1': 'FPC_1',
    'PC_2': 'FPC_2',
    'PC_3': 'FPC_3',
    'PC_S': 'FPC_S',
    'FBD_1': 'FB_1',
    'FBD_2': 'FB_2',
    'FBD_3': 'FB_3',
    'FBD_S': 'FB_S',
    'FCL_1': 'FLJ_1',
    'FCL_2': 'FLJ_2',
    'FCL_3': 'FLJ_3',
    'FCL_S': 'FLJ_S',
    'FCT_1': 'FTJ_1',
    'FCT_2': 'FTJ_2',
    'FCT_3': 'FTJ_3',
    'FCT_S': 'FTJ_S',
    'FJT_S': 'FTJ_S',
    'FJL_S': 'FLJ_S',
    'FJL_1': 'FLJ_1',
    'FJL_2': 'FLJ_2',
    'FJL_3': 'FLJ_3',
    'FJT_1': 'FTJ_1',
    'FJT_2': 'FTJ_2',
    'FJT_3': 'FTJ_3',
    'FL_1': 'FLF_1',
    'FL_2': 'FLF_2',
    'FL_3': 'FLF_3',
    'FL_S': 'FLF_S',
    'FT_1': 'FLF_1',
    'FT_2': 'FLF_2',
    'FT_3': 'FLF_3',
    'FT_S': 'FLF_1',
    'DSU_1': 'PL_1',
    'DSU_2': 'PL_2',
    'DSU_3': 'PL_3',
    'DC_1': 'D_1',
    'DC_2': 'D_2',
    'DC_3': 'D_3',
    'PCH_1': 'B_1',
    'PCH_2': 'B_2',
    'PCH_3': 'B_3',
    'BCH_1': 'O_1',
    'BCH_2': 'O_2',
    'BCH_3': 'O_3',
    'FR_1_POL': 'FLF_1',
    'FR_2_POL': 'FLF_2',
    'FR_3_POL': 'FPC_1',
    'FR_S_POL': 'FPC_S',
    'PC_1_POL': 'FPC_1',
    'PC_2_POL': 'FPC_2',
    'PC_3_POL': 'FPC_3',
    'PC_S_POL': 'FPC_S',
    'FML_1': 'FML_1',
    'FML_2': 'FML_2',
    'FML_3': 'FML_3',
    'PA_1': 'PA_1',
    'PA_2': 'PA_2',
    'PA_3': 'PA_3',
    'S_1': 'S_1',
    'S_2': 'S_2',
    'S_3': 'S_3',
    'OND_1': 'DM_1',
    'OND_2': 'DM_2',
    'OND_3': 'DM_3',
    'AB_1': 'DM_1',
    'AB_2': 'DM_2',
    'AB_3': 'DM_3',
    'AFA_1': 'AA_1',
    'AFA_2': 'AA_2',
    'HUN_1': 'DL_1',
    'HUN_2': 'DL_2',
    'AHU_1': 'AH_1',
    'AHU_2': 'AH_2',
    'AHU_3': 'AH_3',
    'SU': 'SU',
    'RM': 'RM',
    'CV_2': 'ECB_2',
    'CV_3': 'ECB_3',
    'EX_1': 'EX_1',
    'EX_2': 'EX_2',
    'DB_1': 'DB_1',
    'DB_2': 'DB_2',
    'DB_3': 'DB_3',
    'PLF_1': 'PLF_1',
    'PLF_2': 'PLF_2',
    'PLF_3': 'PLF_3'
}

ENGIN2PCI = {
    'DSU_1': '20_1',
    'DSU_2': '20_2',
    'DSU_3': '20_3',
    'PA_1': '19_2',
    'PA_2': '19_2',
    'PA_3': '19_3',
    'OND_1': '6_2',
    'OND_2': '6_2',
    'OND_3': '6_3',
    'AB_1': '4_1',
    'AB_2': '4_2',
    'AB_3': '4_3',
    'HUN_1': '6_1',
    'HUN_2': '6_2',
    'HUN_3': '6_3',
    'AHU_1': '15_1',
    'AHU_2': '15_2',
    'AHU_3': '15_3',
    'EX_1': '2_1',
    'EX_2': '2_2',
    'EX_3': '2_3',
    'DB_1': '7_3',
    'DB_2': '7_3',
    'DB_3': '7_3',
    'PCH_1': '11_1',
    'PCH_2': '11_2',
    'PCH_3': '11_3',
    'PLF_1': '14_1',
    'PLF_2': '14_2',
    'PLF_3': '14_3',
    'FBD_1': '7_1',
    'FBD_2': '7_2',
    'FBD_3': '7_2',
    'FBD_S': '7_1',
    'FCL_1': '10_1',
    'FCL_2': '10_2',
    'FCL_3': '10_3',
    'FCL_S': '10_1',
    'FCT_1': '10_1',
    'FCT_2': '10_2',
    'FCT_3': '10_3',
    'FCT_S': '10_1',
    'FJT_S': '10_1',
    'FJL_S': '10_1',
    'FJL_1': '10_1',
    'FJL_2': '10_2',
    'FJL_3': '10_3',
    'FJT_1': '10_1',
    'FJT_2': '10_2',
    'FJT_3': '10_3',
    # 'FJT_S': '8_1',
    # 'FJL_S': '8_1',
    # 'FJL_1': '8_1',
    # 'FJL_2': '8_2',
    # 'FJL_3': '8_3',
    # 'FJT_1': '8_1',
    # 'FJT_2': '8_2',
    # 'FJT_3': '8_3',
    'FL_1': '10_1',
    'FL_2': '10_2',
    'FL_3': '10_3',
    'FL_S': '10_1',
    'FT_1': '10_1',
    'FT_2': '10_2',
    'FT_3': '10_3',
    'FT_S': '10_1',
    'FR_1': '10_2',
    'FR_2': '1_1',
    'FR_3': '1_2',
    'FR_S': '1_1',
    'FR_1_POL': '10_2',
    'FR_2_POL': '1_1',
    'FR_3_POL': '1_2',
    'FR_S_POL': '1_1',
    'FB_1': '3_1',
    'FB_2': '3_2',
    'FB_3': '3_3',
    'FB_S': '3_1',
    'PC_1': '1_1',
    'PC_2': '1_2',
    'PC_3': '1_3',
    'PC_S': '1_1',
    'PC_1_POL': '1_1',
    'PC_2_POL': '1_2',
    'PC_3_POL': '1_3',
    'PC_S_POL': '1_1',
    'FML_1': '1_1',
    'FML_2': '1_2',
    'FML_3': '1_3',
    'DC_1': '19_2',
    'DC_2': '19_2',
    'DC_3': '19_3',
    'BCH_1': '13_1',
    'BCH_2': '13_2',
    'BCH_3': '13_3',
    'AFA_1': '10_2',
    'AFA_2': '10_3',
    'SU': '19_3',
    'RM': '19_2',
    'CV_1': '9_1',
    'CV_2': '9_2',
    'CV_3': '9_3'
}

FR_DICT = {'FR_1': ['FB_1', 'FB_2', 'FL_2', 'FT_2', 'FL_1', 'FT_1', 'PC_1', 'FML_1'],
           'FR_2': ['FB_2', 'FB_1', 'FB_3', 'FL_3', 'FT_3', 'FL_2', 'FT_2', 'PC_1', 'PC_2', 'FML_2'],
           'FR_3': ['FB_3', 'FB_2', 'FL_3', 'FT_3', 'FL_2', 'FT_2', 'FL_1', 'FT_1', 'PC_2', 'PC_3', 'FML_3'],
           'FR_S': ['FB_S', 'FL_S', 'FT_S', 'FL_1', 'FT_1', 'PC_S', 'FB_1', 'PC_1']}

# Lists based on Engin.AI tags

## Cracks

LINE_CRACKS = ['FBD_1', 'FBD_2', 'FBD_3', 'FBD_S', 'FCL_1', 'FCL_2', 'FCL_3', 'FCL_S', 'FCT_1', 'FCT_2', 'FCT_3',
               'FCT_S', 'FJT_S', 'FJL_S', 'FJL_1', 'FJL_2', 'FJL_3', 'FJT_1', 'FJT_2', 'FJT_3', 'FL_1', 'FL_2', 'FL_3',
               'FL_S', 'FT_1', 'FT_2', 'FT_3', 'FT_S']
LINE_CRACKS_ID = [CONV_LU[dmg] for dmg in LINE_CRACKS]
AREA_CRACKS = ['FR_1', 'FR_2', 'FR_3', 'FR_S', 'FR_1_POL', 'FR_2_POL', 'FR_3_POL', 'FR_S_POL', 'FB_1', 'FB_2', 'FB_3',
               'FB_S', 'PC_1', 'PC_2', 'PC_3', 'PC_S', 'PC_1_POL', 'PC_2_POL', 'PC_3_POL', 'PC_S_POL', 'FML_1', 'FML_2',
               'FML_3']
AREA_CRACKS_ID = [CONV_LU[dmg] for dmg in AREA_CRACKS]
CRACKS = LINE_CRACKS + AREA_CRACKS
CRACKS_ID = LINE_CRACKS_ID + AREA_CRACKS_ID

## Other

OTHER_DISTRESS = ['DSU_1', 'DSU_2', 'DSU_3', 'PA_1', 'PA_2', 'PA_3', 'S_1', 'S_2', 'S_3', 'OND_1', 'OND_2', 'OND_3',
                  'AB_1', 'AB_2', 'AB_3', 'AFA_1', 'AFA_2', 'HUN_1', 'HUN_2', 'AHU_1', 'AHU_2', 'AHU_3', 'SU', 'RM',
                  'CV_2', 'CV_3', 'EX_1', 'EX_2', 'DB_1', 'DB_2', 'DB_3', 'PLF_1', 'PLF_2', 'PLF_3', 'DC_1', 'DC_2',
                  'DC_3', 'PCH_1', 'PCH_2', 'PCH_3', 'BCH_1', 'BCH_2', 'BCH_3']
OTHER_DISTRESS_ID = [CONV_LU[dmg] for dmg in OTHER_DISTRESS]

PCI_CONVERTER = {
    'DSU_1': '20_1',
    'DSU_2': '20_2',
    'DSU_3': '20_3',
    'PA_1': '19_2',
    'PA_2': '19_2',
    'PA_3': '19_3',
    'OND_1': '6_2',
    'OND_2': '6_2',
    'OND_3': '6_3',
    'AB_1': '4_1',
    'AB_2': '4_2',
    'AB_3': '4_3',
    'HUN_1': '6_1',
    'HUN_2': '6_2',
    'HUN_3': '6_3',
    'AHU_1': '15_1',
    'AHU_2': '15_2',
    'AHU_3': '15_3',
    'EX_1': '2_1',
    'EX_2': '2_2',
    'EX_3': '2_3',
    'DB_1': '7_3',
    'DB_2': '7_3',
    'DB_3': '7_3',
    'PCH_1': '11_1',
    'PCH_2': '11_2',
    'PCH_3': '11_3',
    'PLF_1': '14_1',
    'PLF_2': '14_2',
    'PLF_3': '14_3',
    'FBD_1': '7_1',
    'FBD_2': '7_2',
    'FBD_3': '7_2',
    'FBD_S': '7_1',
    'FCL_1': '10_1',
    'FCL_2': '10_2',
    'FCL_3': '10_3',
    'FCL_S': '10_1',
    'FCT_1': '10_1',
    'FCT_2': '10_2',
    'FCT_3': '10_3',
    'FCT_S': '10_1',
    'FJT_S': '10_1',
    'FJL_S': '10_1',
    'FJL_1': '10_1',
    'FJL_2': '10_2',
    'FJL_3': '10_3',
    'FJT_1': '10_1',
    'FJT_2': '10_2',
    'FJT_3': '10_3',
    # 'FJT_S': '8_1',
    # 'FJL_S': '8_1',
    # 'FJL_1': '8_1',
    # 'FJL_2': '8_2',
    # 'FJL_3': '8_3',
    # 'FJT_1': '8_1',
    # 'FJT_2': '8_2',
    # 'FJT_3': '8_3',
    'FL_1': '10_1',
    'FL_2': '10_2',
    'FL_3': '10_3',
    'FL_S': '10_1',
    'FT_1': '10_1',
    'FT_2': '10_2',
    'FT_3': '10_3',
    'FT_S': '10_1',
    'FR_1': '10_2',
    'FR_2': '3_1',
    'FR_3': '3_2',
    'FR_S': '3_1',
    'FR_1_POL': '10_2',
    'FR_2_POL': '1_1',
    'FR_3_POL': '1_2',
    'FR_S_POL': '1_1',
    'FB_1': '3_1',
    'FB_2': '3_2',
    'FB_3': '3_3',
    'FB_S': '3_1',
    'PC_1': '1_1',
    'PC_2': '1_2',
    'PC_3': '1_3',
    'PC_S': '1_1',
    'PC_1_POL': '1_1',
    'PC_2_POL': '1_2',
    'PC_3_POL': '1_3',
    'PC_S_POL': '1_1',
    'FML_1': '1_1',
    'FML_2': '1_2',
    'FML_3': '1_3',
    'DC_1': '19_2',
    'DC_2': '19_2',
    'DC_3': '19_3',
    'BCH_1': '13_1',
    'BCH_2': '13_2',
    'BCH_3': '13_3',
    'AFA_1': '10_2',
    'AFA_2': '10_3',
    'SU': '19_3',
    'RM': '19_2',
    'CV_1': '9_1',
    'CV_2': '9_2',
    'CV_3': '9_3'
}


PCI_CODE2NAME= {1: 'Alligator Cracking',
 2: 'Bleeding',
 3: 'Block Cracking',
 4: 'Bumps and Sags',
 5: 'Corrugation',
 6: 'Depression',
 7: 'Edge Cracking',
 8: 'Jt. Reflextion Cracking',
 9: 'Lane/Shoulder Drop Off',
 10: 'Longitudinal and Transverse Cracking',
 11: 'Patching and  Utility Cut Patching',
 12: 'Polished Aggregate',
 13: 'Pothole',
 14: 'Railroad Crossing',
 15: 'Rutting',
 16: 'Shoving',
 17: 'Slippage Cracking',
 18: 'Swell',
 19: 'Raveling',
 20: 'Weathering'}

TOLERANCE_POLYGON = 5
TOLERANCE_POLYLINE = 5