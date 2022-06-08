import logging
import os
import sys

import pytest
from qiskit import QuantumCircuit

sys.path.append(os.path.join('../src'))
print(sys.path)


from circuitToLogic import *

class circuitToLogicTests(object):
    def test_not(self):
        qc = QuantumCircuit(1)
        qc.x(0)
        qc_string = get_qc_string(qc)
        assert qc_string[0] == "( ¬ q0 )"

    def test_cnot(self):
        qc = QuantumCircuit(2)
        qc.cx(0,1)
        qc_string = get_qc_string(qc)
        assert qc_string[1] == "( ( ¬ q0 ) /\\ q1 ) ) \\/ ( ( q0 ) /\\ ¬ q1 ) )"

    def test_mct(self):
        qc = QuantumCircuit(3)
        qc.ccx(0,1,2)
        qc_string = get_qc_string(qc)
        assert qc_string[2] == "(    q2   /\\ (q0 /\\ q1) ) ) \\/ ( ( q2 /\\ ¬ (q0 /\\ q1 ) )"
    
    
    def test2_circ(self):
        # example Qiskit Circuit
        nStates = 4
        qc = QuantumCircuit(nStates)
        qc.x(1)
        qc.cx(0, 1)
        qc.ccx(1, 2, 3)



