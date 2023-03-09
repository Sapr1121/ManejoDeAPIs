from UI import atencion

def principal():
    while(input() == 's'):
        atencion()
        print("¿Quiere volver a hacer otra consulta?(s/n): ")

if __name__ == '__main__':
    principal()