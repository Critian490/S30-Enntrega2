# Amazon Scraper

Un script en Python para realizar scraping de datos estáticos y dinámicos desde Amazon. Este proyecto utiliza las bibliotecas `requests`, `BeautifulSoup` y `Selenium` para extraer información como el nombre del producto, el precio y las reseñas.

---

## 📋 Características

1. **Extracción estática con BeautifulSoup**:
   - Obtiene el nombre y el precio del producto desde el HTML de la página.
   
2. **Extracción dinámica con Selenium**:
   - Extrae reseñas cargadas dinámicamente al interactuar con elementos de la página.

3. **Integración continua (CI)**:
   - Configuración de GitHub Actions para ejecutar pruebas, análisis estático y verificaciones de calidad del código.

---

## 🚀 Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio


project/
├── main.py                   # Código principal del scraper
├── requirements.txt          # Dependencias del proyecto
├── tests/                    # Directorio de pruebas
│   ├── test_static.py
│   └── test_dynamic.py
└── .github/workflows/        # Configuración de GitHub Actions
    └── python-ci.yml
