from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from data_service.service.models.home import Home
from .serializers import QuerySerializer, HomeSerializer

class QueryData(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Home.objects.all()

    serializer_class = QuerySerializer


    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        print(serializer.data)
        table = serializer.data['table']
        and_predicates = serializer.data.get('AND', None)
        or_predicates = serializer.data.get('OR', None)


        if table == 'home':
            query = Q()

            if and_predicates:
                for predicate in and_predicates:
                    column_name = predicate['column_name']
                    operator = predicate['operator']
                    value= predicate['value']

                    temp = {f'{column_name}__{operator}': value}

                    query = query & Q(**temp)

            if or_predicates:
                for predicate in or_predicates:
                    column_name = predicate['column_name']
                    operator = predicate['operator']
                    value= predicate['value']

                    temp = {f'{column_name}__{operator}': value}

                    query = query | Q(**temp)
            
            
            homes = Home.objects.filter(query).prefetch_related('address')

            print(homes.count())

        return Response(HomeSerializer(homes, many=True).data)


