#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
	The colouring.py applies colour mapping to grid data.
	Copyright (C) 2015 The University of Sydney, Australia

	This program is free software; you can redistribute it and/or
	modify it under the terms of the GNU General Public License, version 2,
	as published by the Free Software Foundation.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program; if not, write to the Free Software
	Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

	*******************************************************************************
	  
    Filename: colouring.py
    Author: Xiaodong Qin
    Email: michael.chin@sydney.edu.au
    
	Get latest version and submit bug report at 
	GitHub: https://github.com/GPlates/Portal/blob/master/Utils/colouring.py
	
    This function applies colours on grid data.
    
    Parameters:
        data:      a 2-d numpy array 
        colours:   a list of colours to be used to create colour map
        steps:     a list of values to be used to intepolate colours
                   The 'steps' list must have the exactly same size as the 'colours' list does.
    Return:
        coloured and shaded grid data in RGB
		
	Example:
	dataset = gdal.Open('GRID_DATA.nc', GA_ReadOnly )
	band = dataset.GetRasterBand(1)
	r = band.ReadAsArray( 0, 0, band.XSize, band.YSize, band.XSize, band.YSize)
	colours = [
			[0,0,255],
			[0,255,255],
			[0,255,0],
			[0,255,0],
			[255,255,0],
			[255,0,0],
		]
	steps = [-200, -100, -50, 50, 100, 200]
	rgb = colouring(np.array(r,colours, steps)
	plt.imshow(rgb)
'''

import shading
from matplotlib.colors import LinearSegmentedColormap

def colouring(data, colours, steps):
    colour_list = []
    for i in range(len(steps)):
        colour_list.append((float(steps[i]-steps[0])/(steps[-1]-steps[0]), [x/255.0 for x in colours[i]]))

    my_cmap = LinearSegmentedColormap.from_list('my_cmap', colour_list, N=1024)
    return shading.shade(data, cmap=my_cmap, intensity=shading.intensity(data))
