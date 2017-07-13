# Mental Health in the Workplace
## What can 1300 responses to a Workplace survey tell us about Mental Health?

### TABLE OF CONTENTS
1. __[Overview](https://github.com/be-ns/Mental_Health#overview)__
 * [Goal](https://github.com/be-ns/Mental_Health#goal)
 * [Process](https://github.com/be-ns/Mental_Health#process)
 * [Results](https://github.com/be-ns/Mental_Health#results)
 * [Tools Used](https://github.com/be-ns/Mental_Health#tools-used)
2. __[Technical Approach](https://github.com/be-ns/Mental_Health#technical_approach)__
 * [Data](https://github.com/be-ns/Mental_Health#data)
 * [Cleaning / Munging](https://github.com/be-ns/Mental_Health#cleaning)
 * [Model Selection / Benchmarking](https://github.com/be-ns/simpsons_analysis/blob/master/README.md#model-selection--benchmarking)
 * [Modeling Process](https://github.com/be-ns/simpsons_analysis/blob/master/README.md#modeling--algorithms)
 * [Error Metric](https://github.com/be-ns/simpsons_analysis/blob/master/README.md#error-metric-choice)
 * [Features](https://github.com/be-ns/simpsons_analysis/blob/master/README.md#model---features)
 * [Model Rationale](https://github.com/be-ns/simpsons_analysis/blob/master/README.md#model---rationale)
3. __[Future Steps](https://github.com/be-ns/simpsons_analysis/blob/master/README.md#next-steps)__
---
### Overview
Mental Health affects nearly [1 in 5](https://www.nami.org/Learn-More/Mental-Health-By-the-Numbers) people in the US every year. This project aimed to look at how demographic information, workplace standards like wellness programs, and even the perceived stigma of mental illness would influence the likelihood of mental illness.

My initial goal was to clean the data, then use a Random Forest to obtain the top features. After this I cross-trained two models - one using Principal Component Analysis to turn the entire feature space into 5 components, the other utilizing the top 8 features from the Random Forest.
Both secondary models tested out K-Nearest Neighbors, a Support Vector Classifier, and an Ensemble Classifier using Gradient Boosting.
#### Goal
Identify any consistent indicators for those who sought treatment for mental health problems.
#### Process
* Analyze data landscape in order to understand what features are important to predicting those who sought mental health treatment
  * This was done through a Random Forest Classifier
* Attempt to model using a limited feature space to see just how precise we can get with limited feature space and ideally see the impact top features have on the predicted outcome.
#### Results
TBD
#### Tools Used
All analysis was done using local code development and cloud-based computing / analysis. An Amazon Web Services EC2 instance was utilized  


* [Python](https://www.python.org)
* [Pandas](http://pandas.pydata.org/index.html)
* [Numpy](https://docs.scipy.org/doc/numpy-1.12.0/reference/)
* [SciKitLearn](http://scikit-learn.org/stable/)
* [MatPlotLib](https://matplotlib.org/)
* [AWS (EC2)](https://www.aws.amazon.com])

### __Technical Approach__
#### __Data__
#### __Cleaning / Munging__
#### __Model Selection / Benchmarking__
In my initial benchmarking, ensemble methods tended to outperform others out of the box.
* Random Forest - F1 score of .836
* K-Nearest Neighbors - F1 score of .725
* Support Vector Classifier - F1 score of
