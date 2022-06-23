from qiskit import QuantumCircuit,QuantumRegister
from dd.autoref import BDD

def synthesize(phase_function,bdd,qr):
    return [QuantumCircuit(qr),QuantumCircuit(qr), QuantumCircuit(qr),QuantumCircuit(qr)]
