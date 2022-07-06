from qiskit import QuantumCircuit,QuantumRegister
from dd.autoref import BDD
from src.circuit_to_logic import *

def calculate(qc,bdd):
    
    qubit_states = []
    for i in range(len(qc.qubits)):
        qubit_states.append('q' + str(i))
    qc_gates = retrieve_gates(qc)
    total_phase = ['t', 'f', 'f', 'f']
    for gate in qc_gates:
        if gate[0] == 'cx':
            qubit_states[gate[1][1]] = cnot_string(
                qubit_states[gate[1][0]], qubit_states[gate[1][1]])
        elif gate[0] == 'x':
            qubit_states[gate[1][0]] = not_string(qubit_states[gate[1][0]])
        elif gate[0] == 'ccx':
            if gate[1][2] == 3:
                add_phase = ['t', 't', 't', 't']
                add_phase[1] = and_string(qubit_states[gate[1][0]], and_string(qubit_states[gate[1][1]], not_string(qubit_states[gate[1][2]])))
                add_phase[2] = and_string(qubit_states[gate[1][0]], and_string(qubit_states[gate[1][2]], not_string(qubit_states[gate[1][1]])))
                add_phase[3] = and_string(qubit_states[gate[1][0]], and_string(qubit_states[gate[1][0]], qubit_states[gate[1][2]]))
                add_phase[0] = not_string(or_string(add_phase[0], or_string(add_phase[1], add_phase[2])))

                for index in range(0, 4):
                    string_index = 't'
                    for j in range(0, 4):
                        for k in range(0, 4):
                            if (j + k) % 4 == index:
                                string_index = or_string(string_index, and_string(total_phase[j], add_phase[k]))
                    total_phase[index] = string_index
            qubit_states[gate[1][2]] = cnot_string(qubit_states[gate[1][0]], qubit_states[gate[1][1]])

    return [bdd.add_expr(total_phase[0]),
            bdd.add_expr(total_phase[1]),
            bdd.add_expr(total_phase[2]),
            bdd.add_expr(total_phase[3])]

def synthesize(phase_function,bdd,qr):
    return [QuantumCircuit(qr),QuantumCircuit(qr), QuantumCircuit(qr),QuantumCircuit(qr)]


