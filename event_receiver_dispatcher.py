import serial

# All handlers must accept data parameter, even if not used
def handle_a(data):
    print('A:' + data)

def handle_b(data):
    print('B:' + data)

handlers = {
    'BTN_A': handle_a,
    'BTN_B': handle_b
}

ser = serial.Serial('/dev/ttyACM0', 115200)

while True:
    if ser.in_waiting:
        try:
            line = ser.readline().decode('utf-8').strip()
            parts = line.split(':')
            event_type = parts[0]
            data = parts[1] if len(parts) > 1 else None

            handler = handlers.get(event_type)
            if handler:
                handler(data)
        except e:
            print(e)

