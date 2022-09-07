from qiskit import QuantumCircuit


def retrieve_gates(qc):

    # Takes a QuantumCircuit object as input, and returns a list of gates in the circuit, in the order they act in the circuit.
    # Each gate is of the format (list) [(string) gateName, (list) QubitIndices]
    # The QubitIndices follow the same format as the Qiskit QuantumCircuit
    # Gates

    gates_list = []
    for gate in qc.data:
        temp_list = []
        temp_list.append(gate[0].name)
        qubit_list = []
        for i in range(len(gate[1])):
            qubit_list.append(gate[1][i].index)
        temp_list.append(qubit_list)
        gates_list.append(temp_list)
    return gates_list


def not_bdd(qubit):

    # Takes a qubit as input, and returns the string representation of the NOT gate on that qubit
    # Brackets are added to prevent ambiguity in the string representation of
    # the circuit
    if (qubit == 'True'):
        return 'False'
    if (qubit == 'False'):
        return 'True'
    qubit = '( ~ ' + qubit + ' )'
    return qubit

def and_bdd(qubit_one, qubit_two):

    # Takes a qubit as input, and returns the string representation of the NOT gate on that qubit
    # Brackets are added to prevent ambiguity in the string representation of
    # the circuit

    if (qubit_one == 'False') or (qubit_two == 'False'):
        return 'False'

    if (qubit_one == 'True'):
        return qubit_two
    if (qubit_two == 'True'):
        return qubit_one
    qubit = '( '+ qubit_one + ' /\\ ' + qubit_two + ' )'
    
    return qubit

def or_bdd(qubit_one, qubit_two):

    # Takes a qubit as input, and returns the string representation of the NOT gate on that qubit
    # Brackets are added to prevent ambiguity in the string representation of
    # the circuit
    if (qubit_one == 'True') or (qubit_two == 'True'):
        return 'True'

    if (qubit_one == 'False'):
        return qubit_two
    if (qubit_two == 'False'):
        return qubit_one
    
    qubit = '( '+ qubit_one + ' \\/ ' + qubit_two + ' )'
    return qubit

def cnot_bdd(qubit_control, qubit_target):
    qubit_target = ' ( ( ~ ' + qubit_target + ' ) /\\ ' + qubit_control + \
        ' ) \\/ ( ' + qubit_target + ' /\\ ( ~ ' + qubit_control + ' ) )'
    return qubit_target


def toffoli_bdd(qubit_control_one, qubit_control_two, qubit_target):

    # Takes a qubit as input, and returns the string representation of the Toffoli gate with first two arguments as control bits and the third as target bits
    # Brackets are added to prevent ambiguity in the string representation of
    # the circuit

    qubit_target = ' ( ( ~ ' + qubit_target + ' )' + ' /\\ ( ' + qubit_control_one + ' /\\ ' + qubit_control_two + ' ) ) ' + \
        '\\/ ( ' + qubit_target + ' /\\' + ' ( ~ ( ' + qubit_control_one + ' /\\ ' + qubit_control_two + ' ) ) )'
    return qubit_target


def get_qc_bdd(qc,bdd):
    gate_list = retrieve_gates(qc)
    # prepares the initial state of qubits
    qubit_states = []
    for i in range(len(qc.qubits)):
        qubit_states.append('q' + str(i))

    # applies the circuit gates to the qubits and modifies the qubit_states
    # list in place
    for gate in gate_list:
        if gate[0] == 'ccx':
            qubit_states[gate[1][2]] = toffoli_bdd(
                qubit_states[gate[1][0]], qubit_states[gate[1][1]], qubit_states[gate[1][2]])
        elif gate[0] == 'x':
            qubit_states[gate[1][0]] = not_bdd(qubit_states[gate[1][0]])
        elif gate[0] == 'cx':
            qubit_states[gate[1][1]] = cnot_bdd(
                qubit_states[gate[1][0]], qubit_states[gate[1][1]])
    
    bdd_list = []
    for i in range(len(qc.qubits)):
        bdd_list.append(bdd.add_expr(qubit_states[i]))
    return bdd_list
