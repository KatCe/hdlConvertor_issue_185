# hdlConvertor_issue_185
This Verilog version of the PicoRv32 core (https://github.com/YosysHQ/picorv32) was not correctly parsed by hdlConvertor (https://github.com/Nic30/hdlConvertor/), because the parallel_case attribute is not supported. A good demonstrative example is the one in line 1139/1140. Created issue 185 (https://github.com/Nic30/hdlConvertor/issues/185).
