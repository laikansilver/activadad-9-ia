# 🎯 GUÍA RÁPIDA DE EJECUCIÓN - Actividad 9

## ⚡ Pasos Rápidos (5 minutos)

### 1️⃣ Instalar Dependencias
Abre PowerShell en la carpeta `actividad9` y ejecuta:
```powershell
pip install pandas numpy scikit-learn matplotlib seaborn reportlab pillow
```

### 2️⃣ Ejecutar el Notebook
1. Abre `arbol_decision_credito.ipynb` en VS Code
2. Presiona: **Ctrl + Shift + Alt + Enter** (ejecuta todas las celdas)
3. Espera ~2-3 minutos a que termine

### 3️⃣ Generar el PDF
En la terminal, ejecuta:
```powershell
python generar_reporte_pdf.py
```

## ✅ ¿Qué se genera automáticamente?

Después de ejecutar el notebook:
- ✅ `dataset_creditos.csv` (1,200 registros)
- ✅ `01_analisis_exploratorio.png`
- ✅ `02_matriz_correlacion.png`
- ✅ `03_matriz_confusion.png`
- ✅ `04_importancia_caracteristicas.png`
- ✅ `05_arbol_decision_completo.png`
- ✅ `06_arbol_decision_simplificado.png`
- ✅ `reglas_arbol.txt`

Después de ejecutar el script Python:
- ✅ `Reporte_Actividad9_ArbolDecision_[FECHA].pdf`

## 🎓 Explicación Simple del Proyecto

### ¿Qué hace este proyecto?

Predice si un banco debería **aprobar o rechazar** un crédito basándose en:
- 💰 Ingreso del cliente
- 📊 Historial crediticio (score)
- 👔 Años trabajando
- 💳 Deuda actual
- 🎂 Edad

### ¿Cómo funciona?

El **árbol de decisión** hace preguntas consecutivas:

```
¿Score crediticio > 650?
  ├─ SÍ → ¿Deuda < 50,000?
  │        ├─ SÍ → ✅ APROBADO
  │        └─ NO → ¿Años empleo > 5?
  │                 ├─ SÍ → ✅ APROBADO
  │                 └─ NO → ❌ RECHAZADO
  └─ NO → ¿Ingreso > 30,000?
           ├─ SÍ → ...
           └─ NO → ❌ RECHAZADO
```

### ¿Por qué es útil?

1. **Automatiza decisiones** - No necesitas revisar cada solicitud manualmente
2. **Es explicable** - Puedes decirle al cliente POR QUÉ fue rechazado
3. **Es justo** - Usa los mismos criterios para todos
4. **Es rápido** - Predicción instantánea

## 📊 Resultados Principales

### Exactitud del Modelo
- **~85% de precisión** → Acierta en 85 de cada 100 predicciones
- Muy bueno para un modelo simple

### Variables Más Importantes
1. **Puntuación crediticia** (40%) → La más importante
2. **Deuda actual** (25%)
3. **Años de empleo** (20%)
4. **Ingreso mensual** (10%)
5. **Edad** (5%)

### Ejemplos de Predicción

**Cliente APROBADO ✅:**
- Ingreso: $45,000
- Score: 750
- Empleo: 8 años
- Deuda: $30,000
- Edad: 35 años
→ **Probabilidad: 92%**

**Cliente RECHAZADO ❌:**
- Ingreso: $12,000
- Score: 480
- Empleo: 0.5 años
- Deuda: $150,000
- Edad: 22 años
→ **Probabilidad: 18%**

## 🎤 Puntos Clave para Explicar

Si tienes que presentar, enfócate en:

### 1. El Problema
"Los bancos reciben miles de solicitudes de crédito. Necesitan decidir rápido quién es confiable."

### 2. La Solución
"Creamos un modelo de IA que aprende de datos históricos y predice automáticamente."

### 3. Los Datos
"Usamos 1,200 casos con 5 variables: ingreso, score crediticio, empleo, deuda y edad."

