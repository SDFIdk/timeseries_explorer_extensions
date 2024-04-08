# import ee

# ee.Initialize()

# def add_scaled_lst_band(image):
#     """Scales the LST_Day_1km band of an image."""
#     scaled_lst = image.select('MODIS_LST').multiply(0.02)
    
#     return image.addBands(scaled_lst, overwrite=True)


# # bandNames = ['COMBINED_LST', 'LANDSAT_LST', 'MODIS_LST']
# modis_bandnames = ['MODIS_LST']
# landsat_bandnames = ['LANDSAT_QA_PIXEL', 'LANDSAT_LST']

# modis = ee.ImageCollection('MODIS/061/MOD11A2') \
#     .select(['LST_Day_1km'], modis_bandnames)
# modis = modis.map(add_scaled_lst_band)

# l8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2') \
#     .select(['QA_PIXEL', 'ST_B10'], landsat_bandnames)
# l9 = ee.ImageCollection('LANDSAT/LC09/C02/T1_L2') \
#     .select(['QA_PIXEL', 'ST_B10'], landsat_bandnames)

# collections = [l8, l9, modis]
# collection = ee.ImageCollection([])
# for li in collections:
#     collection = collection.merge(li)

# collection = ee.ImageCollection(collection)

# # modis = ee.ImageCollection(modis)
# # collection.merge(modis)
    
# # collection = ee.ImageCollection([landsat_collection, modis])
    
# # default colors for bands and spectral indices
# bandColors = {
#     'MODIS_LST_K': '#bd1717',
#     'LANDSAT_LST': '#4861c7',
#     'QA_PIXEL': '#b4b4b4'
# }
    

# # # mapping from spectral index formular identifiers to image bands
# # wavebandMapping = {
# #     'MODIS': 'LST_Day_1km',
# #     'LANDSAT': 'THERMAL'
# # }

# qaFlags = {
#         "QA_PIXEL": ["Fill", "Dilated Cloud", "Cirrus (high confidence)", "Cloud", "Cloud Shadow", "Snow"]
# }

#--------------------------------

import ee

ee.Initialize()

landsat_bandnames = ['LANDSAT_QA_PIXEL', 'LANDSAT_LST']

# Landsat 8 and 9 collections with renamed bands
l8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2') \
    .select(['QA_PIXEL', 'ST_B10'], landsat_bandnames)
l9 = ee.ImageCollection('LANDSAT/LC09/C02/T1_L2') \
    .select(['QA_PIXEL', 'ST_B10'], landsat_bandnames)

# Define the function to add and scale the LST band for MODIS images
def add_scaled_lst_band(image):
    # Scale the 'LST_Day_1km' band by the factor (0.02) to convert to Kelvin
    scaled_lst = image.select(['LST_Day_1km']).multiply(0.02)
    # Update the band name to reflect it's been scaled and to avoid confusion
    return image.addBands(scaled_lst.rename('MODIS_LST_K'))

# MODIS LST Day 1km band, adding it as a separate collection and applying the scaling
modis = ee.ImageCollection('MODIS/061/MOD11A2') \
    .select(['LST_Day_1km']) \
    .map(add_scaled_lst_band)  # Apply the scaling function to each image

# Merge the Landsat collections
collection = ee.ImageCollection(l8.merge(l9))

# collection = ee.FeatureCollection([collection, modis])

# Default colors for bands and spectral indices
bandColors = {
    'MODIS_LST_K': '#bd1717',  # MODIS LST
    'LANDSAT_LST': '#4861c7',  # Landsat LST
    'QA_PIXEL': '#b4b4b4'  # QA Pixel
}

qaFlags = {
    "QA_PIXEL": ["Fill", "Dilated Cloud", "Cirrus (high confidence)", "Cloud", "Cloud Shadow", "Snow"]
}