## This is the program to run the AutoCountry Vehicle Finder app, version 0.2 ##

## ------------------------------ Functions ------------------------------ ##
# F(x) to check which choice inputted, validate choice #
def checkValidInputFX(testInputNum):
  if testInputNum == "1":
    print(f"{choice1Message}")
    for a in range(0,5):
      print(carMakes[a])
  elif testInputNum == "2":
    return True
  elif testInputNum == "3":
    print("\nThank you for using AutoCountry Car Finder, good-bye!")
    exit()
  else:
    print(f"""
    Sorry, {testInputNum} is not a valid input.
    Please try again with the correct input from the provided list.
    """)
    exit()

# F(x) to check authorization of vehicle #
def checkVehicleFX(testInputVehicle):
  if testInputVehicle in carMakes:
    print(f"\n{testInputVehicle} is an authorized vehicle")
  else:
    print(f"""
    {testInputVehicle} is not an authorized vehicle, if you recieved this in error please check the spelling and try again.
    """)


## --------------------------- Declerations ---------------------------- ##
carMakes = ["Ford F-150", "Chevrolet Silverado", "Tesla CyberTruck", "Toyota Tundra", "Nissan Titan"]
welcomeMessage = """
  ********************************
  AutoCountry Vehicle Finder v0.2
  ********************************
  Please enter the following number from the following menu:
   \n
    1. PRINT all Authorized Vehicles
    2. SEARCH for Authorized Vehicle
    3. Exit
"""
choice1Message = "\nThe AutoCountry sales manages has authorized the purchase and selling of the following vehicles: "
choice2Message = """
  ***********************************
  Please enter the full vehicle name:
  ***********************************
"""


## --------------------- Customer facing, functions, output --------------------- ##
print(welcomeMessage)
customerChoiceInput = input()
validChoiceInput = checkValidInputFX(customerChoiceInput)

if validChoiceInput == True:
  print(choice2Message)
  customerVehicleInput = input()
  validVehicleInput = checkVehicleFX(customerVehicleInput)
