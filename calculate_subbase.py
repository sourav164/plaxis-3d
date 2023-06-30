import os, shutil
import numpy as np
# from plxscripting.easy import *


# change working directory to the folder location
file_path = "C:/Users/sourav/Downloads/Cell188/Cell188_rain1inperhr.p3d"
folder_loc , file_loc = os.path.split(file_path)
os.chdir(folder_loc)
log_file = "error_details.txt"
server_location = "C:/Users/sourav/Box/2021 - MnDOT - Freeze-Thaw Cycle - Phase 2/Code/plaxis results/188_precipitation"

if not os.path.exists(log_file) :
    open(log_file, 'a').close()


if not os.path.exists("out") :
	os.makedirs("out")


sres = [.089]
gn = [3.5]
ga = [2.64]
gl = [-0.25]
kx = [.5, .6, .7, .8, .9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]
precipitation = [0.6, 1.2, 1.8, 2.4, 3, 3.6, 4.2, 4.8, 5.4, 6]

simulation = len(sres)*len(gn)*len(ga)*len(gl)*len(kx)

i = 1
for sres_val in sres:
	for gn_val in gn:
		for ga_val in gn:
			for gl_val in gl:
				for kx_val in kx:
					for precipitation_val in precipitation:
						print (f'{i} out of {simulation} simulation is being conducted') 
						i+=1

						copy_name = str(sres_val)+"_"+str(gn_val)+"_"+str(ga_val)+"_"+str(gl_val)+"_"+str(kx_val)+str(precipitation_val)

						try:
							g_i.gotosoil()

							g_i.Subbase.SaturationResidual.set(sres_val)
							g_i.Subbase.GenuchtenGn.set(gn_val)
							g_i.Subbase.GenuchtenGa.set(ga_val)
							g_i.Subbase.GenuchtenGl.set(gl_val)
							g_i.Subbase.PermHorizontalPrimary.set(kx_val)
							g_i.Subbase.PermHorizontalSecondary.set(kx_val)
							g_i.Subbase.PermVertical.set(kx_val)

							g_i.gotostages()

							g_i.InitialPhase.ShouldCalculate.set(True)
							g_i.Phase_1.ShouldCalculate.set(True)
							g_i.Phase_2.ShouldCalculate.set(True)
							g_i.Phase_3.ShouldCalculate.set(True)
							g_i.Phase_4.ShouldCalculate.set(True)
							g_i.Precipitation.Discharge.Phase_4 = precipitation_val
							g_i.calculate()
							g_i.save()


							# give new name and save in local drive
							
							file_save = "out/"+copy_name+".p3d"
							shutil.copy2(file_loc, file_save)

							folder_save = "out/"+copy_name+".p3dat"
							shutil.copytree((file_loc+"at"), folder_save)

							print (f'File saved in : \"out/\"') 

							# give new name and save in server

							try:

								file_save_server = os.path.join(server_location, (copy_name+".p3d"))
								shutil.copy2(file_loc, file_save_server)

								folder_save_server = os.path.join(server_location, (copy_name+".p3dat"))
								shutil.copytree((file_loc+"at"), folder_save_server)


								shutil.copy2(log_file, os.path.join(server_location, log_file))

							except:
								pass


						except Exception as e:
							with open(log_file, "a") as log:
								log.write("Failed for : {}\n".format(copy_name))
							pass

