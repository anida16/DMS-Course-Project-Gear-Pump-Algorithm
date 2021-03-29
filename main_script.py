import math

def range_index(table, val):
    for (k1, k2) in table:
        if k1 < val <= k2:
            return table[(k1, k2)]

def range_index1(table, val):
    for (k1, k2) in table:
        if k1 <= val < k2:
            return table[(k1, k2)]
'''
Input
Discharge in LPM (Litre per minute) and Pressure (in bar)
'''
Discharge = 100
Pressure = 80

#####################################################################################################################################

#Drive Unit

#Assumptions Start
Mech_efficiency = 0.93
Volumetric_Efficiency = 0.97
Service_Factor = 1.5 #PSG 7.109 for Rotary Pump
#Assumptions Ends

#Part 1: Drive Unit

Corrected_Discharge = Discharge/(60 * 1000)
Corrected_Pressure = Pressure * 100000

Motor_Power = (Corrected_Discharge * Corrected_Pressure)/(Mech_efficiency * Volumetric_Efficiency)

New_Motor_Power = Motor_Power * Service_Factor


Pre_Standard_Motor = New_Motor_Power/1000
Standard_Motor = float(("{:.0f}".format(Pre_Standard_Motor))) #Float to Integer
#print(type(Standard_Motor))
print(Standard_Motor)

#PSG 5.124 Start

Motor_check = ({
(1, 1.1): 1.1,
(1.1, 1.5): 1.5, 
(1.5, 2.2): 2.2,
(2.2, 3.7): 3.7,
(3.7, 5.5): 5.5,
(5.5, 7.5): 7.5,
(7.5, 11): 11, 
(11, 15): 15,
(15, 18.5): 18.5,
(18.5, 22): 22
})

#PSG 5.124 End


Corrected_Standard_Motor = range_index(Motor_check, Standard_Motor)

if Corrected_Standard_Motor is None:
    print("Error: Standard Motor is not availible in PSG")


print("corrected standard motor", Corrected_Standard_Motor)


#We completely assume the Speed as 960RPM (Rukhande Sir said too), no mention anywhere
Speed = 960

#Part 1 End: Drive Unit

#####################################################################################################################################

#Part 2: Tranmission Unit

KW_per_100_RPM = (Corrected_Standard_Motor*100)/Speed
print("KW_per_100_RPM",KW_per_100_RPM)
#PSG 7.108 Start

#DATABASE for FLexible Coupling Proportions (Bush Type only)
Coupler_Proportions = ({
(0, 0.4): 0.4,
(0.4, 0.6): 0.6, 
(0.6, 0.8): 0.8,
(0.8, 2.5): 2.5,
(2.5, 4.0): 4.0,
(4.0, 6.0): 6.0,
(6.0, 16.0): 16.0, 
(16.0, 25.0): 25.0,
(25.0, 52.0): 52.0,
(52.0, 74.0): 74.0
})

Standard_Max_rating = range_index(Coupler_Proportions, KW_per_100_RPM)

if Standard_Max_rating is 0.4:
    Coupling_No = 1
    Amin = 12
    Amax = 16
    B = 80
    C = 25
    E = 28
    G = 18

if Standard_Max_rating is 0.6:
    Coupling_No = 2
    Amin = 16
    Amax = 22
    B = 100
    C = 30
    E = 30
    G = 20

if Standard_Max_rating is 0.8:
    Coupling_No = 3
    Amin = 22
    Amax = 30
    B = 112
    C = 38
    E = 32
    G = 22

if Standard_Max_rating is 2.5:
    Coupling_No = 4
    Amin = 30
    Amax = 45
    B = 132
    C = 55
    E = 40
    G = 30

if Standard_Max_rating is 4.0:
    Coupling_No = 5
    Amin = 45
    Amax = 56
    B = 170
    C = 80
    E = 45
    G = 35

