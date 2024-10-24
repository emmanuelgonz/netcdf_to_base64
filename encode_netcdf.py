import netCDF4 as nc

# Open the NetCDF file
file_path = 'efficiency_snow_cover.nc'
dataset = nc.Dataset(file_path, mode='r')

# Print the dataset information
print(dataset)