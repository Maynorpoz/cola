class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  
        self.rear = None   
        self.size = 0      

    def is_empty(self):
        return self.size == 0

    def enqueue(self, element):
        """Agrega un elemento al final de la cola"""
        new_node = Node(element)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        """Elimina y devuelve el primer elemento de la cola"""
        if self.is_empty():
            raise IndexError("No hay elementos en la cola")
        removed_value = self.front.value
        self.front = self.front.next
        self.size -= 1
        if self.front is None:
            self.rear = None
        return removed_value

    def front_value(self):
        """Devuelve el primer elemento sin eliminarlo"""
        if self.is_empty():
            return None
        return self.front.value

    def get_size(self):
        """Retorna el tamaño de la cola"""
        return self.size

    def __str__(self):
        """Muestra la cola en formato de lista"""
        elements = []
        current = self.front
        while current:
            elements.append(str(current.value))
            current = current.next
        return " <- ".join(elements) if elements else "Cola vacía"

class TaskAndCustomerManager:
    def __init__(self):
        # Colas para la gestión de tareas
        self.high_priority_tasks = Queue()  
        self.normal_tasks = Queue()  

        # Colas para la atención al cliente
        self.vip_customers = Queue()  
        self.regular_customers = Queue()  

    def add_task(self, task, priority="normal"):
        """Agrega una tarea con prioridad"""
        if priority.lower() == "alta":
            self.high_priority_tasks.enqueue(task)
        else:
            self.normal_tasks.enqueue(task)

    def add_customer(self, name, type_="regular"):
        """Agrega un cliente a la cola VIP o Regular"""
        if type_.lower() == "vip":
            self.vip_customers.enqueue(name)
        else:
            self.regular_customers.enqueue(name)

    def process_task(self):
        """Procesa la siguiente tarea (prioridad alta primero)"""
        if not self.high_priority_tasks.is_empty():
            return f"Procesando tarea PRIORITARIA: {self.high_priority_tasks.dequeue()}"
        elif not self.normal_tasks.is_empty():
            return f"Procesando tarea NORMAL: {self.normal_tasks.dequeue()}"
        else:
            return "No hay tareas pendientes"

    def serve_customer(self):
        """Atiende al próximo cliente (VIP tiene prioridad)"""
        if not self.vip_customers.is_empty():
            return f"Atendiendo cliente VIP: {self.vip_customers.dequeue()}"
        elif not self.regular_customers.is_empty():
            return f"Atendiendo cliente Regular: {self.regular_customers.dequeue()}"
        else:
            return "No hay clientes en la cola"

    def show_status(self):
        """Muestra el estado actual de tareas y clientes"""
        return (f"Tareas:\nPrioritarias: {self.high_priority_tasks}\nNormales: {self.normal_tasks}\n\n"
                f"Clientes:\nVIP: {self.vip_customers}\nRegulares: {self.regular_customers}")

manager = TaskAndCustomerManager()

# Agregar tareas
manager.add_task("Revisar servidor", "alta")
manager.add_task("Actualizar software", "normal")
manager.add_task("Respaldo de datos", "alta")
manager.add_task("Generar reportes", "normal")

# Agregar clientes
manager.add_customer("Juan", "regular")
manager.add_customer("Ana", "vip")
manager.add_customer("Carlos", "regular")
manager.add_customer("María", "vip")

# Mostrar estado inicial
print(manager.show_status())

# Procesar tareas y atender clientes
print(manager.process_task())  # Tarea PRIORITARIA
print(manager.serve_customer())  # Cliente VIP
print(manager.process_task())  # Tarea PRIORITARIA
print(manager.serve_customer())  # Cliente VIP
print(manager.process_task())  # Tarea NORMAL
print(manager.serve_customer())  # Cliente Regular

# Mostrar estado final
print(manager.show_status())
