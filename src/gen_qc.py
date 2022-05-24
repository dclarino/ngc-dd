from qiskit import *

def build_qc(qc_args):
    qr_out = QuantumRegister(len(qc_args["variables"].keys()))
    qc_out = QuantumCircuit(qr_out)
    for gate in qc_args["gates"]:
        if("CNOT" in gate["type"]):
            qc_out.x(qr_out[gate["i_vars_int"][0]])
        elif("MCT" in gate["type"]):
            c_qubits = []
            for int_var in gate["i_vars_int"]:
                c_qubits.append(qr_out[int_var])
            o_qubits = [qr_out[gate["o_vars_int"][0]]]
            qc_out.mct(c_qubits,o_qubits)

    return qc_out
                     



