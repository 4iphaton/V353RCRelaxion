import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
import math

U_0 = 18.6/2

fr, ph = np.genfromtxt('content/values/phasen.txt',unpack=True)
fr, U = np.genfromtxt('content/values/amplitudenpol.txt',unpack=True)
U /= 2
U /=U_0
fr *= 2*np.pi
ph /= 1000
i=0
while i<len(ph):
    ph[i]*=fr[i]
    i += 1
print('pi/',const.pi/ph)
#ph = np.sin(ph)
#A/U_0=sin(ph)/wRC

x=np.arange(fr[0],fr[len(fr)-1],10)
r=1/np.sqrt(1+(x**2)*((1.422e-3)**2))
theta=np.arcsin(x*1.422e-3/np.sqrt(1+(x**2)*((1.422e-3)**2)))
print(ph,U, fr)
pol = plt.subplot(111,projection='polar')
pol.plot(ph,U,'rx',label='Messwerte')
pol.plot(theta,r,'b-',label='Theoriekurve über RC der Amplitude')
pol.set_rticks([0.2, 0.4, 0.6, 0.8])
pol.set_xticklabels([r'$0$', r'$\pi /4', r'$\pi /2$', r'$3\pi /4$', r'$\pi$', r'$5\pi /4$', r'$3\pi /2$', r'$7\pi /4$'])
pol.grid(True)
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/polar.pdf')
print('------------------')
