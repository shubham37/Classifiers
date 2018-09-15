import numpy  as np
from sklearn.metrics import accuracy_score


#Hypothesis Class
class LinearRegressionOneVariable:

    #Train Model
    def fit(train_inputs,train_outpus):
        x = train_inputs
        y = train_outpus

        #XY
        p = []
        for i in range(len(y)):
            p.append(x[i]*y[i])
        pro = sum(p)

        #X^2
        sqr = np.power(np.array(x),2)
        s = sqr.sum()

        #y = mx +b
        self.m = pro/s
        self.b = y[0] - (self.m*x[0]) 
        

    #Predict Model
    def predict(test_inputs):
        out = []
        for i in test_inputs:
            out.append((self.m*i)+self.b)
        return out


#Training Data
train_input = "your training data input list"
train_output = "your training data output list"

#make an object
linear_regresson = LinearRegressionOneVariable()

#train data
linear_regression.fit(train_input,train_output)

#Testing Data
test_input = "your testing data input list"
test_output = "your testing data output list"

#test or predict
predictions = linear_regression(test_input)



#Accuracy
accuracy = accuracy_score(test_output,predictions)

print("Accuracy : %d"%(accuracy))


