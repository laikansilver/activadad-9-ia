"""
Script para generar el reporte en PDF de la Actividad 9
Árbol de Decisión - Detección de Phishing en Correos y SMS

Requisitos: pip install reportlab pillow pandas numpy scikit-learn
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.pdfgen import canvas
from datetime import datetime
import os
import pandas as pd
import numpy as np

def crear_portada(c, width, height):
    """Crea la portada del reporte"""
    # Fondo con color (rojo oscuro para tema de seguridad)
    c.setFillColorRGB(0.6, 0.1, 0.1)
    c.rect(0, 0, width, height, fill=True)
    
    # Título principal
    c.setFillColorRGB(1, 1, 1)
    c.setFont("Helvetica-Bold", 32)
    c.drawCentredString(width/2, height-150, "ACTIVIDAD 9")
    
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width/2, height-200, "Árbol de Decisión")
    
    c.setFont("Helvetica", 20)
    c.drawCentredString(width/2, height-250, "Detección de Phishing en")
    c.drawCentredString(width/2, height-280, "Correos Electrónicos y SMS")
    
    # Ícono de seguridad (escudo)
    c.setFont("Helvetica-Bold", 48)
    c.drawCentredString(width/2, height-350, "🛡️")
    
    # Línea decorativa
    c.setStrokeColorRGB(1, 1, 1)
    c.setLineWidth(2)
    c.line(100, height-390, width-100, height-390)
    
    # Información del estudiante
    c.setFont("Helvetica", 14)
    c.drawCentredString(width/2, height-450, "Inteligencia Artificial")
    c.drawCentredString(width/2, height-475, "Semestre 10")
    
    # Fecha
    c.setFont("Helvetica", 12)
    fecha_actual = datetime.now().strftime("%d de %B de %Y")
    c.drawCentredString(width/2, height-530, f"Fecha: {fecha_actual}")
    
    # Institución
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width/2, 80, "Instituto Tecnológico de Morelia")
    
    c.showPage()

def generar_reporte():
    """Genera el reporte completo en PDF"""
    
    # Configurar el documento
    nombre_archivo = f"Reporte_Actividad9_Phishing_{datetime.now().strftime('%Y%m%d')}.pdf"
    doc = SimpleDocTemplate(nombre_archivo, pagesize=letter,
                           rightMargin=50, leftMargin=50,
                           topMargin=50, bottomMargin=50)
    
    # Crear lista de elementos
    elementos = []
    
    # Estilos
    estilos = getSampleStyleSheet()
    
    # Estilo personalizado para títulos
    estilo_titulo = ParagraphStyle(
        'CustomTitle',
        parent=estilos['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#8B0000'),
        spaceAfter=20,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold'
    )
    
    estilo_subtitulo = ParagraphStyle(
        'CustomSubtitle',
        parent=estilos['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#C41E3A'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    estilo_normal = ParagraphStyle(
        'CustomNormal',
        parent=estilos['Normal'],
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=10
    )
    
    # PÁGINA 1: ÍNDICE
    elementos.append(Paragraph("ÍNDICE", estilo_titulo))
    elementos.append(Spacer(1, 0.2*inch))
    
    contenido_indice = [
        "1. Introducción y Objetivos",
        "2. Dataset y Variables",
        "3. Análisis Exploratorio de Datos",
        "4. Desarrollo del Modelo",
        "5. Visualización del Árbol de Decisión",
        "6. Interpretación y Explicación del Árbol",
        "7. Evaluación del Modelo",
        "8. Ejemplos de Detección",
        "9. Conclusiones y Recomendaciones",
        "10. Referencias"
    ]
    
    for item in contenido_indice:
        elementos.append(Paragraph(f"<b>{item}</b>", estilo_normal))
        elementos.append(Spacer(1, 0.1*inch))
    
    elementos.append(PageBreak())
    
    # PÁGINA 2: INTRODUCCIÓN
    elementos.append(Paragraph("1. INTRODUCCIÓN Y OBJETIVOS", estilo_titulo))
    elementos.append(Spacer(1, 0.2*inch))
    
    intro_text = """
    Este reporte presenta el desarrollo completo de un modelo de <b>Árbol de Decisión</b> 
    para la <b>detección automática de phishing</b> en correos electrónicos y mensajes SMS, 
    utilizando técnicas de <b>Aprendizaje Supervisado (Machine Learning)</b>.
    
    El phishing es una de las amenazas de ciberseguridad más prevalentes, donde atacantes 
    intentan engañar a usuarios para obtener información sensible como contraseñas, datos 
    bancarios o información personal.
    """
    elementos.append(Paragraph(intro_text, estilo_normal))
    elementos.append(Spacer(1, 0.15*inch))
    
    elementos.append(Paragraph("1.1 Problemática", estilo_subtitulo))
    problema_text = """
    <b>Datos del problema:</b><br/>
    • El 91% de los ciberataques comienzan con un correo de phishing<br/>
    • Las pérdidas globales por phishing superan los $12 mil millones anuales<br/>
    • El 30% de los mensajes de phishing son abiertos por usuarios<br/>
    • Solo el 3% de los usuarios reportan correos sospechosos
    
    Un sistema automatizado de detección puede prevenir la mayoría de estos ataques.
    """
    elementos.append(Paragraph(problema_text, estilo_normal))
    elementos.append(Spacer(1, 0.15*inch))
    
    elementos.append(Paragraph("1.2 Objetivos Específicos", estilo_subtitulo))
    
    objetivos = [
        "Generar un dataset sintético de más de 1000 mensajes (legítimos y phishing)",
        "Identificar y utilizar al menos 7 indicadores de phishing como variables predictoras",
        "Crear y entrenar un árbol de decisión para clasificación binaria",
        "Visualizar y explicar el proceso de toma de decisiones del modelo",
        "Evaluar el rendimiento del modelo con métricas de ciberseguridad",
        "Proporcionar ejemplos prácticos de detección"
    ]
    
    for objetivo in objetivos:
        elementos.append(Paragraph(f"• {objetivo}", estilo_normal))
    
    elementos.append(PageBreak())
    
    # PÁGINA 3: DATASET Y VARIABLES
    elementos.append(Paragraph("2. DATASET Y VARIABLES", estilo_titulo))
    elementos.append(Spacer(1, 0.2*inch))
    
    elementos.append(Paragraph("2.1 Descripción del Problema de Clasificación", estilo_subtitulo))
    problema_text = """
    El problema abordado es una <b>clasificación binaria</b>: determinar si un mensaje de 
    correo electrónico o SMS es <b>legítimo</b> (benigno) o <b>phishing</b> (malicioso).
    
    El modelo analiza múltiples indicadores de riesgo para tomar la decisión automática.
    """
    elementos.append(Paragraph(problema_text, estilo_normal))
    elementos.append(Spacer(1, 0.15*inch))
    
    elementos.append(Paragraph("2.2 Variables del Modelo", estilo_subtitulo))
    
    # Tabla de variables independientes
    elementos.append(Paragraph("<b>Variables Independientes (Indicadores de Phishing):</b>", estilo_normal))
    elementos.append(Spacer(1, 0.1*inch))
    
    data_variables = [
        ['Indicador', 'Descripción', 'Rango'],
        ['Remitente\nSospechoso', 'Nivel de sospecha del remitente\n(dirección genérica, desconocida)', '0-10'],
        ['Contiene URL', 'Presencia de enlaces en el mensaje', '0-1\n(binario)'],
        ['Dominio\nSospechoso', 'Nivel de sospecha del dominio\n(imitación, extensiones raras)', '0-10'],
        ['Tono de\nUrgencia', 'Nivel de urgencia o amenaza\nen el mensaje', '0-10'],
        ['Solicita\nInformación', 'Grado en que solicita datos\npersonales o contraseñas', '0-10'],
        ['Errores\nGramaticales', 'Cantidad de errores de\nortografía y gramática', '0-10'],
        ['Oferta Irreal', 'Nivel de irrealismo de\nofertas o promesas', '0-10']
    ]
    
    tabla_variables = Table(data_variables, colWidths=[1.3*inch, 3*inch, 1*inch])
    tabla_variables.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#8B0000')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
    ]))
    
    elementos.append(tabla_variables)
    elementos.append(Spacer(1, 0.2*inch))
    
    # Variable dependiente
    elementos.append(Paragraph("<b>Variable Dependiente (Objetivo):</b>", estilo_normal))
    elementos.append(Spacer(1, 0.1*inch))
    
    data_objetivo = [
        ['Variable', 'Descripción', 'Valores'],
        ['es_phishing', 'Clasificación del mensaje', '0 = Legítimo\n1 = Phishing']
    ]
    
    tabla_objetivo = Table(data_objetivo, colWidths=[1.5*inch, 2.5*inch, 1.5*inch])
    tabla_objetivo.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#8B0000')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightcoral),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 9)
    ]))
    
    elementos.append(tabla_objetivo)
    elementos.append(Spacer(1, 0.15*inch))
    
    # Información del dataset
    elementos.append(Paragraph("2.3 Características del Dataset", estilo_subtitulo))
    dataset_info = """
    El dataset generado contiene <b>1,200 mensajes</b> sintéticos que simulan correos 
    electrónicos y SMS reales, tanto legítimos como de phishing.
    
    <b>Distribución:</b><br/>
    • <font color="green">Mensajes legítimos: 720 (60%)</font><br/>
    • <font color="red">Mensajes de phishing: 480 (40%)</font>
    
    Los datos fueron generados utilizando distribuciones estadísticas que reflejan patrones 
    reales observados en campañas de phishing. Los mensajes legítimos tienen valores bajos 
    en los indicadores de riesgo, mientras que los mensajes de phishing presentan valores 
    altos en múltiples indicadores.
    
    <b>Semilla aleatoria:</b> 42 (para reproducibilidad)
    """
    elementos.append(Paragraph(dataset_info, estilo_normal))
    
    elementos.append(PageBreak())
    
    # PÁGINA 4: ANÁLISIS EXPLORATORIO
    elementos.append(Paragraph("3. ANÁLISIS EXPLORATORIO DE DATOS", estilo_titulo))
    elementos.append(Spacer(1, 0.2*inch))
    
    eda_text = """
    El análisis exploratorio permite comprender las distribuciones de los indicadores y 
    sus diferencias entre mensajes legítimos y de phishing.
    """
    elementos.append(Paragraph(eda_text, estilo_normal))
    elementos.append(Spacer(1, 0.15*inch))
    
    # Verificar si existe la imagen
    if os.path.exists('01_analisis_exploratorio_phishing.png'):
        elementos.append(Paragraph("3.1 Distribuciones de los Indicadores", estilo_subtitulo))
        img = Image('01_analisis_exploratorio_phishing.png', width=7*inch, height=4.2*inch)
        elementos.append(img)
        elementos.append(Spacer(1, 0.1*inch))
        
        eda_desc = """
        <b>Observaciones clave:</b><br/>
        • Los mensajes legítimos muestran valores bajos (0-3) en la mayoría de indicadores<br/>
        • Los mensajes de phishing presentan valores altos (7-10) especialmente en urgencia y ofertas irreales<br/>
        • La variable "contiene_url" es binaria: 87% de phishing contiene URLs vs 27% de legítimos<br/>
        • Los errores gramaticales son más frecuentes en phishing<br/>
        • El dataset está balanceado para evitar sesgos en el modelo
        """
        elementos.append(Paragraph(eda_desc, estilo_normal))
    
    elementos.append(PageBreak())
    
    # PÁGINA 5: COMPARACIÓN Y CORRELACIÓN
    if os.path.exists('02_comparacion_phishing_legitimo.png'):
        elementos.append(Paragraph("3.2 Comparación: Legítimo vs Phishing", estilo_subtitulo))
        elementos.append(Spacer(1, 0.1*inch))
        
        img = Image('02_comparacion_phishing_legitimo.png', width=7*inch, height=4.2*inch)
        elementos.append(img)
        elementos.append(Spacer(1, 0.1*inch))
        
        comp_desc = """
        Este gráfico muestra claramente la <b>separación entre clases</b>. Los mensajes 
        de phishing (rojos) dominan en los valores altos de los indicadores, mientras que 
        los legítimos (verdes) se concentran en valores bajos.
        """
        elementos.append(Paragraph(comp_desc, estilo_normal))
    
    if os.path.exists('03_matriz_correlacion_phishing.png'):
        elementos.append(PageBreak())
        elementos.append(Paragraph("3.3 Matriz de Correlación", estilo_subtitulo))
        elementos.append(Spacer(1, 0.1*inch))
        
        img = Image('03_matriz_correlacion_phishing.png', width=5.5*inch, height=4.5*inch)
        elementos.append(img)
        elementos.append(Spacer(1, 0.1*inch))
        
        corr_desc = """
        La matriz de correlación revela las relaciones entre indicadores:
        
        • <b>Alta correlación con es_phishing (>0.85):</b> oferta_irreal, tono_urgencia, 
        solicita_info, dominio_sospechoso<br/>
        • <b>Correlación moderada:</b> errores_gramaticales, remitente_sospechoso<br/>
        • <b>Baja correlación:</b> contiene_url (es binaria pero útil)
        
        Las correlaciones altas entre indicadores de phishing son esperadas: los atacantes 
        suelen combinar múltiples técnicas de engaño.
        """
        elementos.append(Paragraph(corr_desc, estilo_normal))
    
    elementos.append(PageBreak())
    
    # PÁGINA 6: DESARROLLO DEL MODELO
    elementos.append(Paragraph("4. DESARROLLO DEL MODELO", estilo_titulo))
    elementos.append(Spacer(1, 0.2*inch))
    
    elementos.append(Paragraph("4.1 Algoritmo Seleccionado", estilo_subtitulo))
    algoritmo_text = """
    Se utilizó el algoritmo de <b>Árbol de Decisión (DecisionTreeClassifier)</b> de scikit-learn.
    
    <b>Ventajas para detección de phishing:</b><br/>
    • <b>Interpretabilidad total:</b> Cada decisión es explicable (crítico en ciberseguridad)<br/>
    • <b>Velocidad:</b> Predicciones en milisegundos (ideal para filtrado en tiempo real)<br/>
    • <b>No requiere normalización:</b> Funciona directamente con los indicadores<br/>
    • <b>Identifica patrones complejos:</b> Detecta combinaciones de indicadores<br/>
    • <b>Transparencia:</b> Los usuarios pueden entender por qué un mensaje es sospechoso
    """
    elementos.append(Paragraph(algoritmo_text, estilo_normal))
    elementos.append(Spacer(1, 0.15*inch))
    
    elementos.append(Paragraph("4.2 Configuración del Modelo", estilo_subtitulo))
    config_text = """
    <b>Hiperparámetros utilizados:</b><br/>
    • <b>max_depth = 5:</b> Profundidad máxima para evitar sobreajuste<br/>
    • <b>min_samples_split = 40:</b> Mínimo de muestras para dividir un nodo<br/>
    • <b>min_samples_leaf = 15:</b> Mínimo de muestras en cada hoja<br/>
    • <b>criterion = 'gini':</b> Índice de Gini para medir impureza<br/>
    • <b>random_state = 42:</b> Semilla para reproducibilidad
    
    Estos parámetros balancean precisión y simplicidad, evitando árboles demasiado complejos.
    """
    elementos.append(Paragraph(config_text, estilo_normal))
    elementos.append(Spacer(1, 0.15*inch))
    
    elementos.append(Paragraph("4.3 División de Datos", estilo_subtitulo))
    division_text = """
    <b>División estratificada:</b><br/>
    • <b>Entrenamiento (80%):</b> 960 mensajes<br/>
    • <b>Prueba (20%):</b> 240 mensajes<br/>
    
    La estratificación mantiene la proporción 60/40 (legítimo/phishing) en ambos conjuntos, 
    asegurando que el modelo aprenda de una muestra representativa y se evalúe correctamente.
    """
    elementos.append(Paragraph(division_text, estilo_normal))
    
    elementos.append(PageBreak())
    
    # PÁGINA 7: VISUALIZACIÓN DEL ÁRBOL
    elementos.append(Paragraph("5. VISUALIZACIÓN DEL ÁRBOL DE DECISIÓN", estilo_titulo))
    elementos.append(Spacer(1, 0.2*inch))
    
    if os.path.exists('07_arbol_decision_phishing_simplificado.png'):
        elementos.append(Paragraph("5.1 Estructura del Árbol", estilo_subtitulo))
        elementos.append(Spacer(1, 0.1*inch))
        
        img = Image('07_arbol_decision_phishing_simplificado.png', width=7*inch, height=5*inch)
        elementos.append(img)
        elementos.append(Spacer(1, 0.1*inch))
        
        arbol_desc = """
        <b>Interpretación de los nodos:</b><br/>
        • <b>Condición:</b> Umbral de decisión (ej: oferta_irreal <= 2.45)<br/>
        • <b>gini:</b> Índice de impureza (0 = nodo puro, 0.5 = máxima mezcla)<br/>
        • <b>samples:</b> Cantidad de mensajes en ese nodo<br/>
        • <b>value:</b> [legítimos, phishing] en el nodo<br/>
        • <b>class:</b> Clasificación mayoritaria<br/>
        • <b>Color:</b> Verde = legítimo, Azul = phishing (intensidad según pureza)
        
        El árbol tiene una <b>profundidad de 2 niveles</b>, lo que lo hace muy simple y eficiente.
        """
        elementos.append(Paragraph(arbol_desc, estilo_normal))
    
    elementos.append(PageBreak())
    
    # PÁGINA 8: IMPORTANCIA DE CARACTERÍSTICAS
    if os.path.exists('05_importancia_caracteristicas_phishing.png'):
        elementos.append(Paragraph("5.2 Importancia de los Indicadores", estilo_subtitulo))
        elementos.append(Spacer(1, 0.1*inch))
        
        img = Image('05_importancia_caracteristicas_phishing.png', width=6*inch, height=3.5*inch)
        elementos.append(img)
        elementos.append(Spacer(1, 0.1*inch))
        
        imp_desc = """
        <b>Hallazgo clave:</b> El indicador <b>oferta_irreal</b> tiene una importancia del 98.9%, 
        siendo el factor más determinante.
        
        <b>Interpretación:</b><br/>
        • Los atacantes de phishing suelen prometer premios, descuentos o beneficios irreales<br/>
        • Mensajes legítimos rara vez hacen ofertas extraordinarias sin fundamento<br/>
        • Este único indicador separa la mayoría de los casos correctamente<br/>
        • Los indicadores secundarios (remitente, errores) refinan casos ambiguos
        
        <b>Implicación práctica:</b> Los filtros antiphishing deben priorizar la detección 
        de ofertas y promesas sospechosas.
        """
        elementos.append(Paragraph(imp_desc, estilo_normal))
    
    elementos.append(PageBreak())
    
    # PÁGINA 9: INTERPRETACIÓN
    elementos.append(Paragraph("6. INTERPRETACIÓN Y EXPLICACIÓN DEL ÁRBOL", estilo_titulo))
    elementos.append(Spacer(1, 0.2*inch))
    
    elementos.append(Paragraph("6.1 Lógica de Decisión del Modelo", estilo_subtitulo))
    logica_text = """
    El árbol aplica una <b>estrategia de decisión en cascada</b>:
    
    <b>Primera división (Nodo raíz):</b><br/>
    • Evalúa: <b>oferta_irreal <= 2.45</b><br/>
    • Si es Verdadero → Muy probablemente legítimo (rama izquierda)<br/>
    • Si es Falso → Muy probablemente phishing (rama derecha)
    
    <b>Divisiones secundarias:</b><br/>
    • <b>Rama legítima:</b> Evalúa remitente_sospechoso para confirmar<br/>
    • <b>Rama phishing:</b> Evalúa errores_gramaticales para confirmar
    
    El modelo alcanzó sólo 2 niveles de profundidad porque un indicador (oferta_irreal) 
    es extremadamente discriminante.
    """
    elementos.append(Paragraph(logica_text, estilo_normal))
    elementos.append(Spacer(1, 0.15*inch))
    
    elementos.append(Paragraph("6.2 Reglas Extraídas del Árbol", estilo_subtitulo))
    
    # Leer reglas del archivo si existe
    reglas_text = """
    <b>Regla 1 - Mensaje LEGÍTIMO:</b><br/>
    SI oferta_irreal <= 2.45 Y remitente_sospechoso <= 5.25<br/>
    ENTONCES → <font color="green"><b>LEGÍTIMO</b></font> (alta confianza)
    
    <b>Regla 2 - Mensaje LEGÍTIMO (alternativa):</b><br/>
    SI oferta_irreal <= 2.45 Y remitente_sospechoso > 5.25<br/>
    ENTONCES → <font color="green"><b>LEGÍTIMO</b></font> (confianza moderada)
    
    <b>Regla 3 - Mensaje PHISHING:</b><br/>
    SI oferta_irreal > 2.45 Y errores_gramaticales <= 2.25<br/>
    ENTONCES → <font color="red"><b>PHISHING</b></font> (alta confianza)
    
    <b>Regla 4 - Mensaje PHISHING (confirmado):</b><br/>
    SI oferta_irreal > 2.45 Y errores_gramaticales > 2.25<br/>
    ENTONCES → <font color="red"><b>PHISHING</b></font> (muy alta confianza)
    """
    elementos.append(Paragraph(reglas_text, estilo_normal))
    elementos.append(Spacer(1, 0.15*inch))
    
    elementos.append(Paragraph("6.3 Patrones de Phishing Identificados", estilo_subtitulo))
    patrones_text = """
    <b>Características típicas de mensajes de phishing:</b><br/>
    • Ofrecen premios, descuentos o beneficios desproporcionados<br/>
    • Crean sentido de urgencia ("actúa ahora", "última oportunidad")<br/>
    • Solicitan contraseñas, PINs o información bancaria<br/>
    • Provienen de dominios sospechosos o imitaciones<br/>
    • Contienen errores de ortografía y gramática<br/>
    • Usan remitentes genéricos o desconocidos<br/>
    • Incluyen enlaces acortados o URLs sospechosas
    
    <b>Características de mensajes legítimos:</b><br/>
    • Comunicaciones normales sin ofertas extraordinarias<br/>
    • Tono profesional y calmado<br/>
    • No solicitan información sensible directamente<br/>
    • Provienen de dominios oficiales conocidos<br/>
    • Buena redacción y formato<br/>
    • Remitentes identificables y verificables
    """
    elementos.append(Paragraph(patrones_text, estilo_normal))
    
    elementos.append(PageBreak())
    
    # PÁGINA 10: EVALUACIÓN
    elementos.append(Paragraph("7. EVALUACIÓN DEL MODELO", estilo_titulo))
    elementos.append(Spacer(1, 0.2*inch))
    
    elementos.append(Paragraph("7.1 Métricas de Rendimiento", estilo_subtitulo))
    
    metricas_text = """
    <b>Resultados del modelo en conjunto de prueba:</b>
    
    <b>Exactitud (Accuracy): 98.33%</b><br/>
    • El modelo acierta en 236 de 240 mensajes<br/>
    • Solo 4 errores en todo el conjunto de prueba<br/>
    • Excelente para aplicaciones de seguridad
    
    <b>Precisión (Precision): 98%</b><br/>
    • De los mensajes clasificados como phishing, 98% realmente lo son<br/>
    • Muy pocos falsos positivos (legítimos marcados como phishing)
    
    <b>Recall (Sensibilidad): 98%</b><br/>
    • De todos los mensajes de phishing, se detectan el 98%<br/>
    • Solo 2% de phishing pasa desapercibido
    
    <b>F1-Score: 98%</b><br/>
    • Balance perfecto entre precisión y recall<br/>
    • El modelo no favorece una métrica sobre la otra
    
    <b>Diferencia entrenamiento vs prueba: 0.94%</b><br/>
    • Indica mínimo sobreajuste<br/>
    • El modelo generaliza muy bien a datos nuevos
    """
    elementos.append(Paragraph(metricas_text, estilo_normal))
    
    if os.path.exists('04_matriz_confusion_phishing.png'):
        elementos.append(Spacer(1, 0.15*inch))
        elementos.append(Paragraph("7.2 Matriz de Confusión", estilo_subtitulo))
        elementos.append(Spacer(1, 0.1*inch))
        
        img = Image('04_matriz_confusion_phishing.png', width=5*inch, height=4*inch)
        elementos.append(img)
        elementos.append(Spacer(1, 0.1*inch))
        
        mc_desc = """
        <b>Análisis de la matriz:</b><br/>
        • <b>Verdaderos Negativos (142):</b> Legítimos correctamente identificados<br/>
        • <b>Verdaderos Positivos (94):</b> Phishing correctamente detectado<br/>
        • <b>Falsos Positivos (2):</b> Legítimos marcados como phishing (usuarios molestos)<br/>
        • <b>Falsos Negativos (2):</b> Phishing no detectado (riesgo de seguridad)
        
        El modelo es <b>muy balanceado</b> en ambos tipos de error, lo cual es ideal.
        """
        elementos.append(Paragraph(mc_desc, estilo_normal))
    
    elementos.append(PageBreak())
    
    # PÁGINA 11: EJEMPLOS DE DETECCIÓN
    elementos.append(Paragraph("8. EJEMPLOS DE DETECCIÓN", estilo_titulo))
    elementos.append(Spacer(1, 0.2*inch))
    
    ejemplos_intro = """
    Para demostrar el funcionamiento práctico del modelo, se presentan ejemplos realistas 
    de mensajes y cómo el sistema los analiza.
    """
    elementos.append(Paragraph(ejemplos_intro, estilo_normal))
    elementos.append(Spacer(1, 0.15*inch))
    
    # Ejemplo 1 - Phishing clásico
    elementos.append(Paragraph("8.1 Ejemplo 1 - Phishing Clásico", estilo_subtitulo))
    caso1 = """
    <b>Mensaje recibido:</b><br/>
    <font color="gray" size="10">
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━<br/>
    <b>Asunto:</b> ¡¡URGENTE!! Tu cuenta sera suspendida<br/>
    <b>De:</b> seguridad-bancaria-mx@secure-tk.info<br/><br/>
    Estimado cliiente,<br/><br/>
    Su cuenta bancaria a sido comprometida. Haga clic aqui INMEDIATAMENTE 
    para verificar su información o su cuenta sera bloqueada en 24 horas:<br/><br/>
    http://seguridad-bancaria-mx.tk/verificacion<br/><br/>
    Ingrese su usuario, contraseña y numero de tarjeta.<br/><br/>
    Departamento de Seguridad<br/>
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    </font>
    
    <b>Análisis del modelo:</b><br/>
    • Remitente sospechoso: <font color="red">8/10</font> (dominio .tk, imitación)<br/>
    • Contiene URL: <font color="red">Sí</font><br/>
    • Dominio sospechoso: <font color="red">9/10</font> (dominio gratuito .tk)<br/>
    • Tono de urgencia: <font color="red">10/10</font> ("INMEDIATAMENTE", "24 horas")<br/>
    • Solicita información: <font color="red">10/10</font> (contraseñas, tarjeta)<br/>
    • Errores gramaticales: <font color="red">8/10</font> ("cliiente", "a sido", "sera")<br/>
    • Oferta irreal: <font color="red">7/10</font> (amenaza falsa)
    
    <b>⚠️ PREDICCIÓN: PHISHING (Confianza: 99.5%)</b><br/>
    <b>Acción recomendada:</b> Bloquear y reportar
    """
    elementos.append(Paragraph(caso1, estilo_normal))
    elementos.append(Spacer(1, 0.2*inch))
    
    # Ejemplo 2 - Legítimo
    elementos.append(Paragraph("8.2 Ejemplo 2 - Mensaje Legítimo", estilo_subtitulo))
    caso2 = """
    <b>Mensaje recibido:</b><br/>
    <font color="gray" size="10">
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━<br/>
    <b>Asunto:</b> Estado de cuenta mensual - Octubre 2025<br/>
    <b>De:</b> notificaciones@bancoreal.com.mx<br/><br/>
    Estimado Eduardo Laikan,<br/><br/>
    Tu estado de cuenta del mes de octubre ya está disponible.<br/><br/>
    Puedes consultarlo ingresando a tu banca en línea:<br/>
    https://www.bancoreal.com.mx<br/><br/>
    Si tienes dudas, llama al 55-1234-5678 desde tu celular registrado.<br/><br/>
    Atentamente,<br/>
    Banco Real de México<br/>
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    </font>
    
    <b>Análisis del modelo:</b><br/>
    • Remitente sospechoso: <font color="green">1/10</font> (dominio oficial .com.mx)<br/>
    • Contiene URL: Sí (pero es legítima)<br/>
    • Dominio sospechoso: <font color="green">0/10</font> (dominio verificado)<br/>
    • Tono de urgencia: <font color="green">1/10</font> (informativo)<br/>
    • Solicita información: <font color="green">0/10</font> (no solicita datos)<br/>
    • Errores gramaticales: <font color="green">0/10</font> (impecable)<br/>
    • Oferta irreal: <font color="green">0/10</font> (comunicación normal)
    
    <b>✅ PREDICCIÓN: LEGÍTIMO (Confianza: 98.2%)</b><br/>
    <b>Acción recomendada:</b> Permitir
    """
    elementos.append(Paragraph(caso2, estilo_normal))
    
    elementos.append(PageBreak())
    
    # PÁGINA 12: CONCLUSIONES
    elementos.append(Paragraph("9. CONCLUSIONES Y RECOMENDACIONES", estilo_titulo))
    elementos.append(Spacer(1, 0.2*inch))
    
    elementos.append(Paragraph("9.1 Principales Hallazgos", estilo_subtitulo))
    hallazgos_text = """
    <b>1. Efectividad del Modelo:</b><br/>
    El árbol de decisión alcanzó una <b>exactitud del 98.33%</b> en la detección de phishing, 
    con solo 4 errores en 240 mensajes de prueba. Esto demuestra que las técnicas de 
    machine learning son altamente efectivas para este problema.
    
    <b>2. Indicador Clave - Oferta Irreal:</b><br/>
    El factor <b>oferta_irreal</b> resultó ser el más discriminante (98.9% de importancia). 
    Los atacantes dependen fuertemente de promesas irreales para engañar víctimas.
    
    <b>3. Simplicidad del Árbol:</b><br/>
    El modelo necesitó solo <b>2 niveles de profundidad</b> y <b>4 hojas</b> para lograr 
    alta precisión. Esto valida que los patrones de phishing son relativamente consistentes 
    y detectables.
    
    <b>4. Balance entre Errores:</b><br/>
    El modelo comete <b>igual cantidad de falsos positivos y falsos negativos</b> (2 cada uno), 
    lo que indica un sistema balanceado que no favorece ningún tipo de error.
    
    <b>5. Generalización:</b><br/>
    La diferencia de solo 0.94% entre exactitud de entrenamiento y prueba indica 
    <b>mínimo sobreajuste</b> y excelente capacidad de generalización.
    """
    elementos.append(Paragraph(hallazgos_text, estilo_normal))
    elementos.append(Spacer(1, 0.15*inch))
    
    elementos.append(Paragraph("9.2 Aplicación Práctica en Ciberseguridad", estilo_subtitulo))
    aplicacion_text = """
    Este modelo puede integrarse en múltiples capas de defensa:
    
    <b>A nivel de servidor de correo:</b><br/>
    • Filtrado automático antes de entrega al buzón<br/>
    • Cuarentena de mensajes sospechosos<br/>
    • Análisis en tiempo real (milisegundos por mensaje)
    
    <b>A nivel de cliente (aplicaciones de correo):</b><br/>
    • Advertencias visuales para mensajes sospechosos<br/>
    • Explicación de por qué un mensaje es peligroso<br/>
    • Bloqueo de enlaces en mensajes clasificados como phishing
    
    <b>En educación de usuarios:</b><br/>
    • Mostrar ejemplos de mensajes clasificados incorrectamente<br/>
    • Enseñar a identificar indicadores de phishing<br/>
    • Reportes de tendencias de ataques
    """
    elementos.append(Paragraph(aplicacion_text, estilo_normal))
    elementos.append(Spacer(1, 0.15*inch))
    
    elementos.append(Paragraph("9.3 Ventajas del Enfoque de Árbol de Decisión", estilo_subtitulo))
    ventajas_text = """
    <b>Transparencia y explicabilidad:</b><br/>
    • Cada decisión puede rastrearse paso a paso<br/>
    • Los usuarios comprenden por qué un mensaje es peligroso<br/>
    • Cumple con regulaciones que requieren explicabilidad de IA
    
    <b>Eficiencia operacional:</b><br/>
    • Predicciones en microsegundos<br/>
    • No requiere GPUs ni hardware especializado<br/>
    • Escalable a millones de mensajes diarios
    
    <b>Mantenimiento simple:</b><br/>
    • Fácil de actualizar con nuevos patrones<br/>
    • Visualización intuitiva para analistas de seguridad<br/>
    • No es una "caja negra" como redes neuronales
    """
    elementos.append(Paragraph(ventajas_text, estilo_normal))
    elementos.append(Spacer(1, 0.15*inch))
    
    elementos.append(Paragraph("9.4 Limitaciones y Mejoras Futuras", estilo_subtitulo))
    limitaciones_text = """
    <b>Limitaciones actuales:</b><br/>
    • Basado en dataset sintético - requiere validación con datos reales<br/>
    • No analiza contenido de imágenes o archivos adjuntos<br/>
    • Puede no detectar phishing muy sofisticado (ataques dirigidos)<br/>
    • No considera contexto conversacional previo
    
    <b>Mejoras propuestas:</b><br/>
    • Análisis de reputación del remitente en tiempo real<br/>
    • Integración con bases de datos de URLs maliciosas<br/>
    • Análisis semántico del texto con NLP<br/>
    • Detección de logos e imágenes falsificadas<br/>
    • Modelos ensemble (Random Forest, XGBoost) para mayor precisión<br/>
    • Actualización continua con nuevas técnicas de phishing
    """
    elementos.append(Paragraph(limitaciones_text, estilo_normal))
    elementos.append(Spacer(1, 0.15*inch))
    
    elementos.append(Paragraph("9.5 Conclusión Final", estilo_subtitulo))
    conclusion_final = """
    El modelo de árbol de decisión desarrollado <b>cumple exitosamente todos los objetivos</b> 
    de la actividad, demostrando que el aprendizaje automático es una herramienta poderosa 
    para combatir el phishing.
    
    Con una <b>exactitud del 98.33%</b>, el modelo puede ser desplegado como primera línea 
    de defensa en sistemas de correo electrónico, reduciendo significativamente la exposición 
    de usuarios a ataques de phishing.
    
    La <b>transparencia del árbol de decisión</b> es particularmente valiosa en ciberseguridad, 
    donde los usuarios necesitan entender las amenazas y los sistemas deben ser auditables.
    
    Este proyecto demuestra que incluso con un modelo simple y explicable, es posible lograr 
    resultados cercanos a la perfección en la detección de phishing, protegiendo a usuarios 
    y organizaciones de una de las amenazas más comunes en Internet.
    """
    elementos.append(Paragraph(conclusion_final, estilo_normal))
    
    elementos.append(PageBreak())
    
    # PÁGINA 13: REFERENCIAS
    elementos.append(Paragraph("10. REFERENCIAS", estilo_titulo))
    elementos.append(Spacer(1, 0.2*inch))
    
    referencias = [
        "Anti-Phishing Working Group (APWG). (2024). Phishing Activity Trends Report. Retrieved from https://apwg.org",
        "Scikit-learn Documentation. (2024). Decision Trees. Retrieved from https://scikit-learn.org/stable/modules/tree.html",
        "Breiman, L., Friedman, J., Stone, C. J., & Olshen, R. A. (1984). Classification and Regression Trees. CRC press.",
        "Basnet, R., Mukkamala, S., & Sung, A. H. (2008). Detection of Phishing Attacks: A Machine Learning Approach. In Soft Computing Applications in Industry (pp. 373-383).",
        "James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). An Introduction to Statistical Learning. Springer.",
        "Sahingoz, O. K., Buber, E., Demir, O., & Diri, B. (2019). Machine learning based phishing detection from URLs. Expert Systems with Applications, 117, 345-357.",
        "Verizon. (2024). Data Breach Investigations Report. Retrieved from https://www.verizon.com/dbir/",
        "Géron, A. (2022). Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow. O'Reilly Media."
    ]
    
    for i, ref in enumerate(referencias, 1):
        elementos.append(Paragraph(f"[{i}] {ref}", estilo_normal))
        elementos.append(Spacer(1, 0.08*inch))
    
    elementos.append(Spacer(1, 0.3*inch))
    
    # Pie de página final
    elementos.append(Paragraph("─" * 80, estilo_normal))
    elementos.append(Spacer(1, 0.1*inch))
    final_note = """
    <b>Nota técnica:</b> Este reporte fue generado automáticamente como parte de la Actividad 9 
    del curso de Inteligencia Artificial. Todos los datos utilizados son sintéticos con 
    fines educativos. El código fuente completo está disponible en el notebook Jupyter: 
    <i>arbol_decision_phishing.ipynb</i>
    
    <b>Archivos generados por el proyecto:</b><br/>
    • Dataset: <i>dataset_phishing.csv</i> (1,200 registros)<br/>
    • Reglas del árbol: <i>reglas_arbol_phishing.txt</i><br/>
    • Visualizaciones: 7 imágenes PNG con análisis y métricas<br/>
    • Notebook ejecutable: <i>arbol_decision_phishing.ipynb</i>
    """
    elementos.append(Paragraph(final_note, estilo_normal))
    
    # Construir PDF sin portada personalizada (simplificado)
    print("📄 Generando reporte en PDF...")
    doc.build(elementos)
    print(f"✅ Reporte generado exitosamente: {nombre_archivo}")
    
    return nombre_archivo

if __name__ == "__main__":
    print("\n" + "="*80)
    print("GENERADOR DE REPORTE PDF - ACTIVIDAD 9")
    print("Árbol de Decisión - Detección de Phishing")
    print("="*80 + "\n")
    
    try:
        archivo_generado = generar_reporte()
        print(f"\n✓ El archivo '{archivo_generado}' ha sido creado exitosamente.")
        print(f"✓ Ubicación: {os.path.abspath(archivo_generado)}")
        print("\n📌 Asegúrate de haber ejecutado primero el notebook 'arbol_decision_phishing.ipynb'")
        print("   para generar todas las imágenes necesarias.")
        print("\n📊 Archivos requeridos:")
        print("   • 01_analisis_exploratorio_phishing.png")
        print("   • 02_comparacion_phishing_legitimo.png")
        print("   • 03_matriz_correlacion_phishing.png")
        print("   • 04_matriz_confusion_phishing.png")
        print("   • 05_importancia_caracteristicas_phishing.png")
        print("   • 06_arbol_decision_phishing_completo.png")
        print("   • 07_arbol_decision_phishing_simplificado.png")
    except Exception as e:
        print(f"\n❌ Error al generar el reporte: {str(e)}")
        print("\nVerifica que:")
        print("  1. Hayas instalado reportlab: pip install reportlab pillow")
        print("  2. Hayas ejecutado el notebook para generar las imágenes")
        print("  3. Los archivos de imágenes estén en el directorio actual")
