from qiskit import *
from dd.autoref import BDD
import graphviz

bdd = BDD()

bdd.declare('q0','q1','q2','q3')
#bdd.declare('q0','q1')
u = bdd.add_expr(r'q0 /\ q1')  # symbols `&`, `|` are supported too 
    # note the "r" before the quote, which signifies a raw string and is
    # needed to allow for the backslash

#print(bdd)
#v = ~ u
bdd.collect_garbage()
bdd.dump('bdd0.pdf',roots=[u])
#add not after
d = dict(q1=bdd.add_expr(r'~q1'))
bdd.collect_garbage()
v = bdd.let(d,u)
final = u & v
#v = ~ v
#BDD.reorder(bdd)

bdd.collect_garbage()
#bdd.dump('bdd.pdf')
bdd.dump('bdd.pdf',roots=[final])

#qc = QuantumCircuit(4)
#qc.x(1)
#qc.mct([0,1],2)
#qc.mct([1,2],3)
#qc.draw('latex')
