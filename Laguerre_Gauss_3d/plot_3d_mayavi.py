"""
file:   plot_3d_mayavi.py
brief:  Python script to visualise (intensity) isosurfaces of scattered vortex beams. 
        The program uses as input an HDF5 file generated by the FDTD solver Meep.
author: Daniel Kotik
date:   19.01.2018

invocation: ipython plot_3d_mayavi.py LaguerreGauss3d-out/e2_s-000001232.h5
"""

import numpy as np
import h5py
import sys
from   mayavi import mlab
import matplotlib.pyplot as plt

filename = sys.argv[1]
#filename = "LaguerreGauss3d-out/e2_s-000010.00.h5"

cutoff = 30   # cut-off borders of data (removing PML layer and line source placment is desired)

with h5py.File(filename, 'r') as hf:
    print("Keys: %s" % hf.keys())
    #data = hf['e2_s'][:]
    data = hf[hf.keys()[0]][:]   # use first data set

print(np.shape(data))

print(data.max(), data.min())

data_optimised = np.transpose(data[cutoff:-cutoff, cutoff:-cutoff, cutoff:-cutoff]) / data.max()

mlab.figure(bgcolor=(1,1,1))

#mlab.contour3d(data_optimised, contours=10, colormap="hot", transparent=True, opacity=0.5)
mlab.pipeline.volume(mlab.pipeline.scalar_field(data_optimised), vmin=0.02, vmax=0.3) #intensity
#mlab.pipeline.volume(mlab.pipeline.scalar_field(data_optimised)) #interface
#mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(data_optimised),
#                            plane_orientation='x_axes',
#                            slice_index=10,
#                        )
#mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(data_optimised),
#                            plane_orientation='y_axes',
#                            slice_index=10,
#                        )
#mlab.outline()

mlab.show()

