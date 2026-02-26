# GrAfIcAcIoN_aPuNtEs_En_ClAsEs
# Unidad I. Introducción a la graficación por computadora.

## 1.1. Historia y evolución de la graficación por computadora

La graficación por computadora es la disciplina que se encarga de generar, representar y manipular imágenes visuales mediante el uso de computadoras. Su evolución ha sido vertiginosa, pasando de simples representaciones de líneas en monitores a complejos mundos virtuales fotorrealistas.

### Los inicios (décadas de 1950 y 1960)
Los primeros pasos de la graficación por computadora están ligados a proyectos militares y de investigación académica. El **Whirlwind I** en el MIT (Instituto Tecnológico de Massachusetts), a principios de los años 50, fue uno de los primeros computadores en utilizar un monitor de tubo de rayos catódicos (CRT) para mostrar gráficos simples. Sin embargo, el hito fundacional se atribuye a **Iván Sutherland**, quien en 1963 presentó su tesis doctoral, **Sketchpad**. Este sistema permitía a los usuarios dibujar sobre una pantalla con un lápiz óptico, interactuando directamente con los objetos gráficos, lo que sentó las bases de la interacción humano-computadora y el diseño asistido por computadora (CAD).

### La consolidación y el realismo (décadas de 1970 y 1980)
Durante los años 70, la investigación se centró en añadir realismo a las imágenes. Surgieron conceptos fundamentales como el **sombreado** (desarrollado por Henri Gouraud y Bui Tuong Phong, dando lugar a los sombreados que llevan sus nombres) y las **superficies ocultas** (algoritmo del pintor, Z-buffer). En esta época, **Xerox PARC** desarrolló la interfaz gráfica de usuario (GUI) con ventanas, iconos y menús, popularizada después por Apple y Microsoft. Los años 80 vieron la llegada de las estaciones de trabajo gráficas y los primeros esfuerzos por lograr el **fotorrealismo**, con técnicas como el **trazado de rayos** (ray tracing) y la **radiosidad**, que simulan el comportamiento complejo de la luz.

### La era digital y la masificación (década de 1990 al presente)
Con la bajada de costos del hardware, los gráficos por computadora se masificaron. La industria del entretenimiento fue un gran motor: **Pixar** estrenó "Toy Story" (1995), el primer largometraje completamente animado por computadora. Las tarjetas gráficas (GPUs) se volvieron ubicuas en los ordenadores personales, permitiendo videojuegos en 3D y efectos visuales en tiempo real. Hoy en día, la graficación converge con tecnologías como la **realidad virtual (VR)** , la **realidad aumentada (AR)** y el renderizado basado en inteligencia artificial.

## 1.2. Áreas de aplicación

La graficación por computadora es una tecnología transversal que impacta numerosos campos:

- **Entretenimiento:** Es el área más visible, incluyendo los efectos visuales (VFX) en el cine, la animación por computadora (3D y 2D) y la totalidad de los videojuegos modernos, que crean mundos inmersivos y personajes complejos.
- **Diseño asistido por computadora (CAD) y fabricación:** Utilizado en ingeniería, arquitectura y diseño industrial para crear modelos precisos de productos, edificios y piezas, permitiendo simulaciones, pruebas de estrés y generación de planos antes de la fabricación física.
- **Visualización científica y médica:** Ayuda a comprender grandes volúmenes de datos. En medicina, se utilizan para crear reconstrucciones 3D a partir de tomografías o resonancias magnéticas, planear cirugías y crear simuladores para entrenamiento. En ciencias, se visualizan moléculas, fenómenos meteorológicos o simulaciones astrofísicas.
- **Simulación y entrenamiento:** Permite crear entornos seguros y controlados para el entrenamiento de pilotos (simuladores de vuelo), conductores de vehículos pesados, personal militar o cirujanos.
- **Arte digital y diseño gráfico:** Abarca desde la creación de ilustraciones digitales, tipografía y diseño de páginas web hasta el arte generativo y las instalaciones interactivas.

