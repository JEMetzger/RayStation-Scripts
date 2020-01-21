
#   RayStation version: 6.2.0.7
#   Selected patient: ...

from connect import *

import os, math
#Script to create a text file of SSD's every 20 degrees you can change range to 
#suit your needs. This is helpful for SBRT's
#
#

patient = get_current('Patient')
case = get_current('Case')
plan = get_current('Plan')
beam_set = get_current('BeamSet')

patient_name = patient.PatientName

os.chdir('C:\\Users\\....')#Enter your own path

f = open(patient_name +' SBRT SSD.txt','w')


for i in range(0,360,20):#can change ranges yourself
	patient.Cases[0].TreatmentPlans[0].BeamSets[0].PatientSetup.SetupBeams[0].GantryAngle = i
	x = patient.Cases[0].TreatmentPlans[0].BeamSets[0].PatientSetup.SetupBeams[0].GetSSD()
	rx = round(x,1)
	f.write('At Gantry angle '+str(i)+' the SSD is '+str(rx)+'\n')
	

	

f.close()
patient.Cases[0].TreatmentPlans[0].BeamSets[0].PatientSetup.SetupBeams[0].GantryAngle = 0
