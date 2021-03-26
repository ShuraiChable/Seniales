import numpy as np 
import matplotlib.pyplot as plt


# rango de los valores en tiempo (eje x)
tiempo=np.arange(0, 0.1, 10**(-5.7)) # número de ondas
Fc=300 # frecuencia

x=np.sin(40*np.pi*tiempo) # mensaje
w=np.sin(2*Fc*np.pi*tiempo) # portadora
p=w*x # salida de la función

plt.subplot(511)
plt.plot(tiempo, x, linewidth=0.4)
plt.title("Señal del mensaje", fontsize=12)
plt.xlabel("tiempo")
plt.ylabel("amplitud")

plt.subplot(513)
plt.plot(tiempo, w, linewidth=0.4)
plt.title("Función portadora (Canal)", fontsize=12)
plt.xlabel("Índice de tiempo")
plt.ylabel("amplitud")

plt.subplot(515)
plt.plot(tiempo, p, linewidth=0.4)
plt.title("Señal modulada", fontsize=12)
plt.xlabel("Índice de tiempo")
plt.ylabel("amplitud")

plt.show()

