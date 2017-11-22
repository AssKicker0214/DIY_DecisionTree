#
from DecisionTree.DecisionTree import DecisionTree

a = ["sales", "31-35", "46k-50k"]
b = ["sales", "26-30", "26k-30k"]
c = ["sales", "31-35", "31k-35k"]
d = ["systems", "21-25", "46k-50k"]
e = ["systems", "31-35", "66k-70k"]
f = ["systems", "26-30", "46k-50k"]
g = ["systems", "41-45", "66k-70k"]
h = ["marketing", "36-40", "46k-50k"]
i = ["marketing", "31-35", "41k-45k"]
j = ["secretary", "46-50", "36k-40k"]
k = ["secretary", "26-30", "26k-30k"]
data = []
target = []
for i0 in range(30):
    data.append(a)
    target.append('senior')

for i1 in range(40):
    data.append(b)
    target.append('junior')

for i2 in range(40):
    data.append(c)
    target.append('junior')

for i3 in range(20):
    data.append(d)
    target.append('junior')

for i4 in range(5):
    data.append(e)
    target.append('senior')

for i5 in range(3):
    data.append(f)
    target.append('junior')

for i6 in range(3):
    data.append(g)
    target.append('senior')

for i7 in range(10):
    data.append(h)
    target.append('senior')

for i8 in range(4):
    data.append(i)
    target.append('junior')

for i9 in range(4):
    data.append(j)
    target.append('senior')


for i10 in range(6):
    data.append(k)
    target.append('junior')


# targets = [
#     'senior',
#     'junior',
#     'junior',
#     'junior',
#     'senior',
#     'junior',
#     'senior',
#     'senior',
#     'junior',
#     'senior',
#     'junior'
# ]

dt = DecisionTree()
root = dt.fit(data, target, ['dpt', 'age', 'sly'])
root.make_html()
