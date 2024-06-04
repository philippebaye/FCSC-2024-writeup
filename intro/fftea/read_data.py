import numpy as np

# Lecture des données
data = np.fromfile("fftea", dtype = np.complex64)
#print(data)

# Calcul de la DFT (Discrete Fourier Transform) pour inverser l'opération
result = np.array(np.fft.fft(data, n=64), dtype=np.complex64)

# Récuparation de la partie réelle uniquement
result = np.real(result)
flag = ''. join([chr(int(r)) for r in result])
print(f'{flag=}')