## 1.3. Aspectos matemáticos de la graficación

La matemática es el lenguaje subyacente de los gráficos por computadora. Los principales pilares son:

- **Álgebra lineal:** Es la base fundamental. Los puntos en el espacio se representan como **vectores**. Las operaciones de traslación, rotación y escalado (transformaciones) se realizan mediante la multiplicación de estos vectores por **matrices**. La capacidad de combinar múltiples transformaciones en una sola matriz (composición de transformaciones) es clave para la eficiencia en los motores gráficos.
- **Geometría:** Se utilizan distintos tipos de geometría para modelar objetos. La **geometría de sólidos constructivos (CSG)** combina formas primitivas (cubos, esferas, cilindros) mediante operaciones booleanas (unión, intersección, diferencia). Las **superficies paramétricas**, como las curvas y superficies de Bézier y las B-splines, permiten crear formas suaves y orgánicas, siendo esenciales en el diseño industrial y la animación de personajes.
- **Trigonometría:** Esencial para calcular ángulos de rotación, determinar la dirección de la luz (vectores), calcular normales a superficies (fundamentales para la iluminación) y en la definición del campo de visión de las cámaras virtuales.
- **Cálculo:** Se aplica en la simulación de fenómenos físicos (movimiento de partículas, dinámica de fluidos, colisiones), en la generación de superficies suaves (cálculo de derivadas para normales) y en algoritmos de renderizado avanzados.

## 1.4. Modelos del color: RGB, CMY, HSV y HSL

Un modelo de color es una abstracción matemática que permite representar los colores como tuplas de números (generalmente tres o cuatro). La elección del modelo depende de la aplicación: visualización en pantalla, impresión, o manipulación intuitiva por parte de un diseñador.

### Modelo RGB (Red, Green, Blue)
Es un modelo **aditivo**, basado en la síntesis de la luz. Los colores se crean sumando cantidades de luz roja, verde y azul. La ausencia total de las tres da el negro, y la suma total (a máxima intensidad) da el blanco. Se representa comúnmente como un cubo unitario.
- **Aplicación:** Es el modelo estándar para todos los dispositivos que emiten luz: monitores de computadora, televisores, proyectores, pantallas de teléfonos móviles, cámaras digitales y escáneres.
- **Característica:** Es **dependiente del dispositivo**, lo que significa que un mismo valor RGB puede verse ligeramente diferente en dos pantallas distintas.

### Modelo CMY (Cyan, Magenta, Yellow) y CMYK (Cyan, Magenta, Yellow, Key/Black)
Es un modelo **sustractivo**, basado en la absorción de la luz. Los colores se crean restando componentes de la luz blanca mediante pigmentos (tinta o pintura). El cian absorbe el rojo, el magenta absorbe el verde y el amarillo absorbe el azul. En teoría, la mezcla de los tres da el negro, pero en la práctica produce un marrón sucio, por lo que en la impresión profesional se añade el negro (K) para mejorar el contraste y la profundidad, dando lugar al modelo **CMYK**.
- **Aplicación:** Es el modelo estándar para todas las artes gráficas e impresión: impresoras de inyección de tinta, imprentas offset, fotocopiadoras.

### Modelo HSV (Hue, Saturation, Value) y HSL (Hue, Saturation, Lightness/Luminance)
Estos modelos se diseñaron para ser más **intuitivos para el ser humano** que el RGB. Separan el color en tres componentes perceptuales:
- **Matiz (Hue):** Es el pigmento puro, el tipo de color (rojo, verde, azul, amarillo...). Se representa como un ángulo de 0° a 360° en una rueda de color.
- **Saturación (Saturation):** Es la viveza o pureza del color. Una saturación del 100% es el color puro; a medida que disminuye, el color se vuelve más grisáceo y apagado.
- **Valor (Value) en HSV / Luminosidad (Lightness) en HSL:** Representa la claridad u oscuridad del color.
    - En **HSV**, el Valor (Value) representa el brillo máximo del color (desde negro hasta el color puro).
    - En **HSL**, la Luminosidad (Lightness) es una mezcla que va desde el negro (0%) hasta el blanco (100%), pasando por el color puro en el 50%.
