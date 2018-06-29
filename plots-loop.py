
import numpy
import matplotlib.pyplot
#import operating system
import os
import matplotlib.backends.backend_pdf

pdf = matplotlib.backends.backend_pdf.PdfPages("plots.pdf")
#loop where we plot our graphics
for filename in os.listdir('C:/Users/Ainhoa/Desktop/Python/data'):
	if filename.startswith("inflammation"):
		
		data = numpy.loadtxt(fname=filename, 
		delimiter=',')

		fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

		axes1 = fig.add_subplot(1, 3, 1)
		axes2 = fig.add_subplot(1, 3, 2)
		axes3 = fig.add_subplot(1, 3, 3)

		axes1.set_ylabel('average')
		axes1.plot(numpy.mean(data, axis=0))

		axes2.set_ylabel('max')
		axes2.plot(numpy.max(data, axis=0))

		axes3.set_ylabel('min')
		axes3.plot(numpy.min(data, axis=0))

		fig.tight_layout()
		#If we wanted to extract the graphs one by one		
		#matplotlib.pyplot.show()
		pdf.savefig ( fig)
pdf.close()
