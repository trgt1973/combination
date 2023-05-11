with open("data.txt") as f:
    numbers = f.readlines()

with open("exit.txt", "w") as f_exit:
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            combined = numbers[i].strip() + numbers[j].strip()
            f_exit.write(combined + "\n")
