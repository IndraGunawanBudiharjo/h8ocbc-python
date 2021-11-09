''' 1. function untuk convert kelvin ke celsius dan sebaliknya. 
    data type -> 
        parameter: 
            temperature: float
            unit: string
        return: float
'''
def convert_kelvin_celsius(temperature, unit):           
    ''' rumus convert celsius -> kelvin
        return -> float '''    
    if unit.lower() == 'c':
        return temperature + 273.15
        
    ''' rumus convert kelvin -> celsius
        return -> float '''
    if unit.lower() == 'k':
        return temperature - 273.15         

    ''' return apabila nilai unit bukan k atau c '''            
    return temperature                                 


''' 2. function untuk convert kelvin / celsius -> fahrenheit. 
    data type -> 
        parameter: 
            temperature: float
            unit: string
        return: float 
'''
def convert_to_fahrenheit(temperature, unit):           
    temp = temperature

    ''' return apabila nilai unit bukan k atau c '''    
    if unit.lower() != 'k' and unit.lower() != 'c':     
        return temp

    ''' apabila parameter unit bernilai kelvin (K/k), 
    maka suhu diconvert dulu ke celcius (C/c) '''
    if unit.lower() == 'k':                             
        temp = convert_kelvin_celsius(temperature, unit)

    ''' return convert celsius -> fahrenheit '''
    return (temp * 9 / 5) + 32                          


''' 3. function untuk convert fahrenheit -> kelvin / celsius. 
    data type -> 
        parameter: 
            temperature: float
            unit: string
        return: float 
'''
def convert_from_fahrenheit(temperature, unit):
    ''' convert fahrenheit -> celcius '''
    if unit.lower() == 'c':
        return ((temperature - 32) * 5 / 9)
    ''' convert fahrenheit -> kelvin '''
    if unit.lower() == 'k':
        return ((temperature - 32) * 5 / 9 + 273.15)
    ''' return temperature awal, apabila nilai unit bukan c atau k '''
    return temperature



# tes
result1 = convert_kelvin_celsius(100, 'C')
result2 = convert_to_fahrenheit(373.15, 'K')
result3 = convert_to_fahrenheit(100, 'C')
result4 = convert_from_fahrenheit(64, 'C')

print(result1)
print(result2)
print(result3)
print(result4)

