import pandas as pd
import cartopy.crs as ccrs
import cartopy.feature as cf
from matplotlib import pyplot as plt


# Read csv files, first is precovid flights, second postcovid flights, and last is airports
precf = pd.read_csv("Files/precovid_flights.csv", sep=";")
postcf = pd.read_csv("Files/postcovid_flights.csv", sep=";")
airports = pd.read_csv("Files/airports.dat", sep=",")

# Merge the airports table and the pre-postcovid flights one
precf_coord = pd.merge(precf, airports[['Longitude', 'Latitude', 'IATA']], on='IATA')
postcf_coord = pd.merge(postcf, airports[['Longitude', 'Latitude', 'IATA']], on='IATA')

# Draw a map of Europe using cartopy
proj = ccrs.PlateCarree()
ax = plt.axes(projection=proj)
ax.set_extent([-13, 45, 30, 70])
ax.stock_img()
ax.add_feature(cf.COASTLINE, lw=2)
ax.add_feature(cf.BORDERS)
plt.gcf().set_size_inches(20, 10)

# Save figure as PNG and set title
plt.title("Pre- and Postcovid direct flights from Tallinn\nMariano D'Angelo\n", fontsize=20)
plt.savefig("Flights.png")
