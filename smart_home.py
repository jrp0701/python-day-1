'''
Task: convert c to f
Name: c_to_f
Input: degrees_c
Side Effects: none
Return: degrees_f
'''
def c_to_f(degrees_c):
    degrees_f = (degrees_c * 9/5) + 32
    return degrees_f

'''
Task: Tell user current temperature
Name: print_temp
Input: temp_in_f
Side Effects: "The temperature is: x"
Return: no
'''
def print_temp(temp_in_f):
    print("The temperature is: ", temp_in_f)
    return None
