import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans


input1 = open("C:\\Users\\yxl121030\\Desktop\\input1.csv", 'r')
input2 = input1.readlines()
print(len(input2[1]))
print(len(input2))

x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
y8 = []
y9 = []
y10 = []

for i in range(406):
    line1 = input2[i + 1]
    line2 = line1[:263]
    charlist1 = list(line2)
    x.append(charlist1)
    y1.append(line1[263])
    y2.append(line1[264])
    y3.append(line1[265])
    y4.append(line1[266])
    y5.append(line1[267])
    y6.append(line1[268])
    y7.append(line1[269])
    y8.append(line1[270])
    y9.append(line1[271])
    y10.append(line1[272])

print(len(x))

z1 = []
for i in range(406):
    temp1 = x[i]
    z11 = []
    for j in range(263):
        if temp1[j] == "A":
            z11.append(0)
        elif temp1[j] == "R":
            z11.append(1)
        elif temp1[j] == "N":
            z11.append(2)
        elif temp1[j] == "D":
            z11.append(3)
        elif temp1[j] == "C":
            z11.append(4)
        elif temp1[j] == "Q":
            z11.append(5)
        elif temp1[j] == "E":
            z11.append(6)
        elif temp1[j] == "G":
            z11.append(7)
        elif temp1[j] == "H":
            z11.append(8)
        elif temp1[j] == "I":
            z11.append(9)
        elif temp1[j] == "L":
            z11.append(10)
        elif temp1[j] == "K":
            z11.append(11)
        elif temp1[j] == "M":
            z11.append(12)
        elif temp1[j] == "F":
            z11.append(13)
        elif temp1[j] == "P":
            z11.append(14)
        elif temp1[j] == "S":
            z11.append(15)
        elif temp1[j] == "T":
            z11.append(16)
        elif temp1[j] == "W":
            z11.append(17)
        elif temp1[j] == "Y":
            z11.append(18)
        elif temp1[j] == "V":
            z11.append(19)
        else:
            z11.append(20)

    z1.append(z11)

x1 = pd.DataFrame(z1)
spcas9 = z1[318]

print(spcas9)

w1 = []
for i in range(406):
    if y1[i] == "A":
        w1.append(21)
    elif y1[i] == "G":
        w1.append(22)
    elif y1[i] == "C":
        w1.append(23)
    else:
        w1.append(24)

w2 = []
for i in range(406):
    if y2[i] == "A":
        w2.append(21)
    elif y2[i] == "G":
        w2.append(22)
    elif y2[i] == "C":
        w2.append(23)
    else:
        w2.append(24)

w3 = []
for i in range(406):
    if y3[i] == "A":
        w3.append(21)
    elif y3[i] == "G":
        w3.append(22)
    elif y3[i] == "C":
        w3.append(23)
    else:
        w3.append(24)

w4 = []
for i in range(406):
    if y4[i] == "A":
        w4.append(21)
    elif y4[i] == "G":
        w4.append(22)
    elif y4[i] == "C":
        w4.append(23)
    else:
        w4.append(24)

w5 = []
for i in range(406):
    if y5[i] == "A":
        w5.append(21)
    elif y5[i] == "G":
        w5.append(22)
    elif y5[i] == "C":
        w5.append(23)
    else:
        w5.append(24)

w6 = []
for i in range(406):
    if y6[i] == "A":
        w6.append(21)
    elif y6[i] == "G":
        w6.append(22)
    elif y6[i] == "C":
        w6.append(23)
    else:
        w6.append(24)

w7 = []
for i in range(406):
    if y7[i] == "A":
        w7.append(21)
    elif y7[i] == "G":
        w7.append(22)
    elif y7[i] == "C":
        w7.append(23)
    else:
        w7.append(24)

w8 = []
for i in range(406):
    if y8[i] == "A":
        w8.append(21)
    elif y8[i] == "G":
        w8.append(22)
    elif y8[i] == "C":
        w8.append(23)
    else:
        w8.append(24)

w9 = []
for i in range(406):
    if y9[i] == "A":
        w9.append(21)
    elif y9[i] == "G":
        w9.append(22)
    elif y9[i] == "C":
        w9.append(23)
    else:
        w9.append(24)

w10 = []
for i in range(406):
    if y10[i] == "A":
        w10.append(21)
    elif y10[i] == "G":
        w10.append(22)
    elif y10[i] == "C":
        w10.append(23)
    else:
        w10.append(24)

#####################################################Random Forest#######################################

#Create a Gaussian Classifier
c_clf1 = RandomForestClassifier(n_estimators=100)

scores1 = cross_val_score(c_clf1, x1, w1, cv=6)
#print(type(scores3))
print("Random Forest Classifier Cross-validation Mean:", np.mean(scores1))
print("Random Forest Classifier Cross-validation std:", np.std(scores1))
print("Random Forest Classifier Cross-validation Cross-validated scores:", scores1)

#Create a Gaussian Classifier
clf1 = RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf1.fit(x1, w1)

#predict on the test set
y1_predict = clf1.predict([spcas9])
print(y1_predict)

#Create a Gaussian Classifier
clf2 = RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf2.fit(x1, w2)

#predict on the test set
y2_predict = clf2.predict([spcas9])
print(y2_predict)

#Create a Gaussian Classifier
clf3 = RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf3.fit(x1, w3)

#predict on the test set
y3_predict = clf3.predict([spcas9])
print(y3_predict)

#Create a Gaussian Classifier
clf4 = RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf4.fit(x1, w4)

#predict on the test set
y4_predict = clf4.predict([spcas9])
print(y4_predict)

#Create a Gaussian Classifier
clf5 = RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf5.fit(x1, w5)

