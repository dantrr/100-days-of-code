import numpy_financial as npf

retire = npf.pmt(rate=0.07/12, nper=10*12, pv=0, fv=950000)

print(retire)