import numpy as np

def plot_echelle(freq, power, dnu, ax=None, sigma=0.25, nlevels=32, cmap='Greys', power_norm=False):

	n = len(np.where(freq < dnu)[0])
	m = int(np.ceil(len(freq)/n)+1)


	s_width = len(np.where(freq < sigma)[0])

	t_power = np.concatenate(( power, np.zeros(n*m-len(freq)) ))
	t_freq = np.concatenate(( freq, np.zeros(n*m-len(freq)) ))

	s_power = np.sqrt(gaussian_filter(t_power, sigma=s_width))


	if power_norm: s_power = s_power-min(s_power)
	mat = np.reshape(s_power,(m,n))

	for i in range(m):
		if ax is not None:
			plt.contourf(np.arange(n)/(n-1.0)*dnu,np.array([i,i+1])*dnu,[mat[i:i+1,:][0], mat[i:i+1,:][0]], \
				cmap=plt.cm.get_cmap(cmap),levels=np.arange(0,max(s_power)*1.001,max(s_power)/nlevels))
		else:			
			ax.contourf(np.arange(n)/(n-1.0)*dnu,np.array([i,i+1])*dnu,[mat[i:i+1,:][0], mat[i:i+1,:][0]], \
				cmap=plt.cm.get_cmap(cmap),levels=np.arange(0,max(s_power)*1.001,max(s_power)/nlevels))
	return
