import bpy
import math

#Limpiar escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

#Parámetros de la figura
radio = 3
angulo_actual = 0
paso_angular = 10 #Cada 60 grados para obtener 6 circulos alrededor

#1.Circulo Central
bpy.ops.mesh.primitive_circle_add(radius=radio, location=(0, 0, 0), vertices=128)

#...INICIO DEL PATRÓN REPETITIVO

# Circulo 1 (Manual)
'''x1 = radio * math.cos(math.radians(angulo_actual))
y1 = radio * math.sin(math.radians(angulo_actual))
bpy.ops.mesh.primitive_circle_add(radius=radio, location=(x1, y1, 0), vertices=64)

# Circulo 2 (Manual)
angulo_actual += paso_angular
x2 = radio * math.cos(math.radians(angulo_actual))
y2 = radio * math.sin(math.radians(angulo_actual))
bpy.ops.mesh.primitive_circle_add(radius=radio, location=(x2, y2, 0), vertices=64)
'''
# Bucle 
angulo_actual = 0
while angulo_actual <360:

    angulo_actual += paso_angular
    
    x = radio * math.cos(math.radians(angulo_actual))
    y = radio * math.sin(math.radians(angulo_actual))
    bpy.ops.mesh.primitive_circle_add(radius=radio, location=(x, y, 0), vertices=128)