if Standard_Max_rating is 6.0:
    Coupling_No = 6
    Amin = 56
    Amax = 75
    B = 200
    C = 100
    E = 56
    G = 40

if Standard_Max_rating is 16.0:
    Coupling_No = 7
    Amin = 75
    Amax = 85
    B = 250
    C = 140
    E = 63
    G = 45

if Standard_Max_rating is 25.0:
    Coupling_No = 8
    Amin = 85
    Amax = 110
    B = 315
    C = 180
    E = 80
    G = 50

if Standard_Max_rating is 52.0:
    Coupling_No = 9
    Amin = 110
    Amax = 130
    B = 400
    C = 212
    E = 90
    G = 56

if Standard_Max_rating is 74.0:
    Coupling_No = 10
    Amin = 130
    Amax = 150
    B = 500
    C = 280
    E = 100
    G = 60

#print(Coupling_No)

#PSG 7.108 End

#Part 2 End: Transmission Unit
#####################################################################################################################################

#Part 3: Pump Unit

#Assumptions:
Gear_Profile = "Involute"
Quality_Of_Gear = "Precision Cut"
Type_of_Meshing = "Sn gearing"
Gear_Type = "Spur Gear"
Gear_Ratio = 1
Pressure_Angle = 20

#Step 3.1: Design of Gears 

#Material Selection Drop Down
'''
CI_Grade_20_bend = 50
CI_Grade_20_tensile = 500

CI_Grade_25_bend = 60
CI_Grade_25_tensile = 600

CI_Grade_35_bend = 60
CI_Grade_35_tensile = 600

CI_Grade_35_Heated_bend = 80
CI_Grade_35_Heated_tensile = 750


Steel_C45_bend = 140
Steel_C45_tensile = 500

Steel_15Ni_bend = 320
Steel_15Ni_tensile = 950

Steel_40Ni_bend = 400
Steel_40Ni_tensile = 1100
'''
Bending_stress = 400
Tensile_Stress = 1100
Modulus_Elasticity = 210000


#Assumptions:
No_Teeth = 14

Module_in_mm = (((Discharge*4)/(Speed*7*Volumetric_Efficiency*math.pi*112*1000))**(1/3))*1000
print(Module_in_mm)
#PSG PAge 8.2 Start

#DATABASE for Module
Standard_Module = ({
(0, 1): 1,
(1, 1.25): 1.25, 
(1.25, 1.5): 1.5,
(1.5, 2): 2,
(2, 2.5): 2.5,
(2.5, 3): 3,
(3, 4): 4, 
(4, 5): 5,
(5, 6): 6,
(6, 8): 8,
(8, 10): 10,
(10, 12): 12,
(12, 16): 16,
(16, 20): 20
})

Corrected_Standard_Module = range_index1(Standard_Module, Module_in_mm)
print(Corrected_Standard_Module)

Pitch_Diameter_D = Corrected_Standard_Module * No_Teeth
Outer_Diameter_Do = 16*Corrected_Standard_Module
Root_Diameter_Df = 12*Corrected_Standard_Module
Clearance = 0.25 * Corrected_Standard_Module
Width = 7*Corrected_Standard_Module
print("Old width", Width)
New_width = (Discharge * 1000000)/(2*math.pi*(Corrected_Standard_Module**2)*No_Teeth*Volumetric_Efficiency*Speed)
#print("Width", New_width)

if New_width < Width:
    New_width = Width
    print("Old Width is higher")

print("Width", New_width)

#Test for Bending

Y1 = math.pi*(0.175-(0.95/No_Teeth))
print("Y1",Y1)

Torque = (Corrected_Standard_Motor * 1000* 60)/(2*2*math.pi*Speed)
print("Torque",Torque)

Actual_Bending_Stress = (Torque * 2000)/(New_width*No_Teeth*Y1*Corrected_Standard_Module**2)
print("Actual_Bending_Stress",Actual_Bending_Stress)

