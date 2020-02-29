import csv
import numpy as np
file1=open('test_analy_0601.csv','rb')
file1.readline()
reader=csv.reader(file1)
file2=open('test_label_0601.csv','rb')
file2.readline()
reader_label=csv.reader(file2)
writer_accuracy = csv.writer(open('compute_accuracy_0601.csv', 'wb'))
writer_accuracy.writerow(['threshold', 'bad_right','bad_total','accuracy0', 'good_right','good_total', 'accuracy1','pre_true','total', 'accuracy'])
prediction={}
label={}
for item in reader:
    prediction[item[0]]=item[1]
for item in reader_label:
    label[item[1]] = item[2]

for j in np.arange(0,1,0.001):
    sum = sum0 = sum1 = 0
    accuracy = accuracy0 = accuracy1 = 0
    for i in prediction:
        #if sum==0:
            #sum+= 1
            #continue
        sum=sum+1
        if float(prediction[i])>j:
            label0='1'
        else:
            label0='0'
#average accuracy
        if label0==label[i]:
            accuracy+=1
#good accuracy
        if label[i]=='1':
            sum1+=1
            if label0==label[i]:
                accuracy1+=1
#bad accuracy
        if label[i]=='0':
            sum0+=1
            if label0==label[i]:
                accuracy0+=1
    total=float(accuracy)/(sum)
    good=float(accuracy1)/(sum1)
    bad=float(accuracy0)/(sum0)
    writer_accuracy.writerow([j,accuracy0,sum0,bad,accuracy1,sum1,good,accuracy,sum,total])

