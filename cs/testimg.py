# import socketserver
import os
from PIL import Image
import numpy as np
import socket
import cv2
import traceback
import csv
import pickle
host = '111.204.16.37'

port = 3202
def send(src_path, HOST, PORT):
    """
    @params: src_path, the face image path to be detected and aligned
    @return: return the aligned face image path, if failed, return fail info, eg
        error info and 'no face found'
    """
    #  HOST, PORT = "localhost", 3200
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        img=Image.open(src_path)
        img=img.resize((227,227))
        img.save('resize_data/1.jpg')
        send_str=""
        veri = cv2.imread('resize_data/1.jpg')
        for elmt in veri:
            send_str += "%s," % str(elmt)
        sock.send(veri)
        recv_data = sock.recv(1024)
        sock.close()
        print ("recv_data",recv_data)
        #return recv_data.decode('utf-8')
        #return np.fromstring(recv_data)
        return recv_data
        #return 0
        #return recv_data
    except Exception as e:
        print (e)
        traceback.print_exc()
        # print "got an error {0}".format(e)
        #sock.close()
        #return {"error": str(e)}
if __name__ == "__main__":
    #csvfile_test = open('csv_test_analy.csv', 'wb')
    writer_test = csv.writer(open('prediction_20181117_new.csv', 'wb'))
    writer_test.writerow(['image', 'prediction'])
    #send(r'D:\xuejie\data\data1\1482046103566.jpg', host, port)
    #f1 = open('D:/xuejie/data/test.txt', 'w')
    #imgname = []
    #path = 'D:/xuejie/data/data1/'
    #for dirnames in os.listdir(path):
        #imgname.append(dirnames)
    #for i in xrange(len(imgname)):
        #file_path = os.path.join(path, imgname[i])
        #print i
        #print file_path
        #data=send(file_path, host, port)
        #f1.write(imgname[i]+'   ')
       # f1.write(data)
        #f1.write('\n')
    #f1.close()

    for dirnames in os.listdir('D:/liu_data/20181117/20181117/new/'):
        file_path = os.path.join('D:/liu_data/20181117/20181117/new/', dirnames)
        print file_path
        value=send(file_path, host, port)
        writer_test.writerow([dirnames, float(value)])


