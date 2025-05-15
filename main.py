import time
import csv
import tkinter as tk
from tkinter import messagebox, filedialog
from win32gui import GetForegroundWindow, GetWindowText
import threading

# ========================
# Variables globales
# ========================
actividades = {}        # Diccionario con tiempos por actividad y aplicación
actividad_actual = None # Nombre de la actividad actual
tracking = False        # Indica si el seguimiento está activo
last_app = None         # Última aplicación registrada
last_time = None        # Último timestamp
app_times = {}          # Tiempos por aplicación en la actividad actual

# ========================
# Función para obtener ventana activa
# ========================
def get_active_window():
    hwnd = GetForegroundWindow()
    return GetWindowText(hwnd)

# ========================
# Formatear segundos a hh:mm:ss
# ========================
def formatear_tiempo(segundos):
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segundos = int(segundos % 60)
    tiempo = ""
    if horas > 0:
        tiempo += f"{horas}h "
    if minutos > 0 or horas > 0:
        tiempo += f"{minutos}m "
    tiempo += f"{segundos}s"
    return tiempo.strip()

# ========================
# Seguimiento de uso de aplicaciones
# ========================
def track_app_usage(area_resultados):
    global tracking, last_app, last_time, app_times

    while tracking:
        current_app = get_active_window()
        current_time = time.time()

        if last_app is not None:
            elapsed_time = current_time - last_time
            if last_app in app_times:
                app_times[last_app] += elapsed_time
            else:
                app_times[last_app] = elapsed_time

        last_app = current_app
        last_time = current_time

        # Mostrar resultados actualizados
        area_resultados.config(state=tk.NORMAL)
        area_resultados.delete("1.0", tk.END)
        for app, tiempo in app_times.items():
            area_resultados.insert(tk.END, f"{app}: {formatear_tiempo(tiempo)}\n")
        area_resultados.config(state=tk.DISABLED)

        time.sleep(1)

# ========================
# Iniciar seguimiento
# ========================
def iniciar_seguimiento(area_resultados, btn_iniciar, btn_detener, entrada_actividad):
    global tracking, last_time, actividad_actual, actividades, app_times

    nombre = entrada_actividad.get().strip()
    if not nombre:
        messagebox.showwarning("Actividad", "Debes ingresar un nombre para la actividad.")
        return

    actividad_actual = nombre
    if nombre not in actividades:
        actividades[nombre] = {}
    app_times = actividades[nombre]

    tracking = True
    last_time = time.time()
    btn_iniciar.config(state=tk.DISABLED)
    btn_detener.config(state=tk.NORMAL)
    messagebox.showinfo("Inicio", f"Seguimiento de la actividad '{nombre}' iniciado.")

    threading.Thread(target=track_app_usage, args=(area_resultados,), daemon=True).start()

# ========================
# Detener seguimiento
# ========================
def detener_seguimiento(btn_iniciar, btn_detener):
    global tracking, actividad_actual, actividades, app_times
    if tracking:
        tracking = False
        actividades[actividad_actual] = app_times
        btn_iniciar.config(state=tk.NORMAL)
        btn_detener.config(state=tk.DISABLED)
        messagebox.showinfo("Detenido", f"Seguimiento de '{actividad_actual}' finalizado.")

# ========================
# Exportar datos a CSV
# ========================
def exportar_datos():
    if not actividades:
        messagebox.showwarning("Exportar", "No hay datos para exportar.")
        return

    archivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Archivo CSV", "*.csv")])
    if archivo:
        try:
            with open(archivo, mode="w", newline="", encoding="utf-8-sig") as file:
                writer = csv.writer(file)
                
                for actividad, apps in actividades.items():
                    # Escribimos el nombre de la actividad
                    writer.writerow([f"Actividad: {actividad}"])
                    writer.writerow(["Aplicación", "Tiempo"])
                    
                    for app, tiempo in apps.items():
                        app_limpia = app.replace("\n", " ").replace("\r", " ").strip()
                        writer.writerow([app_limpia, formatear_tiempo(tiempo)])
                    
                    writer.writerow([])  # Línea vacía para separar actividades

            messagebox.showinfo("Exportar", f"Datos exportados exitosamente a {archivo}.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al exportar los datos: {e}")


# ========================
# Cerrar aplicación con confirmación
# ========================
def cerrar_aplicacion(ventana):
    global tracking
    if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?"):
        tracking = False
        ventana.destroy()

# ========================
# Configurar interfaz gráfica
# ========================
def iniciar_interfaz():
    ventana = tk.Tk()
    ventana.title("Seguimiento de aplicaciones por actividad")
    ventana.geometry("650x450")

    # Título
    etiqueta = tk.Label(ventana, text="Seguimiento de aplicaciones", font=("Arial", 16))
    etiqueta.pack(pady=10)

    # Área de texto para mostrar resultados
    area_resultados = tk.Text(ventana, height=15, width=80, state=tk.DISABLED)
    area_resultados.pack(pady=10)

    # Campo para nombre de actividad
    frame_actividad = tk.Frame(ventana)
    frame_actividad.pack(pady=5)
    tk.Label(frame_actividad, text="Nombre de la actividad:", font=("Arial", 12)).pack(side=tk.LEFT)
    entrada_actividad = tk.Entry(frame_actividad, width=30)
    entrada_actividad.pack(side=tk.LEFT, padx=5)

    # Botón Iniciar
    btn_iniciar = tk.Button(ventana, text="Iniciar seguimiento", font=("Arial", 12),
                            command=lambda: iniciar_seguimiento(area_resultados, btn_iniciar, btn_detener, entrada_actividad))
    btn_iniciar.pack(side=tk.LEFT, padx=10, pady=10)

    # Botón Detener
    btn_detener = tk.Button(ventana, text="Detener seguimiento", font=("Arial", 12),
                            command=lambda: detener_seguimiento(btn_iniciar, btn_detener))
    btn_detener.pack(side=tk.LEFT, padx=10, pady=10)
    btn_detener.config(state=tk.DISABLED)

    # Botón Exportar
    btn_exportar = tk.Button(ventana, text="Exportar a CSV", font=("Arial", 12), command=exportar_datos)
    btn_exportar.pack(side=tk.LEFT, padx=10, pady=10)

    # Evento al cerrar la ventana
    ventana.protocol("WM_DELETE_WINDOW", lambda: cerrar_aplicacion(ventana))
    ventana.mainloop()

# ========================
# Ejecutar aplicación
# ========================
if __name__ == "__main__":
    iniciar_interfaz()
