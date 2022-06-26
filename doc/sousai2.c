std::vector<BDD*> Circuit::calc_phase(){
  PQgate* gate = getFirstGate();
  std::vector<BDD*> totalPhases;
  for (int i = 0; i < 4; i++) {
    BDD* phase = new BDD;
    *phase = mgr.bddZero();
    totalPhases.push_back(phase);
  }
  *totalPhases[0] = mgr.bddOne();
  int index = 0;
  while(gate != NULL){
    std::vector<BDD*> phaseLFs;
    phaseLFs = gate->getPhaseLF();

    BDD* tmp = new BDD;

    // phase +pi/2 : phaseLFs[0]
    *tmp = mgr.bddZero();
    (*tmp) = (*tmp) | (*totalPhases[3]); // tmp = 3pi/2
    (*totalPhases[3]) = (*totalPhases[3]) ^ ((*phaseLFs[0]) * (*totalPhases[3])); // 3pi/2 -> 0
    (*totalPhases[3]) = (*totalPhases[3]) | ((*phaseLFs[0]) * (*totalPhases[2])); // pi -> 3pi/2
    (*totalPhases[2]) = (*totalPhases[2]) ^ ((*phaseLFs[0]) * (*totalPhases[2])); // pi -> 3pi/2
    (*totalPhases[2]) = (*totalPhases[2]) | ((*phaseLFs[0]) * (*totalPhases[1])); // pi/2 -> pi
    (*totalPhases[1]) = (*totalPhases[1]) ^ ((*phaseLFs[0]) * (*totalPhases[1])); // pi/2 -> pi
    (*totalPhases[1]) = (*totalPhases[1]) | ((*phaseLFs[0]) * (*totalPhases[0])); // 0 -> pi/2
    (*totalPhases[0]) = (*totalPhases[0]) ^ ((*phaseLFs[0]) * (*totalPhases[0])); // pi/2 -> pi
    (*totalPhases[0]) = (*totalPhases[0]) | ((*phaseLFs[0]) * (*tmp)); // 0 -> pi/2

    // phase +pi : phaseLFs[1]
    *tmp = mgr.bddZero();
    (*tmp) = (*tmp) | (*totalPhases[0]); // tmp = pi/2
    (*totalPhases[0]) = (*totalPhases[0]) ^ ((*totalPhases[0]) * (*phaseLFs[1])); // 0 -> pi
    (*totalPhases[0]) = (*totalPhases[0]) | ((*totalPhases[2]) * (*phaseLFs[1])); // pi -> 0
    (*totalPhases[2]) = (*totalPhases[2]) ^ ((*totalPhases[2]) * (*phaseLFs[1])); // pi -> 0
    (*totalPhases[2]) = (*totalPhases[2]) | ((*tmp) * (*phaseLFs[1])); // 0 -> pi

    *tmp = mgr.bddZero();
    (*tmp) = (*tmp) | (*totalPhases[1]); // tmp = pi/2
    (*totalPhases[1]) = (*totalPhases[1]) ^ ((*totalPhases[1]) * (*phaseLFs[1])); // pi/2 -> 3pi/2
    (*totalPhases[1]) = (*totalPhases[1]) | ((*totalPhases[3]) * (*phaseLFs[1])); // 3pi/2 -> pi/2
    (*totalPhases[3]) = (*totalPhases[3]) ^ ((*totalPhases[3]) * (*phaseLFs[1])); // 3pi/2 -> pi/2
    (*totalPhases[3]) = (*totalPhases[3]) | ((*tmp) * (*phaseLFs[1])); // pi/2 -> 3pi/2


    // phase -pi/2 : phaseLFs[3]
    *tmp = mgr.bddZero();
    (*tmp) = (*tmp) | (*totalPhases[0]); // tmp = 0
    (*totalPhases[0]) = (*totalPhases[0]) ^ ((*phaseLFs[2]) * (*totalPhases[0])); // 0 -> 3pi/1
    (*totalPhases[0]) = (*totalPhases[0]) | ((*phaseLFs[2]) * (*totalPhases[1])); // pi/2 -> 0
    (*totalPhases[1]) = (*totalPhases[1]) ^ ((*phaseLFs[2]) * (*totalPhases[1])); // pi/2 -> 0
    (*totalPhases[1]) = (*totalPhases[1]) | ((*phaseLFs[2]) * (*totalPhases[2])); // pi -> pi/2
    (*totalPhases[2]) = (*totalPhases[2]) ^ ((*phaseLFs[2]) * (*totalPhases[2])); // pi -> pi/2
    (*totalPhases[2]) = (*totalPhases[2]) | ((*phaseLFs[2]) * (*totalPhases[3])); // 3pi/2 -> pi
    (*totalPhases[3]) = (*totalPhases[3]) ^ ((*phaseLFs[2]) * (*totalPhases[3])); // 3pi/2 -> pi
    (*totalPhases[3]) = (*totalPhases[3]) | ((*phaseLFs[2]) * (*tmp)); // 0 -> 3pi/2

    gate = gate->getNextGate();

  }

  return totalPhases;
}
