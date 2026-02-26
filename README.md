# GrAfIcAcIoN_aPuNtEs_En_ClAsEs
# Unidad I. Introducción a la graficación por computadora.
La graficación por computadora es una rama de la informática que se ocupa de generar, modificar y presentar imágenes y representaciones visuales a través de algoritmos y herramientas digitales especializadas. Integra fundamentos de matemáticas, programación y diseño para producir gráficos en 2D y 3D que pueden ser visualizados en pantallas, dispositivos móviles o entornos de realidad virtual.

Esta disciplina resulta esencial en sectores como los videojuegos, la animación, el diseño asistido por computadora (CAD), la simulación científica y la producción cinematográfica digital. Mediante procesos como el modelado, el renderizado y la animación, la graficación por computadora hace posible convertir datos y nociones abstractas en representaciones visuales claras e interactivas.
## 1.1. Historia y evolución de la graficación por computadora

La graficación por computadora es la disciplina que se encarga de generar, representar y manipular imágenes visuales mediante el uso de computadoras. Su evolución ha sido vertiginosa, pasando de simples representaciones de líneas en monitores a complejos mundos virtuales fotorrealistas.

### Los inicios (décadas de 1950 y 1960)
En la década de 1950, los primeros pasos estuvieron ligados a proyectos militares y académicos. El computador Whirlwind, desarrollado en el MIT, fue pionero al mostrar texto y gráficos en tiempo real en un tubo de rayos catódicos, sentando las bases para sistemas de defensa aérea como SAGE. Paralelamente, en 1958, William Higinbotham creó Tennis for Two utilizando un osciloscopio, demostrando el potencial lúdico de las gráficas. Los años 60 marcaron el nacimiento de la interactividad: Ivan Sutherland, considerado el padre de la graficación, presentó en 1963 su tesis doctoral Sketchpad, un sistema que permitía dibujar con un lápiz óptico sobre la pantalla, introduciendo conceptos como objetos geométricos y restricciones. En 1968, Douglas Engelbart realizó La madre de todas las demostraciones, donde mostró el ratón, el hipertexto y las primeras interfaces gráficas de usuario, sentando las bases de la interacción humano-computadora.

### La consolidación y el realismo (décadas de 1970 y 1980)
Durante los años 70, la investigación se enfocó en añadir realismo a las imágenes. Surgieron técnicas de sombreado como las de Gouraud y Phong, que permitían transiciones suaves de color y reflejos especulares, así como algoritmos para superficies ocultas (como el z-buffer). Además, en Xerox PARC se desarrollaron las primeras interfaces gráficas de usuario con ventanas e iconos, aunque su popularización llegaría después. En el ámbito comercial, Atari llevó los gráficos a los hogares con juegos como Pong, iniciando la industria del entretenimiento electrónico. La década de 1980 trajo la revolución de la computación personal y el cine digital. AutoCAD (1982) transformó el diseño asistido por computadora (CAD) en ingeniería y arquitectura. Pixar, surgida de Lucasfilm, produjo cortometrajes como Luxo Jr. que aplicaban principios de animación tradicional a modelos 3D, demostrando el potencial expresivo del medio. Mientras tanto, Apple popularizó la interfaz gráfica con la Macintosh (1984), acercando las ventanas e iconos al público general.

### La era digital y la masificación (década de 1990 al presente)
En los años 90, la aceleración por hardware revolucionó los gráficos. Aparecieron estándares como OpenGL y DirectX, que facilitaron el desarrollo de aplicaciones 3D. En 1995, Pixar estrenó Toy Story, el primer largometraje completamente animado por computadora. El lanzamiento de la NVIDIA GeForce 256 en 1999, considerada la primera GPU, trasladó el procesamiento geométrico a hardware dedicado, permitiendo gráficos en tiempo real más complejos. El siglo XXI ha difuminado la frontera entre lo real y lo virtual. Los shaders programables permiten efectos como piel realista o agua dinámica. El trazado de rayos (ray tracing), que simula el comportamiento físico de la luz, se ha vuelto posible en tiempo real gracias a núcleos especializados en las GPUs. Además, la realidad virtual y aumentada integran sensores y visión computacional para crear experiencias inmersivas, mientras que la inteligencia artificial comienza a aplicarse en el renderizado y la generación de contenido. Hoy, la graficación por computadora es una disciplina transversal que impulsa desde el entretenimiento hasta la ciencia, permitiendo visualizar datos y conceptos de formas antes inimaginables.

