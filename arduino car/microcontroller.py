import pyfirmata as py

#check from device manager
port= 'COM3'
out=""

board=py.ArduinoMega(port)


SpeedR = board.get_pin('d:8:o')
Rpin1 = board.get_pin('d:7:o')# pintype,pinnum, pinmode//purple 
Rpin2 = board.get_pin('d:6:o')
Lpin3 = board.get_pin('d:4:o')
Lpin4 = board.get_pin('d:5:o')
SpeedL = board.get_pin('d:9:o')


def RCCAR(total):
    if total==0:
        #SpeedR.write(0)
        #SpeedL.write(0)
        Rpin1.write(0)
        Rpin2.write(0)
        Lpin3.write(0)
        Lpin4.write(0)
        print("BREAk in mic")
        return "Brake"
        
        

    if total==2:
        #SpeedR.write(0)
        #SpeedL.write(1)
        Rpin1.write(0)
        Rpin2.write(0)
        Lpin3.write(1)
        Lpin4.write(0)
        print("RIGHT in mic")
        return "Right"

    if total==3:
        #SpeedR.write(1)
        #SpeedL.write(0)
        Rpin1.write(1)
        Rpin2.write(0)
        Lpin3.write(0)
        Lpin4.write(0)
        print("LEFT in mic")
        return "Left"

    if total==5:
        #SpeedR.write(1)
        #SpeedL.write(1)
        Rpin1.write(1)
        Rpin2.write(0)
        Lpin3.write(1)
        Lpin4.write(0)
        print("FORWARD in mic")
        return "Up"
        
    if total==4:
        #SpeedR.write(1)
        #SpeedL.write(1)
        Rpin1.write(0)
        Rpin2.write(1)
        Lpin3.write(0)
        Lpin4.write(1)
        print("BACKWARD in mic")
        return "Down"