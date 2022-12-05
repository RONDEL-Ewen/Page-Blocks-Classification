# Page-Blocks-Classification

Ewen RONDEL - Brahim TALB - Alexandre SMADJA

## Dataset

The 'page-blocks.data' file is the result of a segmentation process realized on different documents and has been made available by Donato Malerba. 
The dataset it contains represents **10 characteristics** of all the blocks of the page layout of those documents and their types.
And we can count **5 different types** among those blocks:
  - text;
  - horizontal line;
  - graphic;
  - vertical line;
  - picture.

The dataset is composed of **5473 lines**.

## Task

The original problem of Donato Malerba was to find a way to classify all the blocks of the page layout of a document.
That's why we have trained multiple **machine learning** models (and one **deep learning model**) on this dataset, in order to be able to classify thoses blocks.
Obviously, as the data is labelled, we have used supervised learning, but we have diversified the models to find the one with the best accuracy.
Here is a list of the models we used, all from **Scikit-learn**:
  - Linear Regression;
  - Logistic Regression;
  - Linear Discriminant Analysis;
  - Linear Classifiers with Stochastic Gradient Descent;
  - Gaussian Naive Bayes;
  - Decision Tree Classifier;
  - Random Forest Classifier;
  - K-Nearest Neighbors;
  - Multi-Layer Perceptron Classifier.

## Conclusion

After training our models, we have compared them, and our comparison was based on 3 major characteristics: training time, training score, testing score. 
And according to their performances, we decided that the **Decision Tree Classifier** was the most efficient model we had.
Here are its **performances**:
  - Training time: 1.562s;
  - Training score: 95.3%;
  - Testing score: 96.0%.
  
Afterwards, we created an **API** that makes predictions based on our dataset. 
It obviously uses a Decision Tree Classifier with the **best parameteres** that we determined:
  - 'criterion': 'gini';
  - 'max_depth': 4;
  - 'max_features': 'log2';
  - 'min_samples_leaf': 4;
  - 'min_samples_split': 3;
  - 'splitter': 'best'.

Our API has those parameters by default but you can play with it as you want and change every parameter with drop-down menus.
