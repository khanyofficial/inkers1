import numpy as np
import pandas as pd

def sigmoid(x, derivative=False):
  return x*(1-x) if derivative else 1/(1+np.exp(-x))

lr = 0.1
x = np.array([
    [1,0,1,0],
    [1,0,1,1],
    [0,1,0,1]
])


#wh = np.array(np.random.random([4,3]))
#bh = np.array(np.random.random([1,3]))
#wout = np.array(np.random.random([3,1]))
#bout = np.array(np.random.random([1]))
y = np.array(np.random.random([3,1]))
wh = np.array([
    [.42, .88, .55],
    [.1, .73, .68],
    [.6, .18, .47],
    [.92, .11, .52]
])

bh = np.array([.46, .72 , .08])

wout = np.array([
    [.3],
    [.25],
    [.23]
])

bout = np.array([.69])
y = np.array([
    [1],[1],[0]
])


hidden_layer_input = np.add(np.matmul(x, wh), bh)
hiddenlayer_activations = sigmoid(hidden_layer_input)
output = sigmoid(np.add(np.matmul (hiddenlayer_activations , wout ) , bout))
E = y-output
slope_output_layer= output* (1-output)
slope_hidden_layer = hiddenlayer_activations* (1-hiddenlayer_activations)
d_output = E * slope_output_layer*lr
Error_at_hidden_layer = np.matmul(d_output, wout.T)
d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
wout = wout + np.matmul(hiddenlayer_activations.T,d_output ) * lr
wh = wh + np.matmul(x.T, d_hiddenlayer) * lr
bh = bh + np.sum(d_hiddenlayer, axis=0) * lr
bout = bout + np.sum(d_output, axis=0)*lr
print("----------")
print("bout", bout)
print("----------")
print("wout", wout)
print("----------")
print("wh", wh)
print("----------")
print("bh", bh)
print("----------")
print("output", output)
print("----------")
print("d_output", d_output)
print("----------")
