# Author: Lucas Gabriel

from base64 import b64encode, b64decode

def open_keys_file(file_name):
    ''' function to open a key type file and returns the keys'''
    try:
        with open(file_name, 'r') as f:
            key1, key2 = f.read().split()
            return int(key1), int(key2)    
    except IOError:
        raise Exception('Error: Chave inválida/Não encontrada.')


def encrypt_text(original_message, public_key_file, encrypted_message_save_file):
    ''' function to encrypt a message
    return the encrypt text and save in a file '''

    if original_message == '':
        raise Exception('Error: Digite o texto para ser criptografado.')
        
    key_e, key_n = open_keys_file(public_key_file)

    # convert the original message to base64
    encode_message = b64encode(original_message.encode()).decode()
    
    # encrypting text
    encrypted_message = ''
    for char in encode_message:
        encrypted_message += f'{((ord(char) ** key_e) % key_n)}.'

    # remove the last "." and convert the encrypted message to base64
    encrypted_message = b64encode(encrypted_message[:-1].encode()).decode()

    # save the encrypted message to a file
    try:
        with open(str(encrypted_message_save_file).strip(), 'w') as file:
            file.write(encrypted_message)  
    except IOError:
        raise Exception('Error: Digite o nome do arquivo aonde deseja salvar o arquivo criptografado.')
    
    return encrypted_message


def decrypt_text(encrypted_text_file, private_key_file, decrypted_message_save_file):
    ''' function to decrypt a message 
    return return the decrypt text and save in a file '''

    key_d, key_n = open_keys_file(private_key_file)

    try:
        with open(str(encrypted_text_file), 'r') as file:
            encrypted_data = file.read()
            
            # get the encrypted data from the string save in the file
            encrypted_data = b64decode(encrypted_data.encode()).decode().split('.')   
    except IOError:
        raise Exception('Error: Arquivo inválida/não encontrado.')

    # decrypt data and get the plain text
    decrypted_message = ''
    for char in encrypted_data:
        decrypted_message += chr((int(char) ** key_d) % key_n)
    
    # decode the decrypted message from base64 back to normal
    try:
        decrypted_message = b64decode(decrypted_message.encode()).decode()
    except:
        raise Exception('Error: Chaves privadas incorretas.')
        
    # save the decrypted message in a file
    try:
        if str(decrypted_message) != '':
            with open(str(decrypted_message_save_file).strip(), 'w') as file:
                file.write(decrypted_message)
        
        else:
            raise Exception('Error: Chaves privadas incorretas.')
    
    except UnicodeError:
        raise Exception('Error: Chaves privadas incorretas.')

    return decrypted_message
