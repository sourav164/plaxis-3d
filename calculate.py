import os, shutil
import numpy as np
# from plxscripting.easy import *


# change working directory to the folder location
file_path = "C:/Users/sourav/Downloads/rainfall analysis/Cell127_real properties_python.p3d"
folder_loc , file_loc = os.path.split(file_path)
os.chdir(folder_loc)

if not os.path.exists("out") :
	os.makedirs("out")



sres = np.linspace(0.01, 0.1, num=2)
gn = np.linspace(1, 10, num=2)
ga = np.linspace(1, 4, num=2)
gl = np.linspace(-3, 3, num=2)
kx = np.linspace(.001, 1, num=2)

simulation = len(sres)*len(gn)*len(ga)*len(gl)*len(kx)

i = 1
for sres_val in sres:
	for gn_val in gn:
		for ga_val in gn:
			for gl_val in gl:
				for kx_val in kx:
					print (f'{i} out of {simulation} simulation is being conducted') 
					i+=1

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


					# give new name and save data
					copy_name = str(sres_val)+str(gn_val)+str(ga_val)+str(gl_val)+str(kx_val)
					
					file_save = "out/"+copy_name+".p3d"
					shutil.copy2(file_loc, file_save)

					folder_save = "out/"+copy_name+".p3dat"
					shutil.copytree((file_loc+"at"), folder_save)

					print (f'File saved in : \"out/\"') 
