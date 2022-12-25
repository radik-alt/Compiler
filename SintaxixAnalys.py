import json
import main as LexicalAnalys

operators = [">", "<", "=", "<=", ">=", "!="]


def recur(i, depth, listlexem):
    list_dicts = []
    while i < len(listlexem):
        if listlexem[i][0] == 1:

            # сложение
            if listlexem[i + 1][1] == "=" and (listlexem[i + 2][0] == 2 or listlexem[i + 2][0] == 1) and \
                    listlexem[i + 3][1] == "+" and (listlexem[i + 4][0] == 2 or listlexem[i + 4][0] == 1):
                list_dicts.append({"class": "addition", "var": listlexem[i][1], "val1": listlexem[i + 2][1], "val2": listlexem[i + 4][1]})
                i += 5

            # вычитание
            elif listlexem[i + 1][1] == "=" and (listlexem[i + 2][0] == 2 or listlexem[i + 2][0] == 1) and \
                    listlexem[i + 3][1] == "-" and (listlexem[i + 4][0] == 2 or listlexem[i + 4][0] == 1):
                list_dicts.append({"class": "subtraction", "var": listlexem[i][1], "val": listlexem[i + 2][1], "val2": listlexem[i + 4][1]})
                i += 5

            # умножение
            elif listlexem[i + 1][1] == "=" and (listlexem[i + 2][0] == 2 or listlexem[i + 2][0] == 1) and \
                 listlexem[i + 3][1] == "*" and (listlexem[i + 4][0] == 2 or listlexem[i + 4][0] == 1):
                list_dicts.append({"class": "multiplication", "var": listlexem[i][1], "val": listlexem[i + 2][1], "val2": listlexem[i + 4][1]})
                i += 5
            # деление
            elif listlexem[i + 1][1] == "=" and (listlexem[i + 2][0] == 2 or listlexem[i + 2][0] == 1) and \
                 listlexem[i + 3][1] == "/" and (listlexem[i + 4][0] == 2 or listlexem[i + 4][0] == 1):
                list_dicts.append({"class": "division", "var": listlexem[i][1], "val": listlexem[i + 2][1], "val2": listlexem[i + 4][1]})
                i += 5
            # присваивание
            elif listlexem[i + 1][1] == "=" and listlexem[i + 2][0] == 2:
                list_dicts.append({"class": "assigment", "var": listlexem[i][1], "val": listlexem[i + 2][1]})
                i += 3

            # инкремент
            elif listlexem[i + 1][1] == "+=" and listlexem[i + 2][0] == 2:
                list_dicts.append({"class": "increment", "var": listlexem[i][1], "val": listlexem[i + 2][1]})
                i += 3

            else:
                print("Ошибка присвоения: " + str(listlexem[i][1]))
                exit()

        elif listlexem[i][1] == "while":
            if (listlexem[i + 1][0] == 1 or listlexem[i + 1][0] == 2) and listlexem[i + 2][1] in operators and (
                    listlexem[i + 3][0] == 1 or listlexem[i + 3][0] == 2) and listlexem[i + 4][1] == ":":
                var1 = listlexem[i + 1][1]
                var2 = listlexem[i + 3][1]
                compare = listlexem[i + 2][1]
                i, depth, mylist = recur(i + 5, depth + 1, listlexem)
                list_dicts.append(
                    {"class": "while", "var1": var1, "var2": var2, "compare": compare, "body": mylist})
            else:
                print("Ошибка объявления цикла while")
                exit()

        if depth > 0:
            if i >= len(listlexem):
                return i, depth, list_dicts
            elif listlexem[i][1] == "tab" and listlexem[i + depth - 1][1] == "tab":
                i += depth

            elif listlexem[i][1] == "tab" and listlexem[i + depth - 1][1] != "tab":
                depth -= 1
                #i += 1
                return i, depth, list_dicts
            elif listlexem[i][1] != "tab":
                depth -= 1
                return i, depth, list_dicts
        if i >= len(listlexem):
            return i, depth, list_dicts


def syntaxis(listlexem):
    file = 'lexem_json.json'
    i, depth, listlexem = recur(0, 0, listlexem)
    with open(file, 'w') as f:
        json.dump(listlexem, f, indent=4)
    print(listlexem)
    return file, listlexem


if __name__ == "__main__":
    syntaxis(LexicalAnalys.lexemeProcess())



