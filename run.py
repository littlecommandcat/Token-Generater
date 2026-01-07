import random, base64


數量 = 10  # 換成數量
用戶id = "1234567890"  # 換成用戶id

def generate_token(id:str):
    characs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    characs2 = '01zr'
    id_encoded = base64.b64encode(bytes(id, 'utf-8'))
    base_code = f".X{random.choices(characs2, k=1)}{random.choices(characs, k=4)}.{random.choices(characs, k=27)}"
    random_code = base_code.replace("'", "").replace(",", "").replace("[", "").replace("]", "").replace(" ", "")
    random_token = (id_encoded.decode('utf-8') + random_code).replace("=", "")
    return random_token


for i in range(數量):
    token = generate_token(用戶id)
    print(token)
