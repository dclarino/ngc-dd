from dd import cudd

cudd.BDD(memory_estimate=0.5 * 2**30)

bdd = cudd.BDD()

bdd.declare('x1', 'x2', 'x3')

x1 = bdd.add_expr('x1')
x2 = bdd.add_expr('x2')
x3 = bdd.add_expr('x3')

z = x1 & x2 
w = z | x3

#bdd.collect_garbage()
bdd.dump('awesome.pdf',roots=[w])
