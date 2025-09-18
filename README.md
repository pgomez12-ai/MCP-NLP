# Exploración del Protocolo de Contexto del Modelo (MCP)

Este repositorio contiene una exploración investigativa del **Model Context Protocol (MCP)** y una demostración funcional de comunicación entre agentes de inteligencia artificial. El proyecto se desarrolló en **Visual Studio Code**, utilizando **Python** y el framework **LangChain** para orquestar la comunicación, en conjunto con la **API de Groq** y el modelo **Llama 3 8B**.

---

## Marco de Referencia: Investigación de MCP

El **Model Context Protocol (MCP)** es un estándar diseñado para estandarizar la forma en que los agentes de IA se comunican y comparten contexto de manera eficiente. A diferencia de las interacciones tradicionales de solicitud-respuesta, MCP permite a los agentes operar con un conocimiento compartido y coherente, facilitando la creación de flujos de trabajo más complejos y colaborativos.

La esencia del protocolo radica en la encapsulación de información en un objeto de contexto estructurado, que incluye:

* **`protocol`**: La versión del protocolo.
* **`sender` y `recipient`**: Los identificadores de los agentes involucrados.
* **`context`**: El corazón del protocolo, que contiene el `payload` (los datos relevantes) y los `metadata` (información adicional como un `conversation_id`).

Esta estructura permite a los agentes mantener el estado y la coherencia de una conversación, superando las limitaciones de los modelos sin memoria que tratan cada interacción como un evento aislado.

---

## Demostración Funcional: Plan de Marketing para Redes Sociales

La demostración práctica de este proyecto simula un escenario de colaboración entre dos agentes: un **Agente_Planificador** y un **Agente_Creativo**.

1.  **El Agente_Planificador** (simulado en el código) genera y envía un paquete de contexto MCP con detalles clave de una campaña de marketing.
2.  **El Agente_Creativo** (implementado con LangChain y Groq) recibe este contexto, lo procesa y, basándose en la información, genera un plan de contenido detallado para redes sociales.

Este ejemplo ilustra cómo los agentes, al compartir un contexto estandarizado, pueden colaborar de manera autónoma para generar un producto final de valor, como un plan de marketing.

### Simulacion y Resultado de MCP
```
PS C:\Users\Pedro Gomez\Desktop\Maestria en Ciencia de los Datos y Analitica\+Segundo Semestre\Procesamiento de Lenguaje Natural Aplicado\Trabajos\Cuarto Trabajo> & "C:/Users/Pedro Gomez/AppData/Local/Programs/Python/Python310/python.exe" "c:/Users/Pedro Gomez/Desktop/Maestria en Ciencia de los Datos y Analitica/+Segundo Semestre/Procesamiento de Lenguaje Natural Aplicado/Trabajos/Cuarto Trabajo/demo_mcp.py"
✅ Agente_Planificador (Emisor) crea el contexto MCP.
{'context': {'conversation_id': 'marketing_campaign_2025',
             'metadata': {'timestamp': '2025-09-19T10:00:00Z'},
             'payload': {'campaign_goal': 'Aumentar el engagement en Instagram '
                                          'en un 20% para el próximo '
                                          'trimestre.',
                         'content_types': ['post carrusel', 'reel', 'story'],
                         'instructions': 'Genera un plan de 3 ideas de '
                                         'contenido para Instagram, una por '
                                         'cada tipo de contenido solicitado. '
                                         'Incluye un título y una descripción '
                                         'breve para cada una.',
                         'key_message': 'Hidratación sostenible y con estilo.',
                         'product_name': 'Eco-Botellas Reusables',
                         'target_audience': 'Jóvenes (18-30 años) con interés '
                                            'en la sostenibilidad y el '
                                            'fitness.'}},
 'protocol': 'mcp-v1',
 'recipient': 'Agente_Creativo',
 'sender': 'Agente_Planificador'}
--------------------------------------------------
c:\Users\Pedro Gomez\Desktop\Maestria en Ciencia de los Datos y Analitica\+Segundo Semestre\Procesamiento de Lenguaje Natural Aplicado\Trabajos\Cuarto Trabajo\demo_mcp.py:81: LangChainDeprecationWarning: The class `LLMChain` was deprecated in LangChain 0.1.17 and will be removed in 1.0. Use RunnableSequence, e.g., `prompt | llm` instead.
  chain = LLMChain(llm=chat, prompt=prompt)
🧠 Agente_Creativo (Receptor) procesa el contexto y genera el plan de marketing:
Aquí te presento tres ideas de contenido para la campaña de Instagram:

**Idea 1: Post Carrusel**

**Título:** "5 formas de llevar tu estilo sostenible a la práctica"

**Descripción:** En este post carrusel, mostraremos 5 formas diferentes de utilizar las Eco-Botellas Reusables en diferentes situaciones, como en la playa, en el gimnasio o en un día de trabajo. Cada imagen mostrará una persona utilizando la botella de manera creativa y sostenible, con un texto que destaque la ventaja de utilizar una botella reutilizable.

**Contenido:**

- Imagen 1: Una persona bebiendo agua en la playa con la Eco-Botella Reusable.
- Imagen 2: Una persona llevando la Eco-Botella Reusable al gimnasio.
- Imagen 3: Una persona utilizando la Eco-Botella Reusable en un día de trabajo.
- Imagen 4: Una persona bebiendo té en un parque con la Eco-Botella Reusable.
- Imagen 5: Una persona mostrando su estilo sostenible con la Eco-Botella Reusable en una ciudad.

**Idea 2: Reel**

**Título:** "La verdad sobre las botellas de plástico y cómo puedes hacer la diferencia"

**Descripción:** En este reel, mostraremos la realidad de las botellas de plástico y cómo pueden afectar el medio ambiente. Luego, presentaremos la solución con las Eco-Botellas Reusables y cómo pueden ayudar a reducir el impacto ambiental.

**Contenido:**

- Introducción: Un gráfico que muestra la cantidad de botellas de plástico que se utilizan cada año.
- Secuencia 1: Un video que muestra la producción de botellas de plástico y su impacto en el medio ambiente.
- Secuencia 2: Un video que muestra la producción de las Eco-Botellas Reusables y cómo se pueden reutilizar.
- Conclusión: Un gráfico que muestra la diferencia que se puede hacer al utilizar las Eco-Botellas Reusables.

**Idea 3: Story**

**Título:** "Desafío de hidratación sostenible"

**Descripción:** En este story, invitaremos a nuestros seguidores a unirse al desafío de hidratación sostenible. Les pediremos que compartan sus propias formas de hidratarse de manera sostenible y que utilicen las Eco-Botellas Reusables.

**Contenido:**

- Pregunta: "¿Cómo te hidratas de manera sostenible?"
- Imagen: Una persona bebiendo agua con la Eco-Botella Reusable.
- Botón: "Comparte tu forma de hidratarte de manera sostenible"
- Imagen: Una persona compartiendo su forma de hidratarse de manera sostenible.
- Botón: "Únete al desafío y comparte tus propias formas de hidratarte de manera sostenible"
```

### Requisitos

Para ejecutar la demostración, necesitas:
1.  **Python 3.8+** instalado.
2.  Una cuenta en [Groq Cloud](https://console.groq.com/keys) para obtener una clave de API gratuita.
