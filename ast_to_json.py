

import os
import sys

from hdlConvertorAst.language import Language
from hdlConvertor import HdlConvertor
from hdlConvertorAst.to.json import ToJson
import json

TEST_DIR = os.path.join(".")

filenames = [os.path.join(TEST_DIR, "picorv32_sv2v_out.v"), ]
include_dirs = []
c = HdlConvertor()
# note that there is also Language.VERILOG_2005, Language.SYSTEM_VERILOG_2017 and others
d = c.parse(filenames, Language.VERILOG, include_dirs, hierarchyOnly=False, debug=True)
tj = ToJson()
j = tj.visit_HdlContext(d)
print(json.dumps(j, sort_keys=True,
                 indent=4, separators=(',', ': ')))




