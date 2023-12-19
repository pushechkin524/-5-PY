

def inp(query: str, type: str, choices: list = None, constraint: int= None):
    answer = None
    if type == "str":
        while answer == None:
            response = input(query).strip()
            if len(response) != 0:
                if constraint:
                    if len(response) < constraint:
                        answer = response
                    else:
                        print(f"Ответ должен быть < {constraint}")
                else:
                    answer = response
            else:
                print("Ответ не может быть пустым")
    if type == "int":
        while answer == None:
            try:
                response = int(input(query).strip())
                if choices:
                    if response not in choices:
                        print(f"Ответ должен быть в {choices}")
                if response < 0:
                    print("Ответ должен быть > 0")
                else:
                    answer = response
            except:
                print("Ответ должен быть числом")
    return answer






