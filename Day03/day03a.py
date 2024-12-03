EXAMPLE = False
input_path = "example" if EXAMPLE else "input"

NUMBERS = [str(i) for i in range (0, 10)]


def get_input(path):
    input_text = ""
    with open(path, "r") as file:
        for line in file:
            input_text += line
    return input_text


def get_instructions(text):
    template = "mul(*,*)"
    pointer = 0
    index = 0
    num1, num2 = 0, 0
    instructions = []
    while index < len(text):
        c = text[index]
        if pointer == 4 or pointer == 6:
            # number work
            number = ""
            for offset in range(3):
                if text[index + offset] in NUMBERS:
                    number += text[index + offset]
                    if offset == 2:
                        if pointer == 4: num1 = int(number)
                        else: num2 = int(number)
                        index += offset + 1
                        pointer += 1
                        break
                elif text[index + offset] == "," and pointer == 4 and offset != 0:
                    num1 = int(number)
                    index += offset
                    pointer += 1
                    break
                elif text[index + offset] == ")" and pointer == 6 and offset != 0:
                    num2 = int(number)
                    index += offset
                    pointer += 1
                    break
                else:
                    pointer = 0
                    index += offset
                    break

        elif c == template[pointer]:
            # stream matches template
            if pointer == 7:
                # complete instruction, save
                print(f"found instruction mul({num1},{num2})")
                instructions.append((num1, num2))
                pointer = 0
            else: pointer += 1
            index += 1
        else:
            # stream does not match template
            pointer = 0
            index += 1
    return instructions

if __name__ == "__main__":
    text = get_input(f"src/inputA/{input_path}.txt")
    print(sum(map(lambda x: x[0] * x[1], get_instructions(text))))