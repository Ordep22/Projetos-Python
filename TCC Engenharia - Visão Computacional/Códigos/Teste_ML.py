import matplotlib.pyplot as plt
from matplotlib import pyplot
import cv2
import  math
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn import model_selection
from sklearn import metrics


img = cv2.imread("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/img/bobina_01.jpg",cv2.IMREAD_GRAYSCALE)[:200,600:800]
cv2.imshow('Imagem',img)
cv2.waitKey(0)
'''''
limiar , inglimiari = cv2.threshold(img,210,255,cv2.THRESH_BINARY_INV)

moments  = cv2.moments(inglimiari)
huMoments = cv2.HuMoments(moments)

for i in range(0,7):
    huMoments[i] = -1 * math.copysign(1.0,huMoments[i])*math.log10(abs(huMoments[i]))
print(huMoments)

fig = pyplot.figure(figsize=(20,20))
ax1 = fig.add_subplot(121)
pyplot.imshow(img,cmap='gray')
pyplot.title("Imagem original")
ax2 = fig.add_subplot(122)
pyplot.imshow(inglimiari,cmap='gray')
pyplot.title("Imagem Binarizada")
pyplot.show()





##Importanto os Dados

data  = pd.read_csv("/Users/PedroVitorPereira/PycharmProjects/CursodePython/Exercícios de Python/Visão computacional/numeros.csv")
nu = pd.DataFrame(data)
nu.head()
nu.info()

##Gerando os gráficos

plt.figure(figsize=(8,4))
sns.countplot(x = 'Numero',data = nu)


sns.set_style('whitegrid')
sns.FacetGrid(nu, hue = 'Numero', height = 6).map(plt.scatter,'c1', 'c2').add_legend()
plt.show()

sns.set_style('whitegrid')
sns.FacetGrid(nu, hue = 'Numero', height = 6).map(plt.scatter,'c3', 'c4').add_legend()
plt.show()


##Gerando uma informação que eu não sei o que é !!!
nu  = nu.values
x = nu[0:,1:8].astype(float)
y = nu[0:,8].astype(object)
x_train, x_test, y_train, y_test = model_selection.train_test_split(x,y,test_size = 0.3, random_state = 0,)
print(x_train.shape)
print(y_train.shape)
model = MLPClassifier(activation = 'relu',hidden_layer_sizes=(3),random_state = 0,max_iter = 20000, verbose = True)
model.fit(x_train,y_train)

prediction = model.predict(x_test)
print(y_test)
print(prediction)

print(metrics.accuracy_score(prediction,y_test))
'''''