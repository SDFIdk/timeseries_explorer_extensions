import numpy as np

import ee

ee.Initialize()

bandNames = ['LST_Day_1km', 'Day_view_time']

collection = ee.ImageCollection('MODIS/061/MOD11A2') \
    .select(['LST_Day_1km', 'Day_view_time'], bandNames)

# default colors for bands and spectral indices
bandColors = {
    'LST_Day_1km': '#bd1717',
    'Day_view_time': '#4861c7',
    'LST_K': '#e31212'
}

def add_scaled_lst_band(image):
    """Scales the LST_Day_1km band of an image."""
    scaled_lst = image.select('LST_Day_1km').multiply(0.02).rename('LST_K')
    
    return image.addBands(scaled_lst, overwrite=True)

# def add_scaled_lst_band(image):
#     """Adds a scaled version of the LST_Day_1km band as a new band 'LST_K'."""
#     scaled_lst = image.select(['LST_Day_1km']).multiply(0.02).rename('LST_K')
    
#     return image.addBands(scaled_lst)


collection = collection.map(add_scaled_lst_band)

# # mapping from spectral index formular identifiers to image bands
# wavebandMapping = {
#     'LST': 'LST_Day_1km',
#     'T': 'Day_view_time',
#     'LST_K': 'LST_K'
# }
