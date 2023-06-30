
hc_val = 
time = 
base_val = 
sub_grade = 
sub_val = 


g_i.DischargeFunction_9.Table[0].DeltaDischarge.set(hc_val)
g_i.DischargeFunction_9.Table[1].DeltaDischarge.set(hc_val)
g_i.DischargeFunction_9.Table[1].Time(time)
g_i.Precipitation.DischargeFunction Phase_4 DischargeFunction_9



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
g_i.Subbase.PermHorizontalPrimary.set(sub_val)
g_i.Subbase.PermHorizontalSecondary.set(sub_val)
g_i.Subbase.PermVertical.set(sub_val)


# build and calculate

g_i.gotostages()
g_i.InitialPhase.ShouldCalculate.set(True)
g_i.Phase_1.ShouldCalculate.set(True)
g_i.Phase_2.ShouldCalculate.set(True)
g_i.Phase_3.ShouldCalculate.set(True)
g_i.Phase_4.ShouldCalculate.set(True)

g_i.calculate()
g_i.save()