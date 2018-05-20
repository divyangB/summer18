#!/usr/bin/python3

from sklearn import tree

#smooth=0, bumpy=1

features=[[110,0],[120,0],[130,1],[130,1]]
output=['Apple', 'Apple','Orange','Orange']

        #using algo
        
algo= tree.DecisionTreeClassifier()
        
#training feature and output set
trained= algo.fit(features,output)

#testing trained model

result= trained.predict([[130,0]])
print(result)
