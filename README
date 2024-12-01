# 🖥️ Seguimiento de Aplicaciones Activas

Este proyecto permite realizar un seguimiento del tiempo que un usuario pasa en diferentes aplicaciones activas en su sistema. Utiliza una interfaz gráfica en **Tkinter** y obtiene la ventana activa mediante la biblioteca **pywin32**. El tiempo registrado se muestra en tiempo real en la interfaz, y los resultados pueden ser exportados a un archivo CSV para su análisis.

---

## 🌟 Características

- **Seguimiento en tiempo real**: Monitorea las aplicaciones activas y calcula el tiempo que el usuario pasa en cada una.
- **Interfaz gráfica sencilla**: Interfaz creada con **Tkinter**, accesible y fácil de usar.
- **Exportación a CSV**: Los datos del seguimiento pueden ser exportados a un archivo CSV para su posterior análisis.
- **Multihilo**: Utiliza **hilos** para realizar el seguimiento sin bloquear la interfaz gráfica.

---

## 📋 Requisitos

### 🔹 Python 3.x

Este proyecto es compatible con Python 3. Asegúrate de tenerlo instalado en tu sistema.

### 🔹 Bibliotecas requeridas

- `tkinter` (viene preinstalado con Python, no es necesario instalarlo por separado).
- `pywin32` para interactuar con las ventanas activas en Windows.
- `time`, `csv`, `threading` (bibliotecas estándar de Python).

Instala las bibliotecas necesarias ejecutando:

```bash
pip install pywin32
---

## ⚙️ Funcionalidades

- **Iniciar seguimiento**: Inicia el monitoreo de las aplicaciones activas, registrando el tiempo que pasas en cada una.
- **Detener seguimiento**: Detiene el monitoreo y desactiva el botón de "Detener seguimiento".
- **Ver resultados en tiempo real**: Muestra en la interfaz el tiempo transcurrido en cada aplicación activa mientras se realiza el seguimiento.
- **Exportar a CSV**: Los datos del seguimiento se exportan a un archivo CSV con la siguiente estructura:

| Aplicación            | Tiempo (segundos) |
|-----------------------|-------------------|
| Nombre de la aplicación | Tiempo transcurrido |

---

## 📝 Instrucciones de Uso

### 1️⃣ Ejecutar el Script

Para ejecutar el proyecto, corre el script `seguimiento_aplicaciones.py`:

```bash
python seguimiento_aplicaciones.py

Esto abrirá la interfaz gráfica donde podrás:

Iniciar el seguimiento: Haz clic en el botón "Iniciar seguimiento".
Detener el seguimiento: Haz clic en "Detener seguimiento" para finalizar el registro.
Exportar los resultados: Haz clic en "Exportar a CSV" para guardar los datos recopilados.
2️⃣ Cerrar la Aplicación
Cuando desees salir, puedes hacerlo de forma segura haciendo clic en el botón de cerrar en la esquina superior derecha de la ventana. Se te pedirá confirmación para asegurarte de que deseas cerrar la aplicación sin perder los datos.

markdown
Copiar código

---

## 📚 Explicación del Código

1. **`get_active_window()`**  
   Obtiene el nombre de la ventana activa utilizando la función `GetForegroundWindow()` de pywin32. Esto permite monitorear las aplicaciones que están siendo utilizadas en el sistema en tiempo real.

2. **`track_app_usage()`**  
   Se encarga de realizar el seguimiento del tiempo transcurrido en cada aplicación activa. Cada iteración calcula el tiempo que ha pasado desde el último registro y actualiza la interfaz.

3. **`iniciar_seguimiento()`**  
   Inicia el seguimiento en un hilo separado, permitiendo que la interfaz gráfica siga siendo interactiva mientras se realiza el monitoreo.

4. **`detener_seguimiento()`**  
   Detiene el seguimiento de las aplicaciones y restablece los botones de la interfaz para permitir reiniciar el seguimiento.

5. **`exportar_datos()`**  
   Exporta los resultados a un archivo CSV que incluye el nombre de la aplicación y el tiempo total que el usuario ha pasado en ella.

---

## 🖼️ Capturas de Pantalla

- **Interfaz Principal**: Muestra el seguimiento en tiempo real y los botones para iniciar/detener el monitoreo.
- **Ventana de Exportación**: Diálogo de guardado de archivo CSV.

---

## 🤝 Contribuciones

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una rama nueva para tus cambios.
3. Realiza tus cambios y agrega pruebas si es necesario.
4. Realiza un pull request explicando qué cambios realizaste.

---
