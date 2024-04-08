# Title: ERA5-Land Daily Aggregated - Produced by ECMWF / Copernicus Climate Change Service

import ee

# bands = ee.List(
#     ['temperature_2m', 'temperature_2m_min', 'temperature_2m_max', 'dewpoint_temperature_2m',
#      'total_precipitation_sum', 'surface_pressure'])
# band_names = ee.List(
#     ['Average air temperature at 2m K', 'Minimum air temperature at 2m K', 'Maximum air temperature at 2m K',
#      'Dewpoint temperature at 2m K', 'Total precipitation m', 'Surface pressure Pa'])
bands = ee.List(
    ['temperature_2m'])
band_names = ee.List(
    ['Average air temperature at 2m K'])

era5d = ee.ImageCollection("ECMWF/ERA5_LAND/HOURLY").select(bands, band_names)

era5d = era5d.map(lambda image: image.addBands(
    image.expression("(b('Average air temperature at 2m K') - 273.15)").rename('Average air temperature at 2m DegC')))

# era5d = era5d.map(lambda image: image.addBands(
#     image.expression("(b('Minimum air temperature at 2m K') - 273.15)").rename('Minimum air temperature at 2m DegC')))

# era5d = era5d.map(lambda image: image.addBands(
#     image.expression("(b('Maximum air temperature at 2m K') - 273.15)").rename('Maximum air temperature at 2m DegC')))

# era5d = era5d.map(lambda image: image.addBands(
#     image.expression("(b('Dewpoint temperature at 2m K') - 273.15)").rename('Dewpoint temperature at 2m DegC')))

# era5d = era5d.map(lambda image: image.addBands(
#     image.expression("(b('Total precipitation m') * 1000)").rename('Total precipitation mm')))

# era5d = era5d.map(
#     lambda image: image.addBands(image.expression("(b('Surface pressure Pa') / 100)").rename('Surface pressure hPa')))

bandColors = {
    'Average air temperature at 2m K': '#ff7f00',
    # 'Minimum air temperature at 2m K': '#27c9ff',
    # 'Maximum air temperature at 2m K': '#ff0400',
    # 'Dewpoint temperature at 2m K': '#00ff0c',
    # 'Total precipitation m': '#0026ff',
    # 'Surface pressure Pa': '#fdae61',
    # 'Average air temperature at 2m DegC': '#ff7f00',
    # 'Minimum air temperature at 2m DegC': '#27c9ff',
    # 'Maximum air temperature at 2m DegC': '#ff0400',
    # 'Dewpoint temperature at 2m DegC': '#00ff0c',
    # 'Total precipitation mm': '#0026ff',
    # 'Surface pressure hPa': '#fdae61',
}

collection = era5d
