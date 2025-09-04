import matplotlib.pyplot as plt
from soilgrids import SoilGrids

# get data from SoilGrids
soil_grids = SoilGrids()
data = soil_grids.get_coverage_data(
    service_id="phh2o",
    coverage_id="phh2o_0-5cm_mean",
    west=-1784000,
    south=1356000,
    east=-1140000,
    north=1863000,
    crs="urn:ogc:def:crs:EPSG::152160",
    output="test.tif",
)

# show metadata
for key, value in soil_grids.metadata.items():
    print(f"{key}: {value}")


# plot data
data.plot(figsize=(9, 5), vmin=0)
plt.title("Mean pH between 0 and 5 cm soil depth in Senegal")
plt.show()
plt.savefig("./map.png")
