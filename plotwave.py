import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter

def echelle(freq, power, dnu, ax=None, sigma=None, nlevels=32, cmap='Greys', power_norm=False):
	'''
	Takes a power spectrum with regular frequency spacing (dnu) and plots an echelle diagram
	
	freq: Frequency bins [array]
	power: Power bins, len(power) == len(freq)
	dnu: Expected separation of modes, peaks, etc. [scaler]
	
	ax: Can specify an axis [e.g. ax = plt.figure()]
	sigma: width of Gaussian smoothing [frequency units]
	nlevels: number of different colour contours
	cmap: colourmap
	power_norm: linearly normalises power such that max/min power is 1/0 respectively.
	
	Tip: if you don't know the value of dnu, use the maximum of the autocorrelated power, works best with equally spaced bins
	'''
	
	
	n = len(np.where(freq < dnu)[0])
	m = int(np.ceil(len(freq)/n)+1)
	
	t_power = np.concatenate(( power, np.zeros(n*m-len(freq)) ))
	t_freq = np.concatenate(( freq, np.zeros(n*m-len(freq)) ))	

	
	if sigma is not None:
		s_width = len(np.where(freq < sigma)[0])
		s_power = gaussian_filter(t_power, sigma=s_width)
	else:
		s_power = t_power
		
	mat = np.reshape(s_power,(m,n))

	if power_norm: 
		s_power -= min(s_power)
		s_power /= max(s_power)
		
	mat = np.reshape(s_power,(m,n))
	
	return

	for i in range(m):
		if ax is not None:
			plt.contourf(np.arange(n)/(n-1.0)*dnu,np.array([i,i+1])*dnu,[mat[i:i+1,:][0], mat[i:i+1,:][0]], \
				cmap=plt.cm.get_cmap(cmap),levels=np.arange(0,max(s_power)*1.00001,max(s_power)/nlevels))
		else:			
			ax.contourf(np.arange(n)/(n-1.0)*dnu,np.array([i,i+1])*dnu,[mat[i:i+1,:][0], mat[i:i+1,:][0]], \
				cmap=plt.cm.get_cmap(cmap),levels=np.arange(0,max(s_power)*1.00001,max(s_power)/nlevels))
	return
