import time

def contar(cantidad):
    for i in range (1,cantidad+1):
        print(f"Segundo {i}")
        time.sleep(1)

print("Contador terminado")