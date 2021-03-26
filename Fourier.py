# Transformadas Rapida de Fourier
# entrada funcion par
import numpy as np
import scipy.fftpack as fourier
import matplotlib.pyplot as plt

# Definir la funcion de Entrada par
def entradax(t,fs):
    x=np.cos(2*np.pi*fs*t)
    return(x)

# PROGRAMA
# INGRESO
t0=0
tn=0.5 #float(input('rango segundos [0,tn]:'))
n= 1024 #int(input(' n muestras en rango:'))

# PROCEDIMIENTO
dt=(tn-t0)/n    # intervalo de muestreo
# Analógica Referencia para mostrar que es par
fs=20
t=np.arange(-tn,tn,dt)  # eje tiempo analógica
m=len(t)
xanalog=np.zeros(m, dtype=float)
for i in range(0,m):
    xanalog[i]=entradax(t[i],fs)

# FFT: Transformada Rapida de Fourier
# Analiza la parte t>=0 de xnalog muestras[n:2*n]
xf=fourier.fft(xanalog[n:2*n])
xf=fourier.fftshift(xf)
# Rango de frecuencia para eje
frq=fourier.fftfreq(n, dt)
frq=fourier.fftshift(frq)

# x[w] real
xfreal=(1/n)*np.real(xf)
# x[w] imaginario
xfimag=(1/n)*np.imag(xf)
# x[w] magnitud
xfabs=(1/n)*np.abs(xf)
# x[w] angulo
xfangle=(1/n)*np.unwrap(np.angle(xf))

#SALIDA
plt.figure(1)       # define la grafica
plt.suptitle('Transformada Rápida Fourier FFT')

plt.subplot(321)    # grafica de 3x2, subgrafica 1
plt.ylabel('xanalog[t]')
plt.xlabel('tiempo')
plt.plot(t,xanalog)
plt.margins(0,0.05)
plt.grid()

ventana=0.2 # ventana de frecuencia a observar alrededor f=0
ra=int(len(frq)*(0.5-ventana))
rb=int(len(frq)*(0.5+ventana))
plt.subplot(323)    # grafica de 3x2, subgrafica 3
plt.ylabel('x[f] real')
plt.xlabel(' frecuencia (Hz)')
plt.plot(frq[ra:rb],xfreal[ra:rb])
plt.margins(0,0.05)
plt.grid()

plt.subplot(325)    # grafica de 3x2, subgrafica 5
plt.ylabel('x[f] imag')
plt.xlabel(' frecuencia (Hz)')
plt.plot(frq[ra:rb],xfimag[ra:rb])
plt.margins(0,0.05)
plt.grid()

plt.subplot(324)    # grafica de 3x2, subgrafica 4
plt.ylabel('x[f] magnitud')
plt.xlabel(' frecuencia (Hz)')
plt.plot(frq[ra:rb],xfabs[ra:rb])
plt.margins(0,0.05)
plt.grid()

plt.subplot(326)    # grafica de 3x2, subgrafica 6
plt.ylabel('x[f] fase')
plt.xlabel(' frecuencia (Hz)')
plt.plot(frq[ra:rb],xfangle[ra:rb])
plt.margins(0,0.05)
plt.grid()

plt.show()