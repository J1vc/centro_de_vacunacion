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
        
