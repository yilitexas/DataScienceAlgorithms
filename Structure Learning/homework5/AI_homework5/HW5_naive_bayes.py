input1 = open('student_test.data', 'r')
set1 = input1.readlines()
input1.close()

size1 = len(set1)-1

train_data1 = []

for i in range(size1):
    temp1 = set1[i+1]
    train_data1.append(temp1)

new_train_data1=[]

for i in range(size1):
    temp1 = train_data1[i].rstrip('\r\n')

    temp2 = temp1.split(',')

    size2 = len(temp2)

    str1 = ''

    for j in range(size2):
        temp3 = temp2[j].rstrip('\r\n')
        temp4 = ''
        if (temp3 == 'A'):
            temp4 = '0 '
            str1 = str1 + temp4

        elif (temp3 == 'T'):
            temp4 = '1 '
            str1 = str1 + temp4

        elif (temp3 == 'yes'):
            temp4 = '0 '
            str1 = str1 + temp4

        elif (temp3 == 'no'):
            temp4 = '1 '
            str1 = str1 + temp4

        else:
            temp4 = temp3 + ' '
            str1 = str1 + temp4

    new_train_data1.append(str1)

print(new_train_data1)

output1 = open('train.txt','w')

for i in range(size1):
    temp1 = new_train_data1[i] + '\n'
    output1.write(temp1)

output1.close()