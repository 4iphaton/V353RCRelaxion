import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
import math

U_0 = 18.6/2

fr, U = np.genfromtxt('content/values/amplituden.txt',unpack=True)
U /= 2
U /=U_0
fr *= 2*np.pi

print(U, fr)

def f(x, a):
    return 1/np.sqrt(1+(a**2)*(x**2))

parameters, pcov = curve_fit(f, fr, U)
errors = np.sqrt(np.diag(pcov))

print('RC= ',parameters[0],'pm',errors[0])
ln = np.linspace(fr[0],fr[len(fr)-1],5000)

plt.plot(np.log10(ln), f(ln, *parameters), 'r-', label='Fit Aufladung')
plt.plot(np.log10(fr),U,'bx',label='Werte Entladung')
plt.xlabel(r'$\text{log}_{10}(\omega)$')
plt.ylabel(r'$A/U_0$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/amplituden.pdf')
print('------------------')
