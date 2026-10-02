# Taller de gRPC con Python

## Enlace del repositorio

> Pendiente: publicar el proyecto y reemplazar este texto por la URL del repositorio.

## Introducción

Este taller introduce **gRPC**, un framework de comunicación remota que permite
que un cliente invoque métodos de un servicio alojado en un servidor como si
fueran funciones locales. Los servicios y sus mensajes se describen con
Protocol Buffers (`.proto`); a partir de esa definición, `grpcio-tools` genera
el código cliente-servidor para Python.

La práctica implementa el servicio `Greeter` y muestra dos patrones de
comunicación: llamadas **unarias**, donde cada solicitud obtiene una respuesta,
y **streaming del servidor**, donde una solicitud produce varias respuestas.
También se modifica el mensaje de solicitud para incluir la edad del estudiante.

## Ejercicios realizados

1. **Nuevo campo en el mensaje:** se agregó `int32 age = 2` a `HelloRequest`.
   El número `2` es nuevo y no reutiliza el identificador de `name`. `SayHello`
   responde, por ejemplo, `Hola, Estudiante! Tienes 20 años.`
2. **Nuevo método unario:** se agregó `SayGoodbye(HelloRequest) returns
   (HelloReply)` al servicio `Greeter`. El servidor devuelve una despedida y el
   cliente invoca el método.
3. **Streaming del servidor:** `SayHelloRepeatedly` conserva sus cinco
   respuestas, emitidas con `yield` aproximadamente una por segundo.

## Requisitos

- Python 3.12 o compatible.
- `pip`.

## Instalación y generación del código

Abre PowerShell en la carpeta raíz de este proyecto (`taller-grpc`) y crea un
entorno virtual si todavía no tienes uno:

```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

Usar la ruta del ejecutable del entorno evita instalar dependencias en otro
Python que esté disponible en el sistema.

Cada vez que cambies `greeter.proto`, regenera los módulos Python desde la raíz
del proyecto:

```powershell
.\venv\Scripts\python.exe -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. greeter.proto
```

Esto genera `greeter_pb2.py` y `greeter_pb2_grpc.py`.

## Ejecución

Inicia el servidor en una terminal:

```powershell
.\venv\Scripts\python.exe .\server.py
```

En otra terminal, desde la misma carpeta y con el mismo entorno virtual activo,
ejecuta el cliente:

```powershell
.\venv\Scripts\python.exe .\client.py
```

El cliente imprime la respuesta unaria con la edad, la despedida unaria y, por
último, las cinco respuestas del streaming.

```text
Respuesta unaria: Hola, Estudiante! Tienes 20 años.
Despedida unaria: ¡Hasta luego, Estudiante!
Respuestas en streaming:
 -> Hola #1, Estudiante!
 -> Hola #2, Estudiante!
 -> Hola #3, Estudiante!
 -> Hola #4, Estudiante!
 -> Hola #5, Estudiante!
```

## Estructura principal

```text
taller-grpc/
├── client.py
├── greeter.proto
├── greeter_pb2.py          # Generado desde greeter.proto
├── greeter_pb2_grpc.py     # Generado desde greeter.proto
├── requirements.txt
└── server.py
```
