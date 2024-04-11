import json
import logging

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status


from entries.integrations.api.serializers import CallDataInfoSerializer




CURRENT_DEALS = []
logger = logging.getLogger(__name__)


def flatten_data(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


class FormResponseAPI(CreateAPIView):
    serializer_class = CallDataInfoSerializer

    @staticmethod
    def get_str_form_response(form_response: list):
        return settings.FORM_SPLIT_QUESTION_SYMBOL.join([
            f"{question.get('question_name', '').replace(settings.FORM_SPLIT_ANSWER_SYMBOL, '')}"
            f"{settings.FORM_SPLIT_ANSWER_SYMBOL}"
            f"{question.get('answer_values', '')[0]}"
            for question in form_response
        ])

    # def post(self, request, *args, **kwargs):
    #     logger.info(json.dumps(request.data))
    #     print(1)
    #     data = flatten_data(request.data)
    #     print(request.data.get("form_response", ""))
    #     #data["form_response"] = self.get_str_form_response(request.data.get("form_response", "").get("answers", ""))
    #     serializer = self.serializer_class(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        logger.info(json.dumps(request.data))
        serializer = self.serializer_class(data=flatten_data(request.data))
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)



class TestAPI(APIView):
    def get(self, request):
        data = dict()
        return Response(data=data, status=status.HTTP_200_OK)