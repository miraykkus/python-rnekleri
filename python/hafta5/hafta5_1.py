#mustafamuratcoskun githubda python kodları paylaşıyo

#csv okuma
import csv
with open('iris.data', newline='') as csvfile:
    print(csvfile)
    reader = csv.DictReader(csvfile)
    print(reader)
    for row in reader:
        print(row['sepal_length'],
              row['sepal_width'],
              row['petal_length'],
              row['petal_width'],
              row['species'])



