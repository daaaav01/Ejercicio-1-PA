from Producto import *

def main():
    
    Lista = []

    Control = True

    while Control == True:

        x = int(input("¿Desea agregar un producto? presione 1 para si, 2 para no: "))
    
        if x == 1:

            y = int(input("¿Que tipo de producto desea agregar?\n Producto fresco ---> 1\n Producto refrigerado ---> 2\n Producto congelado ---> 3\n Seleccione el numero: "))

            if y == 1:

                fecha_cadu = str(input("Digite la fecha de caducidad (DD/MM/AAAA): "))
                fecha_enva = str(input("Digite la fecha de envasado (DD/MM/AAAA): "))
                num_lote = str(input("Digite el numero de lote: "))
                pais_o = str(input("Digite el pais de origen: "))

                Producto_lista = Producto_Fresco(fecha_cadu, fecha_enva, num_lote, pais_o)

                Lista.append(Producto_lista)

        else:
            Control = False

            for i in Lista:
                
                print(i)

if __name__ == "__main__":
    main()