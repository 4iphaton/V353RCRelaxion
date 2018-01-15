import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
import math

fr, ph = np.genfromtxt('content/values/phasen.txt',unpack=True)
fr *= 2*np.pi
ph /= 1000
i=0
while i<len(ph):
    ph[i]*=fr[i]
    i += 1
print(ph)
ph = np.sin(ph)
print(ph, fr)

def f(x, a):
    return a*x/np.sqrt(1+(a**2)*(x**2))

parameters, pcov = curve_fit(f, fr, ph)
errors = np.sqrt(np.diag(pcov))

print('RC= ',parameters[0],'pm',errors[0])
ln = np.linspace(fr[0],fr[len(fr)-1],5000)
ax = plt.subplot(1,1,1)
ax.set_xscale("log", nonposx='clip')
ax.plot(ln, f(ln, *parameters), 'r-', label='Fit')
ax.plot(fr,ph,'bx',label='Werte')
plt.xlabel(r'$\omega$')
plt.ylabel(r'$\text{sin}(\phi)$')
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('build/phasen.pdf')
print('------------------')
