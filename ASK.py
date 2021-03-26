import numpy as np 
import matplotlib.pyplot as plt

v=[0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0] # impulso binario
dim=100 # número de muestras a tomar 
Vx=[] #aqui se almacenará los valores para graficar

#recorremos el vector
for i in range(1, 11):
    f=np.ones(dim)
    x=f*v[i]
    Vx=np.concatenate((Vx, x))
# graficamos el mensaje en impulsos de bit
dim2=len(Vx)
t=np.linspace(0, 5, dim2)
f1=5
# generamos las ondas senoidales (CANAL)
w1=2*np.pi*f1*t 
y1=np.cos(w1)
# generamos la salida de la función
mult=(Vx*y1)

# generamos las salidas
plt.subplot(511)
plt.plot(t, Vx, linewidth=0.5)
plt.title("Señal del mensaje", fontsize=12)
plt.xlabel("tiempo")
plt.ylabel("amplitud")

plt.subplot(513)
plt.plot(t, y1, linewidth=0.5)
plt.title("Función portadora (Canal)", fontsize=12)
plt.xlabel("tiempo")
plt.ylabel("amplitud")

plt.subplot(515)
plt.plot(t, mult, linewidth=0.5)
plt.title("Señal modulada", fontsize=12)
plt.xlabel("tiempo")
plt.ylabel("amplitud")

plt.show()