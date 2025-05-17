Camilo Mitnick Gutierrez(Berners Lee)
Juan Sebastian Pedraza(Berners Lee)
Mariana Velez Suarez(Berners Lee)

Sistema de Gestión de Hojas de Vida
Un sistema en Python para registrar, buscar, filtrar y exportar hojas de vida de candidatos de manera sencilla y efectiva.
Descripción
Este sistema permite gestionar hojas de vida completas, incluyendo información personal, formación académica, experiencia laboral, referencias y habilidades. El programa funciona mediante un menú por consola que facilita la interacción con distintas funciones.
Características

✅ Registro de hojas de vida con validación de correo electrónico
🔍 Búsqueda de candidatos por documento y fecha de nacimiento
🔢 Filtro de candidatos por años de experiencia
📊 Análisis de habilidades más comunes entre candidatos
💾 Exportación de datos a formatos JSON y CSV
🔒 Identificación única por documento y fecha de nacimiento

Librerías Utilizadas
El sistema utiliza únicamente librerías estándar de Python, por lo que no requiere instalación adicional:

json: Para serializar y exportar datos en formato JSON
csv: Para exportar datos en formato CSV
datetime: Para cálculos de edad y manejo de fechas
collections (Counter): Para contar y clasificar habilidades

Estas librerías vienen incluidas en la instalación estándar de Python 3.x.
Instalación
No requiere instalación especial. Solo descargue el archivo y ejecútelo con Python:
bashpython sistema_hojas_vida.py
Instrucciones para ejecutar el programa

Asegúrese de tener Python 3.x instalado en su sistema
Descargue el archivo sistema_hojas_vida.py a su computadora
Abra una terminal o línea de comandos
Navegue hasta el directorio donde guardó el archivo
Ejecute el comando:
bashpython sistema_hojas_vida.py
(En algunos sistemas puede ser necesario usar python3 en lugar de python)
Siga las instrucciones que aparecen en pantalla para interactuar con el programa

Uso
Al ejecutar el programa se mostrará un menú con las siguientes opciones:

Registrar hoja de vida: Permite ingresar una nueva hoja de vida con toda la información del candidato.
Buscar hoja de vida: Localiza y muestra la información completa de un candidato específico.
Filtrar por experiencia: Encuentra candidatos que cumplan con un mínimo de años de experiencia.
Exportar a JSON: Guarda todas las hojas de vida en formato JSON en el directorio actual.
Exportar a CSV: Guarda la información básica de los candidatos en formato CSV en el directorio actual.
Ver habilidades más comunes: Muestra un conteo de las habilidades más frecuentes entre los candidatos.
Salir: Cierra la aplicación.

Estructura de Datos
Cada hoja de vida almacena:

Datos personales: nombre, documento, correo electrónico, teléfono, dirección y fecha de nacimiento
Formación académica: múltiples instituciones, títulos y años de estudio
Experiencia laboral: empresas, cargos, funciones y duración (en años)
Referencias: contactos de referencia con nombre, relación y teléfono
Habilidades: conjunto de competencias del candidato

Ejemplos de Uso
1. Registro de una hoja de vida
--- REGISTRAR HOJA DE VIDA ---
Nombre: Juan Pérez
Documento: 1234567890
Correo electrónico: juan@ejemplo.com
Teléfono: 3001234567
Dirección: Calle 123 #45-67
Fecha de nacimiento (YYYY-MM-DD): 1990-05-15
¿Agregar formación académica? (s/n): s
  Institución: Universidad Nacional
  Título: Ingeniero de Sistemas
  Años: 2010-2015
¿Agregar formación académica? (s/n): n
¿Agregar experiencia laboral? (s/n): s
  Empresa: TechSolutions
  Cargo: Desarrollador
  Funciones: Desarrollo de aplicaciones web
  Duración (años): 3
¿Agregar experiencia laboral? (s/n): n
¿Agregar referencia? (s/n): s
  Nombre: María Rodríguez
  Relación: Jefe anterior
  Teléfono: 3009876543
¿Agregar referencia? (s/n): n
Habilidades (separadas por comas): python, java, sql, html
✅ Hoja de vida registrada exitosamente.
2. Búsqueda de candidato
--- BUSCAR HOJA DE VIDA ---
Documento: 1234567890
Fecha de nacimiento (YYYY-MM-DD): 1990-05-15

--- HOJA DE VIDA ---
Nombre: Juan Pérez
Documento: 1234567890
Correo: juan@ejemplo.com
Contacto: 3001234567
Direccion: Calle 123 #45-67
Fecha_nacimiento: 1990-05-15
Formacion:
   {'institucion': 'Universidad Nacional', 'titulo': 'Ingeniero de Sistemas', 'años': '2010-2015'}
Experiencia:
   {'empresa': 'TechSolutions', 'cargo': 'Desarrollador', 'funciones': 'Desarrollo de aplicaciones web', 'duracion': 3}
Referencias:
   ('María Rodríguez', 'Jefe anterior', '3009876543')
Habilidades:
   python
   java
   sql
   html
3. Filtrar por experiencia
--- FILTRAR POR EXPERIENCIA ---
Filtrar por mínimo de años de experiencia: 2

--- CANDIDATOS CON MÁS DE 2 AÑOS ---
Juan Pérez - 3 años
Ana Gómez - 5 años
Carlos López - 4 años
4. Exportación a JSON 
json{
    "('1234567890', '1990-05-15')": {
        "nombre": "Juan Pérez",
        "documento": "1234567890",
        "correo": "juan@ejemplo.com",
        "contacto": "3001234567",
        "direccion": "Calle 123 #45-67",
        "fecha_nacimiento": "1990-05-15",
        "formacion": [
            {
                "institucion": "Universidad Nacional",
                "titulo": "Ingeniero de Sistemas",
                "años": "2010-2015"
            }
        ],
        "experiencia": [
            {
                "empresa": "TechSolutions",
                "cargo": "Desarrollador",
                "funciones": "Desarrollo de aplicaciones web",
                "duracion": 3
            }
        ],
        "referencias": [
            [
                "María Rodríguez",
                "Jefe anterior",
                "3009876543"
            ]
        ],
        "habilidades": [
            "python",
            "java",
            "sql",
            "html"
        ]
    }
}
5. Datos Simulados para Pruebas
Para probar el sistema, puede utilizar los siguientes datos de ejemplo:
Candidato 1:

Nombre: Ana Gómez
Documento: 9876543210
Correo: ana.gomez@ejemplo.com
Teléfono: 3157894561
Dirección: Av. Principal #28-43
Fecha de nacimiento: 1988-11-23
Formación: Universidad de Antioquia
Experiencia:  Analista Senior
Referencia: Pedro Martínez, Amigo, 3209876543
Habilidades: excel, powerpoint, analisis de datos, gestión de proyectos

Candidato 2:

Nombre: Carlos López
Documento: 5432167890
Correo: carlos.lopez@ejemplo.com
Teléfono: 3001234567
Dirección: Carrera 45 #12-34
Fecha de nacimiento: 1992-03-15
Formación: Universidad Nacional
Experiencia:  Diseñador UI/UX
Referencia: Laura Sánchez, Supervisora, 3114567890
Habilidades: photoshop, illustrator, figma, ui/ux, html, css

