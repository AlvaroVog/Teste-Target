def inverter_string(string):
    inverted_string = ""
    for i in range(len(string) - 1, -1, -1):
        inverted_string += string[i]
    return inverted_string

def main():
    string = input("Digite uma string para inverter: ")
    string_invertida = inverter_string(string)
    print("String original:", string)
    print("String invertida:", string_invertida)

if __name__ == "__main__":
    main()
