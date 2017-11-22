import pickle


class DecisionTreeNode:
    index = 0

    def __init__(self, attr_name, attr_index, size, choice=""):
        self.children = []
        self.name = attr_name
        self.attr_index = attr_index
        self.size = size
        self.choice = choice
        self.pairs = []
        self.pack = []
        self.id = DecisionTreeNode.index
        DecisionTreeNode.index += 1

    def is_leaf(self):
        return len(self.children) == 0

    def decide(self, feature):
        if self.is_leaf():
            return self.name
        else:
            attr_value = feature[self.attr_index]
            next_node = None
            for children in self.children:
                if children.choice == attr_value:
                    next_node = children

            if next_node is None:
                print("can't decide, at node "+ self.name)
                return None
            else:
                return next_node.decide(feature)

    def add_child(self, child_node):
        self.children.append(child_node)

    def set_choice(self, choice):
        self.choice = choice

    def save(self, path="./data/model.m"):
        self.dps(self, -1, wrap=True)
        file = open(path, 'wb')
        pickle.dump(self.pack, file)

    def make_html(self, path="./data/DecisionTree.html"):
        self.dps(self, -1)

        file = open(path, 'w', encoding='utf-8')
        file.write('''
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="utf-8">
            <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
            <script type="text/javascript">
              google.charts.load('current', {packages:['wordtree']});
              google.charts.setOnLoadCallback(drawChart);

              function drawChart() {
                var data = google.visualization.arrayToDataTable([
                ['id', 'childLabel', 'parent', 'size', {role: 'style'}],
        ''')
        for line in self.pairs:
            file.write("[" + line + "],\n")

        file.write('''
                 ]);

                var options = {
                  maxFontSize: 16,
                  wordtree: {
                    format: 'explicit',
                    type: 'suffix   '
                  }
                };

                var chart = new google.visualization.WordTree(document.getElementById('wordtree_basic'));
                chart.draw(data, options);
              }
            </script>
          </head>
          <body>
            <div id="wordtree_basic" style="width: 3000px; height: 1000px;"></div>
          </body>
        </html>
        ''')
        file.close()

    def dps(self, node, parent_id, wrap=False):
        if wrap:
            self.pack.append(node)
        name_str = "" if node.choice == "" else "[%s]→" % node.choice
        name_str += node.name
        pair_str = "%d, '%s', %d, %d, '%s'" % (node.id, name_str, parent_id, 1, "black")
        self.pairs.append(pair_str)
        if len(node.children) == 0:
            # it is a leaf node
            return

        for child in node.children:
            self.dps(child, node.id)

            # test
            # A = DecisionTreeNode("A", 0)
            # B = DecisionTreeNode("B", 0)
            # C = DecisionTreeNode("C", 0)
            # D = DecisionTreeNode("D", 0)
            # E = DecisionTreeNode("E", 0)
            # F = DecisionTreeNode("F", 0)
            # G = DecisionTreeNode("G", 0)
            # A.add_child(B)
            # A.add_child(C)
            # B.add_child(D)
            # C.add_child(E)
            # C.add_child(F)
            # C.add_child(G)
            #
            # A.draw()
