# importing libraries
from sklearn.externals import joblib
import inputScript
import webbrowser


def start(x):
    # load the pickle file
    if x == '1':  # Random Forest
        classifier = joblib.load('rf_final.pkl')
    elif x == '2':  # SVM
        classifier = joblib.load('svm_final.pkl')
    elif x == '3':  # LogisticRegression
        classifier = joblib.load('logisticR_final.pkl')
    else:
        print("Please choose a valid option")
        x = input("Enter the method you want to use:\n1.RandomForest\n2.Support Vector Machine\n3.Logistic Regression\n")
        start(x)

    # input url
    url = input("Enter Website URL: ")

    # checking and predicting
    checkprediction = inputScript.main(url)
    prediction = classifier.predict(checkprediction)
    if prediction == 1:
        print("\nPhishing Website Detected\n")
        print("Can't open website")
    else:
        print("\nNo Phishing Website Detected\n")
        print("Opening Website..........")
        webbrowser.open_new(url)

    y = input("Would you like to continue:\nY\nN\n")
    cont(y)


def cont(y):
    if y == 'Y':
        x = input("Enter the method you want to use:\n1.RandomForest\n2.Support Vector Machine\n3.Logistic Regression\n")
        start(x)
    elif y == 'N':
        print('Thank You')
        exit()
    else:
        print("Please choose a valid option")
        y = input("Would you like to continue:\nY\nN\n")
        cont(y)


x = input("Enter the method you want to use:\n1.RandomForest\n2.Support Vector Machine\n3.Logistic Regression\n")
start(x)
