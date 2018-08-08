# Breast Cancer UCI
##### Model Cancer Classification using `TensorFlow` API.

| __`Label`__ | `diagnosis` |
| --- | --- |

#### Table of Hyperparameters
| __`Parameters`__ | __`Values`__ |
| --- | --- |
| __`learning_rate`__ | `0.00002` |
| __`steps`__ | `500` |
| __`batch_size`__ | `3` |

#### Table of Results
| __`Set`__ | __`LogLoss (error)`__ |
| --- | --- |
| __`Training`__ | `0.67728` |
| __`Validation`__ | `0.67407` |
| __`Testing`__ | `0.67670` |

##### Final Accuracy on `Validation Set` is `0.91`.

#### End Users
This model is useful to classify `Benign` and `Malignant` breast tumours. Model did good learning of categorization as you can see the `LogLoss` slumps down drastically.

![logloss](https://user-images.githubusercontent.com/26320981/39671193-1c1bebd4-5131-11e8-81a8-5a14555d3ffd.png)

Given access to more data, there is greater scope for this model to enhance.
