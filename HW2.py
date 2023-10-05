# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

def main():
    input_file = open("input.txt", "r")
    output_file = open("output.txt", "w")
    line = input_file.readline().split(' ')
    n, m = int(line[0]), int(line[1])
    for i in range(1, min(n, m) + 1):
        for j in range(1, min(n, m) + 1):
            if i + j == n and i * j == m:
                ansq = i
                answ = j

    output_file.write(str(min(ansq, answ)) + " " + str(max(ansq, answ)) + "\n")


if __name__ == "__main__":
    main()