- **Aplicación:** Son ampliamente utilizados en software de diseño gráfico y edición de imágenes (como los selectores de color en Photoshop o GIMP), en gráficos por computadora para la selección de colores y en tareas de procesamiento de imágenes donde se quiere operar sobre el color independientemente de la iluminación.

---

### Tutorial Práctico: Iluminando un cubo y sus caras en Blender

Este tutorial te guiará paso a paso para crear una escena simple con un cubo y aprender a controlar su iluminación en Blender, un potente software de modelado y renderizado 3D.

**Objetivo:** Comprender cómo la posición, el tipo y la intensidad de las luces afectan la apariencia de un objeto 3D básico.

**Paso 1: Configuración inicial de la escena**
1.  Abre Blender. La escena predeterminada ya contiene un cubo, una cámara y una luz puntual.
2.  Para una mejor visualización, cambia el modo de sombreado de la vista 3D a **"Material Preview"** o **"Rendered"**. Puedes hacerlo con el ícono en la esquina superior derecha de la ventana 3D (un círculo con sombras). Esto te permitirá ver los efectos de la luz en tiempo real.

**Paso 2: Añadir y posicionar fuentes de luz**
Vamos a experimentar con tres tipos de luz.
1.  **Eliminar la luz por defecto:** Selecciona la luz (el punto amarillo con una línea punteada) y presióna la tecla `Supr`.
2.  **Añadir una Luz de Área:**
    - Desde el menú superior, ve a `Add` > `Light` > `Area`.
    - Con la luz seleccionada, presióna `G` para moverla y `R` para rotarla. Colócala a la derecha y arriba del cubo, apuntando hacia él. Observa cómo las sombras son suaves y la luz es difusa.
3.  **Probar una Luz Puntual (Point Light):**
    - Añade una nueva luz: `Add` > `Light` > `Point`.
    - Mueve esta luz (`G`) a la izquierda del cubo, muy cerca. La luz puntual emite en todas direcciones desde un punto. Notarás que las sombras son más definidas y la luz es más dura si está cerca. Puedes ajustar su potencia en el panel de propiedades de la luz (el ícono de bombilla).

**Paso 3: Aplicar materiales y colores a las caras del cubo**
1.  **Crear un material para el cubo:**
    - Selecciona el cubo.
    - En el panel de propiedades de la derecha, haz clic en el ícono de material (un círculo).
    - Haz clic en "New". Se creará un material por defecto.
    - En la sección "Surface", haz clic en el cuadro de color junto a "Base Color". Elige un color, por ejemplo, un gris claro o un rojo. Esto nos ayudará a ver el efecto de la luz sobre un color base.
2.  **Asignar colores diferentes a cada cara (Opcional):**
    - Ve al modo "Edit Mode" (tecla `Tab`).
    - Con la herramienta de selección de caras (ícono de cuadrado en la esquina superior izquierda), selecciona una cara del cubo.
    - En el panel de materiales, haz clic en el botón "+" al lado de la lista de materiales para crear un nuevo material.
    - Asígnale un color diferente (ej. azul) y luego haz clic en el botón "Assign". Esto aplicará ese material solo a la cara seleccionada. Repite para las otras caras.

**Paso 4: Experimentar con las propiedades de la luz**
Selecciona la luz principal (la de área o la puntual) y, en el panel de propiedades de la luz, juega con los siguientes parámetros:
- **Color:** Cambia el color de la luz. Una luz roja sobre un cubo azul producirá un efecto muy diferente a una luz blanca.
- **Potencia (Power):** Aumenta y disminuye la intensidad. Una luz muy fuerte sobreexpone los colores, mientras que una muy débil deja la escena oscura.
- **Tamaño (para luz de área):** Aumentar el tamaño de la fuente de luz hace que las sombras sean más suaves y difusas. Disminuirlo hace que las sombras sean más duras y definidas.

