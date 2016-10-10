#!/usr/bin/env python
import utils as ui ##needed to import my iris
import iris
import numpy as np
iris.FUTURE.netcdf_no_unlimited = True

def fill_array(tc,xc,yc,zc):
    valmax = 30
    valmin = 0

    t = tc.points
    x = xc.points
    y = yc.points
    z = zc.points

    zmax = max(z)
    zmin = min(z)

    temp = (valmax-valmin) * np.einsum('i,j,k,l',1+np.sin((t/8760.)/(2.*np.pi)), 1+np.sin(x), np.cos(y), (z - zmax)/(zmax-zmin))

    return temp

#t coordinate in hours: 8760 ~ 1yr
def generate_cube(tmin = 0, tmax = 11*8760,tsamp = 100,
                xmin = -179, xmax = 179, xsamp = 358,
                ymin = -89, ymax = 89, ysamp = 178,
                zmin = 0, zmax = 7000, zsamp = 7):

    #Create coordinates:
    tco = iris.coords.DimCoord(np.linspace(tmin,tmax,tsamp), standard_name='time', units='hours since 2000-01-01 00:00')
    tco.guess_bounds()

    xco = iris.coords.DimCoord(np.linspace(xmin,xmax,xsamp), standard_name='longitude', units='degree')
    xco.guess_bounds()

    yco = iris.coords.DimCoord(np.linspace(ymin,ymax,ysamp), standard_name='latitude', units='degree')
    yco.guess_bounds()

    zco = iris.coords.DimCoord(np.linspace(zmin,zmax,zsamp), standard_name='height', units='metres')
    zco.guess_bounds()

    #Create cube:
    c1 = iris.cube.Cube(fill_array(tco,xco,yco,zco), standard_name='air_temperature', units='celsius')
    c1.add_dim_coord(tco, 0)
    c1.add_dim_coord(xco, 1)
    c1.add_dim_coord(yco, 2)
    c1.add_dim_coord(zco, 3)

    cubefile = 'cube_generated.nc'
    iris.save(c1,cubefile)
    print("Cube saved in {}".format(cubefile))

if __name__ == '__main__':
        generate_cube()
