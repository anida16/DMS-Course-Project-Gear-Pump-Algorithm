import math
import tkinter as tk
from tkinter import *
import time


# Windows of the GUI :-
#     Root1 -> Input Window
#     Root2 -> Assumptions Window
#     Root3 -> Results Window
#     Root4 -> Error Window
def errorFlag(errorMessage):
    Root4 = Tk()
    Root4.title("Error Window")

    errorWindow = Frame(Root4)
    errorWindow.grid(column=0, row=0, sticky=(N, W, E, S))
    errorWindow.columnconfigure(0, weight=1)
    errorWindow.rowconfigure(0, weight=1)
    errorWindow.pack(pady=60, padx=50)  # controls fixed gap in between main content and edges, pady for y padx for x
    Label(errorWindow, text="Error    :").grid(row=1, column=1)
    Label(errorWindow, text=errorMessage).grid(row=1, column=2)

    OK_btn = Button(errorWindow, text='OK', width=15, bd=0, bg='white', pady=5, command=lambda: Root4.destroy())
    OK_btn.grid(row=2, column=1, padx=8, pady=5)
    time.sleep(2)
    Root4.mainloop()


def PSG_Database(database, value):  # centralised database
    if database == 'motorCheck':
        # PSG
        motorCheck = ({
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
        return range_index(motorCheck, value)
    elif database == 'couplerProportions':
        # DATABASE for Flexible Coupling Proportions (Bush Type only)
        couplerProportions = ({
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
        return range_index(couplerProportions, value)
    elif database == 'standardModule':
        # DATABASE for Standard Module values
        standardModule = ({
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
        return range_index1(standardModule, value)
    elif database == 'bearingDiacheck':
        # Database for Needle Bearing, RNA69 Series (without Inner Race)
        bearingDiacheck = ({
            (52, 55): 52,
            (55, 62): 55,
            (62, 68): 62,
            (68, 72): 68,
            (72, 85): 72,
            (85, 100): 85,
            (100, 110): 100,
            (110, 125): 110
        })
        return range_index1(bearingDiacheck, value)
    elif database == 'NewCouplingRange':
        NewCouplingRange = ({
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
        return range_index1(NewCouplingRange, value)
    elif database == 'standardPipedia':
        standardPipedia = ({
            (0, 12.7): 0.5,
            (12.7, 19.05): 0.75,
            (19.05, 25.40): 1,
            (25.40, 38.10): 1.5,
            (38.10, 50.8): 2,
            (50.8, 76.2): 3,
            (76.2, 101.6): 4,
            (101.6, 152.4): 6
        })
        return range_index(standardPipedia, value)
    else:
        print("Error: Invalid value passed.")
        return -1


def range_index(table, val):
    for (k1, k2) in table:
        if k1 < val <= k2:
            return table[(k1, k2)]
    return -1


def range_index1(table, val):
    for (k1, k2) in table:
        if k1 <= val < k2:
            return table[(k1, k2)]
    return -1


# Initializing the GUI Window
Root1 = Tk()
Root1.title("Design of Gear Pump")
inputWindow = Frame(Root1)
inputWindow.grid(column=0, row=0, sticky=(N, W, E, S))
inputWindow.columnconfigure(0, weight=1)
inputWindow.rowconfigure(0, weight=1)
inputWindow.pack(pady=60, padx=50)  # controls fixed gap inbetween main content and edges, pady for y padx for x
material = StringVar(Root1)  # this is where value selected by user is stored #Material Designation
dischargeInput = tk.DoubleVar(Root1)
pressureInput = tk.DoubleVar(Root1)

'''
Input
Discharge in LPM (Litre per minute) and Pressure (in bar)
'''

# Material Selection Drop Down and Gear Material Database
'''
CI_Grade_20_Tensile = 500
CI_Grade_20_Bending = 50

CI_Grade_25_Tensile = 600
CI_Grade_25_Bending = 60

CI_Grade_35_Tensile = 600
CI_Grade_35_Bending = 60

CI_Grade_35_Heat_Treated_Tensile = 750
CI_Grade_35_Heat_Treated_Bending = 80

Steel_C45_Tensile = 500
Steel_C45_Bending = 140

Steel_15Ni2Cr1Mo15_Tensile = 950
Steel_15Ni2Cr1Mo15_Bending = 320

Steel_40Ni2Cr1Mo28_Tensile = 1100 #Rukhande Selected this, so in tkinter, keep default value as this @Anthony
Steel_40Ni2Cr1Mo28_Bending = 400 #Rukhande Selected this, so in tkinter, keep default value as this @Anthony
'''

optList = ['CCI_Grade_20', 'CI_Grade_25', 'CI_Grade_35', 'CI_Grade_35_Heated', 'Steel_C45', 'Steel_15Ni', 'Steel_40Ni']
popupMenu = OptionMenu(inputWindow, material, *optList)

# Input Boxes for the GUI Design
# Discharge and Input Pressure
Label(inputWindow, text="Discharge(LPM)").grid(row=1, column=1)
dischargeInput = tk.Entry(inputWindow)  # power
dischargeInput.grid(row=1, column=2)

Label(inputWindow, text="Pressure(in bar)").grid(row=2, column=1)
pressureInput = tk.Entry(inputWindow)  # speed
pressureInput.grid(row=2, column=2)

# controls position of name of popup grid
Label(inputWindow, text="Choose Material for Gear").grid(row=7, column=1)
popupMenu.grid(row=7, column=2)  # controls position of popup grid

# Submit button to end the input


b1 = tk.Button(inputWindow, text='Submit', command=lambda: mainProgram())
b1.grid(row=12, column=1)

resetButton = tk.Button(inputWindow, text='Reset', command=lambda: exit())
resetButton.grid(row=12, column=2)

str_out = tk.StringVar(Root1)
str_out.set("Output")


#######################################################################################################################


def mainProgram():
    # GUI widgets for Result and assumptions window

    if material.get() == 'CCI_Grade_20':
        Tensile_Stress = 500
        Bending_Stress = 50
        Modulus_Elasticity = 210000
    elif material.get() == 'CI_Grade_25':
        Tensile_Stress = 600
        Bending_Stress = 60
        Modulus_Elasticity = 210000
    elif material.get() == 'CI_Grade_35':
        Tensile_Stress = 600
        Bending_Stress = 60
        Modulus_Elasticity = 210000
    elif material.get() == 'CI_Grade_35_Heated':
        Tensile_Stress = 750
        Bending_Stress = 80
        Modulus_Elasticity = 210000
    elif material.get() == 'Steel_C45':
        Tensile_Stress = 500
        Bending_Stress = 140
        Modulus_Elasticity = 210000
    elif material.get() == 'Steel_15Ni':
        Tensile_Stress = 950
        Bending_Stress = 320
        Modulus_Elasticity = 210000
    elif material.get() == 'Steel_40Ni':
        Tensile_Stress = 1100
        Bending_Stress = 400
        Modulus_Elasticity = 210000
    else:
        print("Error: Invalid material")
        errorFlag('Invalid material')

    Root2 = Tk()
    Root2.title("Assumptions")

    assumptionsWindow = Frame(Root2)
    assumptionsWindow.grid(column=0, row=0, sticky=(W, N, E, S))    # PLEASE CORRECT THIS
    assumptionsWindow.columnconfigure(0, weight=1)
    assumptionsWindow.rowconfigure(0, weight=1)
    assumptionsWindow.pack(pady=60, padx=50)

    # Assumptions Start
    Mech_efficiency = 0.93
    Volumetric_Efficiency = 0.97
    Service_Factor = 1.5  # PSG 7.109 for Rotary Pump

    Label(assumptionsWindow, text="Mechanical Efficiency").grid(row=1, column=1)
    Label(assumptionsWindow, text=Mech_efficiency).grid(row=1, column=2)
    Label(assumptionsWindow, text="").grid(row=1, column=3)     # Enter the units if possible or else leave blank
    Label(assumptionsWindow, text="").grid(row=1, column=4)     # Enter PSG Reference if possible or else leave blank

    Label(assumptionsWindow, text="Volumetric Efficiency").grid(row=2, column=1)
    Label(assumptionsWindow, text=Volumetric_Efficiency).grid(row=2, column=2)
    Label(assumptionsWindow, text="").grid(row=2, column=3)     # Enter the units if possible or else leave blank
    Label(assumptionsWindow, text="").grid(row=2, column=4)     # Enter PSG Reference if possible or else leave blank

    Label(assumptionsWindow, text="Service Factor").grid(row=3, column=1)
    Label(assumptionsWindow, text=Service_Factor).grid(row=3, column=2)
    Label(assumptionsWindow, text="").grid(row=3, column=3)     # Enter the units if possible or else leave blank
    Label(assumptionsWindow, text="").grid(row=1, column=4)     # Enter PSG Reference if possible or else leave blank
    # Assumptions Ends

    # Part 1: Drive Unit

    Discharge = float(dischargeInput.get())
    print("Discharge = ", Discharge)
    Pressure = float(pressureInput.get())
    print("Pressure = ", Pressure)
    print("data type of Discharge :- ", type(Discharge))
    print("data type of Pressure :- ", type(Pressure))
    Discharge = Discharge / (60 * 1000)  # *Corrected Discharge value
    Pressure = Pressure * 100000  # *Corrected Input Pressure value

    Motor_Power = (Discharge * Pressure) / (Mech_efficiency * Volumetric_Efficiency)

    Motor_Power = Motor_Power * Service_Factor  # Corrected Motor Power

    Pre_Standard_Motor = Motor_Power / 1000
    Standard_Motor = float(("{:.0f}".format(Pre_Standard_Motor)))  # Float to Integer
    # print(type(Standard_Motor))
    print(Standard_Motor)

    # Fetch the standard motor value from PSG Database function
    Corrected_Standard_Motor = PSG_Database('motorCheck', Standard_Motor)

    if Corrected_Standard_Motor == -1:
        print("Error: Standard Motor is not available in PSG")
        errorFlag('Standard Motor is not available in PSG')
        time.sleep(5)
        Root2.destroy()
    print("corrected standard motor", Corrected_Standard_Motor)

    # We completely assume the Speed as 960RPM (Rukhande Sir said too), no mention anywhere
    Speed = 960

    Label(assumptionsWindow, text="Speed").grid(row=4, column=1)
    Label(assumptionsWindow, text=Speed).grid(row=4, column=2)
    Label(assumptionsWindow, text="rpm").grid(row=4, column=3)
    Label(assumptionsWindow, text="").grid(row=4, column=4)  # Enter PSG Reference if possible or else leave blank
    # Part 1 End: Drive Unit

    #################################################################################################################

    # Part 2: Tranmission Unit

    KW_per_100_RPM = (Corrected_Standard_Motor * 100) / Speed
    print("KW_per_100_RPM", KW_per_100_RPM)

    # PSG 7.108 Start

    # Fetch KW_per_100_RPM from PSG Database
    Standard_Max_rating = PSG_Database('couplerProportions', KW_per_100_RPM)
    print("Standard MAx Rating = ", Standard_Max_rating)
    if Standard_Max_rating == -1:
        print("Error: Value not found in database")
        errorFlag('Value not found in database')
        time.sleep(5)
    else:
        if Standard_Max_rating == 0.4:
            Coupling_No = 1
            Amin = 12
            Amax = 16
            B = 80
            C = 25
            E = 28
            G = 18
        elif Standard_Max_rating == 0.6:
            Coupling_No = 2
            Amin = 16
            Amax = 22
            B = 100
            C = 30
            E = 30
            G = 20
        elif Standard_Max_rating == 0.8:
            Coupling_No = 3
            Amin = 22
            Amax = 30
            B = 112
            C = 38
            E = 32
            G = 22
        elif Standard_Max_rating == 2.5:
            Coupling_No = 4
            Amin = 30
            Amax = 45
            B = 132
            C = 55
            E = 40
            G = 30
        elif Standard_Max_rating == 4.0:
            Coupling_No = 5
            Amin = 45
            Amax = 56
            B = 170
            C = 80
            E = 45
            G = 35
        elif Standard_Max_rating == 6.0:
            Coupling_No = 6
            Amin = 56
            Amax = 75
            B = 200
            C = 100
            E = 56
            G = 40
        elif Standard_Max_rating == 16.0:
            Coupling_No = 7
            Amin = 75
            Amax = 85
            B = 250
            C = 140
            E = 63
            G = 45
        elif Standard_Max_rating == 25.0:
            Coupling_No = 8
            Amin = 85
            Amax = 110
            B = 315
            C = 180
            E = 80
            G = 50
        elif Standard_Max_rating == 52.0:
            Coupling_No = 9
            Amin = 110
            Amax = 130
            B = 400
            C = 212
            E = 90
            G = 56
        elif Standard_Max_rating == 74.0:
            Coupling_No = 10
            Amin = 130
            Amax = 150
            B = 500
            C = 280
            E = 100
            G = 60

    print(Coupling_No)

    # PSG 7.108 End

    # Part 2 End: Transmission Unit
    ###############################################################################################################

    # Part 3: Pump Unit

    # Assumptions:
    Gear_Ratio = 1
    Pressure_Angle = 20

    Label(assumptionsWindow, text="Gear Profile").grid(row=5, column=1)
    Label(assumptionsWindow, text="Involute").grid(row=5, column=2)
    Label(assumptionsWindow, text="").grid(row=5, column=3)
    Label(assumptionsWindow, text="").grid(row=5, column=4)  # Enter PSG Reference if possible or else leave blank

    Label(assumptionsWindow, text="Quality of Gear").grid(row=6, column=1)
    Label(assumptionsWindow, text="Precision Cut").grid(row=6, column=2)
    Label(assumptionsWindow, text="").grid(row=6, column=3)
    Label(assumptionsWindow, text="").grid(row=6, column=4)  # Enter PSG Reference if possible or else leave blank

    Label(assumptionsWindow, text="Type of Meshing").grid(row=7, column=1)
    Label(assumptionsWindow, text="Sn gearing").grid(row=7, column=2)
    Label(assumptionsWindow, text="").grid(row=7, column=3)
    Label(assumptionsWindow, text="").grid(row=7, column=4)  # Enter PSG Reference if possible or else leave blank

    Label(assumptionsWindow, text="Gear Type").grid(row=8, column=1)
    Label(assumptionsWindow, text="Spur Gear").grid(row=8, column=2)
    Label(assumptionsWindow, text="").grid(row=8, column=3)
    Label(assumptionsWindow, text="").grid(row=8, column=4)  # Enter PSG Reference if possible or else leave blank

    Label(assumptionsWindow, text="Gear Ratio").grid(row=9, column=1)
    Label(assumptionsWindow, text=Gear_Ratio).grid(row=9, column=2)
    Label(assumptionsWindow, text="").grid(row=9, column=3)
    Label(assumptionsWindow, text="").grid(row=9, column=4)  # Enter PSG Reference if possible or else leave blank

    Label(assumptionsWindow, text="Pressure Angle").grid(row=10, column=1)
    Label(assumptionsWindow, text=Pressure_Angle).grid(row=10, column=2)
    Label(assumptionsWindow, text="").grid(row=10, column=3)
    Label(assumptionsWindow, text="").grid(row=10, column=4)  # Enter PSG Reference if possible or else leave blank
    # Step 3.1: Design of Gears

    # Bending_Stress = 400
    # Tensile_Stress = 1100
    # Modulus_Elasticity = 210000

    # Assumptions:
    No_Teeth = 14

    Label(assumptionsWindow, text="No. of Teeth").grid(row=11, column=1)
    Label(assumptionsWindow, text=No_Teeth).grid(row=11, column=2)
    Label(assumptionsWindow, text="").grid(row=11, column=3)
    Label(assumptionsWindow, text="").grid(row=11, column=4)  # Enter PSG Reference if possible or else leave blank

    Module_in_mm = (((Discharge * 4) / (Speed * 7 * Volumetric_Efficiency * math.pi * 112 * 1000)) ** (1 / 3)) * 1000
    print(Module_in_mm)
    # PSG Page 8.2 Start

    # ******************Fetch the value of module(in mm) from PSG Database*********************
    Corrected_Standard_Module = PSG_Database('standardModule', Module_in_mm)
    print(Corrected_Standard_Module)

    Pitch_Diameter_D = Corrected_Standard_Module * No_Teeth
    Outer_Diameter_Do = 16 * Corrected_Standard_Module
    Root_Diameter_Df = 12 * Corrected_Standard_Module
    Clearance = 0.25 * Corrected_Standard_Module
    Width = 7 * Corrected_Standard_Module
    print("Old width", Width)
    New_width = (Discharge * 1000000) / (2 * math.pi * (Corrected_Standard_Module ** 2) * No_Teeth *
                                         Volumetric_Efficiency * Speed)
    # print("Width", New_width)

    if New_width < Width:
        New_width = Width
        print("Old Width is higher")

    print("Width", New_width)

    # Test for Bending

    Y1 = math.pi * (0.175 - (0.95 / No_Teeth))
    print("Y1", Y1)

    Torque = (Corrected_Standard_Motor * 1000 * 60) / (2 * 2 * math.pi * Speed)
    print("Torque", Torque)

    Actual_Bending_Stress = (Torque * 2000) / (New_width * No_Teeth * Y1 * Corrected_Standard_Module ** 2)
    print("Actual_Bending_Stress", Actual_Bending_Stress)

    if Actual_Bending_Stress > Bending_Stress:
        print("Error: Failed at Bending")
        errorFlag('Failure at Bending')
        time.sleep(5)

    elif Actual_Bending_Stress < Bending_Stress:  # Remark: What if the two values are equal? pass or fail
        print("###############Sucessfully passed Bending testing")

    # Test for Dynamic Load
    # PSG 8.50

    Static_Force = (Bending_Stress * New_width * Y1 * Corrected_Standard_Module) / 1000
    print("Static Force", Static_Force)

    Velocity = (math.pi * Pitch_Diameter_D * Speed) / 60000
    print("Velocity", Velocity)

    Barth_Velocity = 1 + (Velocity ** (1 / 2) / Corrected_Standard_Motor)
    print("Barth velocity", Barth_Velocity)

    Tangential_Load = Corrected_Standard_Motor / Velocity
    print("Tangetial Load", Tangential_Load)

    Dynamic_Force = Tangential_Load * Barth_Velocity
    print("dynamic force", Dynamic_Force)

    if Dynamic_Force > Static_Force:
        print("Error: Dynamic force greater than static")
        errorFlag('Dynamic Force greater than Static Force')
        time.sleep(5)
    elif Static_Force > Dynamic_Force:
        print("##############Sucessfully passed Dynamic load testing")

    # Test for Pitting Failure

    # From PSG 8.13
    Actual_Tensile_Stress = (0.74 * (Gear_Ratio + 1) * (
            Torque * 1000 * Modulus_Elasticity * (Gear_Ratio + 1) / (New_width)) ** 0.5) / Pitch_Diameter_D
    print("Actual Tensile Stress", Actual_Tensile_Stress)

    if Actual_Tensile_Stress > Tensile_Stress:
        print("Error: Failed due to Pitting")
        errorFlag('Failed due to Pitting')
        time.sleep(5)
        exit()
    elif Actual_Tensile_Stress < Tensile_Stress:
        print("##############Sucessfully passed Pitting Failure Test")

    # Tooth Proportions
    print("Corrected_Standard_Module", Corrected_Standard_Module)
    print("Pitch_Diameter_D", Pitch_Diameter_D)
    print("Outer_Diameter_Do", Outer_Diameter_Do)
    print("Root_Diameter_Df", Root_Diameter_Df)
    print("Clearance", Clearance)

    # Force Analysis
    Radial_Load = Tangential_Load * math.tan((Pressure_Angle * math.pi) / 180)
    print("Radial Load", Radial_Load)

    Pressure_in_N_mm2 = Pressure / 10
    Pmax = Pressure_in_N_mm2 * 1.2
    print("Pmax", Pmax)

    Ro = Outer_Diameter_Do / 2

    Hydraulic_Force = (1.635 * Ro * New_width * Pmax) / 1000
    print("Hydraulic Force", Hydraulic_Force)

    Resultant_Force = (((Hydraulic_Force + Tangential_Load) ** 2) + Radial_Load ** 2) ** (1 / 2)
    print("Resultant Force", Resultant_Force)

    # Step 3.2 Bearing Design

    Radial_Force = Resultant_Force / 2
    print("Radial_Force", Radial_Force)
    Axial_Force = 0

    # Assuming Lhr value is:
    Lhr = 5000
    Radial_Factor = 1
    Rotation_Factor = 1
    Service_Factor_Bearing = 1.1
    k = 10 / 3  # Needle Bearing

    Lmr = (Lhr * 60 * Speed) / 1000000

    Peq = (Radial_Force * Radial_Factor * Rotation_Factor) * Service_Factor_Bearing
    print("Peq", Peq)
    # PSG 4.2 Start

    C = Peq * (Lmr) ** (1 / k)
    C_inkgf = C * 100
    print("C_inkgf", C_inkgf)

    New_Outer_Diameter_Do = Root_Diameter_Df + 10
    # PSG 5.124 End

    Corrected_Diameter_Do = PSG_Database('bearingDiacheck', New_Outer_Diameter_Do)
    print("Corrected_Diameter_Do", Corrected_Diameter_Do)

    if Corrected_Diameter_Do == 52:
        C_PSG = 4100
        if C_PSG > C_inkgf:
            Dr = 40
            B = 36
            print("Dr", Dr)
            Bearing = "RNA 6906"
        elif C_PSG < C_inkgf:
            Corrected_Diameter_Do = 55
    elif Corrected_Diameter_Do == 55:
        C_PSG = 4200
        if C_PSG > C_inkgf:
            Dr = 42
            B = 36
            print("Dr", Dr)
            Bearing = "RNA 6907"
        elif C_PSG < C_inkgf:
            Corrected_Diameter_Do = 62
    elif Corrected_Diameter_Do == 62:
        C_PSG = 5800
        if C_PSG > C_inkgf:
            Dr = 48
            B = 40
            print("Dr", Dr)
            Bearing = "RNA 6908"
        elif C_PSG < C_inkgf:
            Corrected_Diameter_Do = 68
    elif Corrected_Diameter_Do == 68:
        C_PSG = 6000
        if C_PSG > C_inkgf:
            Dr = 52
            B = 40
            print("Dr", Dr)
            Bearing = "RNA 6909"
        elif C_PSG < C_inkgf:
            Corrected_Diameter_Do = 72
    elif Corrected_Diameter_Do == 72:
        C_PSG = 6200
        if C_PSG > C_inkgf:
            Dr = 58
            B = 40
            print("Dr", Dr)
            Bearing = "RNA 6910"
        elif C_PSG < C_inkgf:
            Corrected_Diameter_Do = 85
    elif Corrected_Diameter_Do == 85:
        C_PSG = 8100
        if C_PSG > C_inkgf:
            Dr = 68
            B = 45
            print("Dr", Dr)
            Bearing = "RNA 6912"
        elif C_PSG < C_inkgf:
            Corrected_Diameter_Do = 100
    elif Corrected_Diameter_Do == 100:
        C_PSG = 11300
        if C_PSG > C_inkgf:
            Dr = 80
            B = 54
            print("Dr", Dr)
            Bearing = "RNA 6914"
        elif C_PSG < C_inkgf:
            Corrected_Diameter_Do = 110
    elif Corrected_Diameter_Do == 110:
        C_PSG = 11900
        if C_PSG > C_inkgf:
            Dr = 90
            B = 54
            print("Dr", Dr)
            Bearing = "RNA 6916"
        elif C_PSG < C_inkgf:
            Corrected_Diameter_Do = 125
    elif Corrected_Diameter_Do == 125:
        C_PSG = 15100
        if C_PSG > C_inkgf:
            Dr = 105
            B = 63
            print("Dr", Dr)
            Bearing = "RNA 6918"

    print(Bearing)

    # Step 3.3: Shaft Design

    # Assumptions:
    Clearance_Shaft = 10
    Shear_Stress_PSG = 45

    Label(assumptionsWindow, text="Clearance Shaft").grid(row=12, column=1)
    Label(assumptionsWindow, text=Clearance_Shaft).grid(row=12, column=2)
    Label(assumptionsWindow, text="mm").grid(row=12, column=3)
    Label(assumptionsWindow, text="").grid(row=12, column=4)    # Enter PSG Reference if possible or else leave blank

    Label(assumptionsWindow, text="Shear Stress(PSG)").grid(row=13, column=1)
    Label(assumptionsWindow, text=Shear_Stress_PSG).grid(row=13, column=2)
    Label(assumptionsWindow, text="N/mm2").grid(row=13, column=3)       # change unit if it's wrong
    Label(assumptionsWindow, text="").grid(row=13, column=4)  # Enter PSG Reference if possible or else leave blank

    Span_Length = B + New_width + Clearance_Shaft
    Max_Bending_Moment = (Resultant_Force * 1000 * Span_Length) / 4

    Equivalent_Torque = math.sqrt((Torque ** 2) + (Max_Bending_Moment ** 2))
    print("Equivalent_Torque", Equivalent_Torque)

    Shear_Stress_Actual = 16 * Equivalent_Torque / (math.pi * Dr ** 3)
    print("Shear_Stress_Actual", Shear_Stress_Actual)
    if Shear_Stress_PSG > Shear_Stress_Actual:
        print("############## Sucessfully passed Shaft-Shear Failure Test")

    elif Shear_Stress_PSG < Shear_Stress_Actual:
        print("############## Shaft failure due to Shear")
        errorFlag('Shaft failure due to Shear')
        time.sleep(5)
        exit()

    # Fetch from PSG Database value of new coupling no.
    Coupling_No_New = PSG_Database('NewCouplingRange', Dr)

    if Coupling_No_New == 1:
        Standard_Max_rating = 0.4
        Coupling_No = 1
        Amin = 12
        Amax = 16
        B = 80
        C = 25
        E = 28
        G = 18
    elif Coupling_No_New == 2:
        Standard_Max_rating = 0.6
        Coupling_No = 2
        Amin = 16
        Amax = 22
        B = 100
        C = 30
        E = 30
        G = 20
    elif Coupling_No_New == 3:
        Standard_Max_rating = 0.8
        Coupling_No = 3
        Amin = 22
        Amax = 30
        B = 112
        C = 38
        E = 32
        G = 22
    elif Coupling_No_New == 4:
        Standard_Max_rating = 2.5
        Coupling_No = 4
        Amin = 30
        Amax = 45
        B = 132
        C = 55
        E = 40
        G = 30
    elif Coupling_No_New == 5:
        Standard_Max_rating = 4.0
        Coupling_No = 5
        Amin = 45
        Amax = 56
        B = 170
        C = 80
        E = 45
        G = 35
    elif Coupling_No_New == 6:
        Standard_Max_rating = 6.0
        Coupling_No = 6
        Amin = 56
        Amax = 75
        B = 200
        C = 100
        E = 56
        G = 40
    elif Coupling_No_New == 7:
        Standard_Max_rating = 16.0
        Coupling_No = 7
        Amin = 75
        Amax = 85
        B = 250
        C = 140
        E = 63
        G = 45
    elif Coupling_No_New == 8:
        Standard_Max_rating = 25.0
        Coupling_No = 8
        Amin = 85
        Amax = 110
        B = 315
        C = 180
        E = 80
        G = 50
    elif Coupling_No_New == 9:
        Standard_Max_rating = 52.0
        Coupling_No = 9
        Amin = 110
        Amax = 130
        B = 400
        C = 212
        E = 90
        G = 56
    elif Coupling_No_New == 10:
        Standard_Max_rating = 74.0
        Coupling_No = 10
        Amin = 130
        Amax = 150
        B = 500
        C = 280
        E = 100
        G = 60

    print("Coupling_No_New", Coupling_No_New)
    print("Standard_Max_rating", Standard_Max_rating)
    # Step 3.4: Casing

    # Assumptions:
    Tensile_Stress_Casing = 200
    FoS_Casing = 6

    Label(assumptionsWindow, text="Tensile Stress Casing").grid(row=14, column=1)
    Label(assumptionsWindow, text=Tensile_Stress_Casing).grid(row=14, column=2)
    Label(assumptionsWindow, text=" ").grid(row=14, column=3)       # Enter units
    Label(assumptionsWindow, text="").grid(row=14, column=4)  # Enter PSG Reference if possible or else leave blank

    Label(assumptionsWindow, text="FoS for Casing").grid(row=15, column=1)
    Label(assumptionsWindow, text=FoS_Casing).grid(row=15, column=2)
    Label(assumptionsWindow, text=" ").grid(row=15, column=3)       # change unit if it's wrong
    Label(assumptionsWindow, text="").grid(row=15, column=4)  # Enter PSG Reference if possible or else leave blank

    Safe_Tensile_Stress_Casing = Tensile_Stress_Casing / FoS_Casing

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

    # By Thick Cylinder Theory:
    Thickness_Casing = (Corrected_Diameter_Do / 2) * (
            ((Safe_Tensile_Stress_Casing + Pmax) / (Safe_Tensile_Stress_Casing - Pmax)) ** (1 / 2) - 1)
    print("Thickness_Casing", Thickness_Casing)

    Final_Thickness_Casing = math.ceil(Thickness_Casing / 2.) * 2
    print("Final_Thickness_Casing", Final_Thickness_Casing)

    C_casing = Corrected_Diameter_Do + Pitch_Diameter_D
    PCD_casing = C_casing + 3 * Bolt_diameter
    Outer_Diameter_Casing = PCD_casing + 3 * Bolt_diameter

    # Step 3.5: Fasteners/ Bolts

    # Assumptions:
    Tensile_Stress_Fastener = 80  # Change to dropdown
    Stiffness_Tighting = 0.33
    Stiffness_External = 0.67

    Label(assumptionsWindow, text="Stiffness Tighting").grid(row=16, column=1)
    Label(assumptionsWindow, text=Stiffness_Tighting).grid(row=16, column=2)
    Label(assumptionsWindow, text=" ").grid(row=16, column=3)
    Label(assumptionsWindow, text="").grid(row=16, column=4)  # Enter PSG Reference if possible or else leave blank

    Label(assumptionsWindow, text="Stiffness External").grid(row=17, column=1)
    Label(assumptionsWindow, text=Stiffness_External).grid(row=17, column=2)
    Label(assumptionsWindow, text=" ").grid(row=17, column=3)
    Label(assumptionsWindow, text="").grid(row=16, column=4)  # Enter PSG Reference if possible or else leave blank

    Design_Pressure = 1.2 * Pressure_in_N_mm2
    Openning_Pressure = 1.5 * Pressure_in_N_mm2
    Projected_Area = ((math.pi / 4) * Outer_Diameter_Do ** 2) + Outer_Diameter_Do * 56
    print("Project Area", Projected_Area)

    External_Force_Fe = Design_Pressure * Projected_Area
    print("External_Force", External_Force_Fe)

    Opening_Force_Fo = Openning_Pressure * Projected_Area
    print("Opening_Force", Opening_Force_Fo)

    Initial_Tightening_Force_Fi = Opening_Force_Fo * Stiffness_Tighting
    Net_Force_Bolt_Fb = Initial_Tightening_Force_Fi + External_Force_Fe * Stiffness_External
    print("Net_Force_Bolt_Fb", Net_Force_Bolt_Fb)

    # Input
    # Bolts like M2.5,3,4,5,6,8,10,12,16,20,24,30,33,36

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

    Actual_Tensile_Bolt = Net_Force_Bolt_Fb / (PCD_Holes * Bolt_Dict["M12"])
    print("Actual_Tensile_Bolt", Actual_Tensile_Bolt)

    while Actual_Tensile_Bolt > Tensile_Stress_Fastener:
        PCD_Holes = PCD_Holes + 1
        # print(PCD_Holes)
        Actual_Tensile_Bolt = Net_Force_Bolt_Fb / (PCD_Holes * Bolt_Dict["M12"])
    #
    if Actual_Tensile_Bolt < Tensile_Stress_Fastener:
        print("No. of Bolt Holes in casing would be ", PCD_Holes)

    print("Actual_Tensile_Bolt", Actual_Tensile_Bolt)

    # Part 3 End: Pump Unit
    #################################################################################################################

    # Part 4: Piping Unit

    # Step4.1: Suction Side

    # Assumptions:
    Velocity_Suction = 1

    Label(assumptionsWindow, text="Velocity of Suction").grid(row=18, column=1)
    Label(assumptionsWindow, text=Velocity_Suction).grid(row=18, column=2)
    Label(assumptionsWindow, text=" ").grid(row=18, column=3)       # Enter units for velocity of Suction
    Label(assumptionsWindow, text="").grid(row=18, column=4)  # Enter PSG Reference if possible or else leave blank

    Diameter_of_Suction = (((4 * Discharge) / (math.pi * Velocity_Suction)) ** (1 / 2)) * 1000
    print("Diameter_of_Suction", Diameter_of_Suction)

    Diameter_of_Suction = PSG_Database('standardPipedia', Diameter_of_Suction)

    print("Corrected Diameter of Suction(in mm) = ", 25.4 * Diameter_of_Suction)

    Actual_Suction_Velocity = (4 * Discharge * 1000000) / (math.pi * (25.4 * Diameter_of_Suction) ** 2)
    print("Actual_Suction_Velocity", Actual_Suction_Velocity)

    # Step4.2: Delivery Side

    # Assumptions:
    Velocity_Delivery = 2

    Label(assumptionsWindow, text="Velocity of Delivery").grid(row=19, column=1)
    Label(assumptionsWindow, text=Velocity_Delivery).grid(row=19, column=2)
    Label(assumptionsWindow, text=" ").grid(row=19, column=3)       # Enter units for velocity of Delivery
    Label(assumptionsWindow, text="").grid(row=19, column=4)  # Enter PSG Reference if possible or else leave blank

    Diameter_of_Delivery = (((4 * Discharge) / (math.pi * Velocity_Delivery)) ** (1 / 2)) * 1000
    print("Diameter_of_Delivery = ", Diameter_of_Delivery)

    Diameter_of_Delivery = PSG_Database('standardPipedia', Diameter_of_Delivery)

    print("Corrected Diameter of Delivery(in mm) = ", Diameter_of_Delivery)

    Actual_Delivery_Velocity = (4 * Discharge * 1000000) / (math.pi * (25.4 * Diameter_of_Delivery) ** 2)
    print("Actual_Delivery_Velocity = ", Actual_Delivery_Velocity)

    # Add a grid for Output
    Root3 = Tk()
    Root3.title("Result")

    resultWindow = Frame(Root3)
    resultWindow.grid(column=0, row=0, sticky=(W, N, E, S))
    resultWindow.columnconfigure(0, weight=1)
    resultWindow.rowconfigure(0, weight=1)
    resultWindow.pack(pady=60, padx=50)

    Label(resultWindow, text="Coupling No.").grid(row=1, column=1)
    Label(resultWindow, text=Coupling_No).grid(row=1, column=2)
    Label(resultWindow, text="").grid(row=1, column=3)      # Enter unit next to coupling No.

    Label(resultWindow, text="Amin").grid(row=2, column=1)
    Label(resultWindow, text=Amin).grid(row=2, column=2)
    Label(resultWindow, text="mm").grid(row=2, column=3)  # Correct if unit is not 'mm'

    Label(resultWindow, text="Amax").grid(row=3, column=1)
    Label(resultWindow, text=Amax).grid(row=3, column=2)
    Label(resultWindow, text="mm").grid(row=3, column=3)  # Correct if unit is not 'mm'

    Label(resultWindow, text="B").grid(row=4, column=1)
    Label(resultWindow, text=B).grid(row=4, column=2)
    Label(resultWindow, text="mm").grid(row=4, column=3)  # Correct if unit is not 'mm'

    Label(resultWindow, text="C").grid(row=5, column=1)
    Label(resultWindow, text=C).grid(row=5, column=2)
    Label(resultWindow, text="mm").grid(row=5, column=3)  # Correct if unit is not 'mm'

    Label(resultWindow, text="E").grid(row=6, column=1)
    Label(resultWindow, text=E).grid(row=6, column=2)
    Label(resultWindow, text="mm").grid(row=6, column=3)  # Correct if unit is not 'mm'

    Label(resultWindow, text="G").grid(row=7, column=1)
    Label(resultWindow, text=G).grid(row=7, column=2)
    Label(resultWindow, text="mm").grid(row=7, column=3)  # Correct if unit is not 'mm'

    Label(resultWindow, text="Diameter of Suction").grid(row=7, column=1)
    Label(resultWindow, text=G).grid(row=7, column=2)
    Label(resultWindow, text="mm").grid(row=7, column=3)  # Correct if unit is not 'mm'

    Root3.mainloop()
    Root2.mainloop()


Root1.mainloop()
