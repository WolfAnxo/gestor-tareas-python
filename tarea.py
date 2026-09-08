class Tarea:

    def __init__(self, titulo, descripcion, prioridad, id = None, completada = False):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.id = id
        self.completada = completada