from django.shortcuts import render, redirect

from .forms import KNNModelForm
from .models import KNNModel

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from joblib import dump, load
import pathlib
from pathlib import Path

def train_model(django_model):
    model = django_model.get_sklearn_model()
    data_path = Path('api/static/api/data.data').resolve()
    data = pd.read_csv(data_path, sep='\s+', header=None)
    data.columns = ['height', 'length', 'area', 'eccen', 'p_black', 'p_and', 'mean_tr', 'blackpix', 'blackand', 'wb_trans', 'type']
    X = data[['height','length','area','eccen','p_black','p_and','mean_tr','blackpix','blackand','wb_trans']].to_numpy()
    y = data['type'].to_numpy()
    X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=0)
    model.fit(X_train, y_train)
    model_path = Path(f'api/static/api/models/knn_{django_model.pk}.joblib').resolve()
    dump(model, model_path)
    django_model.model_path = model_path
    django_model.save()
    return model, X_train, X_test, y_train, y_test


def save_model_metric(django_model, model, X_train, X_test, y_train, y_test):
    django_model.train_score = model.score(X_train, y_train)
    django_model.test_score = model.score(X_test, y_test)
    y_test_pred = model.predict(X_test)
    cm_test = confusion_matrix(y_test, y_test_pred)
    cm_path = Path(f'api/static/api/metrics/cm_knn_{django_model.pk}.npy').resolve()
    np.save(cm_path, cm_test)
    django_model.cm_test_path = cm_path
    django_model.save()


def home(request):
    if request.method == 'POST':
        form = KNNModelForm(request.POST)
        if form.is_valid():
            django_model = form.save()
            model, X_train, X_test, y_train, y_test = train_model(django_model)
            save_model_metric(django_model, model, X_train, X_test, y_train, y_test)
            return redirect('api:model_results', django_model.pk)
    else:
        form = KNNModelForm()
    return render(request, 'api/home.html', {'form': form})

def model_results(request, pk):
    model = KNNModel.objects.get(pk=pk)
    cm_test = pd.DataFrame(np.load(model.cm_test_path),
                           index=[1, 2, 3, 4, 5],
                           columns=[1, 2, 3, 4, 5]).to_html()
    return render(request, 'api/model_results.html', {'model': model, 'cm_test': cm_test})
