from menu import mostrar_menu
import tareas
while True:
    mostrar_menu()
    opcion = int(input("Que opción eliges? "))

    if opcion == 1:
       tareas.mostrar_tareas()
    elif opcion == 2:
        tareas.buscar_tarea()
    elif opcion == 3:
        tareas.crear_tarea()
    elif opcion ==4:
        tareas.modificar_tarea()
    elif opcion == 5:
        tareas.completar_tarea()
    elif opcion == 6:
        tareas.eliminar_tarea()
    elif opcion == 7:
        tareas.tareas_pendientes()
    elif opcion == 8:
        tareas.mostrar_estadisticas()
    elif opcion == 9:
       break
    else:
     print("Opcion Incorrecta")