**Paso 5: Iluminar desde dentro del cubo (efecto especial)**
Una técnica interesante es colocar una luz dentro de un objeto para simular que emite luz propia o para crear reflejos internos.
1.  Asegúrate de tener un cubo con un material que tenga algo de especularidad (el valor por defecto suele funcionar).
2.  Añade una "Luz Puntual" (`Add` > `Light` > `Point`).
3.  En "Edit Mode" o "Object Mode", mueve la luz (`G`) hasta que esté dentro del cubo. Puede ser útil cambiar a "Wireframe" mode (tecla `Z`) para ver la luz dentro.
4.  En el panel de la luz, aumenta considerablemente su "Power". Verás cómo el interior del cubo se ilumina y la luz se refleja en las paredes internas, creando un efecto interesante.

**Paso 6: Renderizar la imagen**
Para guardar tu trabajo, ve al menú `Render` > `Render Image` (o presiona `F12`). Una vez que la imagen se genere, ve a `Image` > `Save As` para guardarla en tu computadora.

---

## 1.5. Representación y trazo de líneas y polígonos

Antes de llenar una pantalla con colores y texturas, es necesario dibujar los contornos de los objetos. Aquí es donde entran en juego los algoritmos de dibujo de primitivas.

- **Algoritmos de trazado de líneas:** Un monitor es una cuadrícula de píxeles. Dibujar una línea recta ideal sobre esta cuadrícula requiere decidir qué píxeles se deben encender para que la línea se vea lo más recta posible. El algoritmo más famoso es el **Algoritmo de Bresenham** (o algoritmo del punto medio), que utiliza solo aritmética de enteros (sumas, restas y desplazamientos de bits) para ser extremadamente rápido.
- **Rasterización de polígonos:** Un polígono (como un triángulo) se rellena determinando qué píxeles están dentro de su área. Un método común es el **algoritmo de scanline**, que procesa la imagen línea de píxeles por línea (scanline), calculando las intersecciones de la línea con los bordes del polígono y rellenando los píxeles entre esas intersecciones.

### 1.5.1 Formatos de imagen

Los formatos de imagen se dividen en dos grandes familias:

- **Mapas de bits (Raster):** Almacenan la imagen como una cuadrícula de píxeles, cada uno con un valor de color. Son ideales para fotografías e imágenes con gradientes suaves.
    - **JPEG (JPG):** Utiliza compresión con pérdida, lo que reduce drásticamente el tamaño del archivo a costa de perder algo de detalle (artefactos). Ideal para fotografías en web y dispositivos.
    - **PNG:** Utiliza compresión sin pérdida. Soporta transparencia (canal alfa) y es excelente para gráficos con líneas nítidas, logotipos e imágenes que requieren alta calidad.
    - **GIF:** Limitado a 256 colores, soporta animación simple. Usa compresión sin pérdida LZW. Bueno para gráficos simples y animaciones cortas.
    - **BMP:** Formato antiguo de Windows, generalmente sin compresión, lo que da como resultado archivos muy grandes.
- **Gráficos vectoriales:** Almacenan la imagen como fórmulas matemáticas que describen líneas, curvas (como las curvas de Bézier) y formas. Son independientes de la resolución, lo que significa que se pueden escalar a cualquier tamaño sin perder calidad.
    - **SVG:** Formato estándar basado en XML para la web.
    - **AI, CDR:** Formatos nativos de Adobe Illustrator y CorelDRAW, respectivamente.

---

