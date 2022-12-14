import csv
import numpy as np
import matplotlib.pyplot as plt

#그래프 그리기
def plot_data(data):
    x = []
    y = []
    for row in data:
        x.append(float(row[0]))
        y.append(float(row[1]))
    plt.plot(x, y, marker='o', markersize=1)
    plt.show()
    
#데이터 불러오기
def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return stringToFloat(list(reader))

#문자를 숫자로 바꾸기
def stringToFloat(data):
    for i in range(len(data)):
        data[i][0] = float(data[i][0])
        data[i][1] = float(data[i][1])
    return data

def main():
    data = read_csv('data.csv')
    
    #몇월인지 표시하기
    for i in range(len(data)):
        if (i%12)/12 == 1:
            data[i][0] += 1
        else :
            data[i][0] += (i%12)/12

    plot_data(data)

if __name__ == '__main__':
    main()
