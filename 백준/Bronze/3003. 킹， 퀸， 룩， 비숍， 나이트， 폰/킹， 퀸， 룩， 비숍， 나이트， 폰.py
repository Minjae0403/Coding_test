num = input()
num_list = num.split(" ")
answer = []
mapping = {0:1, 1:1, 2:2, 3:2, 4:2, 5:8}
for i in range(len(num_list)):
    answer.append(str(mapping[i]-int(num_list[i])))
answer = " ".join(answer)
print(answer)