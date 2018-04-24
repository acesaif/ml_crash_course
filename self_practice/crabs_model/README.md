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
| __learning_rate__ | `0.0001` | `0.00007` |
| __steps__ | `3` | `3` |
| __batch_size__ | `2` | `2` |
| __Test_Loss__ | `0.70145` | `0.68709` |

