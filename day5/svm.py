import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

x = digits.images
y = digits.target

n_samples = len(x)
x = x.reshape((n_samples, -1))

x_train, x_test, y_tain, y_test, = train_test_split(x, y, test_size=0.5, shuffle=False)

clf = svm.SVC(gamma=0.001)
clf.fit(x_train, y_tain)

y_pred = clf.predict(x_test)
print("Classification report:\n", metrics.classification_report(y_test, y_pred))

images_and_predictions = list(zip(digits.images[n_samples // 2:], y_pred))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(1, 4, index +1)
    plt.axis("off")
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    plt.title(f'pred: {prediction}')

plt.show()