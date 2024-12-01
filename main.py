import time  # Importamos el módulo time para gestionar el tiempo
import csv  # Importamos el módulo csv para exportar los datos a un archivo CSV
import tkinter as tk  # Importamos tkinter para crear la interfaz gráfica
from tkinter import messagebox, filedialog  # Importamos widgets adicionales de tkinter (alertas y diálogos de archivos)
from win32gui import GetForegroundWindow, GetWindowText  # Importamos funciones de pywin32 para interactuar con las ventanas de Windows
import threading  # Importamos threading para usar hilos y no bloquear la interfaz

# Variables globales que almacenarán los datos
app_times = {}  # Diccionario que almacenará el tiempo total por aplicación
tracking = False  # Variable que indica si el seguimiento está en curso
last_app = None  # Variable para guardar la última aplicación activa
last_time = None  # Variable para guardar el último tiempo registrado

# Función que obtiene el nombre de la ventana activa
def get_active_window():
    hwnd = GetForegroundWindow()  # Obtiene el identificador de la ventana activa
    return GetWindowText(hwnd)  # Retorna el nombre de la ventana activa

# Función para hacer el seguimiento de las aplicaciones activas
def track_app_usage(area_resultados):
    global tracking, last_app, last_time, app_times  # Accedemos a las variables globales

    # Mientras el seguimiento esté activo (tracking == True)
    while tracking:
        current_app = get_active_window()  # Obtenemos el nombre de la ventana activa
        current_time = time.time()  # Obtenemos el tiempo actual en segundos desde el "epoch"

        if last_app is not None:  # Si ya tenemos una aplicación registrada
            elapsed_time = current_time - last_time  # Calculamos el tiempo transcurrido desde la última vez
            if last_app in app_times:  # Si la aplicación ya está en el diccionario, sumamos el tiempo
                app_times[last_app] += elapsed_time
            else:  # Si no, la agregamos con el tiempo transcurrido
                app_times[last_app] = elapsed_time

        last_app = current_app  # Actualizamos la aplicación actual
        last_time = current_time  # Actualizamos el tiempo de la última ejecución

        # Actualizamos la interfaz con el tiempo transcurrido por cada aplicación
        area_resultados.config(state=tk.NORMAL)  # Habilitamos el área de texto para editarla
        area_resultados.delete("1.0", tk.END)  # Limpiamos el área de texto
        for app, time_spent in app_times.items():  # Iteramos sobre las aplicaciones y su tiempo
            area_resultados.insert(tk.END, f"{app}: {time_spent:.2f} segundos\n")  # Mostramos los resultados
        area_resultados.config(state=tk.DISABLED)  # Deshabilitamos la edición del área de texto

        time.sleep(1)  # Esperamos 1 segundo antes de volver a comprobar la ventana activa

# Función que se ejecuta al hacer clic en "Iniciar seguimiento"
def iniciar_seguimiento(area_resultados, btn_iniciar, btn_detener):
    global tracking, last_time  # Accedemos a las variables globales
    if not tracking:  # Si el seguimiento no está en curso
        tracking = True  # Activamos el seguimiento
        last_time = time.time()  # Guardamos el tiempo inicial
        btn_iniciar.config(state=tk.DISABLED)  # Deshabilitamos el botón de "Iniciar" para evitar múltiples clics
        btn_detener.config(state=tk.NORMAL)  # Habilitamos el botón de "Detener"
        messagebox.showinfo("Inicio", "El seguimiento ha comenzado.")  # Mostramos un mensaje informativo

        # Creamos un hilo para ejecutar el seguimiento sin bloquear la interfaz gráfica
        threading.Thread(target=track_app_usage, args=(area_resultados,), daemon=True).start()

# Función que se ejecuta al hacer clic en "Detener seguimiento"
def detener_seguimiento(btn_iniciar, btn_detener):
    global tracking  # Accedemos a la variable global
    if tracking:  # Si el seguimiento está en curso
        tracking = False  # Detenemos el seguimiento
        btn_iniciar.config(state=tk.NORMAL)  # Habilitamos el botón de "Iniciar"
        btn_detener.config(state=tk.DISABLED)  # Deshabilitamos el botón de "Detener"
        messagebox.showinfo("Detener", "El seguimiento ha terminado.")  # Mostramos un mensaje informativo