if Actual_Bending_Stress > Bending_stress:
    print("Error: Failed at Bending")
    exit()

if Actual_Bending_Stress < Bending_stress:
    print("###############Sucessfully passed Bending testing")


#Test for Dynamic Load
#PSG 8.50

Static_Force = (Bending_stress*New_width*Y1*Corrected_Standard_Module)/1000
print("Static Force", Static_Force)

Velocity = (math.pi*Pitch_Diameter_D*Speed)/60000
print("Velocity", Velocity)

Barth_Velocity = (Corrected_Standard_Motor + Velocity**(1/2))/Corrected_Standard_Motor
print("Barth velocity", Barth_Velocity)

Tangential_Load = (Corrected_Standard_Motor)/Velocity
print("Tangetial Load", Tangential_Load)

Dynamic_Force = Tangential_Load * Barth_Velocity
print("dynamic force", Dynamic_Force)

if Dynamic_Force > Static_Force:
    print("Error Dynamic force greater than static")

if Static_Force > Dynamic_Force:
    print("##############Sucessfully passed Dynamic load testing")

#Test for Pitting Failure

# From PSG 8.13
Actual_Tensile_Stress = (0.74*(Gear_Ratio+1)*(Torque*1000*Modulus_Elasticity*(Gear_Ratio+1)/(New_width))**(1/2))/Pitch_Diameter_D
print("Actual Tensile Stress", Actual_Tensile_Stress)

if Actual_Tensile_Stress > Tensile_Stress:
    print("Error: Failed due to Pitting")

if Actual_Tensile_Stress < Tensile_Stress:
    print("##############Sucessfully passed Pitting Failure Test")


#Tooth Proportions
print("Corrected_Standard_Module",Corrected_Standard_Module)
print("Pitch_Diameter_D",Pitch_Diameter_D)
print("Outer_Diameter_Do",Outer_Diameter_Do)
print("Root_Diameter_Df",Root_Diameter_Df)
print("Clearance", Clearance)

#Force Analysis
Radial_Load = Tangential_Load*math.tan((Pressure_Angle*math.pi)/180)
print("Radial Load", Radial_Load)

Pressure_in_N_mm2 = Pressure/10
Pmax = Pressure_in_N_mm2*1.2
print("Pmax",Pmax)

Ro = Outer_Diameter_Do/2

Hydraulic_Force = (1.635*Ro*New_width*Pmax)/1000
print("Hydraulic Force", Hydraulic_Force)

Resultant_Force = (((Hydraulic_Force+Tangential_Load)**2)+Radial_Load**2)**(1/2)
print("Resultant Force", Resultant_Force)

#Step 3.2 Bearing Design

Radial_Force = Resultant_Force/2
print("Radial_Force",Radial_Force)
Axial_Force = 0

#Assuming Lhr value is:
Lhr = 5000
Radial_Factor = 1
Rotation_Factor = 1
Service_Factor_Bearing = 1.1
k = 10/3 #Needle Bearing


Lmr = (Lhr*60*Speed)/1000000

Peq = (Radial_Force*Radial_Factor*Rotation_Factor)*Service_Factor_Bearing
print("Peq",Peq)
#PSG 4.2

C = Peq*(Lmr)**(1/k)
C_inkgf = C*100
print("C_inkgf",C_inkgf)

New_Outer_Diameter_Do = Root_Diameter_Df + 10

#Database for Needle Bearing, RNA69 Series (without Inner Race)

Bearing_Dia_check = ({
(52, 55): 52,
(55, 62): 55, 
(62, 68): 62,
(68, 72): 68,
(72, 85): 72,
(85, 100): 85,
(100, 110): 100, 
(110, 125): 110
})

#PSG 5.124 End


Corrected_Diameter_Do = range_index1(Bearing_Dia_check, New_Outer_Diameter_Do)
print("Corrected_Diameter_Do",Corrected_Diameter_Do)

