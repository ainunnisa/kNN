import csv
import LoadData
import KNN

from LoadData import LoadDataTrain, LoadDataTest

if __name__=='__main__':
    data_train = LoadDataTrain()

    filehasil = open('Hasilnya.csv','w')
    writer = csv.writer(filehasil, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    data_test = LoadDataTest()
    for data in data_test:
        result = KNN.prosesknn(3, data, data_train)
        data.append(result)
        print (data)
        writer.writerow(data)

Train = LoadData.LoadDataTrain()
dataTrain = Train[:2000]
validasiTrain = Train[2000:]

data_sama=0

for dataValidasi in validasiTrain:
    result = KNN.prosesknn(3, dataValidasi, validasiTrain)
    print (dataValidasi, result)

    if result == dataValidasi[-1]:
        data_sama = data_sama+1

akurasi = float(data_sama)/len(validasiTrain) * 100

print ("Hasil Akurasinya = ", akurasi,"%")