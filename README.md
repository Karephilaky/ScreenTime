# Seguimiento de Aplicaciones Activas

Este proyecto permite realizar un seguimiento del tiempo que un usuario pasa en diferentes aplicaciones activas en su sistema. Utiliza una interfaz gráfica en **Tkinter** y obtiene la ventana activa mediante el uso de la biblioteca **pywin32**. El tiempo registrado se muestra en tiempo real en la interfaz, y los resultados pueden ser exportados a un archivo CSV para su análisis.

---

## Características

- **Seguimiento en tiempo real**: Monitorea las aplicaciones activas y calcula el tiempo que el usuario pasa en cada una.
- **Interfaz gráfica sencilla**: La interfaz está creada con **Tkinter**, permitiendo una interacción fácil y accesible.
- **Exportación a CSV**: Los datos del seguimiento pueden ser exportados a un archivo CSV para su posterior análisis.
- **Multihilo**: Utiliza **hilos** para realizar el seguimiento sin bloquear la interfaz gráfica.

---

## Requisitos

- **Python 3.x**  
  Este proyecto es compatible con Python 3. Asegúrate de tenerlo instalado en tu sistema.

- **Bibliotecas requeridas**:
  - `tkinter` (viene preinstalado con Python, no es necesario instalarlo por separado).
  - `pywin32` para interactuar con las ventanas activas en Windows.
  - `time`, `csv`, `threading` (bibliotecas estándar de Python).

  Puedes instalar las bibliotecas necesarias ejecutando:

  ```bash
  pip install pywin32

---

# Funcionalidades
Iniciar seguimiento: Inicia el monitoreo de las aplicaciones activas, registrando el tiempo que pasas en cada una.

Detener seguimiento: Detiene el monitoreo y desactiva el botón de "Detener seguimiento".

Ver resultados en tiempo real: Muestra en la interfaz el tiempo transcurrido en cada aplicación activa mientras se realiza el seguimiento.

Exportar a CSV: Los datos del seguimiento pueden ser exportados a un archivo CSV, con la siguiente estructura:

Aplicación: Nombre de la aplicación activa.
Tiempo (segundos): Tiempo total que se ha pasado en esa aplicación en segundos.

---

# Instrucciones de Uso
1. Ejecutar el Script
Para ejecutar el proyecto, simplemente corre el script seguimiento_aplicaciones.py:

bash
Copiar código
python seguimiento_aplicaciones.py
Esto abrirá la interfaz gráfica donde podrás:

Iniciar el seguimiento: Haz clic en el botón Iniciar seguimiento.
Detener el seguimiento: Haz clic en el botón Detener seguimiento para finalizar el registro.
Exportar los resultados: Haz clic en Exportar a CSV para guardar los datos recopilados.
2. Cerrar la Aplicación
Cuando desees salir, puedes hacerlo de forma segura haciendo clic en el botón de cerrar en la esquina superior derecha de la ventana. Se te pedirá confirmación para asegurarte de que deseas cerrar la aplicación sin perder los datos.

---

# Explicación del Código
1. get_active_window()
Esta función obtiene el nombre de la ventana activa utilizando la función GetForegroundWindow() de la biblioteca pywin32. Esto permite monitorear las aplicaciones que están siendo utilizadas en el sistema en tiempo real.

2. track_app_usage()
Esta función se encarga de realizar el seguimiento del tiempo transcurrido en cada aplicación activa. En cada iteración, se calcula el tiempo que ha pasado desde el último registro y se actualizan los resultados en la interfaz.

3. iniciar_seguimiento()
Esta función inicia el seguimiento en un hilo separado, permitiendo que la interfaz gráfica siga siendo interactiva mientras se realiza el monitoreo.

4. detener_seguimiento()
Detiene el seguimiento de las aplicaciones y restablece los botones de la interfaz para permitir reiniciar el seguimiento.

5. exportar_datos()
Exporta los resultados a un archivo CSV, que incluye el nombre de la aplicación y el tiempo total que el usuario ha pasado en ella.

---

# Capturas de Pantalla
Interfaz Principal: Muestra el seguimiento en tiempo real y los botones para iniciar/detener el monitoreo.
Ventana de Exportación: Diálogo de guardado de archivo CSV.

---

# Contribuciones
Si deseas contribuir a este proyecto, puedes seguir estos pasos:

Haz un fork de este repositorio.
Crea una rama nueva para tus cambios.
Realiza tus cambios y agrega pruebas si es necesario.
Realiza un pull request explicando qué cambios realizaste.