## 1.2. Áreas de aplicación

La graficación por computadora es una tecnología transversal que impacta numerosos campos:

- **Entretenimiento:** Es el área más visible, incluyendo los efectos visuales (VFX) en el cine, la animación por computadora (3D y 2D) y la totalidad de los videojuegos modernos, que crean mundos inmersivos y personajes complejos.
- **Diseño asistido por computadora (CAD) y fabricación:** Utilizado en ingeniería, arquitectura y diseño industrial para crear modelos precisos de productos, edificios y piezas, permitiendo simulaciones, pruebas de estrés y generación de planos antes de la fabricación física.
- **Visualización científica y médica:** Ayuda a comprender grandes volúmenes de datos. En medicina, se utilizan para crear reconstrucciones 3D a partir de tomografías o resonancias magnéticas, planear cirugías y crear simuladores para entrenamiento. En ciencias, se visualizan moléculas, fenómenos meteorológicos o simulaciones astrofísicas.
- **Simulación y entrenamiento:** Permite crear entornos seguros y controlados para el entrenamiento de pilotos (simuladores de vuelo), conductores de vehículos pesados, personal militar o cirujanos.
- **Arte digital y diseño gráfico:** Abarca desde la creación de ilustraciones digitales, tipografía y diseño de páginas web hasta el arte generativo y las instalaciones interactivas.
<img width="960" height="490" alt="image" src="https://github.com/user-attachments/assets/1a09497c-8c2b-4a33-9d8e-4afbc13ea60b" />

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
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/845ac27b-e0fc-417e-ab46-98a343e82d06" />

### Modelo CMY (Cyan, Magenta, Yellow) y CMYK (Cyan, Magenta, Yellow, Key/Black)
Es un modelo **sustractivo**, basado en la absorción de la luz. Los colores se crean restando componentes de la luz blanca mediante pigmentos (tinta o pintura). El cian absorbe el rojo, el magenta absorbe el verde y el amarillo absorbe el azul. En teoría, la mezcla de los tres da el negro, pero en la práctica produce un marrón sucio, por lo que en la impresión profesional se añade el negro (K) para mejorar el contraste y la profundidad, dando lugar al modelo **CMYK**.
- **Aplicación:** Es el modelo estándar para todas las artes gráficas e impresión: impresoras de inyección de tinta, imprentas offset, fotocopiadoras.
<img width="1920" height="250" alt="image" src="https://github.com/user-attachments/assets/e28b7fe0-73e7-4230-8336-d9303010717f" />

### Modelo HSV (Hue, Saturation, Value) y HSL (Hue, Saturation, Lightness/Luminance)
Estos modelos se diseñaron para ser más **intuitivos para el ser humano** que el RGB. Separan el color en tres componentes perceptuales:
- **Matiz (Hue):** Es el pigmento puro, el tipo de color (rojo, verde, azul, amarillo...). Se representa como un ángulo de 0° a 360° en una rueda de color.
- **Saturación (Saturation):** Es la viveza o pureza del color. Una saturación del 100% es el color puro; a medida que disminuye, el color se vuelve más grisáceo y apagado.
- **Valor (Value) en HSV / Luminosidad (Lightness) en HSL:** Representa la claridad u oscuridad del color.
    - En **HSV**, el Valor (Value) representa el brillo máximo del color (desde negro hasta el color puro).
    - En **HSL**, la Luminosidad (Lightness) es una mezcla que va desde el negro (0%) hasta el blanco (100%), pasando por el color puro en el 50%.
