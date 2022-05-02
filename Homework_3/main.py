import pandas as pd
import cartopy.crs as ccrs
import cartopy.feature as cf
from matplotlib import pyplot as plt


def createmap_Europe():
    """
    Draw a map of Europe using cartopy
    """
    proj = ccrs.LambertCylindrical()
    ax = plt.axes(projection=proj)
    ax.set_extent([-20, 45, 25, 70])
    ax.stock_img()
    ax.add_feature(cf.COASTLINE, lw=2)
    ax.add_feature(cf.BORDERS)
    plt.gcf().set_size_inches(20, 10)


def draw_flights(flights_data, lon, lat, clr, mrkr):
    """
    Draw flights with desired color and style. Flights file must contain 
    columns Latitude and Longitude of departing country.
    """
    # without index gives error because of tuple
    for index, row in flights_data.iterrows():
        plt.plot([lon, row['Longitude']], [lat, row['Latitude']], color=clr, marker=mrkr, transform=ccrs.Geodetic(), linewidth=2, markersize=10)
        plt.text(row['Longitude'], row['Latitude'], row['IATA'], transform=ccrs.Geodetic(), fontsize=12, fontweight='bold')


# Read csv files, first is precovid flights, second postcovid flights, and last is airports
precf = pd.read_csv("Files/precovid_flights.csv", sep=";")
postcf = pd.read_csv("Files/postcovid_flights.csv", sep=";")
airports = pd.read_csv("Files/airports.dat", sep=",")

# Merge the airports table and the pre-postcovid flights one
precf_coord = pd.merge(precf, airports[['Longitude', 'Latitude', 'IATA']], on='IATA')
postcf_coord = pd.merge(postcf, airports[['Longitude', 'Latitude', 'IATA']], on='IATA')

# Draw the map of Europe
createmap_Europe()

# Create two variables holding Tallin's latitude and longitude
tallinn_lat = 59.4162
tallinn_lon = 24.8004

# Call function in order to draw flight data, precovid will be in blue, postcovid in yellow
draw_flights(precf_coord, tallinn_lon, tallinn_lat, 'blue', '*')
draw_flights(postcf_coord, tallinn_lon, tallinn_lat, 'yellow', '*')

# Save figure as PNG and set title
plt.title("Pre- and Postcovid direct flights from Tallinn\nMariano D'Angelo\n", fontsize=20)
plt.savefig("Flights.png")
plt.show()
