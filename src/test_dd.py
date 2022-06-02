from qiskit import *
from dd.autoref import BDD
import graphviz

bdd = BDD()

bdd.declare('q0','q1','q2','q3')
u = bdd.add_expr(r'q0 /\ q1')  # symbols `&`, `|` are supported too 
    # note the "r" before the quote, which signifies a raw string and is
    # needed to allow for the backslash
#print(bdd)
bdd.dump('bdd.pdf')

qc = QuantumCircuit(4)
qc.x(1)
qc.mct([0,1],2)
qc.mct([1,2],3)
qc.draw('latex')