- **Aplicación:** Son ampliamente utilizados en software de diseño gráfico y edición de imágenes (como los selectores de color en Photoshop o GIMP), en gráficos por computadora para la selección de colores y en tareas de procesamiento de imágenes donde se quiere operar sobre el color independientemente de la iluminación.
<img width="1000" height="452" alt="image" src="https://github.com/user-attachments/assets/60aa31dd-4f00-4d20-98b7-eb8a2121a5c3" />

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
El procesamiento de mapas de bits, también conocido como imágenes raster, constituye un pilar fundamental en áreas como la graficación por computadora, la visión artificial y el renderizado digital. A diferencia de los gráficos vectoriales, que se definen mediante ecuaciones matemáticas, una imagen raster se estructura como una rejilla bidimensional de píxeles. Cada píxel, la unidad mínima de información, almacena valores numéricos que representan color, brillo u otras propiedades visuales.

Estas imágenes, también denominadas bitmap, raster image o imagen matricial, tienen sus dimensiones determinadas por la cantidad de píxeles en horizontal y vertical. Su función principal es capturar y representar el mundo analógico en formato digital: cuando tomamos una fotografía con un smartphone o una cámara profesional, la escena se traduce a datos de píxel que, al visualizarse en pantalla o compartirse en línea, conforman una imagen raster.
<img width="371" height="211" alt="image" src="https://github.com/user-attachments/assets/f3e4ef88-bbaa-473e-a31c-67ea72c82f1b" />

## Operaciones fundamentales en el procesamiento de imágenes raster

El procesamiento digital de imágenes (PDI) abarca un conjunto de algoritmos que manipulan los píxeles para lograr diversos efectos o extraer información. Estas operaciones pueden clasificarse en varias categorías:

### 1. Operaciones puntuales (píxel a píxel)
En este tipo de transformación, el valor resultante de cada píxel depende exclusivamente de su valor original, sin considerar los píxeles vecinos. Algunos ejemplos comunes son:

- **Ajuste de brillo y contraste**: se modifica el brillo sumando una constante a cada píxel, mientras que el contraste se altera multiplicando por un factor.
- **Inversión de color**: se convierte cada color en su complementario (por ejemplo, negro a blanco, azul a amarillo).
- **Umbralización (thresholding)**: se transforma la imagen en blanco y negro puro según si el valor del píxel supera o no un límite establecido.
<img width="548" height="343" alt="image" src="https://github.com/user-attachments/assets/d7165dca-4bb6-425a-a987-118267593862" />

### 2. Filtros de vecindad (convolución)
Aquí el nuevo valor de un píxel se calcula a partir de sus vecinos, utilizando una matriz denominada **kernel** o máscara de convolución que se desliza sobre la imagen. Entre las aplicaciones más frecuentes se encuentran:

- **Desenfoque (blur)**: se promedian los colores de los píxeles cercanos para suavizar la imagen (por ejemplo, filtro gaussiano).
- **Enfoque (sharpen)**: se realzan las diferencias de color entre píxeles adyacentes para aumentar la nitidez.
- **Detección de bordes**: algoritmos como Sobel o Canny identifican cambios bruscos de intensidad, resaltando los contornos de los objetos.

### 3. Transformaciones geométricas
Estas operaciones alteran la disposición espacial de los píxeles:

- **Escalado**: al ampliar o reducir una imagen, es necesario recurrir a técnicas de interpolación (vecino más cercano, bilineal, bicúbica) para determinar los colores de los nuevos píxeles.
- **Rotación y traslación**: se modifica la orientación o posición de la imagen, lo que también puede requerir interpolación para mantener la calidad.
<img width="555" height="403" alt="image" src="https://github.com/user-attachments/assets/d7b310d5-605f-4941-8593-78c0301b47c0" />

### 4. Operaciones en el dominio de la frecuencia
En este enfoque, la imagen se transforma al dominio de la frecuencia mediante herramientas como la **Transformada Rápida de Fourier (FFT)**. Allí se aplican filtros (por ejemplo, eliminar frecuencias altas para suavizar o bajas para realzar bordes) y luego se regresa al dominio espacial.

## Formatos de archivo para mapas de bits

La elección del formato adecuado depende del uso previsto (web, impresión, edición profesional, etc.). A continuación, se describen los más relevantes:

