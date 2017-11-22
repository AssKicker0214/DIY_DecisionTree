import pickle

from DecisionTree.DecisionTree import DecisionTree


def train():
    file = open('./data/mushroom.train', encoding='utf-8')
    header = None
    targets = []
    features = []
    cnt = 0
    for line in file:
        line = line.strip()
        if header is None:
            header = line.split(",")
            del header[0]
            print(header)
        else:
            class_and_features = line.split(",")
            feature = []
            isTarget = True
            for item in class_and_features:
                if isTarget:
                    targets.append(item)
                    isTarget = False
                else:
                    feature.append(item)
            features.append(feature)

            # cnt += 1
            # if cnt > 100:
            #     break

    decision_tree = DecisionTree()
    root_node = decision_tree.fit(features, targets, header)
    root_node.make_html("./data/MushroomDecisionTree.html")
    root_node.save()


def test():
    file = open('./data/model.m', 'rb')
    node_array = pickle.load(file, encoding='utf-8')
    root = node_array[0]
    root.make_html("./data/loaded_MushroomDecisionTree.html")
    stub = root.children[0]

    test_file = open('./data/mushroom.test')
    features = []
    targets = []
    for line in test_file:
        line = line.strip()
        class_and_features = line.split(",")
        feature = []
        is_target = True
        for item in class_and_features:
            if is_target:
                targets.append(item)
                is_target = False
            else:
                feature.append(item)
        features.append(feature)

    total = 0
    bingo = 0.0
    for feature in features:
        print("feature:")
        print(feature)
        pre = stub.decide(feature)
        actual = targets[total]
        print("predict:" + str(pre))
        print("actual:" + actual)
        total += 1
        if pre == actual:
            bingo += 1.

    print("accuracy: %f" % (bingo/total))


test()
# train()
