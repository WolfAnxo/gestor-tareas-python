from tarea import Tarea
from conexion import conectar

def mostrar_tareas():
    conexion = conectar()
    if conexion is None:
         return
    cursor = conexion.cursor() 
    cursor.execute(
        "SELECT * FROM tareas ")
    tareas = cursor.fetchall()
    for tarea in tareas:
        print(f" ID: {tarea[0]} - Título: {tarea[1]} - Descripción: {tarea[2]} - Prioridad: {tarea[3]} - Completada: {tarea[4]}")
    conexion.close()

def buscar_tarea():
    try:
        conexion= conectar()
        if conexion is None:
                 return
        cursor = conexion.cursor() 
        id_tarea = int(input("ID de la tarea a buscar: "))
    
        cursor.execute("SELECT * FROM tareas WHERE id = %s", (id_tarea,))
        tarea = cursor.fetchone()
        if tarea is not None:
            print(f" ID: {tarea[0]} - Título: {tarea[1]} - Descripción: {tarea[2]} - Prioridad: {tarea[3]} - Completada: {tarea[4]}")
        else: 
            print("No existe ninguna tarea con ese ID")
        conexion.close()
    except ValueError:
        print("Debes introducir un número válido")
        conexion.close()
        return

def crear_tarea():
    conexion = conectar()
    if conexion is None:
             return
    cursor = conexion.cursor() 
    while True:
        titulo_tarea = input(" Título de la tarea: ")
        if titulo_tarea.strip() == "":
             print("La tarea necesita un título valido")
        else:
             break

    descripcion_tarea = input(" Describe la tarea a realizar: ")
    while True:
        prioridad_tarea = input("Prioridad de la tarea (Alta, Media, Baja): ").strip().lower()
        if prioridad_tarea in ["alta", "media", "baja"]:
             break
        else:
             print("Introduce un nivel de prioridad correcto")

    nueva_tarea = Tarea(titulo_tarea, descripcion_tarea, prioridad_tarea)

    cursor.execute(
        "INSERT INTO tareas (titulo, descripcion , prioridad) VALUES (%s,%s,%s)",
        (nueva_tarea.titulo, nueva_tarea.descripcion, nueva_tarea.prioridad,)
    )
    conexion.commit()
    conexion.close()
    mostrar_tareas()
    

def modificar_tarea():
    try:
        conexion=conectar()
        if conexion is None:
                 return
        cursor = conexion.cursor() 

        mostrar_tareas()
     
         
        id_modificado = int(input("ID de la tarea que quieres modificar: "))
    
        cursor.execute("SELECT * FROM tareas WHERE id = %s ", (id_modificado,))

        tarea_modificada = cursor.fetchone()

        if tarea_modificada is not None:
            while True:
                    nuevo_titulo = input("Nuevo titulo de la tarea: ")
                    if nuevo_titulo.strip() == "":
                         print("La tarea necesita un título valido")
                    else:
                         break
            
            nueva_descripcion = input("Nueva descripción: ")
            while True:
                    nueva_prioridad = input("Prioridad de la tarea (Alta, Media, Baja): ").strip().lower()
                    if nueva_prioridad in ["alta", "media", "baja"]:
                         break
                    else:
                         print("Introduce un nivel de prioridad correcto")

            tareamod = Tarea(nuevo_titulo, nueva_descripcion, nueva_prioridad)
            cursor.execute("UPDATE tareas SET titulo = %s , descripcion = %s , prioridad = %s WHERE id = %s", (tareamod.titulo, tareamod.descripcion, tareamod.prioridad, id_modificado,))
            conexion.commit()
            conexion.close()
            mostrar_tareas()
        
        else:
            print("No hay ninguna tarea con ese ID")
            conexion.close()
    except ValueError:
            print("Debes introducir un número válido")
            conexion.close()
            return

def completar_tarea():
     try:
        conexion = conectar()
        if conexion is None:
                 return
        cursor = conexion.cursor()

        mostrar_tareas()
     
        id_tarea_completada = int(input("ID de la tarea que quieres marcar como completada: "))
     

        cursor.execute("SELECT * FROM tareas WHERE id = %s", (id_tarea_completada,))

        tarea_completada = cursor.fetchone()

        if tarea_completada is not None:
          cursor.execute("UPDATE tareas SET completada = TRUE WHERE id = %s", (id_tarea_completada,))
          conexion.commit()

        else:
            print("No hay ninguna tarea con ese ID")
        conexion.close()
     except ValueError:
            print("Debes introducir un número válido")
            conexion.close()

def eliminar_tarea():
    try:
        conexion= conectar()
        if conexion is None:
                 return
        
        cursor = conexion.cursor() 
    
        mostrar_tareas()
    
        id_eliminar = int(input("ID de la tarea que quieres eliminar: "))
    
        cursor.execute("SELECT * FROM tareas WHERE id = %s ", (id_eliminar,))
    
        tarea_eliminada = cursor.fetchone()
    
        if tarea_eliminada is not None:
            cursor.execute("DELETE FROM tareas WHERE id = %s", (id_eliminar,))
            conexion.commit()
            print("Tarea eliminada correctamente")
            conexion.close()
            mostrar_tareas()
            
        else:
            print("No hay ninguna tarea con ese ID")
            conexion.close()
    except ValueError:
        print("Debes introducir un número válido")
        conexion.close()

def tareas_pendientes():
     conexion = conectar()
     if conexion is None:
              return

     cursor = conexion.cursor()

     cursor.execute("SELECT * FROM tareas WHERE completada = FALSE")

     tareas_pedientes = cursor.fetchall()
     if tareas_pedientes :
            for tarea_pediente in tareas_pedientes:
                print(f" ID: {tarea_pediente[0]} - Título: {tarea_pediente[1]} - Descripción: {tarea_pediente[2]} - Prioridad: {tarea_pediente[3]} - Completada: {tarea_pediente[4]}")
     else: 
                print("No hay tareas pendientes")
     conexion.close()

def mostrar_estadisticas():
     conexion = conectar()
     if conexion is None:
              return

     cursor = conexion.cursor()

     cursor.execute("SELECT * FROM tareas")

     tareas = cursor.fetchall()

     total_tareas = len(tareas)

     estat_tareas_completadas = [tarea for tarea in tareas if tarea[4] == True ]

     total_tareas_compl =  len(estat_tareas_completadas)

     estat_tareas_pendientes = [tarea for tarea in tareas if tarea[4] == False ]

     total_tareas_pend = len(estat_tareas_pendientes)

     if total_tareas > 0:
          porcen_completadas = (total_tareas_compl /total_tareas) * 100
     else:
          porcen_completadas = 0
          
          

     print("===== ESTADÍSTICAS =====")
     print(f"Total tareas {total_tareas} ")
     print(f"Tareas completadas {total_tareas_compl}")
     print(f"Tareas pendientes {total_tareas_pend}")
     print(f"Porcentaje completado: {porcen_completadas}%")
     conexion.close()

