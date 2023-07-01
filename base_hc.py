import os
import shutil
import glob

# SET DischargeFunction_9 MANUALLY BEFORE RUNNING THIS CODE

# USER INPUT STARTS 
file_path = "C:/Users/sourav/Downloads/USB Jibon/Final combination_Cell188_Jibon_2_21_may2020_raifall_actual properties.p3d"
rainfall = []
times = []
bases = []
sub_grades =  []
sub_bases = []

# USER INPUT ENDS 


folder_loc , file_loc = os.path.split(file_path)
os.chdir(folder_loc)

if not os.path.exists("out") :
	os.makedirs("out")
already_run = [os.path.split(i[:-4])[1] for i in glob.glob("out/*p3d")]


value_combination = [(rain, time, base_val, sub_grade, sub_base) for rain in rainfall for time in times 
		     for base_val in bases for sub_grade in sub_grades for sub_base in sub_bases]

for value in value_combination:

	rain, time, base_val, sub_grade, sub_base = value
	copy_name = str(rain)+"_"+str(time)+"_"+str(base_val)+"_"+str(sub_grade)+"_"+str(sub_base)

	print (copy_name, value_combination.index(value), " out of ", len(value_combination))

	if copy_name not in already_run:
		try: 
			# discharge function selection
			g_i.DischargeFunction_9.Table[0].DeltaDischarge.set(rain)
			g_i.DischargeFunction_9.Table[1].DeltaDischarge.set(rain)
			g_i.DischargeFunction_9.Table[1].Time.set(time)
			g_i.gotosoil()

			# Base change
			g_i.Base.PermHorizontalPrimary.set(base_val)
			g_i.Base.PermHorizontalSecondary.set(base_val)
			g_i.Base.PermVertical.set(base_val)

			# subgrade change
			g_i.Subgrade.PermHorizontalPrimary.set(sub_grade)
			g_i.Subgrade.PermHorizontalSecondary.set(sub_grade)
			g_i.Subgrade.PermVertical.set(sub_grade)

			# subbase change
			g_i.Subbase.PermHorizontalPrimary.set(sub_base)
			g_i.Subbase.PermHorizontalSecondary.set(sub_base)
			g_i.Subbase.PermVertical.set(sub_base)

			# build and calculate
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

		except Exception as e:
			print (copy_name, " not ran")
			pass

