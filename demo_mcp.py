from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from pprint import pprint

# Carga las variables del archivo .env
load_dotenv()

# 1. Configuración de la API de Groq y del LLM
try:
    groq_api_key = os.environ["GROQ_API_KEY"]
except KeyError:
    print("Error: La variable de entorno 'GROQ_API_KEY' no está configurada.")
    print("Por favor, configúrala antes de ejecutar el script.")
    exit()

chat = ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name="llama-3.1-8b-instant")

# 2. Creación del "Contexto MCP" (simulación)
mcp_context = {
    "protocol": "mcp-v1",
    "sender": "Agente_Planificador",
    "recipient": "Agente_Creativo",
    "context": {
        "conversation_id": "marketing_campaign_2025",
        "metadata": {
            "timestamp": "2025-09-19T10:00:00Z"
        },
        "payload": {
            "campaign_goal": "Aumentar el engagement en Instagram en un 20% para el próximo trimestre.",
            "product_name": "Eco-Botellas Reusables",
            "target_audience": "Jóvenes (18-30 años) con interés en la sostenibilidad y el fitness.",
            "key_message": "Hidratación sostenible y con estilo.",
            "content_types": ["post carrusel", "reel", "story"],
            "instructions": "Genera un plan de 3 ideas de contenido para Instagram, una por cada tipo de contenido solicitado. Incluye un título y una descripción breve para cada una."
        }
    }
}

print("✅ Agente_Planificador (Emisor) crea el contexto MCP.")
pprint(mcp_context)
print("-" * 50)

# 3. Simulación del Agente Receptor con LangChain
# Extraemos la información relevante del contexto para el prompt.
goal = mcp_context['context']['payload']['campaign_goal']
product = mcp_context['context']['payload']['product_name']
audience = mcp_context['context']['payload']['target_audience']
message = mcp_context['context']['payload']['key_message']
content_types = ", ".join(mcp_context['context']['payload']['content_types'])
instructions = mcp_context['context']['payload']['instructions']

# Definimos la plantilla del prompt para el Agente Receptor
prompt_template = """
Eres un especialista en marketing digital. Tu tarea es generar ideas de contenido para una campaña de redes sociales.
Basado en la siguiente información de la campaña:
- Objetivo: {goal}
- Producto: {product}
- Audiencia objetivo: {audience}
- Mensaje clave: {message}

{instructions}
Los tipos de contenido solicitados son: {content_types}

Formato de respuesta:
Título de la Idea 1:
Descripción:
---
Título de la Idea 2:
Descripción:
---
Título de la Idea 3:
Descripción:
---
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["goal", "product", "audience", "message", "instructions", "content_types"])

# Creamos la cadena (Chain) que conectará el prompt con el LLM
chain = LLMChain(llm=chat, prompt=prompt)

# Ejecutamos la cadena con la información extraída del contexto MCP
response = chain.invoke(
    {
        "goal": goal,
        "product": product,
        "audience": audience,
        "message": message,
        "instructions": instructions,
        "content_types": content_types
    }
)

# 4. Impresión de la respuesta del Agente Receptor
print("🧠 Agente_Creativo (Receptor) procesa el contexto y genera el plan de marketing:")
print(response['text'])
