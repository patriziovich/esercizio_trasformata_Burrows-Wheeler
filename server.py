
    
import socket as sck
from bwt import trasforma

server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

IP = "127.0.0.1"
PORTA = 5000

server.bind((IP, PORTA))

server.listen()

print("Server in ascolto su", IP, "porta", PORTA)

connessione, indirizzo_client = server.accept()

dati = connessione.recv(1024)

print("Messaggio ricevuto dal client:", dati.decode())

connessione.sendall(dati)

connessione.close()

server.close()

print("Server terminato")
