# -*- coding: utf-8 -*-
"""Gensizedata

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p2NPJ18YpliKfiRw9rw9YJw4clJ16xX0

# Installation
"""

# run this cell to install pycaret in Google Colab
!pip install pycaret

# If you are using Jupyter notebook, you can pip install pycaret using jupyter notebook or command line
# pip install pycaret

from pycaret.utils import version
version()

"""# 1. Importing Dataset"""

import pandas as pd
data = pd.read_csv('Projec_final.csv')
data.info()

data

"""# 2. Setting up Environment"""

from pycaret.classification import setup
# Binarizar a coluna "Genome size (mbp)"
data['Class'] = data['Genome size (mbp)'].apply(lambda x: 0 if x <= 5.1 else 1)

# Configurar o ambiente PyCaret
exp = setup(data, target='Class', session_id=123)

data.head()

"""# 3. Compare Models"""

from pycaret.classification import compare_models
compare_models()

"""# 4. Create Model"""

from pycaret.classification import create_model
lr = create_model('lr')

dt = create_model('dt')

gbc = create_model('gbc')

knn = create_model('knn')

rf = create_model('rf')

"""# 8. Analyze Model"""

plot_model(knn)

plot_model(knn, plot = 'confusion_matrix')

plot_model(knn, plot = 'threshold')

plot_model(knn, plot = 'pr')

plot_model(knn, plot = 'vc')

plot_model(knn, plot = 'boundary')

plot_model(tuned_nb, plot = 'boundary')

plot_model(blender, plot = 'boundary')

evaluate_model(knn)

"""# Learning Resources:

- PyCaret Classification Module : https://www.pycaret.org/classification
- Binary Classification Tutorial (Level Beginner) : https://pycaret.org/clf101/
- Binary Classification Tutorial (Level Intermediate) : https://pycaret.org/clf102/
- Kaggle Titanic Predictions (Video Tutorial) : https://www.youtube.com/watch?v=nqMM6rngNCA
"""