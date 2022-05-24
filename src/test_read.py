from read_real import *
from gen_qc    import *
import sys
from qiskit import *

fname       = sys.argv[1]
real_string = readRealFile(fname)
qc          = build_qc(real_string)

print(qc)
