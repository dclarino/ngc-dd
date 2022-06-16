import logging
import os
import sys
from dd.autoref import BDD
import graphviz

import pytest
from qiskit import QuantumCircuit

sys.path.append(os.path.join('../src'))
print(sys.path)


from circuit_to_logic import *

class circuitToLogicTests(object):
    def test_not(self):
        bdd = BDD()
        bdd.declare('q0')

        qc = QuantumCircuit(1)
        qc.x(0)
        
        bdd_act = get_qc_bdd(qc)
        bdd_exp = bdd.add_expr(r'~q0')

        assert bdd_act == bdd_exp, (bdd_act,bdd_exp)
        


    def test_cnot(self):
        bdd = BDD()
        bdd.declare('q0','q1')

        qc = QuantumCircuit(2)
        qc.cx(0,1)
        
        bdd_act = get_qc_bdd(qc)
        bdd_exp = bdd.add_expr(r"( ( ~ q0 ) /\\ q1 ) ) \\/ ( ( q0 ) /\\ ~ q1 ) )")

        assert bdd_act == bdd_exp, (bdd_act,bdd_exp)

    def test_mct(self):
        bdd = BDD()
        bdd.declare('q0','q1','q2')

        qc = QuantumCircuit(3)
        qc.ccx(0,1,2)
        
        bdd_act = get_qc_bdd(qc)
        bdd_exp = bdd.add_expr(r"(    q2   /\\ (q0 /\\ q1) ) ) \\/ ( ( q2 /\\ ¬ (q0 /\\ q1 ) )")

        assert bdd_act == bdd_exp, (bdd_act,bdd_exp)
    
    def test_circ(self):
        # example Qiskit Circuit
        bdd = BDD()
        bdd.declare('q0','q1','q2')

        qc = QuantumCircuit(3)
        qc.x(1)
        qc.cx(0, 1)

        bdd_act = get_qc_bdd(qc)
        bdd_exp = bdd.add_expr(r'~q1 /\ q0')

        assert bdd_act == bdd_exp, (bdd_act,bdd_exp)


