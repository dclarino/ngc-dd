from qiskit import QuantumCircuit

def retrieveGates(qc):

    # Takes a QuantumCircuit object as input, and returns a list of gates in the circuit, in the order they act in the circuit. 
    # Each gate is of the format (list) [(string) gateName, (list) QubitIndices]
    # The QubitIndices follow the same format as the Qiskit QuantumCircuit Gates
    
    gatesList = []
    for gate in qc.data:
        tempList = []
        tempList.append(gate[0].name)
        qubitList = []
        for i in range(len(gate[1])):
            qubitList.append(gate[1][i].index)
        tempList.append(qubitList)
        gatesList.append(tempList)
    return gatesList

def NOTString(qubit):

    # Takes a qubit as input, and returns the string representation of the NOT gate on that qubit
    # Brackets are added to prevent ambiguity in the string representation of the circuit

    qubit = '( ¬ ' + qubit + ' )'
    return qubit

def cNOTString(qubitControl, qubitTarget):
    qubitTarget = ' ( ( ¬ ' + qubitTarget + ' ) /\\ ' + qubitControl + ' ) \\/ ( ' + qubitTarget + ' /\\ ( ¬ ' + qubitControl + ' ) )'
    return qubitTarget

def toffoliString(qubitControlOne, qubitControlTwo, qubitTarget):

    # Takes a qubit as input, and returns the string representation of the Toffoli gate with first two arguments as control bits and the third as target bits
    # Brackets are added to prevent ambiguity in the string representation of the circuit
    
    qubitTarget = ' ( ( ¬ ' + qubitTarget + ' )' + ' /\\ ( ' + qubitControlOne + ' /\\ ' + qubitControlTwo + ' ) ) ' + '\\/ ( ' + qubitTarget + ' /\\' + ' ( ¬ ( ' + qubitControlOne + ' /\\ ' + qubitControlTwo + ' ) ) )'
    return qubitTarget

def get_qc_string(qc):
    gateList = retrieveGates(qc)
    #prepares the initial state of qubits
    qubitStates = []
    for i in range(len(qc.qubits)):
        qubitStates.append('q' + str(i))

    #applies the circuit gates to the qubits and modifies the qubitStates list in place
    for gate in gateList:
        if gate[0] == 'ccx':
            qubitStates[gate[1][2]] = toffoliString(qubitStates[gate[1][0]], qubitStates[gate[1][1]], qubitStates[gate[1][2]])
        elif gate[0] == 'x':
            qubitStates[gate[1][0]] = NOTString(qubitStates[gate[1][0]])
        elif gate[0] == 'cx':
            qubitStates[gate[1][1]] = cNOTString(qubitStates[gate[1][0]], qubitStates[gate[1][1]])

    return qubitStates
