import numpy  as np

#Hypothesis Class
class LinearRegressionMultiVariable:

    #Train Model
    def fit(train_x,train_y):
        x = train_x
        y = np.array(train_y).reshape(len(train_y),1)
        c = []
        self.p = []
        
        for li in x:
            c.append(np.insert(np.array(li),0,1))

        ##P = (((X.T*X)^-1)*X)*Y
        self.p = np.matmul(np.matmul(np.linalg.inv(np.matmul(c.T,c)),c),y).reshape(1,len(train_y))
        

    #Predict Model
    def predict(test_x):
        out = []
        for i test_x:
            out.append(np.multiply(self.p,np.insert(np.array(i),0,1)).sum())
        return out


#Training Data
train_features = "your training data input list"
train_y = "your training data output list"

#make an object
linear_regresson = LinearRegressionOneVariable()

#train data
linear_regression.fit(train_features,train_y)

#Testing Data
test_features = "your testing data input list"
test_y = "your testing data output list"

#test or predict
predictions = linear_regression(test_features)



#Accuracy
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(test_y,predictions)

print("Accuracy : %d"%(accuracy))


