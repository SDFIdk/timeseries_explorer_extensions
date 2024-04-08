import ee
ee.Initialize()

bandNames = ['LST_1KM']

collection = ee.ImageCollection("NOAA/VIIRS/001/VNP21A1D") \
    .select(['LST_1KM'], bandNames)

bandColors = {
    'LST_1KM': '#bd1717',
}
