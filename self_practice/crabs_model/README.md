# Leptograpsus Crabs

#### Model of Crabs using TensorFlow API.

### Labels:
 
`SP` -- `species`

### Features:

* `sex` -- `Male` or `Female`
* `FL` -- `Frontal Lip of Carapace`
* `RW` -- `Rear with Carapace`
* `CL` -- `Length of Carapace`
* `CW` -- `Width of Carapace`
* `BD` -- `Body Length`

### Table of Result (Test Loss):

| Linear_Classification `parameters` | ![equation](http://latex.codecogs.com/gif.latex?log) Normalized | ![equation](http://latex.codecogs.com/gif.latex?Z-score) Normalized |
| --- | --- | --- |
| *learning_rate* | `0.0001` | `0.00007` |
| *steps* | `3` | `3` |
| *batch_size* | `2` | `2` |
| *Test_Loss* | `0.70145` | `0.68709` |

