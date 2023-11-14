Proyecto hecho por Nicolas Vargas Flores (1001368855)

Informática II
Bioingeniería
Universidad de Antioquia

Enlace de repositorio de GitHub: https://github.com/NicolasUdea/Info2_Taller4.git

** Documentación **

El proyecto propuesto sigue el patrón de diseño Modelo-Vista-Controlador (MVC) de
la siguiente manera:

1. Modelo (model): las clases User y DICOMimage actúan como el Modelo. La Clase User
representa los datos y la lógica de negocio relacionados con los usuarios de
la aplicación. La clase DICOMimage representa los datos y la lógica de negocio
relacionados con las imágenes DICOM que se van a visualizar.

2. Vista (view): la clase ImageDisplay actúa como la Vista. Esta clase se encarga de
la presentación de los datos al usuario. En este caso, la clase ImageDisplay se encarga
de mostrar la imágenes DICOM al usuario.

3. Controlador (controller): la clase Application actúa como el Controlador. Esta clase
se encarga de manejar la interaccion del usuario con la Vista y de actualizar el Modelo
según sea necesario. Por ejemplo, cuando el usuario selecciona una carpeta de imágenes
a tráves de la Vista, el Controlador se encarga de cargas estas imágenes en el Modelo.

Extra: la clase SliderController puede considerarse como un controlador adicional que
se encarga de la interacción del usuario con el control deslizante de la Vista.

Por lo tanto, el proyecto se considera de tipo MVC porque separa claramente las
responsabilidades de manejo de datos (Model), presentación de datos (View) e interacción
del usuario (Controller).