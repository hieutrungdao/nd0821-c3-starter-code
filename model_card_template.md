# Model Card

For additional information see the Model Card paper: <https://arxiv.org/pdf/1810.03993.pdf>

## Model Details

- Developed by HieuDT47
- Gradient boosting framework that uses tree based learning algorithms.

## Intended Use

- Intended to used to predict people makes over 50K a year or not for Udacity MLOps Project 3: Deploying a ML Model to Cloud Application Platform with FastAPI.

## Training Data

- Census Income training data split.
- Extraction was done by Barry Becker from the 1994 Census database.
- Information on the dataset can be found [here](https://archive.ics.uci.edu/dataset/20/census+income).

## Evaluation Data

- Census Income testing data split.
- Extraction was done by Barry Becker from the 1994 Census database.
- Information on the dataset can be found [here](https://archive.ics.uci.edu/dataset/20/census+income).

## Metrics

- The F-beta score combines precision and recall to assess a model's performance, with the weighting determined by the beta parameter. Precision measures the accuracy of positive predictions, while recall quantifies the model's ability to identify positive instances correctly.

|Model |F-beta |Precision |Recall |
| ------        |:---: | :---:    | :---:       |
| LightGBM   |0.73 | 0.79    | 0.67       |

## Ethical Considerations

- Ethical considerations for the given scenario include obtaining informed consent, ensuring data privacy and anonymity, addressing potential biases and fairness issues, promoting transparency and explainability, emphasizing accountability and responsibility, evaluating the impact on individuals and society, mitigating bias and discrimination, and implementing data governance and security measures.

## Caveats and Recommendations

- Caveats: Consider limitations in dataset scope, accuracy, and generalizability of the prediction task.

- Recommendations: Validate data source, evaluate feature selection, assess model performance, conduct ethical impact assessment, update periodically, and promote transparency.
