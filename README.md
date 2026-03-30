# 🧠 PsicoSystem - SaaS Multi-tenant para Centros Psicológicos

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/DRF-Red?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-JSON%20Web%20Tokens-black?style=for-the-badge&logo=json%20web%20tokens)

**PsicoSystem** es una plataforma integral diseñada bajo el modelo **SaaS (Software as a Service)** para la transformación digital de centros psicológicos. El sistema permite la gestión clínica y administrativa garantizando la seguridad y el aislamiento de datos entre diferentes instituciones gracias a su **arquitectura Multi-tenant**.

---

## 🛠️ Stack Tecnológico

La plataforma integra un robusto ecosistema monolítico con soporte dedicado para clientes externos (Móvil / React) gracias a su provisión de APIs RESTful seguras:

* **Backend Framework:** [Django 6.0](https://www.djangoproject.com/) (Python)
* **API Framework:** [Django REST Framework (DRF)](https://www.django-rest-framework.org/)
* **Seguridad y Autenticación:** Tokens JWT (JSON Web Tokens) mediante `djangorestframework-simplejwt`.
* **Base de Datos:** [PostgreSQL](https://www.postgresql.org/) con modelado Multi-tenant.
* **Control de Versiones:** Git & GitHub

---

## 🚀 Arquitectura Multi-tenant y Seguridad

El sistema está diseñado de tal manera que las diferentes clínicas que adquieren el SaaS no comparten ni exponen sus datos entre sí:
* **Tenant Isolation:** En cada petición al servidor y la base de datos, toda consulta se segmenta por la `Clinica` a la que pertenece el usuario (Admin o Psicólogo) intentando acceder.
* **API Rest Segura:** Toda interacción con recursos de la API requiere un `Bearer Token` tramitado mediante nuestro endpoint de autenticación nativo JWT.

---

## 📡 Endpoints de la API (RESTful)

El sistema expone las siguientes rutas bajo el prefijo `/api/` para interactuar de forma programática con Frontends desacoplados o Aplicaciones Móviles.

### Autenticación y JWT
| Método | Endpoint | Descripción | Body (Ejemplo) |
| --- | --- | --- | --- |
| `POST` | `/api/token/` | Obtener Token de Acceso y Refresh (Login) | `{"username": "usr", "password": "pwd"}`|
| `POST` | `/api/token/refresh/` | Renovar Token de Acceso vencido usando el Refresh token | `{"refresh": "<token>"}` |

### Recursos de Gestión Clínica
*Nota: Es obligatorio enviar el header `Authorization: Bearer <Access_Token>` para acceder a estos endpoints.*

| Método | Endpoint | Descripción |
| --- | --- | --- |
| `GET` | `/api/pacientes/` | Lista a todos los pacientes matriculados en la **clínica** a la que pertenece el psicólogo autenticado. |

*(Nota: La API está en curso de desarrollo e incorporación de Endpoints para la creación, actualización y eliminación de recursos orientados a DRF ModelViewSets).*

---

## 🌐 Endpoints y Vistas Web (Aplicación Interna)

La aplicación también cuenta con paneles clásicos renderizados por el servidor para la gestión administrativa:

* `GET` `/` - Dashboard Principal del sistema.
* `GET/POST` `/login/` - Inicio de sesión del personal administrativo.
* `GET` `/logout/` - Cierre de sesión.
* `GET/POST` `/registro-clinica/` - Onboarding de una nueva Clínica (creación de Tenant).
* `GET/POST` `/registro-psicologo/` - Alta de psicólogos para una clínica existente.
* `GET/POST` `/registro-paciente/` - Alta de pacientes gestionados.
* `GET/POST` `/admin/` - Panel superusuario de Django.

---

## 📂 Estructura del Proyecto

* `psicosystem/`: Configuración principal del proyecto (Settings, URLs, Middleware).
* `core/`: Aplicación principal que contiene la lógica de negocio, los modelos Multi-tenant y los serializadores de la API.

---

## 🔧 Instalación y Configuración Local

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/alecaballero17/PsicoSystem_SI2.git
   cd PsicoSystem_SI2
   ```

2. **Crear y activar entorno virtual:**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias necesarias:**
   ```bash
   pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary
   ```

4. **Configurar Base de Datos:**
   * Asegúrate de tener una base de datos en PostgreSQL llamada `db_psicosystem`.
   * Configura las credenciales correctas en el archivo `psicosystem/settings.py`.

5. **Ejecutar Migraciones:**
   ```bash
   python manage.py migrate
   ```

6. **Iniciar Servidor:**
   ```bash
   python manage.py runserver
   ```

---
*Desarrollado por: Alejandro Caballero - Grupo12 SI2*