import base64

encoded_string = "AQAAANCMnd8BFdERjHoAwE/Cl+sBAAAAaC07lawbikSzTQgQS/ZO4gAAAAAKAAAAQgBlAGEAcgAAABBmAAAAAQAAIAAAAG0OHKFWSbhOHLjfhTIu/kQMfwpU9rnvya4KFGQLPPq1AAAAAA6AAAAAAgAAIAAAAC95lqIyzMHjsE+PxnzapE8nCwX+sirYBG3KxRDybF7zMAAAAKM1jYP5RJLA6uO+FJgqzbBqzYbzegWALNF3htpP41oOzqNiGo+0Gjo25TS6S6E8tEAAAADnyIcWtcpSRUwSKlMFJjb5DhruVh6xo2pkLZrGvp3z5PA0j0DnWsHvqOntrIndfy0gXUmdPT7W/hZ+vQ76i+z4"

decoded_bytes = base64.b64decode(encoded_string)

try:
    decoded_string = decoded_bytes.decode('utf-8')
except UnicodeDecodeError:
    decoded_string = decoded_bytes.decode('utf-8', errors='ignore')

print(decoded_string)