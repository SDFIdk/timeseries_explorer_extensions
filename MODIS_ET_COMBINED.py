import numpy as np

import ee

ee.Initialize()

bandNames = ['ET', 'LE', 'PET', 'PLE']
displayNames = ['Total ET', 'Avg lat heat flux', 'Total PET', 'Avg pot lat heat flux']

terra = ee.ImageCollection("MODIS/061/MOD16A2") \
    .select(bandNames, displayNames)

aqua = ee.ImageCollection("MODIS/061/MYD16A2") \
    .select(bandNames, displayNames)

collections = [aqua, terra]

collection = ee.ImageCollection([])
for li in collections:
    collection = collection.merge(li)

# default colors for bands and spectral indices
bandColors = {
    'Total ET': '#0345fc',
    'Avg lat heat flux': '#0345fc',
    'Total PET': '#0345fc',
    'Avg pot lat heat flux': '#fc035e' 
}