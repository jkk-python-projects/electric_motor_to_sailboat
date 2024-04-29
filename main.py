
def calculate_battery_capacity():

    # Prompting for user input

    required_operation_time_hours = float(input("Enter the required operation time in hours: "))
    average_power_consumption_a = float(input("Enter the average power consumption in Amps: "))
    safe_discharge_percentage = float(input("Enter the safe discharge limit as a percentage of total capacity: "))

    # Calculating the required capacity in Amp-hours
    required_capacity_ah = average_power_consumption_a * required_operation_time_hours

    # Adjusting for safe discharge limit (convert percentage to decimal)
    actual_capacity_needed_ah = required_capacity_ah / (safe_discharge_percentage / 100)

    return actual_capacity_needed_ah

''' battery_capacity = calculate_battery_capacity(required_operation_time_hours, average_power_consumption_a, safe_discharge_percentage)
'''
print("Akun kapasiteetin tarve:", calculate_battery_capacity())
