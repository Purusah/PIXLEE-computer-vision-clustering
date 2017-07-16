import scipy as sp
import numpy as np
import matplotlib.pyplot as plt


def errorf(f, x, y):
       return np.sum((f(x) - y)**2)

def fit(x, y, deg=2):
       f = sp.poly1d(sp.polyfit(x, y, deg))
       err = errorf(f, x, y)
       print 'Error of {} degree: {}\n'.format(deg, err)
       fx = np.linspace(0,x[-1]+0.1, 100) # generate X-values for plotting
       plt.plot(fx, f(fx), linewidth=1, label = deg)
       plt.legend(["d=%i" % f.order], loc="upper left")

deg = [1, 2, 3, 4]
data = np.loadtxt("ch01//data//web_traffic.tsv", delimiter = "\t")
x = data[:, 0]
y = data[:, 1]

x = x[np.logical_not(np.isnan(y))]
y = y[np.logical_not(np.isnan(y))]

x_norm = x / np.max(x)
y_norm = y / np.max(y)

for i in xrange(4):
       fit(x_norm, y_norm, deg[i])
plt.scatter(x_norm, y_norm, alpha = 0.75, linewidths = 1, s = 10)
plt.xticks([w*2.4*0.7 for w in np.linspace(0, 1, 11)], ["week %i" % w for w in range(10)])
plt.title("Traffic")
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.autoscale(tight=False)
plt.grid(True, linestyle="-", color="0.75")
plt.show()
