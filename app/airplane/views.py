from rest_framework import viewsets
from rest_framework.response import Response
from airplane.serializers import AirplaneSerializer, AirplaneGetResultSerializer
from airplane.models import Airplane
from drf_yasg.utils import swagger_auto_schema
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED


class AirplaneView(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    lookup_field = 'airplane_id'

    @swagger_auto_schema(responses={HTTP_201_CREATED: AirplaneSerializer})
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    @swagger_auto_schema(responses={HTTP_200_OK: AirplaneGetResultSerializer})
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = AirplaneGetResultSerializer
        return super().retrieve(request, *args, **kwargs)
