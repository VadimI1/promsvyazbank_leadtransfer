import json
import logging

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status


from ...integrations.api.serializers import CallDataInfoSerializer
from ...service.validation import SkorozvonCall
from ...service.integration import create_PSB_deal_by_call, create_my_business_deal_by_call
from ...service.exceptions import ScenarioNotFoundError, UnsuccessfulLeadCreationError, CategoryNotFoundError, SkorozvonAPIError





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

    def post(self, request, *args, **kwargs):
        logger.info(json.dumps(request.data))
        info = flatten_data(request.data)
        serializer = self.serializer_class(data=info)
        if serializer.is_valid() and info['call_scenario_id'] in [50000006506, 50000014323]:
            serializer.save()
            lead_info = SkorozvonCall.model_validate(info)
            #print(lead_info)
            try:
                if lead_info.scenario_id == 50000006506: # ПСБ
                    pass
                    #create_PSB_deal_by_call(lead_info)
                elif lead_info.scenario_id == 50000014323:
                    create_my_business_deal_by_call(lead_info)
            except (ScenarioNotFoundError, UnsuccessfulLeadCreationError, CategoryNotFoundError, SkorozvonAPIError):
                pass
            except Exception:
                pass
        return Response(status=status.HTTP_201_CREATED)



class TestAPI(APIView):
    def get(self, request):
        data = dict()
        return Response(data=data, status=status.HTTP_200_OK)