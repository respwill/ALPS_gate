#Job 8:7
#Though your beginning was small, yet your latter end would greatly increase.

import sys
sys.path.append("D:\Python")
from HI_tool.schedule_check import sch_check


# create sch_check class instance.
WF = sch_check("ALPS(603) Wafer CES v1.0.xlsm", "Probe schedule", "Bank Lot#(Job#)", "dcc", "Test device","PO#",  ship_column="Ship To", current_fg_column="FG",)

# collecting target lot number using 'set_target()' method in WF instance.
WF.set_target(603, "wafer", "Wfr")
WF.parser(WF.target_lots, WF.EMES_df, WF.result_df)
WF.get_info(["test_device", 'test_po', 'ship_code', 'current_fg', ])
WF.comparing("Wafer")
print("Inspection complete")


# except PermissionError:
#     input("Please close result files. Proram needs to overwrite them.")
#
# except:
#     input("Unexpected error caused, please run it in pycharm to check error")

