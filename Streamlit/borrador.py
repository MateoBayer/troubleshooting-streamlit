messages = [ {'is_user': True, 'content': 'Hola'}, {'is_user': False, 'content': 'Hola, ¿cómo puedo ayudarte?'} ]

for message in messages:
    role = 'user' if message['is_user'] == True else 'system'
    content = message['content']
    print(f"Role: {role}, Content: {content}")
