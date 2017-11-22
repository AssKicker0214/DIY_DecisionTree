import random

file = open("./data/mushrooms.csv", encoding='utf-8')
train_file = open("./data/mushroom.train", 'w', encoding='utf-8')
test_file = open("./data/mushroom.test", 'w', encoding='utf-8')

is_first_line = True
for line in file:
    if is_first_line or random.random() > 0.2:
        is_first_line = False
        train_file.write(line)
        # train_file.write("\n")
    else:
        test_file.write(line)
        # test_file.write("\n")