#!/usr/bin/python3

def make_ncgrid(age):
    """Makes netcdf grid from xyz file"""
    print(f'Age is {age}')
    return 'test'

# #==========================================================================
# # IMPORT LIBRARIES                #
# #==========================================================================
# import math
# import numpy as np
# import os
# import pygmt
# import shutil
# import sys
# import pandas as pd

# #==========================================================================
# # Initial main model parameters and dir path for post-processing analysis
# #==========================================================================
# #Specify model name and approximation
# model_name = "vanilla1Ga-MacOS"
# model_type = "standard" # "standard" (0 to 1 non-dim temperature) or "deviation" (deviation of temperature from horizontal avg)
# variable   = "temp"
# dimension = False # choose whether to dimensionalise the variable or not (currently only for temp)
# grid_spacing = "0.25d" # Spacing for the output grid used by gmt
# gmt_region = "g" # global region used by gmt

# # Base directory
# main_directory    = ('/Users/jono/Documents/postprocessing_analysis/1GaClusterVanilla') #input directory

# # debugging flaf - not sure what this is...
# # printmod=0;             # Want the extra to be saved?
# # FilesVisible = 'off';  # want to keep?

# if model_type == "standard":
#     # Specify the directory in which you want to visualize the models
#     outputPath = os.path.join(os.path.abspath("."),"temperature/")

#     #create the directory where you want to store your models
#     os.makedirs(outputPath,exist_ok=True)
    
# if model_type == "deviation":
#     outputPath = os.path.join(os.path.abspath("."),"temperature_deviation/")
#     os.makedirs(outputPath,exist_ok=True)

# #==========================================================================
# # define some useful functions:
# #==========================================================================
# def get_age_and_depth(file_name):
#     "Retrieves the age and depth from a grid_maker.py .xyz file"
#     # Splits the file name into a list spearated by dashes
#     params = file_name.split('-')
    
#     #retrieve paramater from list and remove the units
#     age = params[-2][:-2]
#     depth = params[-1][0:4]
    
#     return age, depth

# q

# #==========================================================================
# # get to the base directory:
# #==========================================================================
# os.chdir(main_directory)
# cur_dir           = os.getcwd()
# print ('Current working directory: ',cur_dir)
# print ('-----------------------------')
# print ('Start sampling the data:')

# #==========================================================================
# # the main part:
# #==========================================================================

# # get a list of text files (created with grid maker) that you will create grids for- logic may need adjusting based on what's in the input directory
# files = [f for f in os.listdir(main_directory) if f.endswith("xyz") and not f.endswith("median.xyz") and f.startswith(model_name)]

# # initialise the count of grids computed 
# count=1
# totalnum=len(files)

# # Loop over each file in our list of files, i.e. loop over each depth
# for file in files:
#     print(f"Working on {file}")
#     age, depth = get_age_and_depth(file)
#     print(f"Computing {model_type} model type at {age}Ma, {depth}km")

#     output_directory = outputPath + age
#     os.makedirs(output_directory,exist_ok=True) # Make the output directory separated by age

#     try:
#         data = pd.read_csv(file, sep = " ", names = ['x','y','z']) # read the file as a dataframe
#     except Exception as e:
#         print(f"Something wrong with the file {file}. Check the data is correct")
#         print(e)

#     # Set the name of the output file and dimensionalise temperature if required
#     if dimension: 
#         data['z'] = dimensionalise_temp(data['z'])
#         outgrid = f'Dimensionalised_{model_name}_t{age}_{depth}.nc'
#     else:
#         outgrid = f'{model_name}_t{age}_{depth}.nc'

#     # Append the average temp for each depth into a file
#     avefile = f'{model_name}_t{age}_average_temps.dat'
#     ave = data['z'].mean()
#     if count == 1:
#         with open(avefile, "w") as file:
#             file.write(str(depth) + '\t' + str(ave) + '\n')
#     else:
#         with open(avefile, "a") as file:
#             file.write(str(depth) + '\t' + str(ave) + '\n')

#     # Split the grid into cells and get the median of each cell
#     if model_type == "standard":
#         median = pygmt.blockmedian(data, region=gmt_region, spacing=grid_spacing)

#     elif model_type == "deviation":
#         cols = {'x':data['x'], 'y':data['y'], 'dev':data['z'] - ave, f'{variable}':data['z'], 'ave':ave}
#         df = pd.DataFrame(data=cols,index=None)

#         median = pygmt.blockmedian(df, region=gmt_region, spacing=grid_spacing)

#     # Interpolate the median values onto a new grid
#     pygmt.sphinterpolate(median, outgrid=outgrid, region=gmt_region, spacing=grid_spacing, Q='s')

#     # Count how many grids of the total have been looped through
#     print(f'{str(count)} out of {str(totalnum)} depths processed')

#     # Move the interpolated grid of medians to the designated output directory (and delete any exisiting grids there that have the same name)
#     if os.path.isfile(output_directory + '/' + outgrid):
#         os.remove(output_directory + '/' + outgrid)
#     shutil.move(f'{main_directory}/{outgrid}', output_directory)

#     count += 1

# # Move the file of averages to the output directory (will need some adjusting for multiple ages)
# if os.path.isfile(output_directory + '/' + avefile):
#     os.remove(output_directory + '/' + avefile)
# shutil.move(avefile, output_directory)