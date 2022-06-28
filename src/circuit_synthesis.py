from qiskit import QuantumCircuit,QuantumRegister
from dd.autoref import BDD

def calculate(qc,bdd):
    
    return [bdd.add_expr('False'),
            bdd.add_expr('False'),
            bdd.add_expr('False'),
            bdd.add_expr('False')]

def synthesize(phase_function,bdd,qr):
    return [QuantumCircuit(qr),QuantumCircuit(qr), QuantumCircuit(qr),QuantumCircuit(qr)]


