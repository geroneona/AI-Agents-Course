import subprocess

def get_weather(city : str):
    if city == "California":
        return "sunny"
    if city == "Arizona":
        return "snowy"
    if city == "Paris":
        return "rainy"
    if city == "London":
        return "cloudy"
    if city == "New York":
        return "sunny"
    if city == "Toronto":
        return "rainy"
    
# function to return employee's boss name
def get_ibm_aep_boss_name(employee_name: str):
    if employee_name == "Gerone Ona" or employee_name == "Gerone" or employee_name == "Me":
        return "Chad Flores"
    if employee_name == "Don De Gala" or employee_name == "Don":
        return "Gene Evasco"
    if employee_name == "Hurry Calingacion" or employee_name == "Hurry":
        return "Chad Flores"
    if employee_name == "Ely Limbo" or employee_name == "Ely":
        return "Alwil Geresola"
    if employee_name == "Wilson Serquina" or employee_name == "Wilson":
        return "Hurry Calingacion"
    if employee_name == "Aldrin Gutierrez" or employee_name == "Aldrin":
        return "Chad Flores"
    if employee_name == "Chad Flores" or employee_name == "Chad":
        return "Dinday Cabangon"
    
# function to engage ICA
def engage_ica():
    subprocess.run(["python", "ICA_Engager_2FAuth.py"])
    return "ICA Engaged"

# function to log ILC weekly time in based from previous week
def log_ilc_weekly_time():
    result = subprocess.run(["python", "ILC_Weekly_Time_In.py"])
    if result.returncode == 0:
        return "ILC Weekly Time In Successfully Logged"
    else:
        return "ILC Weekly Time In Failed to Log"