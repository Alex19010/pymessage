from .models import GroupChat, GroupMessage

from itsdangerous import URLSafeSerializer


serializer = URLSafeSerializer(secret_key='Group_chat')

def encrypt_chat_id(chat_id):
    encrypted = serializer.dumps(chat_id)
    return encrypted

def decrypt_chat_id(encrypted_id):
    try:
        decrypted = serializer.loads(encrypted_id)
        return decrypted
    except Exception as e:
        print("Error", e)
        return None