std::vector<BDD*> PQgate::getPhaseLF()
{
  std::vector<BDD*> phaseLFs;
  for (int i = 0; i < 3; i++) {
    BDD* lf = new BDD;
    *lf = mgr.bddZero();
    phaseLFs.push_back(lf);
  }
  std::list<Qgate*>::iterator iter = qgates.begin();
	std::list<BitNo> tBits = (*iter)->getTargetBits();
	std::list<BitNo>::iterator tIter = tBits.begin();
  BitNo tNo = *tIter;
  // next_lf[tNo]->PrintMinterm();
  // std::cout << "" << '\n';
  std::list<CB> cBits = (*iter)->getControlBits();
  if(cBits.size() < 2){  // tNo != target bit
    return phaseLFs;
  }

  std::list<CB>::iterator cIter = cBits.begin();
  BDD* phaseLF = new BDD;
  *phaseLF = mgr.bddOne();

  (*phaseLF) = (*phaseLF) * (*prev_lf[(*cIter).bitNo]); // c1
	cIter++;
  (*phaseLF) = (*phaseLF) * (*prev_lf[(*cIter).bitNo]); // c2
  (*phaseLF) = (*phaseLF) * !(*prev_lf[tNo]); // t
  cIter--;
  *phaseLFs[0] = *phaseLFs[0] | *phaseLF;


  *phaseLF = mgr.bddOne();
  (*phaseLF) = (*phaseLF) * (*prev_lf[(*cIter).bitNo]); // c1
	cIter++;
  (*phaseLF) = (*phaseLF) * !(*prev_lf[(*cIter).bitNo]); // c2
  (*phaseLF) = (*phaseLF) * (*prev_lf[tNo]); // t
  cIter--;
  *phaseLFs[1] = *phaseLFs[1] | *phaseLF; // pi

  *phaseLF = mgr.bddOne();
  (*phaseLF) = (*phaseLF) * (*prev_lf[(*cIter).bitNo]); // c1
	cIter++;
  (*phaseLF) = (*phaseLF) * (*prev_lf[(*cIter).bitNo]); // c2
  (*phaseLF) = (*phaseLF) * (*prev_lf[tNo]); // t
  cIter--;
  *phaseLFs[2] = *phaseLFs[2] | *phaseLF; // -pi/2

  return phaseLFs;

}
