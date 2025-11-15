# Actividad 9: Árbol de Decisión - Predicción de Créditos Bancarios

## 📋 Descripción del Proyecto

Este proyecto implementa un **modelo de árbol de decisión** usando **aprendizaje supervisado (Machine Learning)** para predecir la aprobación de créditos bancarios basándose en características financieras y personales de los solicitantes.

## 🎯 Objetivos Cumplidos

✅ **Dataset**: 1,200 registros generados (supera los 1,000 requeridos)  
✅ **Variables independientes**: 5 variables (supera las 3 requeridas)
- Ingreso mensual
- Puntuación crediticia
- Años de empleo
- Deuda actual
- Edad

✅ **Variable dependiente**: Aprobación del crédito (0 = Rechazado, 1 = Aprobado)  
✅ **Modelo creado y entrenado**: Decision Tree Classifier  
✅ **Árbol visualizado**: Múltiples visualizaciones generadas  
✅ **Interpretación completa**: Reglas y patrones explicados  
✅ **Reporte PDF**: Documento completo con hallazgos principales

## 📁 Estructura de Archivos

```
actividad9/
│
├── arbol_decision_credito.ipynb          # Notebook principal con todo el código
├── generar_reporte_pdf.py                # Script para generar el reporte PDF
├── README.md                             # Este archivo (instrucciones)
│
├── dataset_creditos.csv                  # Dataset generado (se crea al ejecutar)
├── reglas_arbol.txt                      # Reglas del árbol en texto
│
├── 01_analisis_exploratorio.png          # Visualizaciones generadas:
├── 02_matriz_correlacion.png
├── 03_matriz_confusion.png
├── 04_importancia_caracteristicas.png
├── 05_arbol_decision_completo.png
└── 06_arbol_decision_simplificado.png
```

## 🚀 Instrucciones de Uso

### Paso 1: Instalar Dependencias

Abre una terminal en la carpeta `actividad9` y ejecuta:

```powershell
pip install pandas numpy scikit-learn matplotlib seaborn reportlab pillow
```

### Paso 2: Ejecutar el Notebook

1. Abre **VS Code**
2. Abre el archivo `arbol_decision_credito.ipynb`
3. Ejecuta **todas las celdas** en orden (Ctrl + Shift + Alt + Enter)
   - O ejecuta celda por celda para ver el progreso

Esto generará:
- El dataset (`dataset_creditos.csv`)
- Todas las visualizaciones (archivos PNG)
- Las reglas del árbol (`reglas_arbol.txt`)
- El modelo entrenado

### Paso 3: Generar el Reporte PDF

Una vez que hayas ejecutado TODO el notebook, ejecuta:

```powershell
python generar_reporte_pdf.py
```

Esto creará un archivo PDF con nombre:
```
Reporte_Actividad9_ArbolDecision_YYYYMMDD.pdf
```

## 📊 Contenido del Notebook

El notebook está organizado en las siguientes secciones:

1. **Importación de librerías** - Configuración inicial
2. **Generación del dataset** - 1,200 registros sintéticos realistas
3. **Análisis exploratorio (EDA)** - Visualización de distribuciones
4. **Preparación de datos** - División entrenamiento/prueba (80/20)
5. **Creación del modelo** - Árbol de decisión configurado
6. **Entrenamiento** - Ajuste del modelo con datos de entrenamiento
7. **Evaluación** - Métricas de rendimiento (exactitud, precisión, recall)
8. **Visualización del árbol** - Múltiples representaciones gráficas
9. **Interpretación** - Reglas y patrones identificados
10. **Ejemplos de predicción** - Casos prácticos demostrados
11. **Análisis de caminos** - Cómo el modelo toma decisiones
12. **Resumen final** - Hallazgos y conclusiones

## 📈 Resultados Esperados

- **Exactitud del modelo**: ~85%
- **Profundidad del árbol**: 5 niveles
- **Variable más importante**: Puntuación crediticia
- **Archivos generados**: 8+ (dataset, imágenes, reglas, reporte PDF)

