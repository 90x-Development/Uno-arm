import serial

port = "COM6"
connection = serial.Serial(port, 9600)
print(f"Serial {port} is working well")

def base_turn(ang):
    rounded_ang = round(ang)
    data = f"b{rounded_ang+10}"
     connection.write(data.encode())

