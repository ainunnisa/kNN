import csv

def LoadDataTrain():
        dataTrain = []
        csvfile = open('DataTrainAi.csv','r')
        scan = csv.reader(csvfile, delimiter=';', quotechar='"')
        next(scan)
        for data in scan:
            berita, like, provokasi, comment, emosi, hoax = data
            dataTrain.append([berita,int(like),int(provokasi),int(comment),int(emosi),int(hoax)])
        return dataTrain

def LoadDataTest():
    dataTest = []
    csvfile = open('DataTestAi.csv', 'r')
    scan = csv.reader(csvfile, delimiter=';', quotechar='"')
    next(scan)
    for data in scan:
        berita, like, provokasi, comment, emosi, hoax = data
        dataTest.append([berita, int(like), int(provokasi), int(comment), int(emosi), hoax])
    return dataTest
