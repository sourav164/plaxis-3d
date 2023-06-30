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
                        print (copy_name)