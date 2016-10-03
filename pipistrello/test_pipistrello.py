#!/usr/bin/env python

######################################################
#                                                    #
#  For this program to run, you need to acrivate     #
#  the pipistrello environment. You can do this by   #
#  entering the following command in the shell:      #
#                                                    #
#        $ source activate pipistrello               #
#                                                    #
######################################################

#Import modules:
import pipistrello
import utils
import time
import os

utils.cleanup_start()
#database_dir = ('/home/esp-shared-b/RegCM_Data/CAM2')
#database_dir = ('/home/esp-shared-b/RegCM_Data/regcm3')
#database_dir = ('/home/esp-shared-b/RegCM_Data')
#database_dir = '/home/esp-shared-a/GlobalModels/CMIP5/monthly'

database_dir = '/home/juan/MHPC-Thesis/NetCDF_Files'
my_database = pipistrello.database(database_dir,new_catalogue=True)
cubesA = my_database.load_cubes('temperature')
cubesB = my_database.load_no_catalogue('temperature')

#This cleans up leftover files (compiled python files)
#and prints a good-bye message.
utils.cleanup_and_finish()