## 🔍 Interpretación del Árbol

El modelo sigue una lógica jerárquica:

1. **Primera división**: Evalúa la **puntuación crediticia**
2. **Divisiones secundarias**: Considera **deuda** y **años de empleo**
3. **Factores adicionales**: **Ingreso** y **edad** en casos específicos

### Patrones Identificados

**✅ Alta probabilidad de aprobación:**
- Score crediticio > 700
- Relación deuda/ingreso < 30%
- Años de empleo > 5

**❌ Alta probabilidad de rechazo:**
- Score crediticio < 550
- Deuda muy alta vs. ingresos
- Poca antigüedad laboral

## 🎨 Visualizaciones Incluidas

1. **Análisis exploratorio**: Distribuciones de todas las variables
2. **Matriz de correlación**: Relaciones entre variables
3. **Matriz de confusión**: Rendimiento del modelo
4. **Importancia de características**: Variables más influyentes
5. **Árbol completo**: Visualización detallada de todos los nodos
6. **Árbol simplificado**: Vista más clara para presentaciones

## 📄 Reporte PDF

El reporte incluye:

- ✅ Portada profesional
- ✅ Índice de contenidos
- ✅ Introducción y objetivos
- ✅ Descripción del dataset y variables
- ✅ Análisis exploratorio con gráficos
- ✅ Desarrollo del modelo
- ✅ Visualización del árbol
- ✅ Interpretación detallada
- ✅ Evaluación con métricas
- ✅ Ejemplos de predicción
- ✅ Conclusiones y hallazgos
- ✅ Referencias

## 💡 Ventajas del Árbol de Decisión

1. **Interpretable**: Fácil de entender y explicar
2. **Transparente**: Se puede rastrear cada decisión
3. **No requiere normalización**: Funciona con datos en escala original
4. **Versátil**: Maneja variables numéricas y categóricas
5. **Identifica automáticamente**: Las características más importantes

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**
- **Pandas**: Manipulación de datos
- **NumPy**: Operaciones numéricas
- **Scikit-learn**: Algoritmo de ML
- **Matplotlib & Seaborn**: Visualizaciones
- **ReportLab**: Generación de PDF

## 📅 Fechas de Entrega

- **Lunes 17 de noviembre**: 100% de calificación
- **Martes 18 de noviembre**: 80% de calificación

## ⚠️ Notas Importantes

1. **Ejecuta TODO el notebook primero** antes de generar el PDF
2. Las imágenes deben existir para que el PDF se genere correctamente
3. Si hay errores, verifica que todas las librerías estén instaladas
4. El dataset es sintético pero realista para fines educativos

## 🎓 Aprendizajes Clave

Este proyecto demuestra:
- Generación de datasets sintéticos realistas
- Implementación completa de un modelo de ML supervisado
- Evaluación rigurosa con múltiples métricas
- Interpretabilidad de modelos de IA
- Documentación profesional de proyectos de ciencia de datos

## 📞 Solución de Problemas

**Error: Módulo no encontrado**
```powershell
pip install [nombre_del_modulo]
```

**Error: No se encuentran las imágenes**
- Ejecuta TODAS las celdas del notebook primero

**Error: El PDF no se genera**
- Verifica: `pip install reportlab pillow`
- Asegúrate de que las imágenes existan

## ✅ Checklist de Entrega

Antes de entregar, verifica que tengas:

- [ ] Notebook ejecutado completamente
- [ ] Dataset CSV generado
- [ ] 6 imágenes PNG generadas
- [ ] Archivo de reglas TXT generado
- [ ] Reporte PDF generado
- [ ] Todos los archivos en la carpeta `actividad9`

---

**¡Proyecto completado con éxito! 🎉**

*Desarrollado para el curso de Inteligencia Artificial - Semestre 10*  
*Instituto Tecnológico de Morelia*
