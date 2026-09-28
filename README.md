# 🐼 Proyecto: Sistema de Gestión - Restaurante App (Semana 15)

## 📌 Membrete Institucional
* **Universidad:** Universidad Estatal Amazónica (UEA) / Universidad Técnica del Norte (UTN)
* **Estudiante:** Xavier Alexander Valencia Rodriguez
* **Carrera:** Ingeniería en Tecnologías de la Información (Modalidad en Línea)
* **Asignatura / Módulo:** Programación / Desarrollo de Software
* **Fecha:** Septiembre 2026

========================================================================================================================================================================

## 🚀 Resumen de Cambios Recientes (Actualización Semana 15)
En esta fase del proyecto se han implementado mejoras fundamentales en la arquitectura modular y la experiencia de usuario:
- **Módulo de Ventas Integrado:** Se añadió la lógica de negocio para gestionar y registrar transacciones de venta de manera eficiente.
- **Persistencia de Datos en JSON:** Conexión robusta entre el servicio de archivos (`ArchivoServicio`) y los repositorios locales (`usuarios.json`, `productos.json`, `ventas.json`) para garantizar que la información no se pierda al cerrar el sistema.
- **Interfaz Gráfica Interactiva (Tkinter & Pillow):** Optimización de la ventana principal (`MainView`) incorporando menús desplegables (`ttk.Combobox`) sincronizados con los datos del sistema, gestión de eventos mediante comandos y renderizado de recursos gráficos institucionales y personalizados.

========================================================================================================================================================================

## 🎨 Detalles del Diseño y Personalización
El diseño visual e interfaz de esta aplicación ha sido conceptualizado bajo los siguientes criterios de originalidad y autoría:
- **Asistencia Tecnológica:** Se utilizó inteligencia artificial como herramienta de apoyo y consulta para optimizar la estructura del código, depurar errores de lógica en Python y estructurar los componentes visuales de la interfaz.
- **Identidad Personal:** Se integró la temática de un **panda** (animal favorito del autor) dentro de los elementos visuales y el logotipo (`assets/logo.png`) para darle un sello único al software.
- **Autoría Verificable:** Se incorporaron las iniciales de la universidad y marcas de agua/detalles personales en el diseño gráfico para certificar y corroborar que la autoría de la maquetación y la implementación final pertenecen enteramente al estudiante Xavier Alexander Valencia Rodriguez.

========================================================================================================================================================================

restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── assets/                  (obligatorio: íconos, logo/logotipo y recursos visuales)
├── main.py
└── README.md 

========================================================================================================================================================================

USUARIO: Xavichi
CONTRASEÑA: contraseñaxd