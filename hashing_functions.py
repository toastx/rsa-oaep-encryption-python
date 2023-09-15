import base64
from  six import binary_type, text_type
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


PRIVATE_KEY_PATH = "private.key"
PUBLIC_KEY_PATH = "public.key"

def generate_keys()-> bytes:
    random_generator = Random.new().read
    key = RSA.generate(2048, random_generator)
    private= key.exportKey() 
    public = key.publickey().exportKey()

    with open(PRIVATE_KEY_PATH, 'wb') as private_key_file:
        private_key_file.write(private)
    with open(PUBLIC_KEY_PATH, 'wb') as public_key_file:
        public_key_file.write(public)
    
    private_key_file.close()
    public_key_file.close()
    return private, public

def get_public_key()-> str:
    with open(PUBLIC_KEY_PATH, 'r') as _file:
        public_key =  _file.read()
        _file.close()
        return public_key
    

def get_private_key()-> str:
    with open(PRIVATE_KEY_PATH, 'r') as _file:
        private_key =  _file.read()
        _file.close()
        return private_key

def format_data(data)->bytes:
    if isinstance(data, int): #if data is an integer, return binary representation
        return binary_type(data)

    elif isinstance(data, binary_type): #if data is in binary, return the data itself
        return data
    else:
        if isinstance(data, str): #if data is in str format, return the byte representation of it
            return data.encode('utf8')

def encrypt(message)->bytes:
    try:
        public_key = get_public_key() 
        public_key_obj = RSA.import_key(public_key)
        pkcs1_key = PKCS1_OAEP.new(public_key_obj)
        if pkcs1_key.can_encrypt():
            encrypted_message = pkcs1_key.encrypt(format_data(message)) 
            return base64.b64encode(encrypted_message)
        else:
            raise AttributeError
    except AttributeError as e:
        print(f"Unable to encrypt data: {e}")

def decrypt(b64_encoded_encrypted_message)-> str:
        encrypted_message = base64.b64decode(b64_encoded_encrypted_message)
        private_key = get_private_key() 
        private_key_obj = RSA.import_key(private_key)
        pkcs1_key = PKCS1_OAEP.new(private_key_obj)
        decrypted_message = pkcs1_key.decrypt(encrypted_message)
        return text_type(decrypted_message, encoding='utf8')
