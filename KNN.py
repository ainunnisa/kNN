import math
from operator import itemgetter

def EuclideanDistance(a,b):
    distance=0
    n=len(a)
    for i in range (0,n):
        distance = distance + ((a[i]-b[i]) ** 2)
    result = math.sqrt(distance)
    return result


def prosesknn (k, testing, training):
    neighbor = []
    for data in training:
        distance = EuclideanDistance (testing[1:-1], data[1:-1])
        neighbor.append((distance, data))

    sorting= sorted(neighbor, key=itemgetter(0))
    knn = sorting[:k]

    hasil0 = 0
    hasil1 = 0

    for data in knn:
        distance, object = data
        label = object[-1]

        if label == 0:
            hasil0 += 1
        else:
            hasil1 += 1

    if hasil0 > hasil1:
        return 0
    else:
        return 1