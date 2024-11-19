import os, shutil, glob
import numpy as np
# from plxscripting.easy import *


# change working directory to the folder location
file_path = "C:/Users/sourav/Downloads/USB Jibon/Final combination_Cell188_Jibon_2_21_may2020_raifall_actual properties.p3d"
folder_loc , file_loc = os.path.split(file_path)
os.chdir(folder_loc)
log_file = "error_details.txt"
server_location = "C:/Users/sourav/Box/2021 - MnDOT - Freeze-Thaw Cycle - Phase 2/Code/plaxis results/server_cell188"

if not os.path.exists(log_file) :
    open(log_file, 'a').close()


if not os.path.exists("out") :
	os.makedirs("out")


sres = [.01, .05]
gn = [3, 4, 5, 6]
ga = [1.25, 1.5, 2.0,2.5]
gl = [-2, -1, 0]
kx = [.001,.002, 0.05, 0.1,0.2]

simulation = len(sres)*len(gn)*len(ga)*len(gl)*len(kx)

already_run = [os.path.split(i[:-4])[1] for i in glob.glob("out/*p3d")]


i = 1
for sres_val in sres:
	for gn_val in gn:
		for ga_val in gn:
			for gl_val in gl:
				for kx_val in kx:
					print (f'{i} out of {simulation} simulation is being conducted') 
					i+=1
					copy_name = str(sres_val)+"_"+str(gn_val)+"_"+str(ga_val)+"_"+str(gl_val)+"_"+str(kx_val)
					print (copy_name)

					if copy_name not in already_run:

						try:
							g_i.gotosoil()

							g_i.Asphalt.SaturationResidual.set(sres_val)
							g_i.Asphalt.GenuchtenGn.set(gn_val)
							g_i.Asphalt.GenuchtenGa.set(ga_val)
							g_i.Asphalt.GenuchtenGl.set(gl_val)
							g_i.Asphalt.PermHorizontalPrimary.set(kx_val)
							g_i.Asphalt.PermHorizontalSecondary.set(kx_val)
							g_i.Asphalt.PermVertical.set(kx_val)

							g_i.gotostages()

							g_i.InitialPhase.ShouldCalculate.set(True)
							g_i.Phase_1.ShouldCalculate.set(True)
							g_i.Phase_2.ShouldCalculate.set(True)
							g_i.Phase_3.ShouldCalculate.set(True)
							g_i.Phase_4.ShouldCalculate.set(True)
							
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

