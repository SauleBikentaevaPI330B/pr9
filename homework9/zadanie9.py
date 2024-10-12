import re

def parse_email(email):
    pattern = r'([^@]+)@([a-zA-Z0-9.-]+)'
    match = re.match(pattern, email)
    
    if match:
        username = match.group(1)   
        domain = match.group(2)   
        return username, domain
    else:
        return None, None

while True:
    email_input = input("Введите ваш email (или введите 'exit' для выхода): ")
    if email_input.lower() == 'exit':
        print("Выход из программы.")
        break

    username, domain = parse_email(email_input)

    if username and domain:
        print(f"Имя пользователя: {username}")
        print(f"Доменное имя: {domain}")
    else:
        print("Некорректный email. Попробуйте еще раз.")
