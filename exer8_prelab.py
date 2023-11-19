import csv
import matplotlib.pyplot as plt

file = "iris.csv"

class Datapoint:
    def __init__(self, sepalLength, sepalWidth, petalLength, group=None):
        self.sepalLength = sepalLength
        self.sepalWidth = sepalWidth
        self.petalLength = petalLength
        self.group = group

dataset = []

with open(file, "r",encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader) #ignore header
    for row in csv_reader:
        newdatapoint = Datapoint(float(row[0]),float(row[1]),float(row[2]))
        dataset.append(newdatapoint)
        print("Sepal Length: {}; Sepal Width: {}; Petal Length: {}".format(newdatapoint.sepalLength,newdatapoint.sepalWidth,newdatapoint.petalLength))

k = 3
n = len(dataset)

#assign groups based in k
for i in range(len(dataset)):
    dataset[i].group = i % k

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(
    [datapoint.sepalLength for datapoint in dataset],
    [datapoint.sepalWidth for datapoint in dataset],
    [datapoint.petalLength for datapoint in dataset],
    c=[datapoint.group for datapoint in dataset],  # Using values for color mapping
    cmap='jet'
)

ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')
ax.set_zlabel('Petal Length')

plt.show()