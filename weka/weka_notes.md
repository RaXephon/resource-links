####Weka Notes

This is a hands-on task using Weka.  Please load the dataset “mailing_tree.arff" and build a tree using the J48 classifier induction technique.  

Recall: you choose the induction technique using the Choose button on the Classify tab; J48 is under “trees”.  Before you run the algorithm, please change the minNumObj option to 100. You get to the option menu by right clicking on the bar next to the ‘Choose’ button that should say ‘J48’ after you selected the technique. Copy the results from the large window and submit with your homework.  Look through the statistics at the bottom.  We will cover many of those in the weeks that follow, as we build up a repertoire of model performance analytics.

[J48 Tree options](https://github.com/reshama/resource-links/blob/master/weka/j48_tree.png)

--
```
WEKA Explorer
Open File
    Mailing_tree.arff

2nd tab:  Classify
Classifier / Choose
Weka/classifiers/trees/J48

At Classify/Choose, right click and a window will open up.
4th row down is “minNumObj”
change this to “100”
click:  OK

To run algorithm:
Hit:  “Start”
```

```
=== Run information ===

Scheme:weka.classifiers.trees.J48 -C 0.25 -M 100
Relation:     mailingx
Instances:    9999
Attributes:   10
              income
              Firstdate
              Lastdate
              Amount
              rfaf2
              rfaa2
              pepstrfl
              glast
              gavr
              class
Test mode:10-fold cross-validation

=== Classifier model (full training set) ===

J48 pruned tree
------------------

pepstrfl = 0
|   Amount <= 0.12: 0 (2874.0/1104.0)
|   Amount > 0.12
|   |   rfaa2 = D: 1 (109.0/41.0)
|   |   rfaa2 = E
|   |   |   Lastdate <= 9512: 1 (262.0/125.0)
|   |   |   Lastdate > 9512: 0 (332.0/157.0)
|   |   rfaa2 = F
|   |   |   income = 0: 0 (201.0/96.0)
|   |   |   income = 1: 0 (76.0/32.0)
|   |   |   income = 2: 0 (116.0/58.0)
|   |   |   income = 3: 0 (65.0/32.0)
|   |   |   income = 4: 0 (126.0/55.0)
|   |   |   income = 5: 0 (128.0/58.0)
|   |   |   income = 6: 1 (81.0/34.0)
|   |   |   income = 7: 1 (65.0/28.0)
|   |   rfaa2 = G: 0 (256.0/101.0)
pepstrfl = X
|   rfaf2 = 1
|   |   Lastdate <= 9604
|   |   |   income = 0: 0 (292.0/127.0)
|   |   |   income = 1: 0 (135.0/38.0)
|   |   |   income = 2: 0 (221.0/96.0)
|   |   |   income = 3: 1 (126.0/62.0)
|   |   |   income = 4: 1 (181.0/80.0)
|   |   |   income = 5: 0 (272.0/128.0)
|   |   |   income = 6: 1 (118.0/55.0)
|   |   |   income = 7: 1 (122.0/59.0)
|   |   Lastdate > 9604: 1 (121.0/43.0)
|   rfaf2 = 2: 1 (1172.0/522.0)
|   rfaf2 = 3: 1 (1249.0/475.0)
|   rfaf2 = 4: 1 (1299.0/464.0)

Number of Leaves  : 	25

Size of the tree : 	33


Time taken to build model: 0.22 seconds

=== Stratified cross-validation ===
=== Summary ===

Correctly Classified Instances        5809               58.0958 %
Incorrectly Classified Instances      4190               41.9042 %
Kappa statistic                          0.1619
Mean absolute error                      0.4806
Root mean squared error                  0.4918
Relative absolute error                 96.1235 %
Root relative squared error             98.3563 %
Total Number of Instances             9999     

=== Detailed Accuracy By Class ===

               TP Rate   FP Rate   Precision   Recall  F-Measure   ROC Area  Class
                 0.608     0.446      0.577     0.608     0.592      0.604    0
                 0.554     0.392      0.585     0.554     0.569      0.604    1
Weighted Avg.    0.581     0.419      0.581     0.581     0.581      0.604

=== Confusion Matrix ===

    a    b   <-- classified as
 3039 1961 |    a = 0
 2229 2770 |    b = 1


```
