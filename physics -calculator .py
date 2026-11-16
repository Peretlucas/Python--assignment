


# Function 1: Force
def force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s^2): "))
    result = mass * acceleration
    print("Force =", result, "N")


# Function 2: Momentum
def momentum():
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    result = mass * velocity
    print("Momentum =", result, "kg m/s")


# Function 3: Work
def work():
    force_value = float(input("Enter force (N): "))
    distance = float(input("Enter distance (m): "))
    result = force_value * distance
    print("Work =", result, "J")


# Function 4: Power
def power():
    work_done = float(input("Enter work done (J): "))
    time = float(input("Enter time (s): "))
    if time <= 0:
        print("Time must be greater than zero.")
    else:
        result = work_done / time
        print("Power =", result, "W")


# Function 5: Kinetic Energy
def kinetic_energy():
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    result = 0.5 * mass * velocity ** 2
    print("Kinetic Energy =", result, "J")


# Main program
while True:
    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Force")
    print("2. Momentum")
    print("3. Work")
    print("4. Power")
    print("5. Kinetic Energy")

    choice = input("Select an operation (1-5): ")

    if choice == "1":
        force()
    elif choice == "2":
        momentum()
    elif choice == "3":
        work()
    elif choice == "4":
        power()
    elif choice == "5":
        kinetic_energy()
    else:
        print("Invalid choice. Please select 1-5.")

    continue_choice = input(
        "\nWould you like to continue? (yes/no): "
    ).lower()

    if continue_choice != "yes":
        print("Thank you for using the Physics Calculator!")
        break
