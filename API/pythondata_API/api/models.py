from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from sklearn.neighbors import KNeighborsClassifier
import pathlib
from pathlib import Path
import joblib

# Create your models here.

class KNNModel(models.Model):
    n_neighbors = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=7)
    weights = models.CharField(choices=[('uniform', 'uniform'),
                                        ('distance', 'distance')],
                               max_length=8,
                               default='distance')
    algorithm = models.CharField(choices=[('auto', 'auto'),
                                          ('ball_tree', 'ball_tree'),
                                          ('kd_tree', 'kd_tree'),
                                          ('brute', 'brute')],
                                 max_length=9,
                                 default='ball_tree')
    leaf_size = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=31)
    p = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=2)
    metric = models.CharField(choices=[('chebyshev', 'chebyshev'),
                                       ('cityblock', 'cityblock'),
                                       ('euclidean', 'euclidean'),
                                       ('infinity', 'infinity'),
                                       ('l1', 'l1'),
                                       ('l2', 'l2'),
                                       ('manhattan', 'manhattan'),
                                       ('minkowski', 'minkowski'),
                                       ('p', 'p'),],
                              max_length=14,
                              default='minkowski')

    model_path = models.CharField(max_length=100, null=True)
    train_score = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    test_score = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    cm_test_path = models.CharField(max_length=100, null=True)
    
    def get_sklearn_model(self):
        model = None
        if self.model_path is not None and Path(self.model_path).is_file():
            model = load(self.model_path)
        else:
            model = KNeighborsClassifier(
                        n_neighbors=self.n_neighbors,
                        weights=self.weights,
                        algorithm=self.algorithm,
                        leaf_size=self.leaf_size,
                        p=self.p,
                        metric=self.metric)
        return model