#predict on the test set
y5_predict = clf5.predict([spcas9])
print(y5_predict)

#Create a Gaussian Classifier
clf6 = RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf6.fit(x1, w6)

#predict on the test set
y6_predict = clf6.predict([spcas9])
print(y6_predict)

#Create a Gaussian Classifier
clf7 = RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf7.fit(x1, w7)

#predict on the test set
y7_predict = clf7.predict([spcas9])
print(y7_predict)

#Create a Gaussian Classifier
clf8 = RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf8.fit(x1, w8)

#predict on the test set
y8_predict = clf8.predict([spcas9])
print(y8_predict)

#Create a Gaussian Classifier
clf9 = RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf9.fit(x1, w9)

#predict on the test set
y9_predict = clf9.predict([spcas9])
print(y9_predict)

#Create a Gaussian Classifier
clf10 = RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf10.fit(x1, w10)

#predict on the test set
y10_predict = clf10.predict([spcas9])
print(y10_predict)

########################################Logistic Regression Classifier###################################################

c_logReg1 = LogisticRegression()
scores2 = cross_val_score(c_logReg1, x1, w1, cv=6)
#print(type(scores3))
print("Logistic Regression Classifier Cross-validation Mean:", np.mean(scores2))
print("Logistic Regression Classifier Cross-validation std:", np.std(scores2))
print("Logistic Regression Classifier Cross-validation Cross-validated scores:", scores2)

logReg1 = LogisticRegression()
logReg1.fit(x1, w1)

#use the trained logistic regression model to predict the outcomes of the test set
y_predict1 = logReg1.predict([spcas9])
print(y_predict1)

logReg2 = LogisticRegression()
logReg2.fit(x1, w2)

#use the trained logistic regression model to predict the outcomes of the test set
y_predict2 = logReg2.predict([spcas9])
print(y_predict2)

logReg3 = LogisticRegression()
logReg3.fit(x1, w3)

#use the trained logistic regression model to predict the outcomes of the test set
y_predict3 = logReg3.predict([spcas9])
print(y_predict3)

logReg4 = LogisticRegression()
logReg4.fit(x1, w4)

#use the trained logistic regression model to predict the outcomes of the test set
y_predict4 = logReg4.predict([spcas9])
print(y_predict4)

logReg5 = LogisticRegression()
logReg5.fit(x1, w5)

#use the trained logistic regression model to predict the outcomes of the test set
y_predict5 = logReg5.predict([spcas9])
print(y_predict5)

logReg6 = LogisticRegression()
logReg6.fit(x1, w6)

#use the trained logistic regression model to predict the outcomes of the test set
y_predict6 = logReg6.predict([spcas9])
print(y_predict6)

logReg7 = LogisticRegression()
logReg7.fit(x1, w7)

#use the trained logistic regression model to predict the outcomes of the test set
y_predict7 = logReg7.predict([spcas9])
print(y_predict7)

logReg8 = LogisticRegression()
logReg8.fit(x1, w8)

#use the trained logistic regression model to predict the outcomes of the test set
y_predict8 = logReg8.predict([spcas9])
print(y_predict8)

logReg9 = LogisticRegression()
logReg9.fit(x1, w9)

#use the trained logistic regression model to predict the outcomes of the test set
y_predict9 = logReg1.predict([spcas9])
print(y_predict9)

logReg10 = LogisticRegression()
logReg10.fit(x1, w10)

#use the trained logistic regression model to predict the outcomes of the test set
y_predict10 = logReg10.predict([spcas9])
print(y_predict10)

######################################SVM###################################################################

c_model1 = svm.SVC(kernel="linear")
scores3 = cross_val_score(c_model1, x1, w1, cv=6)
#print(type(scores3))
print("SVM Classifier Cross-validation Mean:", np.mean(scores3))
print("SVM Classifier Cross-validation std:", np.std(scores3))
print("SVM Classifier Cross-validation Cross-validated scores:", scores3)

model1 = svm.SVC(kernel="linear")
model1.fit(x1, w1)

#predict on the test dataset
yy_predict1 = model1.predict([spcas9])
print(yy_predict1)

model2 = svm.SVC(kernel="linear")
model2.fit(x1, w2)

#predict on the test dataset
yy_predict2 = model2.predict([spcas9])
print(yy_predict2)

model3 = svm.SVC(kernel="linear")
model3.fit(x1, w3)

#predict on the test dataset
yy_predict3 = model3.predict([spcas9])
print(yy_predict3)

model4 = svm.SVC(kernel="linear")
model4.fit(x1, w4)

#predict on the test dataset
yy_predict4 = model4.predict([spcas9])
print(yy_predict4)

model5 = svm.SVC(kernel="linear")
model5.fit(x1, w5)

#predict on the test dataset
yy_predict5 = model1.predict([spcas9])
print(yy_predict5)

model6 = svm.SVC(kernel="linear")
model6.fit(x1, w6)

#predict on the test dataset
yy_predict6 = model6.predict([spcas9])
print(yy_predict6)

model7 = svm.SVC(kernel="linear")
model7.fit(x1, w7)

#predict on the test dataset
yy_predict7 = model7.predict([spcas9])
print(yy_predict7)

model8 = svm.SVC(kernel="linear")
model8.fit(x1, w8)

#predict on the test dataset
yy_predict8 = model8.predict([spcas9])
print(yy_predict8)

model9 = svm.SVC(kernel="linear")
model9.fit(x1, w9)

#predict on the test dataset
yy_predict9 = model9.predict([spcas9])
print(yy_predict9)

model10 = svm.SVC(kernel="linear")
model10.fit(x1, w10)

#predict on the test dataset
yy_predict10 = model10.predict([spcas9])
print(yy_predict10)

