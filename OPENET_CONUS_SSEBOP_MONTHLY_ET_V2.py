import ee
ee.Initialize()

"""
https://developers.google.com/earth-engine/datasets/catalog/OpenET_DISALEXI_CONUS_GRIDMET_MONTHLY_v2_0
"""

bandNames = [
    'et'
    ]

displayNames = [
    'ET'
]

collection = ee.ImageCollection("OpenET/DISALEXI/CONUS/GRIDMET/MONTHLY/v2_0") \
    .select(bandNames, displayNames)

bandColors = {
    'ET': '#4842f5',
}
