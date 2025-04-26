from collections import deque

class Persona:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    def __str__(self):
        return f"Nombre: {self.nombre}, Identificacion: {self.identificacion}"
    
class ColaVacunacion:
    def __init__(self,):
        self.cola = deque()
    
    def registrar_persona(self, persona):
        self.cola.append(persona)
        print(f"Persona registrada: {persona}")

    def atender_siguiente(self):
        if not self.cola:
            print("No hay personas en la cola.")
            return None
        
        atendiendo = self.cola.popleft()
        print(f"Atendido a {atendiendo.nombre} Con identificacion {atendiendo.identificacion}")
        return atendiendo
    
    def mostrar_cola(self):
        n = len(self.cola)
        print(f"Personas en la cola: {n}")

        if n == 0:
            print("No hay personas en la cola.")
            return
        
    def mostrar_siguiente(self):
        if not self.cola:
            print("No hay personas en la cola.")
            return None
        
        siguiente = self.cola[0]
        print(f"Siguiente en la cola: {siguiente.nombre} con identificacion {siguiente.identificacion}")
        return siguiente
def menu():
    cola_vacunacion = ColaVacunacion()
    while True:
        print("\n****Centro de Vacunacion****")
        print("1) Registrar persona")
        print("2) Atender siguiente")
        print("3) Mostrar cola")
        print("4) Mostrar siguiente")
        print("5) Salir")

        opcion = input("Seleccione una opcion (1-5): ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la persona: ")
            while True:
                try:
                    identificacion = int(input("Ingrese la identificacion de la persona: "))
                    break
                except ValueError:
                    print("Ingrese un numero para la identificacion.")
            persona = Persona(nombre, identificacion)
            cola_vacunacion.registrar_persona(persona)
        
        elif opcion == "2":
            cola_vacunacion.atender_siguiente()
        
        elif opcion == "3":
            cola_vacunacion.mostrar_cola()

        elif opcion == "4":
            cola_vacunacion.mostrar_siguiente()

        elif opcion == "5":
            print("Saliendo del programa.")
            break

        else:
            print("Opcion no valida. Intente de nuevo.")
            

menu()

