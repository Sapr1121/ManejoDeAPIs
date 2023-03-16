from UI import atencion

def principal():
    while(True):
        atencion()
        print("¿Quiere volver a hacer otra consulta?(s/n): ")
        if(input() != 's'):
            break

if __name__ == '__main__':
    principal()