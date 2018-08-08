# Leptograpsus Crabs

##### Model of Crabs using `TensorFlow` API.

#### Labels
`SP` -- `species`

#### Features
| __`Features`__ | __`Description`__ |
| --- | --- |
| `sex` | `Male` or `Female` |
| `FL` | `Frontal Lip of Carapace` |
| `RW` | `Rear with Carapace` |
| `CL` | `Length of Carapace`
| `CW` | `Width of Carapace`
| `BD` | `Body Length`

#### Table of Result

| `Parameters` | ![equation](http://latex.codecogs.com/gif.latex?log) `Normalized` | ![equation](http://latex.codecogs.com/gif.latex?Z-score) `Normalized` |
| --- | --- | --- |
| __`learning_rate`__ | `0.0001` | `0.00007` |
| __`steps`__ | `3` | `3` |
| __`batch_size`__ | `2` | `2` |
| __`Test_Loss (result)`__ | `0.70145` | `0.68709` |

###### Model's __`test_loss`__ is about `0.69662` before normalization.

#### End Users

These results can be used in __`Crab Cultering`__ where it is required to monitor crabs database to rear crabs and its demands in markets. Biological researchers can use this model to `categorize` crabs for their studies.

Yes, the data in which I modelled is very limited and is devoid of various features. This data consists of just `200 units` which is scarce. This model can be improved to its extensive if it is fed with high quality weighted data.
