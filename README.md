# Analizador de CV

Una aplicación web moderna para el análisis de currículos vitae, desarrollada con FastAPI y tecnologías modernas.

## ✨ Nuevas Funcionalidades

### 🔄 Análisis Bilingüe
- Soporte completo para español e inglés
- Detección automática del idioma del CV
- Interfaz de usuario en ambos idiomas

### 💼 Análisis de Compatibilidad Laboral
- Comparación de CV con descripciones de trabajo
- Puntuación de compatibilidad detallada
- Recomendaciones específicas para mejorar el match

### 🎨 Interfaz Mejorada
- Nuevo diseño moderno y responsivo
- Modo claro/oscuro
- Navegación intuitiva entre análisis

## 🚀 Características Principales

- Extracción automática de información de CVs en PDF
- Análisis detallado de habilidades y experiencia
- Recomendaciones personalizadas
- Soporte para múltiples formatos de CV
- Dashboard interactivo con estadísticas

## 🛠️ Tecnologías

- FastAPI
- Jinja2 Templates
- SQLAlchemy
- Spacy & NLTK
- PyPDF2 & pdfplumber

## 📋 Requisitos

- Python 3.8+
- Dependencias listadas en requirements.txt

## 🔧 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/DemetrioReyes/analizador-cv.git

# Instalar dependencias
pip install -r requirements.txt

# Iniciar el servidor
uvicorn main:app --reload
```

## 🌐 Uso

1. Accede a `http://localhost:8000`
2. Sube un CV en formato PDF
3. Selecciona el tipo de análisis deseado:
   - Análisis General
   - Compatibilidad Laboral
4. Revisa los resultados y recomendaciones

## 📊 Tipos de Análisis

### Análisis General
- Extracción de información clave
- Evaluación de habilidades
- Recomendaciones de mejora

### Análisis de Compatibilidad
- Comparación con descripción del puesto
- Puntuación de compatibilidad
- Sugerencias específicas

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📝 Licencia

Este proyecto es libre de explorar

## 📞 Contacto

- Nombre - Demetrio Reyes
- Email - rdemetrio72@yahoo.com
- linkeind: www.linkedin.com/in/demetrio-reyes-martinez-499765341

## Características

- Análisis de compatibilidad con ATS (Applicant Tracking System)
- Detección de habilidades técnicas (Backend y Frontend)
- Evaluación del nivel de experiencia
- Análisis léxico y semántico
- Interfaz web intuitiva para subir y analizar CVs

## Tecnologías Utilizadas

- **Backend**: FastAPI
- **Frontend**: Jinja2 Templates
- **Análisis de PDF**: Python-multipart
- **Estilos**: CSS personalizado

## Funcionalidades Principales

### 1. Análisis de Compatibilidad ATS
- Detección de correo electrónico
- Detección de número telefónico
- Verificación de secciones de educación y experiencia laboral
- Conteo de palabras y páginas

### 2. Análisis de Habilidades
- **Backend**: Python, Java, C#, Node.js, SQL, Django, Flask, AWS, Docker, Kubernetes
- **Frontend**: JavaScript, React, Vue.js, Angular, HTML, CSS, TypeScript, Redux
- **Habilidades Generales**: Git, CI/CD, Agile, TDD, Unit Testing, RESTful APIs, GraphQL

### 3. Evaluación de Experiencia
- Detección automática del nivel (Junior, Mid-level, Senior)
- Análisis de logros medibles
- Verificación de datos numéricos

## Estructura del Proyecto