if Corrected_Diameter_Do is 52:
    C_PSG = 4100
    if C_PSG > C_inkgf:
        Dr = 40
        B = 36
        print("Dr",Dr)
        Bearing = "RNA 6906"
    
    if C_PSG < C_inkgf:
        Corrected_Diameter_Do = 55

if Corrected_Diameter_Do is 55:
    C_PSG = 4200
    if C_PSG > C_inkgf:
        Dr = 42
        B = 36
        print("Dr",Dr)
        Bearing = "RNA 6907"
    
    if C_PSG < C_inkgf:
        Corrected_Diameter_Do = 62    

if Corrected_Diameter_Do is 62:
    C_PSG = 5800
    if C_PSG > C_inkgf:
        Dr = 48
        B = 40
        print("Dr",Dr)
        Bearing = "RNA 6908"
    
    if C_PSG < C_inkgf:
        Corrected_Diameter_Do = 68

if Corrected_Diameter_Do is 68:
    C_PSG = 6000
    if C_PSG > C_inkgf:
        Dr = 52
        B = 40
        print("Dr",Dr)
        Bearing = "RNA 6909"
    
    if C_PSG < C_inkgf:
        Corrected_Diameter_Do = 72

if Corrected_Diameter_Do is 72:
    C_PSG = 6200
    if C_PSG > C_inkgf:
        Dr = 58
        B = 40
        print("Dr",Dr)
        Bearing = "RNA 6910"
    
    if C_PSG < C_inkgf:
        Corrected_Diameter_Do = 85

if Corrected_Diameter_Do is 85:
    C_PSG = 8100
    if C_PSG > C_inkgf:
        Dr = 68
        B = 45
        print("Dr",Dr)
        Bearing = "RNA 6912"
    
    if C_PSG < C_inkgf:
        Corrected_Diameter_Do = 100

if Corrected_Diameter_Do is 100:
    C_PSG = 11300
    if C_PSG > C_inkgf:
        Dr = 80
        B = 54
        print("Dr",Dr)
        Bearing = "RNA 6914"
    
    if C_PSG < C_inkgf:
        Corrected_Diameter_Do = 110

if Corrected_Diameter_Do is 110:
    C_PSG = 11900
    if C_PSG > C_inkgf:
        Dr = 90
        B = 54
        print("Dr",Dr)
        Bearing = "RNA 6916"
    
    if C_PSG < C_inkgf:
        Corrected_Diameter_Do = 125

if Corrected_Diameter_Do is 125:
    C_PSG = 15100
    if C_PSG > C_inkgf:
        Dr = 105
        B = 63
        print("Dr",Dr)
        Bearing = "RNA 6918"

print(Bearing)

#Step 3.3: Shaft Design

#Assumptions:
Clearance_Shaft = 10
Shear_Stress_PSG = 45

Span_Length = B + New_width + Clearance_Shaft
Max_Bending_Moment = (Resultant_Force * 1000 * Span_Length)/4

Equivalent_Torque = math.sqrt((Torque**2) + (Max_Bending_Moment**2))
print("Equivalent_Torque",Equivalent_Torque)

Shear_Stress_Actual = 16*Equivalent_Torque/((math.pi)*Dr**(3))
print("Shear_Stress_Actual", Shear_Stress_Actual)
if Shear_Stress_PSG > Shear_Stress_Actual:
    print("############## Sucessfully passed Shaft-Shear Failure Test")

if Shear_Stress_PSG < Shear_Stress_Actual:
    print("############## Shaft failure due to Shear")

New_Coupling_Range = ({
(12, 16): 1,
(16, 22): 2, 
(22, 30): 3,
(30, 45): 4,
(45, 56): 5,
(56, 75): 6,
(75, 85): 7, 
(85, 110): 8,
(110, 130): 9,
(130, 150): 10
})

Coupling_No_New = range_index1(New_Coupling_Range, Dr)


