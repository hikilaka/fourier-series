from matplotlib import pyplot
from fourier_plot import FourierPlot


if __name__ == '__main__':
    fig, (left_axis, right_axis) = pyplot.subplots(1, 2, sharey=True)

    fig.set_size_inches(10, 5)
    left_axis.grid()
    right_axis.grid()

    plot = FourierPlot(0xC0, 2000, 5.0)

    # adds the oscilating wave our fourier series is mimicing
    plot.add_waveform(left_axis)

    # add some varying n'th order harmonics
    plot.add_fourier(right_axis, 1)
    plot.add_fourier(right_axis, 5)
    plot.add_fourier(right_axis, 10)

    left_axis.legend(['Original Wave'])
    right_axis.legend(['1st Order', '5th Order', '10th Order'])
    pyplot.show()
