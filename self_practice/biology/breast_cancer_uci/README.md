# Breast Cancer UCI
##### Model Cancer Classification using `TensorFlow` API.

Label -- `diagnosis`

#### Table of Hyperparameters
| __`Parameters`__ | __`Values`__ |
| --- | --- |
| __`learning_rate`__ | `0.00002` |
| __`steps`__ | `500` |
| __`batch_size`__ | `3` |

#### Table of Results
| __`Set`__ | __`LogLoss (error)`__ |
| --- | --- |
| __`Training`__ | `0.67128` |
| __`Validation`__ | `0.66875` |
| __`Testing`__ | `0.66785` |

#### End Users
This model is useful to classify `Benign` and `Malignant` breast tumours. Model did goog learning of categorization as you can see the `LogLoss` slumps down drastically.

![logloss](https://user-images.githubusercontent.com/26320981/39395583-c97b065a-4afd-11e8-84c4-9b0bdb64e9b1.png)

Given access to more data, there is greater scope for this model to enhance.
