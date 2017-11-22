import math

from DecisionTree.DecisionTreeNode import DecisionTreeNode


class DecisionTree:
    def __init__(self, selection_method='InformationGain'):
        self.decision_tree_root = None
        self.features = None
        self.targets = None
        self.attr_names = None
        if selection_method == 'InformationGain':
            self.selection_method = InfoGain()
        pass

    def fit(self, features, targets, attr_names):
        self.features = features
        self.targets = targets
        self.attr_names = attr_names

        #
        attr_indices = []
        for i in range(len(features[0])):
            attr_indices.append(i)
            i += 1

        splitting_feature_indices = []
        training_size = 0
        for i in range(len(features)):
            splitting_feature_indices.append(i)
            i += 1
            training_size += 1

        self.decision_tree_root = DecisionTreeNode("(root)", -1, training_size)
        self.__split(splitting_feature_indices, attr_indices, self.decision_tree_root, 0)
        return self.decision_tree_root

    def __split(self, splitting_feature_indices, candidate_attr_indices, parent_node, deep, choice=""):
        print("=============%d============"%deep)
        print(parent_node.name)
        print(candidate_attr_indices)
        pure_class = self.__pure_class(splitting_feature_indices)
        if len(candidate_attr_indices) == 0:
            print("No attribute to split")
            classes = {}
            total = 0.0
            for i in splitting_feature_indices:
                total += 1
                c = self.targets[i]
                if c in classes:
                    classes[c] += 1
                else:
                    classes[c] = 1

            for c, cnt in classes.items():
                parent_node.add_child(DecisionTreeNode(c, -1, cnt/total, choice))
                # parent_node.add_child(DecisionTreeNode("%s#%d" % (self.targets[i], i), 0))
        elif pure_class is not None:
            print("No need to split, pure enough: " + str(pure_class))
            parent_node.add_child(DecisionTreeNode(str(pure_class), -1, 1, choice))
            # for i in splitting_feature_indices:
            #     parent_node.add_child(DecisionTreeNode("%s#%d" % (self.targets[i], i), 0))
        else:
            splitting_attr_index, gain = self.__select_attribute(candidate_attr_indices)
            splitting_node = DecisionTreeNode(str(self.attr_names[splitting_attr_index]), splitting_attr_index, gain, choice)
            parent_node.add_child(splitting_node)
            # candidate_attr_indices = candidate_attr_indices.remove(splitting_attr_index)

            # remove already used attribute
            left_attr_indices = []
            for index in candidate_attr_indices:
                if index != splitting_attr_index:
                    left_attr_indices.append(index)
                else:
                    print("remove:" + str(index))

            # make subtrees
            subtrees = {}
            for i in splitting_feature_indices:
                splitting_attr_value = self.features[i][splitting_attr_index]
                if splitting_attr_value in subtrees:
                    subtrees[splitting_attr_value].append(i)
                else:
                    subtrees[splitting_attr_value] = [i]

            # split subtrees separately
            for attr_value, subtree_feature_indices in subtrees.items():
                self.__split(subtree_feature_indices, left_attr_indices, splitting_node, deep+1, attr_value)

    def __pure_class(self, target_indices):
        classification = None
        for i in target_indices:
            changed = False if classification is None or classification == self.targets[i] else True
            classification = self.targets[i]
            if changed:
                return None
        return classification

    def __select_attribute(self, candidate_attr_indices):
        return self.selection_method.select(self.features, candidate_attr_indices, self.targets)


class InfoGain:
    def select(self, features, candidate_attr_indices, targets):
        info_before = self.info(targets)
        attr_size = len(features[0])
        max_gain = None
        attr_index = None
        for i in candidate_attr_indices:
            features_and_classes = []
            for j in range(len(targets)):
                features_and_classes.append((features[j][i], targets[j]))
            info_on_attr = self.info_after(features_and_classes)
            gain = info_before - info_on_attr
            print("info_before:%f" % info_before)
            print("#%d info=%f gain=%f" % (i, info_on_attr, gain))
            attr_index = i if attr_index is None or gain > max_gain else attr_index
            max_gain = gain if max_gain is None or gain > max_gain else max_gain
            print("max: %d, %f" % (attr_index, max_gain))
            print("----------")
        return attr_index, max_gain

    #
    def info_after(self, features_and_classes):
        division = {}
        total = 0.0
        for f, c in features_and_classes:
            # print("f, c: "+str(f)+" "+str(c))
            # print(division)
            if f in division:
                division[f].append(c)
            else:
                division[f] = [c]
            total += 1
            # print(division)
            # print()

        info_on_attr = 0.0
        for f, cs in division.items():
            division_size = len(cs)
            info = self.info(cs)
            info_on_attr += (division_size / total) * info
        return info_on_attr

    def info(self, targets):
        classes = {}
        total = 0.0
        for target in targets:
            if target in classes:
                classes[target] += 1
            else:
                classes[target] = 1
            total += 1

        info = 0
        for target, cnt in classes.items():
            p = cnt / total
            info -= p * math.log2(p)

        return info
