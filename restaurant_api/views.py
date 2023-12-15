from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from restaurant_api.serializers import RestaurantHoursSerialiser


class RestHoursView(APIView):

    def get(self, request):
        data = RestaurantHoursSerialiser(data=request.data)
        if data.is_valid():
            dict_data = data.validated_data
            result = ''
            new_dict = dict.fromkeys(dict_data.keys(), "")
            new_key = new_dict.keys()
            for key, value in dict_data.items():
                if not value:
                    # result += '\r\n' + key + ': Closed'
                    new_dict[key] = 'Closed'
                else:
                    for idx, item in enumerate(value):
                        item_type = item.get('type')
                        if item_type == 'open':
                            if idx != 0 and new_key == key:
                                new_dict[new_key] += ', '
                            else:
                                new_key = key
                            r_date = datetime.utcfromtimestamp(item.get('value')).time()
                            s_time = f'{r_date.hour}' + \
                                     (f':{r_date.minute}' if r_date.minute else '') + \
                                     f' {r_date.strftime("%p")}'
                            new_dict[new_key] += f'{s_time} - '
                        if item_type == 'close':
                            r_date = datetime.utcfromtimestamp(item.get('value')).time()
                            s_time = f'{r_date.hour}' + \
                                     (f':{r_date.minute}' if r_date.minute else '') + \
                                     f' {r_date.strftime("%p")}'
                            new_dict[new_key] += s_time
                result = ''
            for key, value in new_dict.items():
                result += f"{key}: {value}\r\n"

            return HttpResponse(result)
        else:
            return Response(data=data.errors)



