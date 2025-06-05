import requests
import os
from typing import List, Dict
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

#Msg: (is_user, content)
# Ejemplo: [ {'is_user': True, 'content': 'Hola'}, {'is_user': False, 'content': 'Hola, ¿cómo puedo ayudarte?'} ]

class MGAClient:
    def __init__(self):
        self.api_key = os.getenv('MYGENASSIST_API_KEY')
        self.base_url = 'https://chat.int.bayer.com/api/v2/chat/agent'
        
    async def ask_question_to_assistant(self, messages: List, assistant_id: str) -> str:
        """
        Envía una pregunta al asistente de MGA
        
        Args:
            messages: Lista de mensajes del chat
            assistant_id: ID del asistente
            
        Returns:
            Respuesta del asistente
        """
        if not self.api_key:
            raise ValueError("API Key no configurada")
            
        if not assistant_id:
            raise ValueError("ID del asistente no válido")
            
        try:
            # Formatear mensajes para la API
            formatted_messages = []
            
            for msg in messages:
                formatted_messages.append({
                    'role': 'user' if msg['is_user'] == True else 'system',
                    'content': msg['content']
                })
            
            payload = {
                'messages': formatted_messages,
                'assistant_id': assistant_id,
                'model': 'gpt-4o',
            }
            
            headers = {
                'accept': 'application/json',
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            
            response = requests.post(
                self.base_url,
                json=payload,
                headers=headers,
                timeout=30
            )
            
            if not response.ok:
                st.error(f"Error en la API: {response.status_code}")
                raise Exception(f'API request failed: {response.status_code}')
            
            data = response.json()
            return data['choices'][0]['message']['content']
            
        except Exception as error:
            st.error(f'Error de API: {str(error)}')
            raise error

# Instancia global del cliente
mga_client = MGAClient()