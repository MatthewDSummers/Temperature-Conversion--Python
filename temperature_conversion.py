from typing import Union, Literal

""""""
# Functions:

    # celsius_to_fahrenheit()
        # Purpose: to convert Celsius temperatures to Fahrenheit

    # fahrenheit_to_celsius()
        # Purpose: to convert Fahrenheit temperatures to Celsius

    # Both functions:
        # Accept: str, int, float, list, tuple
        # Return: float, list, str (error)

""""""

# Colors for terminal output
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# Validation
def type_check_temperature(temperature, temp_unit):
    failed = False

    if not isinstance(temperature, (list, tuple)):
        # string
        if isinstance(temperature, str):
            if "," in temperature:
                try:
                    temps = [float(temp) for temp in temperature.split(",")]
                except ValueError:
                    failed = True
            else:
                try:
                    temps = float(temperature)
                except ValueError:
                    failed = True
        # int, float
        else:
            try:
                temps = float(temperature)
            except (TypeError, ValueError):
                failed = True
    # list, tuple
    elif isinstance(temperature, (list, tuple)):
        try:
            temps = [float(temp)for temp in temperature]
        except (TypeError, ValueError):
            failed = True

    if failed:
        return f"{RED}Please provide a numeric {temp_unit} temperature or a list of numeric {temp_unit} temperatures{RESET}"
    return temps

# C to F
def celsius_to_fahrenheit(temperature: Union[str, int, float, list, tuple]) -> Union[float, list, Literal["error"]]:
    temps = type_check_temperature(temperature, "Celsius")
    # error
    if isinstance(temps, str):
        return temps
    # list
    elif isinstance(temps, (list)):
        return [round(((float(temp) * 9/5) + 32), 4) for temp in temps]
    # float
    return round(((temps * 9/5) + 32), 4)

# F to C
def fahrenheit_to_celsius(temperature: Union[str, int, float, list, tuple]) -> Union[float, list, Literal["error"]]:
    temps = type_check_temperature(temperature, "Fahrenheit")
    # error
    if isinstance(temps, str):
        return temps
    # list
    elif isinstance(temps, (list)):
        return [round(((float(temp) - 32) * 5/9), 4) for temp in temps]
    # float
    return round(((temps - 32) * 5/9), 4)


#######################
    # The Program:
#######################

if __name__ == "__main__":
    while True:
        print(f"\n{YELLOW}Choose an option:{RESET}")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")

        selection = input("")

    # Validate input
        if selection not in ["1", "2", "3"]:
            print(f"\n{RED}Please choose a valid option.{RESET}")
            continue

        temp_unit = "Celsius"  if selection == "1" else "Fahrenheit"
        converted_unit = "Fahrenheit" if selection == "1" else  "Celsius"

    # C to F
        if selection == "1":
            value = input(f"{YELLOW}Provide a Celsius temperature or a list of Celsius temperatures\n (lists should be comma separated)\n{RESET}")
            result = celsius_to_fahrenheit(value)

    # F to C
        elif selection == "2":
            value = input(f"{YELLOW}Provide a Fahrenheit temperature or a list of Fahrenheit temperatures\n (lists should be comma separated)\n{RESET}")
            result = fahrenheit_to_celsius(value)

    # Quit
        elif selection == "3":
            print(f"{YELLOW}Goodbye{RESET}")
            break

    # Return results
        if isinstance(result, (list, float)):
            print(f"\n{CYAN}{temp_unit}:{RESET}\n{value}\n{CYAN}{converted_unit}:{RESET}")

        print(result)


#######################
    # Example Usage:
#######################

# # string
#     print(celsius_to_fahrenheit("0"))
#         # Output: 32.0

# # string list
#     print(celsius_to_fahrenheit("0,1,2"))
#         # Output: [32.0, 33.8, 35.6]

# # int
#     print(fahrenheit_to_celsius(-1))
#         # Output: -18.3333

# # float
#     print(celsius_to_fahrenheit(1.2))
#         # Output: 34.16

# # list
#     print(celsius_to_fahrenheit([80, 32, 10]))
#         # Output: [176.0, 89.6, 50.0]

# # tuple
#     print(fahrenheit_to_celsius((80, 32, 10)))
#         # Output: [26.6667, 0.0, -12.2222]

# # error
#     print(celsius_to_fahrenheit("0s,1,2"))
#         # Output: Please provide a numeric Celsius temperature or a list of numeric Celsius temperatures