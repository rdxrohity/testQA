from rest_framework import viewsets
from .models import *
from .serializers import *
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
import pandas as pd
import io
from django.shortcuts import render

class SampleDataView(ListView):
    model = SampleData
    template_name = 'sampledataview.html'

class SampleDataViewSet(viewsets.ModelViewSet):
    serializer_class = SampleDataSerializer
    queryset = SampleData.objects.all()

class CsvUploader(TemplateView):

    template_name = 'upload.html'

    def post(self, request):

        context = {
            'messages':[]
        }

        csv = request.FILES['csv']
        csv_data = pd.read_csv(
            io.StringIO(
                csv.read().decode("utf-8")
            )
        )

        for record in csv_data.to_dict(orient="records"):
            try:
                SampleData.objects.create(
                    guid = record['guid'],
                    geo_latitude = record['geo_latitude'],
                    geo_longitude = record['geo_longitude'],
                    date_y_m_d = record['date_y_m_d'],
                    numeric_00 = record['numeric_00'],
                    numeric_01 = record['numeric_01']
                )
            except Exception as e:
                context['exceptions_raised'] = e
                
        return render(request, self.template_name, context)