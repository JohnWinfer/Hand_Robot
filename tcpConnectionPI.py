import socket

HOST = "10.165.1.253"
PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket Created")

try:
    s.bind((HOST, PORT))
except socket.error:
    print ("Bind failed")

s.listen(1)
print ("Socket awaiting messages")
(conn, addr) = s.accept()
print ("Connected")

while True:
    data = conn.recv(1024)
    a = data.decode("utf-8")
    print(a)
    if a == "quit":
        break

conn.close()
