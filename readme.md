# Esta api la hice con la finalidad de practicar y profundizar DJRF y Tokens de autenticacion y CBVs

## 🚀 API de Lista de Tareas (To-Do List API) con Django REST Framework

Una API RESTful simple y robusta para gestionar tus tareas diarias, construida con Django y Django REST Framework. Incluye autenticación por tokens, permisos a nivel de objeto.

---

## ✨ Características Principales

* **Gestión CRUD completa:** Crea, lee, actualiza y elimina tareas.
* **Autenticación por Tokens:** Usuarios seguros con tokens de acceso.
* **Permisos a Nivel de Objeto:** Cada usuario solo puede ver y modificar sus propias tareas.
* **Registro de Usuarios:** Endpoint para que nuevos usuarios puedan crear una cuenta.
* **Panel de Administración de Django:** Gestión fácil de usuarios y tareas desde el panel de Django.

---

## 🛠️ Tecnologías Utilizadas

* **Backend:**
    * [Python 3.x](https://www.python.org/)
    * [Django](https://www.djangoproject.com/)
    * [Django REST Framework](https://www.django-rest-framework.org/)
* **Base de Datos:**
    * SQLite (por defecto, puedes configurarlo para PostgreSQL, MySQL, etc.)

---

## 🚀 Cómo Empezar

Sigue estos pasos para levantar la API en tu entorno local.

### Prerequisitos

Asegúrate de tener instalado Python 3.8+ y `pip`.

### Instalación

1.  **Crea y activa un entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows:
    # venv\Scripts\activate
    # En macOS/Linux:
    # source venv/bin/activate
    ```

2.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt # O pip install django djangorestframework django-filter
    ```
    *(Nota: Es buena práctica generar un `requirements.txt` con `pip freeze > requirements.txt`)*

3.  **Aplica las migraciones de la base de datos:**
    ```bash
    python manage.py migrate
    ```
    *(Si es la primera vez o si modificaste el modelo `Task` para añadir `owner`, cuando se pregunte por un valor por defecto para 'owner', elige `1` y presiona Enter para asignarlo a tu superusuario inicial).*

4.  **Crea un superusuario (opcional, pero recomendado para el admin):**
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las instrucciones para crear tus credenciales.

5.  **Inicia el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    La API estará disponible en `http://127.0.0.1:8000/`.

---

## 💡 Uso de la API

Puedes interactuar con la API usando herramientas como [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client), Postman, Insomnia o `curl`.

### Endpoints Principales:

* **`GET /admin/`**: Panel de administración de Django.
* **`POST /api/register/`**: Registrar un nuevo usuario.
    * `Body (JSON): {"username": "newuser", "password": "securepassword"}`
* **`POST /api/token-auth/`**: Obtener un token de autenticación para un usuario existente.
    * `Body (JSON): {"username": "youruser", "password": "yourpassword"}`
    * **Respuesta:** `{"token": "tu_token_aqui"}`
* **`GET /api/tasks/`**: Listar todas las tareas.
* **`POST /api/tasks/`**: Crear una nueva tarea.
* **`GET /api/tasks/{id}/`**: Ver los detalles de una tarea específica.
* **`PUT /api/tasks/{id}/`**: Actualizar completamente una tarea.
* **`PATCH /api/tasks/{id}/`**: Actualizar parcialmente una tarea.
* **`DELETE /api/tasks/{id}/`**: Eliminar una tarea.

### 🔐 Autenticación

Para acceder a los endpoints protegidos (cualquier operación excepto `GET` para no autenticados, y todas las operaciones CRUD donde no eres el propietario), debes incluir tu token en el encabezado `Authorization`:

`Authorization: Token TU_TOKEN_AQUI`

## 👨‍💻 Autor

Eber Colmenares / [EJCM05](https://github.com/EJCM05)
