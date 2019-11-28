import numpy as np
from scipy import integrate


class FourierPlot:
    def __init__(self, byte, bit_rate=1000, amplitude=1.0):
        self.byte = int(byte) & 0xFF
        self.bit_rate = bit_rate
        self.amplitude = amplitude
        self.T = 8 / bit_rate
        self.freq = 1 / self.T
        self.step = self.T / 8
        self.series_count = 0

    def __bit__(self, x):
        """ gets the (x % 8)th bit within self.byte """
        val = int(x/self.step)
        return (self.byte & (1 << (val % 8))) >> (val % 8)

    def add_waveform(self, axis, periods=2):
        xs = np.linspace(0, self.T * periods, 1000)
        ys = np.array([self.__bit__(x) * self.amplitude for x in np.flip(xs)])
        axis.plot(xs, ys, color='b')

    def add_fourier(self, axis, n, periods=2):
        # faster way to calculate the DC component of an 8-bit interger
        c = (bin(self.byte).count('1') / 8) * self.amplitude

        def coef(f, n):
            def g(t):
                return (self.__bit__(t) * self.amplitude) * f(2*np.pi * n * self.freq * t)
            return (2/self.T) * integrate.quad(g, 0.0, self.T)[0]

        def g_sum(f, n, x):
            return np.sum([coef(f, j) * f(2*np.pi*j*self.freq*x) for j in np.arange(1, n+1)])

        xs = np.linspace(0, self.T * periods, 1000)
        ys = [c/2 + g_sum(np.sin, n, x) + g_sum(np.cos, n, x)
              for x in np.flip(xs)]
        axis.plot(xs, ys)