if Coupling_No_New is 1:
    Standard_Max_rating = 0.4
    Coupling_No = 1
    Amin = 12
    Amax = 16
    B = 80
    C = 25
    E = 28
    G = 18

if Coupling_No_New is 2:
    Standard_Max_rating = 0.6
    Coupling_No = 2
    Amin = 16
    Amax = 22
    B = 100
    C = 30
    E = 30
    G = 20

if Coupling_No_New is 3:
    Standard_Max_rating = 0.8
    Coupling_No = 3
    Amin = 22
    Amax = 30
    B = 112
    C = 38
    E = 32
    G = 22

if Coupling_No_New is 4:
    Standard_Max_rating = 2.5
    Coupling_No = 4
    Amin = 30
    Amax = 45
    B = 132
    C = 55
    E = 40
    G = 30

if Coupling_No_New is 5:
    Standard_Max_rating = 4.0
    Coupling_No = 5
    Amin = 45
    Amax = 56
    B = 170
    C = 80
    E = 45
    G = 35

if Coupling_No_New is 6:
    Standard_Max_rating = 6.0
    Coupling_No = 6
    Amin = 56
    Amax = 75
    B = 200
    C = 100
    E = 56
    G = 40

if Coupling_No_New is 7:
    Standard_Max_rating = 16.0
    Coupling_No = 7
    Amin = 75
    Amax = 85
    B = 250
    C = 140
    E = 63
    G = 45

if Coupling_No_New is 8:
    Standard_Max_rating = 25.0
    Coupling_No = 8
    Amin = 85
    Amax = 110
    B = 315
    C = 180
    E = 80
    G = 50

if Coupling_No_New is 9:
    Standard_Max_rating = 52.0
    Coupling_No = 9
    Amin = 110
    Amax = 130
    B = 400
    C = 212
    E = 90
    G = 56

if Coupling_No_New is 10:
    Standard_Max_rating = 74.0
    Coupling_No = 10
    Amin = 130
    Amax = 150
    B = 500
    C = 280
    E = 100
    G = 60

print("Coupling_No_New",Coupling_No_New)
print("Standard_Max_rating",Standard_Max_rating)
#Step 3.4: Casing

#Assumptions:
Tensile_Stress_Casing = 200
FoS_Casing = 6
Safe_Tensile_Stress_Casing = Tensile_Stress_Casing/FoS_Casing


Bolt_Dia_Dict = {
    "M2.5": 2.5,
    "M3": 3,
    "M4": 4,
    "M5": 5,
    "M6": 6,
    "M8": 8,
    "M10": 10,
    "M12": 12,
    "M16": 16,
    "M20": 20,
    "M24": 24,
    "M30": 30,
    "M33": 33,
    "M36": 36
}

Bolt_diameter = Bolt_Dia_Dict["M12"]

#By Thick Cylinder Theory:
Thickness_Casing = (Corrected_Diameter_Do/2)*(((Safe_Tensile_Stress_Casing+Pmax)/(Safe_Tensile_Stress_Casing-Pmax))**(1/2) -1)
print("Thickness_Casing",Thickness_Casing)

Final_Thickness_Casing = math.ceil(Thickness_Casing / 2.) * 2 
print("Final_Thickness_Casing",Final_Thickness_Casing)

C_casing = Corrected_Diameter_Do + Pitch_Diameter_D
PCD_casing = C_casing + 3 * Bolt_diameter
Outer_Diameter_Casing = PCD_casing + 3 * Bolt_diameter


#Step 3.5: Fasteners/ Bolts

#Assumptions:

Tensile_Stress_Fastener = 80 #Change to dropdown
Stiffness_Tighting = 0.33
Stiffness_External = 0.67


Design_Pressure = 1.2*Pressure_in_N_mm2
Openning_Pressure = 1.5*Pressure_in_N_mm2
Projected_Area = ((math.pi/4)*(Outer_Diameter_Do)**2) + Outer_Diameter_Do * 56
print("Project Area", Projected_Area)