### Prácticas de Dibujo con Blender Python API
En esta sección se presentan dos scripts escritos en Python para Blender que automatizan la construcción de figuras geométricas, relacionadas directamente con los conceptos vistos en 1.5 Representación y trazo de líneas y polígonos. Estos scripts permiten generar un polígono regular 2D (triángulo) y un patrón de círculos conocido como la Flor de la Vida, utilizando únicamente cálculos trigonométricos y la API de Blender.
## Script 1: Polígono 2D regular (`PoLiGoNo_2D.py`)

Este script define una función que genera un polígono regular de `n` lados, centrado en el origen, y lo añade a la escena de Blender como un objeto de malla.
```python
import bpy
import math

def crear_poligono_2d(nombre, lados, radio):
    # Crear una nueva malla y un nuevo objeto
    malla = bpy.data.meshes.new(nombre)
    objeto = bpy.data.objects.new(nombre, malla)

    # Vincular el objeto a la colección activa
    bpy.context.collection.objects.link(objeto)

    vertices = []
    aristas = []

    # Calcular las coordenadas de cada vértice
    for i in range(lados):
        angulo = 2 * math.pi * i / lados
        x = radio * math.cos(angulo)
        y = radio * math.sin(angulo)
        vertices.append((x, y, 0))

    # Conectar cada vértice con el siguiente (y el último con el primero)
    for i in range(lados):
        aristas.append((i, (i + 1) % lados))

    # Construir la malla a partir de los datos
    malla.from_pydata(vertices, aristas, [])
    malla.update()

# Limpiar la escena (opcional)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Crear un triángulo de radio 10
crear_poligono_2d("Poligono2D", lados=8, radio=10)
```
<img width="552" height="383" alt="image" src="https://github.com/user-attachments/assets/a3db3778-bfb0-467a-9981-855ae661e12a" />

### Explicación
Los vértices se calculan mediante coordenadas polares:
`x = radio * cos(ángulo), y = radio * sen(ángulo)`, con `ángulo = 2π * i / lados`.

Las aristas se definen explícitamente conectando cada vértice con el siguiente (el último con el primero mediante el operador módulo `%`).

Este método refleja el concepto de rasterización de líneas a nivel vectorial: Blender se encarga de dibujar los píxeles finales, pero la definición geométrica sigue los principios de los algoritmos de trazado.

### Instrucciones de uso
1. Abre Blender.
2. Cambia al espacio de trabajo Scripting (en la barra superior).
3. Crea un nuevo texto o pega el código en el editor.
4. Ejecuta el script con el botón Run Script.
5. El polígono aparecerá en la escena. Puedes cambiar a vista superior (Num7) para visualizarlo en 2D.
## Script 2: Flor de la Vida (`FlOr_De_ViDa.py`)

Este script genera un patrón de círculos concéntricos que forman la base de la Flor de la Vida, una figura de geometría sagrada compuesta por múltiples círculos superpuestos con un espaciado regular. El código crea un círculo central y luego, mediante un bucle, añade círculos alrededor en posiciones determinadas por un ángulo y el radio.
```Python
import bpy
import math

# Limpiar la escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Parámetros de la figura
radio = 3
paso_angular = 60  # En grados. Para la flor clásica usar 60°

# 1. Círculo central
bpy.ops.mesh.primitive_circle_add(radius=radio, location=(0, 0, 0), vertices=128)

# Bucle para generar círculos alrededor
angulo_actual = 0
while angulo_actual < 360:
    angulo_actual += paso_angular
    x = radio * math.cos(math.radians(angulo_actual))
    y = radio * math.sin(math.radians(angulo_actual))
    bpy.ops.mesh.primitive_circle_add(radius=radio, location=(x, y, 0), vertices=128)
```
<img width="295" height="289" alt="image" src="https://github.com/user-attachments/assets/d238a3fb-d426-4309-8876-991f47024c38" />

