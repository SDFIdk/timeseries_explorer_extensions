import ee
ee.Initialize()

"""
https://developers.google.com/earth-engine/datasets/catalog/OpenET_ENSEMBLE_CONUS_GRIDMET_MONTHLY_v2_0
"""

bandNames = [
    'et_ensemble_mad', 
    'et_ensemble_mad_min', 
    'et_ensemble_mad_max',
    'et_ensemble_sam'
    ]

displayNames = [
    'Median absolute deviation',
    'Median absolute deviation minimum',
    'Median absolute deviation maximum',
    'Simple arithmetic mean'
]

collection = ee.ImageCollection("OpenET/ENSEMBLE/CONUS/GRIDMET/MONTHLY/v2_0") \
    .select(bandNames, displayNames)

bandColors = {
    'Median absolute deviation': '#4842f5',
    'Median absolute deviation minimum': '#16128a',
    'Median absolute deviation maximum': '#504dbf',
    'Simple arithmetic mean': '#26a64f',
}
