columns = ['PRC_CD', 'TIME', 'COIL_NO', 'COIL_NO_TF', 'PASS_NO', 'PASS_NO_TF', 'EXIT_THK_ACT_MAX', 'EXIT_THK_ACT_AVG', 'EXIT_THK_ACT_MIN', 'EXIT_THK_ACT_TF', 'EXIT_THK_SET_MAX', 'EXIT_THK_SET_AVG', 'EXIT_THK_SET_MIN', 'EXIT_THK_SET_TF', 'ENTRY_LEN_ACT_MAX', 'ENTRY_LEN_ACT_AVG', 'ENTRY_LEN_ACT_MIN', 'ENTRY_LEN_ACT_TF', 'EXIT_LEN_ACT_MAX', 'EXIT_LEN_ACT_AVG', 'EXIT_LEN_ACT_MIN', 'EXIT_LEN_ACT_TF', 'LEFT_ROLL_SPD_MAX', 'LEFT_ROLL_SPD_AVG', 'LEFT_ROLL_SPD_MIN', 'LEFT_ROLL_SPD_TF', 'RIGHT_ROLL_SPD_MAX', 'RIGHT_ROLL_SPD_AVG', 'RIGHT_ROLL_SPD_MIN', 'RIGHT_ROLL_SPD_TF', 'ROLL_SPD_MAX', 'ROLL_SPD_AVG', 'ROLL_SPD_MIN', 'ROLL_SPD_TF', 'YN', 'CAL_YMD']

thk_colums = ['TIME','COIL_NO', 'PASS_NO', 'EXIT_THK_ACT_AVG']
jaryo_columns = ['2CR_IBA_DB230_REAL148', '2CR_IBA_DB230_REAL156', '2CR_IBA_DB230_REAL164', '2CR_IBA_DB340_REAL52', '2CR_IBA_DB500_REAL24', '2CR_IBA_DB500_REAL48', '2CR_IBA_DB500_REAL88', 'N2_AGC_DB222_DD154', 'N2_CPU2_DB801_DD142', 'N2_CPU2_DB801_DD278', 'N2_CPU1_DB801_DD42', 'N2_CPU1_DB801_DD46']

rename_dict = {'EXIT_THK_ACT_AVG' : 'ENTRY_THK_ACT_AVG',
               '2CR_IBA_DB230_REAL148' : 'upper_roll_shift_set',
               '2CR_IBA_DB230_REAL156' : 'lower_roll_shift_set',
               '2CR_IBA_DB230_REAL164' : 'bending_DS_set',
               '2CR_IBA_DB500_REAL24' : 'LH_tension_set',
               '2CR_IBA_DB500_REAL48' : 'RH_tension_set',
               '2CR_IBA_DB500_REAL88' : 'POR_tension_set',
               'N2_AGC_DB222_DD154' : 'roll_force_set',
               'N2_CPU2_DB801_DD142' : 'speed_set',
               'N2_CPU2_DB801_DD278' : 'POR_tension_N/mm2_set',
               'N2_CPU1_DB801_DD42' : 'left_cooler_amount',
               'N2_CPU1_DB801_DD46' : 'right_cooler_amount',
               'EXIT_THK_ACT_AVG_y' : 'EXIT_THK_ACT_AVG'}

used_columns = ['ENTRY_THK_ACT_AVG', 'upper_roll_shift_set', 'lower_roll_shift_set', 'bending_DS_set',
                     'LH_tension_set', 'RH_tension_set', 'POR_tension_set', 'POR_tension_N/mm2_set', 'roll_force_set', 'speed_set',
                     'left_cooler_amount', 'right_cooler_amount', 'EXIT_THK_ACT_AVG']

train_columns = ['ENTRY_THK_ACT_AVG',
                'upper_roll_shift_set',
                'lower_roll_shift_set',
                'bending_DS_set',
                'LH_tension_set',
                'RH_tension_set',
                'POR_tension_set',
                'POR_tension_N/mm2_set',
                'roll_force_set',
                'speed_set',
                'left_cooler_amount',
                'right_cooler_amount']