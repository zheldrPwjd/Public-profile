py_serial = serial.Serial(
    port='COM3',
    baudrate=9600,
)

while True:
    if py_serial.readable():
        response = py_serial.readline()
        print(response[:len(response)-1].decode())
        if response[:len(response)-1].decode() == '1':
            print("대피해야하는 상황")
       else
           print("초기 진화를 해야하는 상황")