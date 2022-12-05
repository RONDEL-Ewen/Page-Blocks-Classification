from django import forms
from .models import KNNModel

class KNNModelForm(forms.ModelForm):
    class Meta:
        model = KNNModel
        fields = ['n_neighbors',
                  'weights',
                  'algorithm',
                  'leaf_size',
                  'p',
                  'metric']
        labels = {'n_neighbors': 'Number of neighbors',
                  'weights': 'Weights',
                  'algorithm': 'Algorithm',
                  'leaf_size': 'Leaf size',
                  'p': 'P',
                  'metric': 'Metric'}
