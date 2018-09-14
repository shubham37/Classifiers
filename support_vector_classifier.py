import numpy as np

class SVClassifier:

    def fit(data):
        self.data = data
        transforms = [[1,1],
                      [1,-1],
                      [-1,1],
                      [-1,-1]
                      ]
        
        #{||w||: [w,b]} and lastly pic the smallest one
        opt_dic = {}


        all_data = []

        for yi in self.data:
            for featureset in self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)

        #to decide range of w
        self.max_f_v = max(all_data)
        self.min_f_v = min(all_data)

        all_data = None

        step_size = [self.max_f_v*0.1,
                     self.max_f_v*0.01,
                     self.max_f_v*0.001]

        b_range = 5
        b_multiple = 5

        latest_optimum = self.max_f_v*10

        for step in step_size:
            w = np.array(latest_optimum,latest_optimum)
            optimizied = False
            while not optimized:
                for b in np.arange(-1*(self.max_feature_value*b_range_multiple),
                                   self.max_feature_value*b_range_multiple,
                                   step*b_multiple):
                    for transformation in transforms:
                        w_t = w*transformation
                        found_option = True
                        # weakest link in the SVM fundamentally
                        # SMO attempts to fix this a bit
                        # yi(xi.w+b) >= 1
                        # 
                        # #### add a break here later..
                        for i in self.data:
                            for xi in self.data[i]:
                                yi=i
                                if not yi*(np.dot(w_t,xi)+b) >= 1:
                                    found_option = False
                                    
                        if found_option:
                            opt_dict[np.linalg.norm(w_t)] = [w_t,b]

            if w[0]<0:
                optimized = True
                print('optimized a step')
            else:
                w = w -step

        norms = sorted([n for n in opt_dict])

        opt_choice = opt_dict[norm[0]]
        self.w = opt_choice[0]
        self.b = opt_choice[1]

        latest_optimum = opt_choice[0][0]+step*2


    def predict(features):i
        classification = []
        for featureset in features:
            classification.append(np.sign(np.dot(np.array(featureset),self.w)+self.b))

        return classification
        
#You can change it with your data
data = {-1:np.array([[1,7],[2,8]
                     ,[3,8]]),1:np.array([[5,1]
                                          ,[6,-1],
                                          [7,3]])}

#Make an object of Classifier
svc = SVClassifier()

#train classifier
svc.fit(data = data)


#test_data
test_data = [[0,10],
             [3,8],
             [-2,9]]

#predict value/label

svc.predict(test_data)


