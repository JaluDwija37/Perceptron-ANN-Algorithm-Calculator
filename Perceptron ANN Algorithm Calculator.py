import numpy as np

def activation(x):
    return 1 if x >= 0 else -1

def perceptron(x1, x2, y, learning_rate=0.1, max_iterations=10):
    w1, w2, bias = 0, 0, 0

    for iteration in range(max_iterations):
        print("ITERASI", iteration + 1)
        for i in range(len(x1)):
            print("\nData", i + 1, ": x1 =", x1[i], ", x2 =", x2[i], ", y =", y[i], ">",format(w1, ".2f"),",",format(w2, ".2f"),",",format(bias, ".2f"))
            total = w1 * x1[i] + w2 * x2[i] + bias
            y_pred = activation(total)

            print("y_pred = activation(x1w1+x2w2+b) = activation(",format(total, ".2f"),") =", format(y_pred, ".2f"))

            if y_pred != y[i]:
                w1 += learning_rate * (y[i] - y_pred) * x1[i]
                w2 += learning_rate * (y[i] - y_pred) * x2[i]
                bias += learning_rate * (y[i] - y_pred)
                print("\nUpdate bobot :")
                print("w1_new = w1_old + learning_rate * (y - y_pred) * x1 =", format(w1, ".2f"))
                print("w2_new = w2_old + learning_rate * (y - y_pred) * x2 =", format(w2, ".2f"))
                print("\nUpdate bias :")
                print("bias_new = = bias_old + learning_rate *(y - y_pred) =", format(bias, ".2f"))

    return w1, w2, bias

# Data
x1 = [5.1, 4.9, 4.7, 4.6, 6.4, 6.9, 5.5, 6.5]
x2 = [3.5, 3.0, 3.2, 3.1, 3.2, 3.1, 2.3, 2.8]
y = [-1, -1, -1, -1, 1, 1, 1, 1]

# Panggil fungsi perceptron
w1, w2, bias = perceptron(x1, x2, y, max_iterations=10)

# Cetak bobot dan bias yang terlatih
print("\nBobot terlatih: w1 =", format(w1, ".2f"), ", w2 =", format(w2, ".2f"))
print("Bias terlatih:", format(bias, ".2f"))