- **JPG / JPEG**: ideal para imágenes de tono continuo (como fotografías) en entornos web, gracias a su buena compresión y calidad. No admite transparencia y no es el formato preferido para fotografía profesional de alta gama, aunque sí es útil para impresión en ciertos contextos.
- **TIFF**: formato sin compresión (o con compresión lossless) que preserva toda la información de la imagen. Es el estándar para archivos de impresión profesional, ya que admite transparencia y es compatible con la mayoría de programas. Su principal desventaja es el gran tamaño de archivo.
- **PSD**: formato nativo de Adobe Photoshop que guarda capas, canales alfa (transparencia), objetos inteligentes, efectos y tipografía. Es ideal para flujos de trabajo de diseño gráfico y puede importarse desde otras aplicaciones de Adobe.
- **GIF**: muy popular en internet por su capacidad de animación y su bajo peso. Utiliza un modo de color indexado (reduce la paleta de colores) y admite transparencia de baja calidad. Es recomendable para imágenes con colores planos, no para fotografías.
- **PNG**: combina compresión eficiente con soporte para transparencia de alta calidad (canales alfa de 8 y 24 bits). Es el formato preferido para composiciones digitales y elementos web que requieren fondo transparente, manteniendo una buena relación de calidad-peso.
<img width="1200" height="800" alt="image" src="https://github.com/user-attachments/assets/7f1a5dde-fcf2-453d-b1b2-b156aa691d1d" />


### Conclusión

La Unidad I ha establecido el piso teórico sobre el que se asienta todo el edificio de la graficación por computadora. Desde los trazos más simples de una línea con el algoritmo de Bresenham hasta la compleja simulación de la luz mediante modelos como RGB o HSV, pasando por el conocimiento de la historia, las matemáticas y las aplicaciones, el estudiante adquiere una visión integral de los procesos que convierten datos numéricos en imágenes visuales. Las prácticas de dibujo y el tutorial en Blender sirven como un primer y valioso contacto tangible con estos conceptos, preparando el camino para unidades más avanzadas.

### Referencias

1.  Vázquez, J. (n.d.). Modelos de color. MindMeister. Retrieved February 26, 2026, from https://www.mindmeister.com/ru/1647489159/modelos-de-color
2.  Liwanag, A. (2023, April 19). Tipos de archivos de imagen: todo lo que necesita saber sobre las imágenes. Anymp4.com; AnyMP4. https://www.anymp4.com/es/photo-converting/image-file-types-and-differences.html
3. Villate, L. (2025, April 8). Formatos de imagen: usos, características y diferencias. Hubspot.es. https://blog.hubspot.es/marketing/formatos-de-imagen
4. (N.d.). Neilpatel.com. Retrieved February 26, 2026, from https://neilpatel.com/br/blog/formatos-de-imagem/
5. Client challenge. (n.d.). Scribd.com. Retrieved February 26, 2026, from https://es.scribd.com/document/393263572/Historia-y-Evolucion-de-La-Graficacion-Por-Computadora
6. Client challenge. (n.d.-a). Scribd.com. Retrieved February 26, 2026, from https://es.scribd.com/document/393263572/Historia-y-Evolucion-de-La-Graficacion-Por-Computadora
7. Historia y evolucion DE la graficacion Por computadora Bernardo gerhar. (n.d.). Genially. Retrieved February 26, 2026, from https://view.genially.com/65bc786c9fa689001318901a/interactive-content-historia-y-evolucion-de-la-graficacion-por-computadora-bernardo-gerhar
8. Machuca, F. (2022, April 1). Aprende qué es un mapa de bits y haz que tus trabajos resalten por su calidad. https://www.crehana.com. https://www.crehana.com/blog/estilo-vida/que-es-mapa-bits/
9. Client challenge. (n.d.-c). Slideshare.net. Retrieved February 26, 2026, from https://es.slideshare.net/slideshow/1-3-aspectos-matematicos-de-la-graficacion-pdf/282295700
10. Client challenge. (n.d.-d). Slideshare.net. Retrieved February 26, 2026, from https://es.slideshare.net/slideshow/1-6-procesamiento-de-mapas-de-bits-en-graficacion/282295902
11. Valdes, A. S., & Completo, V. mi P. (n.d.). Graficación. Blogspot.com. Retrieved February 26, 2026, from https://graficacionito.blogspot.com/2013/09/14-aspectos-matematicos-de-la.html