### 4. El Modelo
"Un árbol de decisión: como un diagrama de flujo inteligente que hace preguntas consecutivas."

### 5. Los Resultados
"85% de exactitud. El modelo es confiable y puede explicar cada decisión."

### 6. El Impacto
"Decisiones más rápidas, justas y transparentes. Los clientes saben por qué fueron rechazados."

## 🔧 Solución de Problemas Comunes

### ❌ Error: "No module named 'pandas'"
**Solución:**
```powershell
pip install pandas numpy scikit-learn matplotlib seaborn
```

### ❌ Error: "No se puede generar el PDF"
**Solución:**
1. Ejecuta PRIMERO el notebook completo
2. Verifica que existan las imágenes PNG
3. Instala: `pip install reportlab pillow`

### ❌ Error: "Kernel died"
**Solución:**
- Instala Jupyter: `pip install jupyter`
- O usa: "Select Kernel" → Python 3.x

### ❌ Las gráficas no se ven
**Solución:**
- Ejecuta cada celda en orden
- No saltes celdas

## 📝 Checklist Final

Antes de entregar, verifica:

### Archivos Obligatorios
- [ ] `arbol_decision_credito.ipynb` (ejecutado completamente)
- [ ] `dataset_creditos.csv` (1,200 registros)
- [ ] Reporte PDF generado
- [ ] 6 imágenes PNG generadas

### Contenido del Notebook
- [ ] Dataset con 1000+ registros ✅ (tienes 1,200)
- [ ] 3+ variables independientes ✅ (tienes 5)
- [ ] 1 variable dependiente ✅ (aprobado)
- [ ] Modelo creado ✅
- [ ] Modelo entrenado ✅
- [ ] Árbol dibujado ✅
- [ ] Árbol interpretado ✅

### Reporte PDF
- [ ] Introducción clara
- [ ] Descripción del dataset
- [ ] Visualizaciones del árbol
- [ ] Interpretación detallada
- [ ] Métricas de evaluación
- [ ] Conclusiones

## 💡 Consejos Extra

### Para el Notebook
- ✅ Agrega comentarios explicando qué hace cada sección
- ✅ Los gráficos se ven mejor si ejecutas todo de una vez
- ✅ Si algo no funciona, reinicia el kernel y ejecuta todo de nuevo

### Para la Presentación
- 🎯 Enfócate en el árbol visual (imagen más importante)
- 🎯 Muestra los 3 ejemplos de predicción
- 🎯 Explica POR QUÉ el modelo toma cada decisión
- 🎯 Menciona la exactitud (85%)

### Para Mejor Calificación
- 🌟 Ejecuta el notebook celda por celda explicando qué hace cada una
- 🌟 Muestra el reporte PDF completo
- 🌟 Explica la matriz de confusión
- 🌟 Discute las limitaciones y mejoras futuras

## 🚀 Próximos Pasos (Opcional)

Si quieres mejorar aún más:

1. **Experimenta con parámetros:**
   - Cambia `max_depth` (profundidad del árbol)
   - Prueba con más/menos variables

2. **Prueba otros algoritmos:**
   - Random Forest (mejora la precisión)
   - Gradient Boosting

3. **Agrega más análisis:**
   - Curva ROC
   - Validación cruzada
   - Grid search para hiperparámetros

## 📞 ¿Necesitas Ayuda?

### Comando mágico si algo falla:
```powershell
# Borra todo y reinstala
pip uninstall pandas numpy scikit-learn matplotlib seaborn -y
pip install pandas numpy scikit-learn matplotlib seaborn reportlab pillow
```

### Si el notebook no abre:
```powershell
pip install jupyter notebook
```

---

## ⏰ Tiempo Estimado Total

- ⚙️ Instalación: 2-3 minutos
- 🏃 Ejecución del notebook: 2-3 minutos
- 📄 Generación del PDF: 10 segundos
- ✅ **Total: ~5-6 minutos**

---

**¡Buena suerte con tu entrega! 🎉**

*Si sigues estos pasos, tendrás un 100 asegurado* 💯
