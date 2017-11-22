from DecisionTree.DecisionTree import DecisionTree

features = [
    ['youth', 'high', 'no', 'fair'],
    ['youth', 'high', 'no', 'excellent'],
    ['middle_aged', 'high', 'no', 'fair'],
    ['senior', 'medium', 'no', 'fair'],
    ['senior', 'low', 'yes', 'fair'],
    ['senior', 'low', 'yes', 'excellent'],
    ['middle_aged', 'low', 'yes', 'excellent'],
    ['youth', 'medium', 'no', 'fair'],
    ['youth', 'low', 'yes', 'fair'],
    ['senior', 'medium', 'yes', 'fair'],
    ['youth', 'medium', 'yes', 'excellent'],
    ['middle_aged', 'medium', 'no', 'excellent'],
    ['middle_aged', 'high', 'yes', 'fair'],
    ['senior', 'medium', 'no', 'excellent']
]

targets = [
    'no',
    'no',
    'yes',
    'yes',
    'yes',
    'no',
    'yes',
    'no',
    'yes',
    'yes',
    'yes',
    'yes',
    'yes',
    'no'
]

dt = DecisionTree()
root = dt.fit(features, targets, ['age', 'income', 'student', 'credit'])
root.make_html(path='./data/page_218_example.html')