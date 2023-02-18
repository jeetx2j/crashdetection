import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import warnings

warnings.filterwarnings('ignore')

def main():
    db = pd.read_csv('dataset/data.csv')
    
    X = db[['ax','ay','az','gx','gy','gz']]
    Y = db['result']

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25)

    DTree = DecisionTreeClassifier()
    DTree.fit(X_train, y_train)
	
    DTreePred = DTree.predict(X_test)
    print("Predicted values:")
    print(DTreePred)
	
    DTreeAcuuracy = round(DTree.score(X_test,y_test)*100, 2)

    print("Descision Tree Accuracy : ", DTreeAcuuracy, '%')

    LReg = LogisticRegression()
    LReg.fit(X_train, y_train)
	
    LRegePred = LReg.predict(X_test)
    print("Predicted values:")
    print(LRegePred)
	
    LRegAcuuracy = round(LReg.score(X_test,y_test)*100, 2)

    print("Logistic Regression Accuracy : ", LRegAcuuracy, '%')


    RForest = RandomForestClassifier()
    RForest.fit(X_train, y_train)
    
    RForestPred = RForest.predict(X_test)
    print("Predicted values:")
    print(RForestPred)
    
    RForestAccuracy = round(RForest.score(X_test,y_test)*100, 2)

    print("Random Forest Accuracy : ", RForestAccuracy, '%')



if __name__ == "__main__":
	main()