External_Force_Fe = Design_Pressure*Projected_Area
print("External_Force", External_Force_Fe)

Opening_Force_Fo = Openning_Pressure*Projected_Area
print("Opening_Force", Opening_Force_Fo)

Initial_Tightening_Force_Fi = Opening_Force_Fo * Stiffness_Tighting
Net_Force_Bolt_Fb = Initial_Tightening_Force_Fi + External_Force_Fe*Stiffness_External
print("Net_Force_Bolt_Fb",Net_Force_Bolt_Fb)

#Input
#Bolts like M2.5,3,4,5,6,8,10,12,16,20,24,30,33,36

PCD_Holes = 1

Bolt_Dict = {
    "M2.5": 3.39,
    "M3": 5.03,
    "M4": 8.78,
    "M5": 14.2,
    "M6": 20.1,
    "M8": 36.6,
    "M10": 58,
    "M12": 84.3,
    "M16": 157,
    "M20": 245,
    "M24": 353,
    "M30": 561,
    "M33": 694,
    "M36": 817
}

Actual_Tensile_Bolt = Net_Force_Bolt_Fb/(PCD_Holes*Bolt_Dict["M12"])
print("Actual_Tensile_Bolt",Actual_Tensile_Bolt)

while Actual_Tensile_Bolt > Tensile_Stress_Fastener:
    PCD_Holes = PCD_Holes + 1
    #print(PCD_Holes)
    Actual_Tensile_Bolt = Net_Force_Bolt_Fb/(PCD_Holes*Bolt_Dict["M12"])
#
if Actual_Tensile_Bolt < Tensile_Stress_Fastener:
    print("No. of Bolt Holes in casing would be ",PCD_Holes)

print("Actual_Tensile_Bolt",Actual_Tensile_Bolt)


#Part 3 End: Pump Unit
#####################################################################################################################################

#Part 4: Piping Unit

#Step4.1: Suction Side

Standard_Pipe_Dia = ({
(0, 12.7): 0.5,
(12.7, 19.05): 0.75, 
(19.05, 25.40): 1,
(25.40, 38.10): 1.5,
(38.10, 50.8): 2,
(50.8, 76.2): 3,
(76.2, 101.6): 4, 
(101.6, 152.4): 6
})

#Assumptions:
Velocity_Suction = 1

Diameter_of_Suction = (((4*Corrected_Discharge)/(math.pi*Velocity_Suction))**(1/2))*1000
print("Diameter_of_Suction",Diameter_of_Suction)

Corrected_Pipe_Dia_inch = range_index(Standard_Pipe_Dia, Diameter_of_Suction)

Corrected_Pipe_Dia_mm = 25.4*Corrected_Pipe_Dia_inch
print(Corrected_Pipe_Dia_mm)

Actual_Suction_Velocity = (4*Corrected_Discharge*1000000)/(math.pi*(Corrected_Pipe_Dia_mm)**(2))
print("Actual_Suction_Velocity",Actual_Suction_Velocity)

#Step4.2: Delivery Side

#Assumptions:
Velocity_Delivery = 2

Diameter_of_Delivery = (((4*Corrected_Discharge)/(math.pi*Velocity_Delivery))**(1/2))*1000
print("Diameter_of_Delivery",Diameter_of_Delivery)

Corrected_Pipe_Dia_inch2 = range_index(Standard_Pipe_Dia, Diameter_of_Delivery)

Corrected_Pipe_Dia_mm2 = 25.4*Corrected_Pipe_Dia_inch2
print(Corrected_Pipe_Dia_mm2)

Actual_Delivery_Velocity = (4*Corrected_Discharge*1000000)/(math.pi*(Corrected_Pipe_Dia_mm2)**(2))
print("Actual_Delivery_Velocity",Actual_Delivery_Velocity)


