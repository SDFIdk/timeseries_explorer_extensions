import ee

ee.Initialize()

landsat_bandnames = ['LANDSAT_QA_PIXEL', 'LANDSAT_LST']

l8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2') \
    .select(['QA_PIXEL', 'ST_B10'], landsat_bandnames)
l9 = ee.ImageCollection('LANDSAT/LC09/C02/T1_L2') \
    .select(['QA_PIXEL', 'ST_B10'], landsat_bandnames)

collections = [l8, l9, modis]
collection = ee.ImageCollection([])
for li in collections:
    collection = collection.merge(li)
    
# default colors for bands and spectral indices
bandColors = {
    'MODIS_LST_K': '#bd1717',
    'LANDSAT_LST': '#4861c7',
    'QA_PIXEL': '#b4b4b4'
}
    
qaFlags = {
        "QA_PIXEL": ["Fill", "Dilated Cloud", "Cirrus (high confidence)", "Cloud", "Cloud Shadow", "Snow"]
}
