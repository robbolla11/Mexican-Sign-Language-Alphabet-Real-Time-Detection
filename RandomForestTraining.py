import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.tree import plot_tree
import numpy as np
import matplotlib.pyplot as plt

#datos
data_dict = pickle.load(open('./data.pickle', 'rb'))

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])
class_names = data_dict.get('class_names', np.unique(labels))

#entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.22, shuffle=True, stratify=labels)

#Random Forest
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Realizar predicciones
y_predict = model.predict(x_test)

# Calcular la precisión
score = accuracy_score(y_predict, y_test)
print('Precisión: {} %'.format(score * 100))

# Mostrar la matriz de confusión
matrizConfusion = confusion_matrix(y_test, y_predict)
disp = ConfusionMatrixDisplay(confusion_matrix=matrizConfusion, display_labels=class_names)
disp.plot(cmap=plt.cm.Blues)
plt.show()


#primeros 3 árboles
for i in range(3):
    plt.figure(figsize=(20,10))
    plot_tree(model.estimators_[i], 
              feature_names=np.arange(data.shape[1]).astype(str), 
              class_names=class_names, 
              filled=True, 
              rounded=True)
    plt.title(f'Árbol {i+1}')
    plt.show()

#guardar modelo en pickle
with open('model.p', 'wb') as f:
    pickle.dump({'model': model}, f)
