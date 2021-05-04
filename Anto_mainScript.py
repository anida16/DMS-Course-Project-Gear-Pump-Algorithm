import math
import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
from PIL import ImageTk, Image
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Windows of the GUI :-
#     Root1 ->  Input Window
#     Root2 ->  Assumptions, Results and Actual vs PSG Stresses Window
#     Root3 ->  Error Window
#     Root4 ->  Graph Window


def errorFlag(errorMessage):
    Root3 = tk.Toplevel()
    Root3.geometry("500x200")
    Root3.title("Error Window")

    # Define background image
    bg = PhotoImage(file="Background.png")

    # Create a Canvas
    errorCanvas = Canvas(Root3)
    errorCanvas.pack(side=LEFT, fill=BOTH, expand=1)

    errorCanvas.create_image(0, 0, image=bg, anchor="nw")
    errorCanvas.create_text(40, 90, text="Error : ", font=("Helvetica", 15), fill="white")
    errorCanvas.create_text(250, 90, text=f'{errorMessage}', font=("Helvetica", 15), fill="white")

    OK_btn = Button(Root3, text='OK', width=5, height=1, command=lambda: Root3.destroy())
    OK_btnWindow = errorCanvas.create_window(200, 120, anchor="nw", window=OK_btn)
    time.sleep(2)
    Root3.mainloop()


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
    elif database == 'Bolt Dia Dict':
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
        return Bolt_Dia_Dict[value]
    elif database == 'Bolt Dict':
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
        return Bolt_Dict[value]
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
Root1.geometry("400x300")

# Define background image
bg1 = PhotoImage(file="Background.png")

# Create a Canvas
inputCanvas = Canvas(Root1)
inputCanvas.pack(side=LEFT, fill=BOTH, expand=1)

inputCanvas.create_image(0, 0, image=bg1, anchor="nw")

'''
Input
Discharge in LPM (Litre per minute) and Pressure (in bar)
'''
# Input Boxes for the GUI Design
# Discharge and Input Pressure
inputCanvas.create_text(70, 10, text="Anthony D'souza", font=("Helvetica", 10), fill="white")
inputCanvas.create_text(170, 10, text="Anish Dalvi", font=("Helvetica", 10), fill="white")
inputCanvas.create_text(270, 10, text="Rohan D'souza", font=("Helvetica", 10), fill="white")
inputCanvas.create_text(390, 10, text="Abhishek Gupta", font=("Helvetica", 10), fill="white")
inputCanvas.create_text(520, 10, text="Spandan Bhatacharjee", font=("Helvetica", 10), fill="white")
inputCanvas.create_text(70, 25, text="201718", font=("Helvetica", 10), fill="white")
inputCanvas.create_text(170, 25, text="201713", font=("Helvetica", 10), fill="white")
inputCanvas.create_text(270, 25, text="201719", font=("Helvetica", 10), fill="white")
inputCanvas.create_text(390, 25, text="201722", font=("Helvetica", 10), fill="white")
inputCanvas.create_text(520, 25, text="201706", font=("Helvetica", 10), fill="white")

inputCanvas.create_text(100, 100, text="Discharge(LPM)", font=("Helvetica", 10), fill="white")
dischargeInput = Entry(Root1, font=("Helvetica", 10), width=10)
inputCanvas.create_window(200, 90, anchor="nw", window=dischargeInput)

inputCanvas.create_text(100, 130, text="Pressure(in bar)", font=("Helvetica", 10), fill="white")
pressureInput = Entry(Root1, font=("Helvetica", 10), width=10)  # speed
inputCanvas.create_window(200, 120, anchor="nw", window=pressureInput)

# Material Selection Drop Down
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

material = StringVar(Root1)  # this is where value selected by user is stored #Material Designation
bolt = StringVar(Root1)
inputCanvas.create_text(100, 160, text="Choose Casing Bolt Diameter", font=("Helvetica", 10), fill="white")
optList = ['CCI_Grade_20', 'CI_Grade_25', 'CI_Grade_35', 'CI_Grade_35_Heat_Treated', 'Steel_C45', 'Steel_15Ni2Cr1Mo15',
           'Steel_40Ni2Cr1Mo28']
material.set(optList[6])
popupMenu = OptionMenu(Root1, material, *optList)
inputCanvas.create_window(200, 150, anchor="nw", window=popupMenu)

# controls position of name of popup grid
inputCanvas.create_text(100, 200, text="Choose Material for Gear", font=("Helvetica", 10), fill="white")
optList2 = ['M2.5', 'M3', 'M4', 'M5', 'M6', 'M8', 'M10', 'M12', 'M16', 'M20', 'M24', 'M30', 'M33', 'M36']
bolt.set(optList2[7])
popupMenu2 = OptionMenu(Root1, bolt, *optList2)
inputCanvas.create_window(200, 190, anchor="nw", window=popupMenu2)

