# Mental Health in the Workplace
## What can 1300 responses to a Workplace survey tell us about Mental Health?

### TABLE OF CONTENTS
1. [Overview](https://github.com/be-ns/simpsons_analysis/blob/master/README.md#overview)
 * [Goal](https://github.com/be-ns/Mental_Health#goal)
 * [Process](https://github.com/be-ns/Mental_Health#process)
 * [Results](https://github.com/be-ns/Mental_Health#results)
 * [Tools Used](https://github.com/be-ns/Mental_Health#tools-used)
2. [Technical Approach](https://github.com/be-ns/Mental_Health#technical_approach)
 * [Data](https://github.com/be-ns/Mental_Health#data)
 * [Cleaning / Munging](https://github.com/be-ns/Mental_Health#cleaning)
 * [Model Selection / Benchmarking](https://github.com/be-ns/simpsons_analysis/blob/master/README.md#model-selection--benchmarking)
 * [Modeling Process](https://github.com/be-ns/simpsons_analysis/blob/master/README.md#modeling--algorithms)
 * [Error Metric](https://github.com/be-ns/simpsons_analysis/blob/master/README.md#error-metric-choice)
 * [Features](https://github.com/be-ns/simpsons_analysis/blob/master/README.md#model---features)
 * [Model Rationale](https://github.com/be-ns/simpsons_analysis/blob/master/README.md#model---rationale)
3. [Future Steps](https://github.com/be-ns/simpsons_analysis/blob/master/README.md#next-steps)
---
#### Goal
Do an analysis on survey data from 2016 to see if there are any consistent indicators of seeking treatment for mental health problems.
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
