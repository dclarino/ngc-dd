from qiskit import *
from dd.autoref import BDD
import graphviz

bdd  = BDD()

bdd.declare('q0','q1','q2','q3')

#simulate an and gate
u = bdd.add_expr(r'q0 /\ q1')  # symbols `&`, `|` are supported too 
    # note the "r" before the quote, which signifies a raw string and is
    # needed to allow for the backslash


bdd.collect_garbage()
#UNCOMMENT FOR DUMP bdd.dump('bdd0.pdf',roots=[u])

x        = bdd.add_expr(r'~q0')
d        = dict(q0=x)
bdd.collect_garbage()

#replace q0 with bdd for ~q0 to simulate adding a NOT gate before AND on q0
bdd_act  = bdd.let(d,u)

bdd.collect_garbage()
#UNCOMMENT FOR DUMP bdd.dump('bdd_act.pdf',roots=[bdd_act])


bdd_exp  = bdd.add_expr(r'q1 /\ ~q0')
#UNCOMMENT FOR DUMP bdd.dump('bdd_exp.pdf',roots=[bdd_exp])

assert bdd_act == bdd_exp, (bdd_act, bdd_exp)
