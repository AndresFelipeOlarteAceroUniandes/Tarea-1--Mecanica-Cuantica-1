import numpy as np
import matplotlib.pyplot as plt

h = 6.626e-34   
c = 3.0e8      
k_B = 1.381e-23 
b = 2.898e-3    

def planck(lmbda, T):
    return (2*np.pi*c**2*h) / (lmbda**5*(np.exp(h*c/(lmbda*k_B*T))-1))

temperaturas = [100, 5800, 120000]  

lmbda = np.linspace(1e-9, 3e-4, 1000000) 

for i, T in enumerate(temperaturas):
    plt.figure()
    I = planck(lmbda, T)
    lmbda_max = b / T

    plt.plot(lmbda * 1e9, I, label=f"T = {T}K, λ_max ≈ {lmbda_max*1e9:.2f} nm") 
    plt.axvline(lmbda_max * 1e9, color="b", linestyle="dashed", alpha=0.5, label="λ_max")

    plt.xscale("log")
    plt.xlim(1, 500000)
    plt.xlabel("Longitud de onda (nm)")
    plt.ylabel("Intensidad espectral I(λ, T)")
    plt.title("Ley de Planck para temperaturas")
    plt.legend()
    plt.grid()
    plt.show()
