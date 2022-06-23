import logging
import os
import sys
from dd.autoref import BDD
import graphviz

import pytest
from mqt.qcec import Configuration, Strategy, verify

from qiskit import *
from qiskit.circuit import classical_function, Int1

sys.path.append(os.path.join('../src'))
print(sys.path)


from circuit_synthesis import synthesize

class SynthesisTests(object):
    def test_paper_example(self):
        qr = QuantumRegister(5, 'x')

        #Declare BDDs
        bdd = BDD()
        bdd.declare('x1','x2','x3','f','aux1')
        phase_function = []
        phase_function.append(bdd.add_expr('False'))
        phase_function.append(bdd.add_expr('False'))
        phase_function.append(bdd.add_expr(r'x1 & x2 & !x3'))
        phase_function.append(bdd.add_expr('False')) #DCDEBUG Come back to this later

        
        qc_exp   = QuantumCircuit(qr)
        qc_exp.x(qr[1])
        qc_exp.ccx(qr[0],qr[1],qr[3])
        qc_exp.ccx(qr[2],qr[3],qr[4])
        qc_inv   = qc_exp.inverse()
        qc_exp.s(qr[4])
        qc_exp.s(qr[4])
        qc_exp   = qc_exp.compose(qc_inv)

        qc_act_arr      = synthesize(phase_function,bdd,qr)

        qc_act          = qc_act_arr[2] #DCDEBUG for now only debug the pi case

        config          = Configuration()
        config.strategy = Strategy.compilationflow

        result          = verify(qc_exp,qc_act,config)

        print(result)
        print(str(result.equivalence))
        
        assert str(result.equivalence) == "Equivalence.equivalent", (result)

