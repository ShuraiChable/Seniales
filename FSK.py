import numpy as np
import matplotlib.pyplot as plt

v=[0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0] # impulso binario
dim=100 # número de muestras a tomar 
Vx=[] #aqui se almacenará los valores para graficar
di=[]

#recorremos el vector
for i in range(1, 11):
    f=np.ones(dim)
    x=f*v[i]
    Vx=np.concatenate((Vx, x))

# graficamos el mensaje en impulsos de bit
dim2=len(Vx)
t=np.linspace(0, 5, dim2)
# generamos las ondas senoidales (CANAL)
f1=5 # frecuencia de 5 hz
w1=2*np.pi*f1*t 
y1=np.cos(w1)
# generamos las ondas senoidales (CANAL) aumentamos la frecuencia
f2=20
w2=2*np.pi*f2*t 
y2=np.cos(w2)
# generamos la salida de la función
for i in range(0, dim2):
    if Vx[i]==0:
        cero=np.array([y1[i]])
        di=np.concatenate((di, cero))
    else:
        uno=np.array([y2[i]])
        di=np.concatenate((di, uno))

# generamos las salidas
plt.subplot(711)
plt.plot(t, Vx, linewidth=0.5)
plt.title("Señal del mensaje", fontsize=12)
plt.xlabel("tiempo")
plt.ylabel("amplitud")

plt.subplot(713)
plt.plot(t, y1, linewidth=0.5)
plt.title("Función portadora (1er Canal)", fontsize=12)
plt.xlabel("tiempo")
plt.ylabel("amplitud")

plt.subplot(715)
plt.plot(t, y2, linewidth=0.5)
plt.title("Función portadora (2do Canal)", fontsize=12)
plt.xlabel("tiempo")
plt.ylabel("amplitud")

plt.subplot(717)
plt.plot(t, di, linewidth=0.5)
plt.title("Señal modulada", fontsize=12)
plt.xlabel("tiempo")
plt.ylabel("amplitud")

plt.show()