### Explicación
- Se coloca un círculo central en el origen.
- El bucle recorre los 360° con un incremento angular (`paso_angular`). Para la flor clásica, se usan 60°, lo que genera seis círculos alrededor del central.
- Las coordenadas de cada nuevo centro se calculan mediante trigonometría:
  `x = radio * cos(θ)`, `y = radio * sen(θ)`, donde `θ` está en radianes.
- El número de vértices por círculo (128) asegura que los círculos se vean suaves.
- Este proceso demuestra cómo transformaciones geométricas (traslación) y la repetición de una operación simple pueden generar una estructura compleja, un principio fundamental en la graficación por computadora.
### Instrucciones de uso
1. En Blender, ve al espacio de trabajo Scripting.
2. Pega el código en el editor de texto.
3. Ejecuta el script.
4. Se crearán siete círculos (central + seis alrededor). Puedes rotar la vista para apreciar la simetría.
## 1.6. Procesamiento de mapas de bits

El procesamiento digital de imágenes (PDI) se refiere a la manipulación de imágenes de mapa de bits mediante algoritmos computacionales. Algunas operaciones fundamentales son:

- **Operaciones puntuales:** Modifican el valor de cada píxel individualmente, sin importar sus vecinos. Ejemplos:
    - **Ajustes de brillo y contraste:** Sumar una constante a todos los píxeles (brillo) o multiplicar por una constante (contraste).
    - **Umbralización (Thresholding):** Convertir una imagen a blanco y negro puro basándose en si el valor del píxel supera o no un cierto umbral.
    - **Inversión de color:** Transformar un color en su complementario (negro a blanco, azul a amarillo, etc.).
- **Filtrado (Operaciones locales):** El nuevo valor de un píxel se calcula en función de los valores de sus vecinos. Esto se hace mediante una matriz pequeña llamada **kernel** o máscara de convolución.
    - **Filtros de suavizado (Paso Bajo):** Promedian los píxeles con sus vecinos para reducir el ruido y suavizar la imagen. Ej: Filtro Gaussiano.
    - **Filtros de realce (Paso Alto):** Detectan bordes y agudizan la imagen. Ej: Filtro de Sobel, Laplaciano.
- **Operaciones geométricas:** Modifican la disposición espacial de los píxeles.
    - **Redimensionamiento (Escalado):** Aumentar o disminuir el tamaño de la imagen, lo que implica un proceso de interpolación (vecino más cercano, bilineal, bicúbica) para calcular los nuevos valores de píxel.
    - **Rotación, traslación y deformación.**
- **Operaciones en el dominio de la frecuencia:** La imagen se transforma al dominio de la frecuencia (por ejemplo, mediante la Transformada Rápida de Fourier - FFT), se aplican filtros en ese dominio (como eliminar frecuencias altas para suavizar o bajas para realzar bordes), y luego se transforma de vuelta al dominio espacial.

### Conclusión

La Unidad I ha establecido el piso teórico sobre el que se asienta todo el edificio de la graficación por computadora. Desde los trazos más simples de una línea con el algoritmo de Bresenham hasta la compleja simulación de la luz mediante modelos como RGB o HSV, pasando por el conocimiento de la historia, las matemáticas y las aplicaciones, el estudiante adquiere una visión integral de los procesos que convierten datos numéricos en imágenes visuales. Las prácticas de dibujo y el tutorial en Blender sirven como un primer y valioso contacto tangible con estos conceptos, preparando el camino para unidades más avanzadas.

### Referencias

1.  DOAJ (Directory of Open Access Journals). (2024). *Research of color models in digital graphics*.
2.  Smith College. (s.f.). *CSC 240 Laboratory 13: Blender Wooden Cup*.
3.  Baidu Baike. (2025). *Color Model (颜色模型)*.
4.  Blender Stack Exchange. (s.f.). *Revisions about lighting inside objects*.
5.  GitHub - james-alex. (2019). *flutter_color_models*.
6.  Pub.dev. (2019). *color_models 0.2.5*.
7.  Aspose. (2024). *ColorModel Enumeration*.
