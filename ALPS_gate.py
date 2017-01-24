#Job 8:7
#Though your beginning was small, yet your latter end would greatly increase.

import sys
sys.path.append("D:\Python")
from HI_tool.schedule_check import sch_check


# create sch_check class instance.
EL = sch_check("ALPS(603) Package CES v1.0.xlsm", "Turnkey schedule", "Lot#/DCC", "Tdevice", current_fg_column="FG/PV",)

# collecting target lot number using 'set_target()' method in WF instance.
EL.set_target(603, "P/D/L", "EOH(D)")
EL.parser(EL.target_lots, EL.EMES_df, EL.result_df)
EL.get_info(['test_device','current_fg'])
EL.comparing('Turnkey')
print("Inspection complete")
#
#
# except PermissionError:
#     input("Please close result files. Proram needs to overwrite them.")
# except:
#     input("Unexpected error caused, please run it in pycharm to check error")
