import matplotlib.pyplot as plt
import matplotlib
from RandomForest import accr
from SupportVectorMachine import accs
from logisticRegression import acc




height = [accr,accs,acc]
bars = ('Random Forest', 'SVM', 'Logistic Regression')
y_pos = np.arange(len(bars))

plt.xlabel("Models")
plt.ylabel("Accuracy")
matplotlib.rcParams.update({'font.size': 22})

plt.bar(y_pos, height, color=(0.2, 0.1, 0.3),  edgecolor='yellow')
plt.xticks(y_pos, bars)
plt.show()
