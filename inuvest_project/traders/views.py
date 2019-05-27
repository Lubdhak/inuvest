from django.http import HttpResponse, JsonResponse
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from .formulae import tr,pdm1

@csrf_exempt
def upload_file(request):
    myfile = request.FILES['file']
    data = pd.read_csv(myfile)
    no_of_rows = data.shape[0]
    no_of_cols = data.shape[1]

    derived_cols = []
    derived_cols.append(tr(data))
    derived_cols.append(pdm1(data))

    for col in derived_cols:
        data = data.join(col)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=results.csv'
    data.to_csv(path_or_buf=response, sep=';', float_format='%.2f', index=False, decimal=",")
    return response