# Input
# Bolts like M2.5,3,4,5,6,8,10,12,16,20,24,30,33,36

# Submit button to end the input
button1 = Button(Root1, text="Submit", bg='cyan', fg='black', height=1, width=6, command=lambda: mainProgram())
inputCanvas.create_window(120, 250, anchor="nw", window=button1)

button1 = Button(Root1, text="Exit", bg='cyan', fg='black', height=1, width=6, command=lambda: Root1.destroy())
inputCanvas.create_window(200, 250, anchor="nw", window=button1)

str_out = tk.StringVar(Root1)
str_out.set("Output")


#######################################################################################################################


def mainProgram():
    # GUI widgets for Result and assumptions window

    if material.get() == 'CCI_Grade_20':
        Bending_stress = 50
        Tensile_Stress = 500
        Modulus_Elasticity = 210000
    elif material.get() == 'CI_Grade_25':
        Bending_stress = 60
        Tensile_Stress = 600
        Modulus_Elasticity = 210000
    elif material.get() == 'CI_Grade_35':
        Bending_stress = 60
        Tensile_Stress = 600
        Modulus_Elasticity = 210000
    elif material.get() == 'CI_Grade_35_Heat_Treated':
        Bending_stress = 80
        Tensile_Stress = 750
        Modulus_Elasticity = 210000
    elif material.get() == 'Steel_C45':
        Bending_stress = 140
        Tensile_Stress = 500
        Modulus_Elasticity = 210000
    elif material.get() == 'Steel_15Ni2Cr1Mo15':
        Bending_stress = 320
        Tensile_Stress = 950
        Modulus_Elasticity = 210000
    elif material.get() == 'Steel_40Ni2Cr1Mo28':
        Bending_stress = 400
        Tensile_Stress = 1100
        Modulus_Elasticity = 210000
    else:
        print("Error: Invalid material")
        errorFlag('Invalid material')
        exit()

    # Bolt designation selected will be used to determine the bolt diameter
    boltDesignation = bolt.get()

    # Assumptions Start
    Mech_efficiency = 0.93
    Volumetric_Efficiency = 0.97
    Service_Factor = 1.5  # PSG 7.109 for Rotary Pump

    # Assumptions Ends

    # Part 1: Drive Unit
    Discharge = float(dischargeInput.get())
    print("Discharge = ", Discharge)
    Pressure = float(pressureInput.get())
    print("Pressure = ", Pressure)
    print("data type of Discharge :- ", type(Discharge))
    print("data type of Pressure :- ", type(Pressure))
    Corrected_Discharge = Discharge / (60 * 1000)
    Corrected_Pressure = Pressure * 100000

    Motor_Power = (Corrected_Discharge * Corrected_Pressure) / (Mech_efficiency * Volumetric_Efficiency)

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
        exit()
    print("corrected standard motor", Corrected_Standard_Motor)

    # We completely assume the Speed as 960RPM (Rukhande Sir said too), no mention anywhere
    Speed = 960


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
        exit()
    else:
        if Standard_Max_rating == 0.4:
            Coupling_No = 1
            Amin = 12
            Amax = 16
            B = 80
            C = 25
            Eo = 28
            G = 18
        elif Standard_Max_rating == 0.6:
            Coupling_No = 2
            Amin = 16
            Amax = 22
            B = 100
            C = 30
            Eo = 30
            G = 20
        elif Standard_Max_rating == 0.8:
            Coupling_No = 3
            Amin = 22
            Amax = 30
            B = 112
            C = 38
            Eo = 32
            G = 22
        elif Standard_Max_rating == 2.5:
            Coupling_No = 4
            Amin = 30
            Amax = 45
            B = 132
            C = 55
            Eo = 40
            G = 30
        elif Standard_Max_rating == 4.0:
            Coupling_No = 5
            Amin = 45
            Amax = 56
            B = 170
            C = 80
            Eo = 45
            G = 35
        elif Standard_Max_rating == 6.0:
            Coupling_No = 6
            Amin = 56
            Amax = 75
            B = 200
            C = 100
            Eo = 56
            G = 40
        elif Standard_Max_rating == 16.0:
            Coupling_No = 7
            Amin = 75
            Amax = 85
            B = 250
            C = 140
            Eo = 63
            G = 45
        elif Standard_Max_rating == 25.0:
            Coupling_No = 8
            Amin = 85
            Amax = 110
            B = 315
            C = 180
            Eo = 80
            G = 50
        elif Standard_Max_rating == 52.0:
            Coupling_No = 9
            Amin = 110
            Amax = 130
            B = 400
            C = 212
            Eo = 90
            G = 56
        elif Standard_Max_rating == 74.0:
            Coupling_No = 10
            Amin = 130
            Amax = 150
            B = 500
            C = 280
            Eo = 100
            G = 60

    print(Coupling_No)

    # PSG 7.108 End

    # Part 2 End: Transmission Unit
    ###############################################################################################################

    # Part 3: Pump Unit

    # Assumptions:
    Gear_Ratio = 1
    Pressure_Angle = 20

    # Step 3.1: Design of Gears

    '''
    Bending_stress = 400
    Tensile_Stress = 1100
    Modulus_Elasticity = 210000
    '''
    # Assumptions:
    No_Teeth = 14

    print("Discharge", Discharge)
    print("Speed", Speed)
    print("Volumetric_Efficiency", Volumetric_Efficiency)

    Module_in_mm = (((Discharge * 4) / (Speed * 7 * Volumetric_Efficiency * math.pi * 112 * 1000)) ** (1 / 3)) * 1000
    print("Module", Module_in_mm)
    # PSG Page 8.2 Start

    # ******************Fetch the value of module(in mm) from PSG Database*********************
    Corrected_Standard_Module = PSG_Database('standardModule', Module_in_mm)
    print("Standard Module", Corrected_Standard_Module)

    Pitch_Diameter_D = Corrected_Standard_Module * No_Teeth
    Outer_Diameter_Do = 16 * Corrected_Standard_Module
    Root_Diameter_Df = 12 * Corrected_Standard_Module
    Clearance = 0.25 * Corrected_Standard_Module
    Width = 7 * Corrected_Standard_Module
    print("Old width", Width)
    New_width = (Discharge * 1000000) / (2 * math.pi * (Corrected_Standard_Module ** 2) * No_Teeth * Volumetric_Efficiency * Speed)
    print("New Width before", New_width)

    if New_width < Width:
        New_width = Width
        print("Old Width is higher")

    print("Width New Final", New_width)

    # Test for Bending

    Y1 = math.pi * (0.154 - (0.912 / No_Teeth))
    print("Y1", Y1)

    Torque = (Corrected_Standard_Motor * 1000 * 60) / (2 * 2 * math.pi * Speed)
    print("Torque", Torque)

    b_by_m = New_width / Corrected_Standard_Module

    Actual_Bending_Stress = (Torque * 2000) / (b_by_m * No_Teeth * Y1 * (Corrected_Standard_Module) ** (3))
    print("Actual_Bending_Stress", Actual_Bending_Stress)

    if Actual_Bending_Stress > Bending_stress:
        print("Error: Failed at Bending")
        errorFlag('Failure at Bending')
        time.sleep(5)
        exit()
    elif Actual_Bending_Stress < Bending_stress:  # Remark: What if the two values are equal? pass or fail
        print("###############Sucessfully passed Bending testing")

    # Test for Dynamic Load
    # PSG 8.50

    Static_Force = (Bending_stress * New_width * Y1 * Corrected_Standard_Module) / 1000
    print("Static Force", Static_Force)

    Velocity = (math.pi * Pitch_Diameter_D * Speed) / 60000
    print("Velocity", Velocity)

    Barth_Velocity = (5.5 + Velocity ** (1 / 2)) / 5.5
    print("Barth velocity", Barth_Velocity)

    Tangential_Load = Corrected_Standard_Motor / Velocity
    print("Tangetial Load", Tangential_Load)

    Dynamic_Force = Tangential_Load * Barth_Velocity
    print("dynamic force", Dynamic_Force)

    if Dynamic_Force > Static_Force:
        print("Error: Dynamic force greater than static")
        errorFlag('Dynamic Force greater than Static Force')
        time.sleep(5)
        exit()
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

    C_1 = Peq * (Lmr) ** (1 / k)
    C_inkgf = C_1 * 100
    print("C_inkgf", C_inkgf)

    New_Outer_Diameter_Do = Root_Diameter_Df + 10
    print("New_Outer_Diameter_Do", New_Outer_Diameter_Do)
    # PSG 5.124 End

    Corrected_Diameter_Do = PSG_Database('bearingDiacheck', New_Outer_Diameter_Do)
    # print("Corrected_Diameter_Do", Corrected_Diameter_Do)

    if Corrected_Diameter_Do == 52:
        C_PSG = 4100
        if C_PSG > C_inkgf:
            Dr = 40
            B = 36
            print("Dr", Dr)
            Bearing = "RNA 6906"
        elif C_PSG < C_inkgf:
            Corrected_Diameter_Do = 55

    if Corrected_Diameter_Do == 55:
        C_PSG = 4200
        if C_PSG > C_inkgf:
            Dr = 42
            B = 36
            print("Dr", Dr)
            Bearing = "RNA 6907"
        elif C_PSG < C_inkgf:
            Corrected_Diameter_Do = 62

    if Corrected_Diameter_Do == 62:
        C_PSG = 5800
        if C_PSG > C_inkgf:
            Dr = 48
            B = 40
            print("Dr", Dr)
            Bearing = "RNA 6908"
        elif C_PSG < C_inkgf:
            Corrected_Diameter_Do = 68

    if Corrected_Diameter_Do == 68:
        C_PSG = 6000
        if C_PSG > C_inkgf:
            Dr = 52
            B = 40
            print("Dr", Dr)
            Bearing = "RNA 6909"
        elif C_PSG < C_inkgf:
            Corrected_Diameter_Do = 72

    if Corrected_Diameter_Do == 72:
        C_PSG = 6200
        if C_PSG > C_inkgf:
            Dr = 58
            B = 40
            print("Dr", Dr)
            Bearing = "RNA 6910"
        elif C_PSG < C_inkgf:
            Corrected_Diameter_Do = 85

    if Corrected_Diameter_Do == 85:
        C_PSG = 8100
        if C_PSG > C_inkgf:
            Dr = 68
            B = 45
            print("Dr", Dr)
            Bearing = "RNA 6912"
        elif C_PSG < C_inkgf:
            Corrected_Diameter_Do = 100

    if Corrected_Diameter_Do == 100:
        C_PSG = 11300
        if C_PSG > C_inkgf:
            Dr = 80
            B = 54
            print("Dr", Dr)
            Bearing = "RNA 6914"
        elif C_PSG < C_inkgf:
            Corrected_Diameter_Do = 110

    if Corrected_Diameter_Do == 110:
        C_PSG = 11900
        if C_PSG > C_inkgf:
            Dr = 90
            B = 54
            print("Dr", Dr)
            Bearing = "RNA 6916"
        elif C_PSG < C_inkgf:
            Corrected_Diameter_Do = 125

    if Corrected_Diameter_Do == 125:
        C_PSG = 15100
        if C_PSG > C_inkgf:
            Dr = 105
            B = 63
            print("Dr", Dr)
            Bearing = "RNA 6918"

    print("Corrected_Diameter_Do", Corrected_Diameter_Do)
    if Corrected_Diameter_Do > New_Outer_Diameter_Do:
        print("No suitable Needle Bearing Available, so selecting Sliding Contact bearing")

        Bearing = "Sliding Contact bearing"
        New_New_Outer_Diameter_Do = New_Outer_Diameter_Do - 2
        Journal_Diameter = New_New_Outer_Diameter_Do - 4
        print("Journal_Diameter"", Journal_Diameter)

        # Assumption,
        Pressure_Journal_Bearing = 1.4  # from PSG 7.31
        Bearing_length = (Radial_Force * 1000) / (Pressure_Journal_Bearing * Journal_Diameter)
        New_bearing_Length = (math.ceil(Bearing_length / 10)) * 10
        print("New_bearing_Length", New_bearing_Length)

        Bearing_span = New_bearing_Length + New_width
        print("Bearing_span", Bearing_span)

        Max_Bending_Moment_temp = (2 * Radial_Force * 1000 * Bearing_span) / 4
        Max_Bending_Moment = Max_Bending_Moment_temp / 1000
        print("Max_Bending_Moment", Max_Bending_Moment)
        Dr1 = Root_Diameter_Df

    if Corrected_Diameter_Do < New_Outer_Diameter_Do:
        print(Bearing)
        Dr1 = Dr

        # Step 3.3: Shaft Design

        # Assumptions:
        Clearance_Shaft = 10

        Span_Length = B + New_width + Clearance_Shaft
        Max_Bending_Moment = (Resultant_Force * 1000 * Span_Length) / 4000
        print("Max_Bending_Moment", Max_Bending_Moment)

    # Step 3.3: Shaft Design

    # Assumptions:

    Shear_Stress_PSG = 45

    Equivalent_Torque = math.sqrt((Torque ** 2) + (Max_Bending_Moment ** 2))
    print("Equivalent_Torque", Equivalent_Torque)

    Shear_Stress_Actual = (16000 * Equivalent_Torque) / (math.pi * (Dr1 ** 3))
    print("Shear_Stress_Actual", Shear_Stress_Actual)
    if Shear_Stress_PSG > Shear_Stress_Actual:
        print("############## Sucessfully passed Shaft-Shear Failure Test")
    elif Shear_Stress_PSG < Shear_Stress_Actual:
        print("############## Shaft failure due to Shear")
        errorFlag('Shaft failure due to Shear')
        time.sleep(5)
        exit()

    # Fetch from PSG Database value of new coupling no.
    if Corrected_Diameter_Do < New_Outer_Diameter_Do:
        Coupling_No_New = PSG_Database('NewCouplingRange', Dr)

        if Coupling_No_New == 1:
            Standard_Max_rating = 0.4
            Coupling_No = 1
            Amin = 12
            Amax = 16
            B = 80
            C = 25
            Eo = 28
            G = 18
        elif Coupling_No_New == 2:
            Standard_Max_rating = 0.6
            Coupling_No = 2
            Amin = 16
            Amax = 22
            B = 100
            C = 30
            Eo = 30
            G = 20
        elif Coupling_No_New == 3:
            Standard_Max_rating = 0.8
            Coupling_No = 3
            Amin = 22
            Amax = 30
            B = 112
            C = 38
            Eo = 32
            G = 22
        elif Coupling_No_New == 4:
            Standard_Max_rating = 2.5
            Coupling_No = 4
            Amin = 30
            Amax = 45
            B = 132
            C = 55
            Eo = 40
            G = 30
        elif Coupling_No_New == 5:
            Standard_Max_rating = 4.0
            Coupling_No = 5
            Amin = 45
            Amax = 56
            B = 170
            C = 80
            Eo = 45
            G = 35
        elif Coupling_No_New == 6:
            Standard_Max_rating = 6.0
            Coupling_No = 6
            Amin = 56
            Amax = 75
            B = 200
            C = 100
            Eo = 56
            G = 40
        elif Coupling_No_New == 7:
            Standard_Max_rating = 16.0
            Coupling_No = 7
            Amin = 75
            Amax = 85
            B = 250
            C = 140
            Eo = 63
            G = 45
        elif Coupling_No_New == 8:
            Standard_Max_rating = 25.0
            Coupling_No = 8
            Amin = 85
            Amax = 110
            B = 315
            C = 180
            Eo = 80
            G = 50
        elif Coupling_No_New == 9:
            Standard_Max_rating = 52.0
            Coupling_No = 9
            Amin = 110
            Amax = 130
            B = 400
            C = 212
            Eo = 90
            G = 56
        elif Coupling_No_New == 10:
            Standard_Max_rating = 74.0
            Coupling_No = 10
            Amin = 130
            Amax = 150
            B = 500
            C = 280
            Eo = 100
            G = 60

        print("Coupling_No_New", Coupling_No_New)
        Coupling_No = Coupling_No_New
        print("Standard_Max_rating", Standard_Max_rating)
    # Step 3.4: Casing

    # Assumptions:
    Tensile_Stress_Casing = 180
    FoS_Casing = 6
    Safe_Tensile_Stress_Casing = Tensile_Stress_Casing / FoS_Casing

    # Fetch Bolt Diameter from PSG Database
    Bolt_diameter = PSG_Database('Bolt Dia Dict', boltDesignation)

    # By Thick Cylinder Theory:
<<<<<<< HEAD
    Thickness_Casing = (Outer_Diameter_Do * 9/ 2) * (
                ((Safe_Tensile_Stress_Casing + Pmax) / (Safe_Tensile_Stress_Casing - Pmax)) ** (1 / 2) - 1)
=======
    Thickness_Casing = (Outer_Diameter_Do / 2) * (((Safe_Tensile_Stress_Casing + Pmax) / (Safe_Tensile_Stress_Casing - Pmax)) ** (1 / 2) - 1)
>>>>>>> Anto
    print("Thickness_Casing", Thickness_Casing)

    Final_Thickness_Casing = math.ceil(Thickness_Casing / 2.) * 2
    print("Final_Thickness_Casing", Final_Thickness_Casing)

    C_casing = Corrected_Diameter_Do + Pitch_Diameter_D
    PCD_casing = C_casing + 3 * Bolt_diameter
    Outer_Diameter_Casing = PCD_casing + 3 * Bolt_diameter
    print("C_casing", C_casing)
    print("PCD_casing", PCD_casing)
    print("Outer_Diameter_Casing", Outer_Diameter_Casing)

    # Step 3.5: Fasteners/ Bolts

    # Assumptions:
    Tensile_Stress_Fastener = 80  # Change to dropdown
    Stiffness_Tighting = 0.33
    Stiffness_External = 0.67

    Design_Pressure = 1.2 * Pressure_in_N_mm2
    Openning_Pressure = 1.5 * Pressure_in_N_mm2
    Projected_Area = ((math.pi / 4) * Outer_Diameter_Do ** 2) + Outer_Diameter_Do * Pitch_Diameter_D
    print("Project Area", Projected_Area)

    External_Force_Fe = Design_Pressure * Projected_Area
    print("External_Force", External_Force_Fe)

    Opening_Force_Fo = Openning_Pressure * Projected_Area
    print("Opening_Force", Opening_Force_Fo)

    Initial_Tightening_Force_Fi = Opening_Force_Fo * Stiffness_Tighting
    Net_Force_Bolt_Fb = Initial_Tightening_Force_Fi + External_Force_Fe * Stiffness_External
    print("Net_Force_Bolt_Fb", Net_Force_Bolt_Fb)

    PCD_Holes = 1

    Actual_Tensile_Bolt = Net_Force_Bolt_Fb / (PCD_Holes * PSG_Database('Bolt Dict', boltDesignation))
    # Fetch Bolt dia from 'Bolt Dict' from PSG Database
    print("Actual_Tensile_Bolt", Actual_Tensile_Bolt)

    while Actual_Tensile_Bolt > Tensile_Stress_Fastener:
        PCD_Holes = PCD_Holes + 1
        # print(PCD_Holes)
        Actual_Tensile_Bolt = Net_Force_Bolt_Fb / (PCD_Holes * PSG_Database('Bolt Dict', boltDesignation))
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

    Diameter_of_Suction = (((4 * Corrected_Discharge) / (math.pi * Velocity_Suction)) ** (1 / 2)) * 1000
    print("Diameter_of_Suction", Diameter_of_Suction)

    Corrected_Pipe_Dia_inch = PSG_Database('standardPipedia', Diameter_of_Suction)

    Corrected_Pipe_Dia_mm = 25.4 * Corrected_Pipe_Dia_inch
    print("(Standard) Corrected_Pipe_Dia_mm", Corrected_Pipe_Dia_mm)

    Actual_Suction_Velocity = (4 * Corrected_Discharge * 1000000) / (math.pi * Corrected_Pipe_Dia_mm ** 2)
    print("Actual_Suction_Velocity", Actual_Suction_Velocity)

    # Step4.2: Delivery Side

    # Assumptions:
    Velocity_Delivery = 2

    Diameter_of_Delivery = (((4 * Corrected_Discharge) / (math.pi * Velocity_Delivery)) ** (1 / 2)) * 1000
    print("Diameter_of_Delivery", Diameter_of_Delivery)

    Corrected_Pipe_Dia_inch2 = PSG_Database('standardPipedia', Diameter_of_Delivery)

    Corrected_Pipe_Dia_mm2 = 25.4 * Corrected_Pipe_Dia_inch2
    print("(Standard) Corrected_Pipe_Dia_mm", Corrected_Pipe_Dia_mm2)

    Actual_Delivery_Velocity = (4 * Corrected_Discharge * 1000000) / (math.pi * Corrected_Pipe_Dia_mm2 ** 2)
    print("Actual_Delivery_Velocity", Actual_Delivery_Velocity)

    Root2 = tk.Toplevel()
    Root2.title("Results Window")

    # Create a mainframe
    mainFrame = Frame(Root2)
    mainFrame.pack(fill=BOTH, expand=1)

    # Create a Canvas
    myCanvas = Canvas(mainFrame)
    myCanvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add a scrollbar to the canvas
    myScrollbar = ttk.Scrollbar(mainFrame, orient=VERTICAL, command=myCanvas.yview)
    myScrollbar.pack(side=RIGHT, fill=Y)

    # Configure the Canvas
    myCanvas.configure(yscrollcommand=myScrollbar.set)
    myCanvas.bind('Configure', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox("all")))

    # create a second Frame
    subFrame = Frame(myCanvas)

    # Add that new frame to the window in the Canvas
    myCanvas.create_window((0, 0), window=subFrame)

    # Define Image
    bgIMG = PhotoImage(file="Background.png")
    fgIMG = PhotoImage(file="Transmission Unit.png")

    # Set Image in Canvas
    myCanvas.create_image(0, 0, image=bgIMG, anchor="nw")
    myCanvas.create_image(150, 10, image=fgIMG, anchor="nw")
    # Assumptions Window starts here
    myCanvas.create_text(200, 280, text="Assumptions", font=("Helvetica", 15), fill="white")

    myCanvas.create_text(100, 310, text="Mechanical Efficiency", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 310, text=Mech_efficiency, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 310, text="", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 310, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 330, text="Volumetric Efficiency", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 330, text=Volumetric_Efficiency, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 330, text="", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 330, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 350, text="Service Factor", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 350, text=Service_Factor, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 350, text="", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 350, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 370, text="Speed", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 370, text=Speed, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 370, text="rpm", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 370, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 390, text="Gear Profile", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 390, text="Involute Full Depth", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 390, text="", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 390, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 410, text="Quality of Gear", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 410, text="Precision Cut", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 410, text="", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 410, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 430, text="Type of Meshing", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 430, text="Sn gearing", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 430, text="", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 430, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 450, text="Gear Type", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 450, text="Spur Gear", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 450, text="", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 450, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 470, text="Gear Ratio", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 470, text=Gear_Ratio, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 470, text="", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 470, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 490, text="Pressure Angle", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 490, text=Pressure_Angle, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 490, text="", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 490, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 510, text="No. of Teeth", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 510, text=No_Teeth, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 510, text="", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 510, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 530, text="Clearance Shaft", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 530, text=Clearance_Shaft, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 530, text="mm", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 530, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 550, text="Shear Stress(PSG)", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 550, text=Shear_Stress_PSG, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 550, text="N/mm2", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 550, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 570, text="Tensile Stress Casing", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 570, text=Tensile_Stress_Casing, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 570, text="N/mm2", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 570, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 590, text="FoS for Casing", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 590, text=FoS_Casing, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 590, text="", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 590, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 610, text="Stiffness Tighting", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 610, text=Stiffness_Tighting, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 610, text="", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 610, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 630, text="Stiffness External", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 630, text=Stiffness_External, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 630, text="", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 630, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 650, text="Velocity of Suction", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 650, text=Velocity_Suction, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 650, text="", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 650, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 670, text="Velocity of Delivery", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 670, text=Velocity_Delivery, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 670, text="", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(400, 670, text="", font=("Helvetica", 10), fill="white")
    # Assumptions Window ends here

    # Results Window starts here
    myCanvas.create_text(200, 700, text="Design Results", font=("Helvetica", 15), fill="white")

    myCanvas.create_text(200, 730, text="Drive Unit Results", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 750, text="Standard Motor", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 750, text=Velocity_Delivery, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 750, text="kW", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 770, text="Motor Speed", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 770, text=Speed, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 770, text="RPM", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(200, 800, text="Transmission Unit Results", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 820, text="Amin", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 820, text='%.2f' % Amin, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 820, text="mm", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 840, text="Amax", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 840, text='%.2f' % Amax, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 840, text="mm", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 860, text="B", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 860, text='%.2f' % B, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 860, text="mm", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 880, text="C", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 880, text='%.2f' % C, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 880, text="mm", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 900, text="E", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 900, text='%.2f' % Eo, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 900, text="mm", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 920, text="G", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 920, text='%.2f' % G, font=("Helvetica", 8), fill="white")
    myCanvas.create_text(300, 920, text="mm", font=("Helvetica", 8), fill="white")

    myCanvas.create_text(200, 950, text="Pump Unit Results", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 970, text="Gear Module", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 970, text='%.2f' % Corrected_Standard_Module, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 970, text="mm", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 990, text="Outer Diameter Do", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 990, text='%.2f' % New_Outer_Diameter_Do, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 990, text="mm", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1010, text="Root Diameter Dr", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1010, text='%.2f' % Root_Diameter_Df, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1010, text="mm", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1020, text="Pitch Diameter D", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1020, text='%.2f' % Pitch_Diameter_D, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1020, text="mm", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1040, text="Width", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1040, text='%.2f' % New_width, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1040, text="mm", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1060, text="Clearance", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1060, text='%.2f' % Clearance, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1060, text="mm", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1080, text="Tangential Load", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1080, text='%.2f' % Tangential_Load, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1080, text="kN", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1100, text="Radial Load", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1100, text='%.2f' % Radial_Load, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1100, text="kN", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1120, text="Hydraulic Force", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1120, text='%.2f' % Hydraulic_Force, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1120, text="kN", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1140, text="Hydraulic Force", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1140, text='%.2f' % Hydraulic_Force, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1140, text="kN", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1160, text="Resultant Force", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1160, text='%.2f' % Resultant_Force, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1160, text="kN", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1180, text="Radial Force", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1180, text='%.2f' % Radial_Force, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1180, text="kN", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1200, text="Radial Force", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1200, text='%.2f' % Radial_Force, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1200, text="kN", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1220, text="LMR", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1220, text=Lmr, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1220, text="millions", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1240, text="Equivalent Load Peq", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1240, text='%.2f' % Peq, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1240, text="kN", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1260, text="Dynamic Load Capacity", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1260, text='%.2f' % C_inkgf, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1260, text="kgf", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1280, text="Bearing Type/Name", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1280, text=Bearing, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1280, text=" ", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1300, text="Coupling Number", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1300, text=Coupling_No, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1300, text=" ", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1320, text="KW per 100RPM", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1320, text='%.2f' % KW_per_100_RPM, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1320, text=" ", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1340, text="Casing Thickness", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1340, text='%.2f' % Final_Thickness_Casing, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1340, text="mm", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1360, text="Bolts PCD (Casing)", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1360, text='%.2f' % PCD_casing, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1360, text="mm", font=("Helvetica", 10), fill="white")

<<<<<<< HEAD
    myCanvas.create_text(100, 1380, text="Outer Diameter of casing", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1380, text='%.2f' % Outer_Diameter_Casing, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1380, text="mm", font=("Helvetica", 10), fill="white")
=======
        Label(newWindow, text="KW per 100RPM", bg='black', fg='yellow').grid(row=19, column=1)
        Label(newWindow, text='%.2f' % Standard_Max_rating, bg='black', fg='yellow').grid(row=19, column=2)
        Label(newWindow, text=" ", bg='black', fg='yellow').grid(row=19, column=3)  # Correct if unit is not 'mm'
>>>>>>> Anto

    myCanvas.create_text(100, 1400, text="Bolts Projected Area", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1400, text='%.2f' % Projected_Area, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1400, text="mm2", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1420, text="External Force", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1420, text='%.2f' % External_Force_Fe, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1420, text="N", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1440, text="Openning Force", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1440, text='%.2f' % Opening_Force_Fo, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1440, text="N", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1460, text="Initial Tightening Load", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1460, text='%.2f' % Initial_Tightening_Force_Fi, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1460, text="N", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1480, text="Net Force on Bolt", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1480, text='%.2f' % Net_Force_Bolt_Fb, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1480, text="N", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1500, text="Number of Bolts", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1500, text=PCD_Holes, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1500, text="", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(200, 1530, text="Piping Unit", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1550, text="Suction Pipe Diameter", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1550, text='%.2f' % Corrected_Pipe_Dia_mm, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1550, text="mm", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1570, text="Suction Velocity", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1570, text='%.2f' % Actual_Suction_Velocity, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1570, text="m/s", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1590, text="Delivery Pipe Diameter", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1590, text='%.2f' % Corrected_Pipe_Dia_mm2, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1590, text="mm", font=("Helvetica", 10), fill="white")

    myCanvas.create_text(100, 1610, text="Delivery Velocity", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(230, 1610, text='%.2f' % Actual_Delivery_Velocity, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1610, text="m/s", font=("Helvetica", 10), fill="white")
    # Results Window ends here

    # Actual Vs. PSG Window starts here
    myCanvas.create_text(200, 1650, text="Actual Vs. PSG Stress", font=("Helvetica", 15), fill="white")

    myCanvas.create_text(130, 1680, text="Bending Stress needed to Bend Gear is", font=("Helvetica", 10),
                         fill="white")
    myCanvas.create_text(300, 1680, text='%.2f' % Actual_Bending_Stress, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(380, 1680, text="which is less than", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(500, 1680, text='%.2f' % Bending_stress, font=("Helvetica", 10), fill="white")

    myCanvas.create_text(130, 1700, text="Dynamic load in gear is", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(300, 1700, text='%.2f' % Dynamic_Force, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(380, 1700, text="which is less than", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(500, 1700, text='%.2f' % Static_Force, font=("Helvetica", 10), fill="white")

    myCanvas.create_text(130, 1720, text="Induced Contact Stress for Pitting failure is", font=("Helvetica", 10),
                         fill="white")
    myCanvas.create_text(300, 1720, text='%.2f' % Actual_Tensile_Stress, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(380, 1720, text="which is less than", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(500, 1720, text='%.2f' % Tensile_Stress, font=("Helvetica", 10), fill="white")

    myCanvas.create_text(130, 1740, text="Shear stress needed to shear shaft is", font=("Helvetica", 10),
                         fill="white")
    myCanvas.create_text(300, 1740, text='%.2f' % Shear_Stress_Actual, font=("Helvetica", 10), fill="white")
    myCanvas.create_text(380, 1740, text="which is less than", font=("Helvetica", 10), fill="white")
    myCanvas.create_text(500, 1740, text='%.2f' % Shear_Stress_PSG, font=("Helvetica", 10), fill="white")

    myCanvas.create_text(200, 1760, text="Sucessfully completed all Tests", font=("Helvetica", 10), fill="white")

    button3 = Button(Root2, text="Plot", bg='cyan', fg='black', height=1, width=5, command=lambda: plot())
    myCanvas.create_window(200, 1790, anchor="nw", window=button3)
    button4 = Button(Root2, text="Exit", height=1, width=5, command=lambda: Root2.destroy())
    myCanvas.create_window(300, 1790, anchor="nw", window=button4)
    # Actual Vs. PSG Window ends here

    def plot():
        Root4 = tk.Toplevel()
        Root4.geometry("500x700")
        Root4.title("Graph of Actual VS. PSG Stress")

        # Define background image
        bg = PhotoImage(file="Background.png")

        # Create a Canvas
        graphCanvas = Canvas(Root4)
        graphCanvas.pack(side=LEFT, fill=BOTH, expand=1)

        graphCanvas.create_image(0, 0, image=bg, anchor="nw")

        # Setting up dataframe for graph plotting
        graphData = {'Actual Stress': [Actual_Bending_Stress, Dynamic_Force, Actual_Tensile_Stress, Shear_Stress_Actual],
                     'Allowable Stress': [Bending_stress, Static_Force, Tensile_Stress, Shear_Stress_PSG]
                     }
        graphDataframe = DataFrame(graphData, columns=['Allowable Stress', 'Actual Stress'])

        # Ploting the graph
        figure = plt.Figure(figsize=(5, 10), dpi=100)
        ax = figure.add_subplot(111)
        line = FigureCanvasTkAgg(figure, graphCanvas)
        line.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, padx=70)
        graphDataframe = graphDataframe[['Allowable Stress', 'Actual Stress']].groupby('Allowable Stress').sum()
        graphDataframe.plot(kind='line', legend=True, ax=ax, color='r', marker='o', fontsize=10)
        ax.set_title('Allowable Stress Vs. Actual Stress')

        Root4.mainloop()

    Root2.mainloop()


Root1.mainloop()
