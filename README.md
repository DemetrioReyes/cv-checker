# Analizador de CV

Una aplicación web para el análisis de currículos vitae, desarrollada con FastAPI para Realizar Varios Analisis de tu CV.

## ✨ Nuevas Funcionalidades

### 🔄 Análisis Bilingüe
- Soporte completo para español e inglés
- Detección automática del idioma del CV
- Interfaz de usuario en ambos idiomas

### 💼 Análisis de Compatibilidad Laboral
- Comparación de CV con descripciones del puesto a Solicitar
- Puntuación de compatibilidad detallada
- Indicaciones sobre que falta en tu Cv para alcanzar el 100%

### 🎨 Interfaz Mejorada
- Nuevo diseño moderno y responsivo
- Modo claro/oscuro
- Navegación intuitiva entre análisis

## 🚀 Características Principales

- Extracción automática de información de CVs en PDF
- Analisis de Tu Cv te da un score segun las tecnologias Actuales y las que tienes en tu CV
- Evaluacion de un CV con la descripcion de un puesto al cual deseas aplicar

## 🛠️ Tecnologías
- **Backend**: FastAPI
- **Frontend**: Jinja2 Templates
- **Análisis de PDF**: Python-multipart
- **Estilos**: CSS personalizado

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

## 📞 Desarrollado por:

- Nombre - Demetrio Reyes
- Email - rdemetrio72@yahoo.com
- linkeind: www.linkedin.com/in/demetrio-reyes-martinez-499765341
