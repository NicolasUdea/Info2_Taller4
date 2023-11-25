# Visualizador de Imágenes DICOM

Este proyecto es una aplicación de visualización de imágenes DICOM construida con PyQt5 y pydicom. Utiliza el patrón de diseño Modelo-Vista-Controlador (MVC) para organizar el código.

## Características

- Inicio de sesión de usuario
- Carga de imágenes DICOM desde una carpeta
- Visualización de imágenes DICOM en la interfaz de usuario
- Desplazamiento a través de las imágenes DICOM utilizando un deslizador
- Visualización de metadatos DICOM en la interfaz de usuario

## Estructura del Código

El código se divide en tres módulos principales: Modelo, Vista y Controlador.

### Modelo

El módulo del Modelo contiene la clase `User`, que maneja la carga de imágenes DICOM y la extracción de metadatos.

### Vista

El módulo de la Vista contiene las clases `LoginWindow`, `MainWindow` y `MyGraphCanvas`. `LoginWindow` es la ventana de inicio de sesión, `MainWindow` es la ventana principal de la aplicación donde se cargan y visualizan las imágenes DICOM, y `MyGraphCanvas` es una subclase de `FigureCanvas` que se utiliza para mostrar las imágenes DICOM.

### Controlador

El módulo del Controlador contiene la clase `Controller`, que maneja la comunicación entre el Modelo y la Vista.

## Uso

Para ejecutar la aplicación, simplemente ejecuta el script `Controller.py`.

## Dependencias

- PyQt5
- pydicom

## Autor

Nicolas Vargas Flores (1001368855)

## Universidad de Antioquia

Programa bioingeniería, informática II
