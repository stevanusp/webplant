import serial 

def Get_data(ser):
    
    temperature = ser.read(5).decode('utf-8')
    humidity = ser.read(5).decode('utf-8')
    soilMoisture = ser.read(5).decode('utf-8')
    
    return temperature,humidity,soilMoisture