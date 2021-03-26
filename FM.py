import numpy as np
import matplotlib.pyplot as plt
plt.title("FM")
# rango de los valores en tiempo (eje x)
tiempo=np.arange(0, 0.01, 10**(-5.7)) #número de ondas
fm1=10**3 # frecuencia inicial
fc=20 # frecuencia moduladora
fe=0.7*fc # frecuencia de la función final

x=2*np.sin(2*np.pi*fm1*tiempo) # mensaje
r=2*np.sin(fc*np.pi*fm1*tiempo) # portadora
y=np.sin(2*np.pi*fc+(fe*np.sin(2*np.pi*fm1*tiempo))) # salida de la función

# generamos nuestras salidas
plt.subplot(511)
plt.plot(tiempo, x, linewidth=0.4)
plt.title("Señal del mensaje", fontsize=12)
plt.xlabel("tiempo")
plt.ylabel("amplitud")

plt.subplot(513)
plt.plot(tiempo, r, linewidth=0.4)
plt.title("Función portadora (Canal)", fontsize=12)
plt.xlabel("tiempo")
plt.ylabel("amplitud")

plt.subplot(515)
plt.title("Señal modulada", fontsize=12)
plt.plot(tiempo, y, linewidth=0.4)
plt.xlabel("tiempo")
plt.ylabel("amplitud")

plt.show()