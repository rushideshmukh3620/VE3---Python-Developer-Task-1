from django.shortcuts import render
from .forms import UploadFileForm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def home(request):
    return render(request, 'analysis/home.html')

def handle_uploaded_file(f):
    upload_dir = 'uploaded_files/'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    file_path = os.path.join(upload_dir, f.name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_uploaded_file(request.FILES['file'])
            return analyze_file(request, file_path)
    else:
        form = UploadFileForm()
    return render(request, 'analysis/upload.html', {'form': form})

def analyze_file(request, file_path):
    data = pd.read_csv(file_path)

    # Perform basic analysis
    head = data.head()
    desc = data.describe()
    missing_values = data.isnull().sum()

    # Generate plots
    plots = {}
    for column in data.select_dtypes(include=[np.number]).columns:
        plt.figure()
        sns.histplot(data[column])
        plot_path = f'static/plots/{column}.png'
        plt.savefig(plot_path)
        plt.close()
        plots[column] = plot_path

    context = {
        'head': head.to_html(),
        'desc': desc.to_html(),
        'missing_values': missing_values.to_frame().to_html(),
        'plots': plots,
    }

    return render(request, 'analysis/result.html', context)
