import basic

while True:
    text = input('banga > ')
    result, error = basic.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)