# Función para exportar los datos a un archivo CSV
def exportar_datos():
    if not app_times:  # Si no se ha registrado ningún tiempo
        messagebox.showwarning("Exportar", "No hay datos para exportar.")  # Mostramos una advertencia
        return  # Salimos de la función

    # Pedimos al usuario que elija el nombre y ubicación del archivo
    archivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Archivo CSV", "*.csv")])
    if archivo:  # Si el usuario seleccionó un archivo
        try:
            # Abrimos el archivo en modo escritura con codificación UTF-8
            with open(archivo, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)  # Creamos un objeto escritor de CSV
                writer.writerow(["Aplicación", "Tiempo (segundos)"])  # Escribimos el encabezado
                # Escribimos los datos de las aplicaciones y el tiempo
                for app, time_spent in app_times.items():
                    # Sanitizamos los nombres de las aplicaciones (eliminamos posibles caracteres especiales problemáticos)
                    sanitized_app_name = app.replace("\n", " ").replace("\r", " ").strip()
                    writer.writerow([sanitized_app_name, round(time_spent, 2)])  # Escribimos la fila de datos
            messagebox.showinfo("Exportar", f"Datos exportados exitosamente a {archivo}.")  # Mostramos un mensaje informativo
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al exportar los datos: {e}")  # Mostramos un mensaje de error en caso de fallo

# Función para configurar la interfaz gráfica
def iniciar_interfaz():
    ventana = tk.Tk()  # Creamos la ventana principal de la interfaz
    ventana.title("Seguimiento de aplicaciones")  # Establecemos el título de la ventana
    ventana.geometry("600x400")  # Establecemos el tamaño de la ventana

    # Etiqueta principal
    etiqueta = tk.Label(ventana, text="Seguimiento de aplicaciones", font=("Arial", 16))
    etiqueta.pack(pady=10)  # Empacamos la etiqueta en la ventana con un poco de espacio alrededor

    # Área para mostrar resultados (no editable por el usuario)
    area_resultados = tk.Text(ventana, height=15, width=70, state=tk.DISABLED)
    area_resultados.pack(pady=10)  # Empacamos el área de texto en la ventana

    # Botón para iniciar el seguimiento
    btn_iniciar = tk.Button(ventana, text="Iniciar seguimiento", font=("Arial", 12),
                            command=lambda: iniciar_seguimiento(area_resultados, btn_iniciar, btn_detener))
    btn_iniciar.pack(side=tk.LEFT, padx=10, pady=10)  # Empacamos el botón a la izquierda

    # Botón para detener el seguimiento
    btn_detener = tk.Button(ventana, text="Detener seguimiento", font=("Arial", 12),
                            command=lambda: detener_seguimiento(btn_iniciar, btn_detener))
    btn_detener.pack(side=tk.LEFT, padx=10, pady=10)  # Empacamos el botón a la izquierda
    btn_detener.config(state=tk.DISABLED)  # Inicialmente, deshabilitamos el botón de "Detener"

    # Botón para exportar los datos a un archivo CSV
    btn_exportar = tk.Button(ventana, text="Exportar a CSV", font=("Arial", 12), command=exportar_datos)
    btn_exportar.pack(side=tk.LEFT, padx=10, pady=10)  # Empacamos el botón a la izquierda

    # Configuramos el cierre de la ventana
    ventana.protocol("WM_DELETE_WINDOW", lambda: cerrar_aplicacion(ventana))
    ventana.mainloop()  # Iniciamos el bucle principal de la interfaz gráfica

# Función para cerrar la aplicación de manera segura
def cerrar_aplicacion(ventana):
    global tracking
    if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?"):  # Preguntamos si el usuario está seguro
        tracking = False  # Detenemos el seguimiento si se cierra la ventana
        ventana.destroy()  # Cerramos la ventana

# Ejecución de la interfaz gráfica
if __name__ == "__main__":
    iniciar_interfaz()  # Llamamos a la función para iniciar la interfaz
