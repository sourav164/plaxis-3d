import os
import numpy as np


sres = np.linspace(0.01, 0.1, num=2)
gn = np.linspace(1, 10, num=2)
ga = np.linspace(1, 4, num=2)
gl = np.linspace(-3, 3, num=2)
kx = np.linspace(.001, 1, num=2)

simulation = len(sres)*len(gn)*len(ga)*len(gl)*len(kx)

i = 0
for sres_val in sres:
	for gn_val in gn:
		for ga_val in gn:
			for gl_val in gl:
				for kx_val in kx:
					print () 

					g_i._gotosoil()

					g_i.Asphalt.SaturationResidual.set(sres_val)
					g_i.Asphalt.GenuchtenGn.set(gn_val)
					g_i.Asphalt.GenuchtenGa.set(ga_val)
					g_i.Asphalt.GenuchtenGl.set(gl_val)
					g_i.Asphalt.PermHorizontalPrimary.set(kx_val)
					g_i.Asphalt.PermHorizontalSecondary.set(kx_val)
					g_i.Asphalt.PermVertical.set(kx_val)


					g_i.InitialPhase.ShouldCalculate.set(True)
					g_i.Phase_1.ShouldCalculate.set(True)
					g_i.Phase_2.ShouldCalculate.set(True)
					g_i.Phase_3.ShouldCalculate.set(True)
					g_i.Phase_4.ShouldCalculate.set(True)
					g_i.calculate()
					g_i.save()

					file_name = "out\\"+str(sres_val)+str(gn_val)+str(ga_val)+str(gl_val)+str(kx_val)+".p3d"
					copy_file = os.path.join(os.path.split(file_path)[0], file_name)
					shutil.copy2(file_path, copy_file)


