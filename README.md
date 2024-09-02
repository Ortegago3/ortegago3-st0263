# ST0263-Topicos especiales en telematica

- **Estudiante:** Holmer Ortega Gomez. hortegag@eafit.edu.co
- **Profesor:** Edwin Nelson Montoya Munera. emontoya@eafit.edu.co

# Reto 1:
- # 1. Breve descripcion de la actividad:
- Este proyecto consiste en la implementación de un sistema P2P para la compartición de archivos utilizando microservicios distribuidos. Los peers pueden comunicarse entre sí utilizando REST y gRPC para realizar operaciones como registro de peers, búsqueda de archivos, y transferencia de archivos. Además, se implementa un sistema de notificaciones simple utilizando REST para informar a otros peers sobre nuevos archivos disponibles.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor:
- Implementación de un sistema P2P utilizando microservicios distribuidos.
- Comunicación entre peers utilizando REST para operaciones de registro, búsqueda, y transferencia de archivos.
- Implementación de un servidor gRPC para manejar operaciones de transferencia de archivos más eficientes.
- Sistema de notificaciones utilizando REST para informar a otros peers sobre nuevos archivos disponibles.
- Manejo de errores y robustez en la comunicación entre peers.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor:
-El proyecto no utiliza un middleware orientado a mensajes como RabbitMQ para la coordinación entre peers, sino que implementa un sistema de notificaciones más simple utilizando REST.
- El proyecto no se logro la dockerizacion ni el despliegue en AWS.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
- Arquitectura: La arquitectura del proyecto es P2P, donde cada peer actúa tanto como cliente y servidor. La comunicación se realiza a través de REST para operaciones de control y gRPC para la transferencia de archivos.
- Patrones de Diseño: Se utilizaron patrones como Microservicios y API Gateway (para manejar la comunicación entre peers).
- Mejores Prácticas: Uso de entorno virtual para gestionar dependencias, separación de preocupaciones entre diferentes servicios, y manejo de errores robusto en la comunicación entre peers.


# 3. Descripción del ambiente de desarrollo y técnico:
- Lenguaje de Programación: Python 3.x
- Librerías y Paquetes Utilizados:
- Flask: 2.1.0 (para construir las APIs REST)
- gRPC (grpcio, grpcio-tools): 1.46.3 (para la comunicación gRPC)
- Otros paquetes como requests para manejar las solicitudes HTTP.

## como se compila y ejecuta.
Compilación: Python es un lenguaje interpretado, por lo que no se requiere compilación previa. Sin embargo, es necesario instalar las dependencias.
"pip install -r requirements.txt".

## detalles del desarrollo.
- REST: Utilizado para registrar peers, buscar archivos y transferir archivos.
- gRPC: Utilizado para operaciones más eficientes de transferencia de archivos.
- Notificaciones: Implementadas usando REST en lugar de RabbitMQ.

## detalles técnicos
**Parámetros del Proyecto:**
- IP y puerto de cada peer se configuran en el archivo peer1_config.json.
- Directorio donde se almacenan los archivos compartidos.
- **Configuración y Estructura del Proyecto**
- **Estructura del Proyecto:**
- src/config/: Contiene archivos de configuración JSON.
- src/peers/: Contiene los clientes REST y gRPC.
- src/services/: Contiene los servidores REST y gRPC.
- src/proto/: Contiene el archivo proto y sus compilaciones para gRPC.

# 4. Descripción del ambiente de EJECUCIÓN (en producción).
- Lenguaje de Programación: Python 3.x
- Librerías y Paquetes Utilizados: Igual que en el ambiente de desarrollo.
- IP o Nombres de Dominio en la Nube o Máquina Servidor: Se utiliza 127.0.0.1 para localhost durante las pruebas.

## descripción y como se configura los parámetros del proyecto.
- IP y Puertos: Configurados en los archivos peer1_config.json. Ejemplo:
{
  "ip": "127.0.0.1",
  "port": 5001,
  "directory": "./shared/files",
  "peer_seed_url": "http://127.0.0.1:5002"
}.

## como se lanza el servidor.
- Servidor REST: "python src/services/server.py"
- Servidor gRPC: "python src/services/grpc_server.py"

## Miniguia de uso:
-Registro de Peer: El peer se registra automáticamente con otro peer al iniciar client.py.
- Búsqueda de Archivos: Se realiza utilizando client.py.
- Carga y Descarga de Archivos: Se pueden cargar y descargar archivos utilizando client.py para REST o grpc_client.py para gRPC.
- Notificaciones: Los peers son notificados de nuevos archivos disponibles a través de REST.

# 5. otra información que considere relevante para esta actividad.
- Robustez: El sistema maneja errores comunes como fallos de red y archivos no encontrados, lo que lo hace adecuado para entornos distribuidos.
- Simplicidad: La eliminación de RabbitMQ simplifica la implementación y reduce la complejidad del sistema.

# referencias:
## Documentación de Flask:
- URL: https://flask.palletsprojects.com/
- Descripción: Documentación oficial de Flask, un microframework para Python utilizado en la implementación de APIs REST.

## Documentación de gRPC para Python:
- URL: https://grpc.io/docs/languages/python/
- Descripción: Documentación oficial de gRPC para Python, utilizada para implementar la comunicación eficiente entre servicios.

## Documentación de Requests:
- URL: https://docs.python-requests.org/en/latest/
- Descripción: Documentación oficial de la librería Requests, utilizada para manejar solicitudes HTTP en Python.

## Documentación de Python venv:
- URL: https://docs.python.org/3/library/venv.html
- Descripción: Documentación oficial de la herramienta venv en Python para la creación de entornos virtuales.

## Referencias sobre arquitecturas P2P:
- URL: https://en.wikipedia.org/wiki/Peer-to-peer
- Descripción: Página de Wikipedia que proporciona una visión general de las arquitecturas P2P, sus usos y ventajas.

## Documentación de gRPC en Python (GitHub):
- URL: https://github.com/grpc/grpc
- Descripción: Repositorio oficial de gRPC en GitHub, donde se puede encontrar el código fuente y ejemplos de uso.
