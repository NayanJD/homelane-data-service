from importlib.metadata import requires
from random import choices
from secrets import choice
from rest_framework import serializers

class QueryOperatorSerializer(serializers.Serializer):
    column_name = serializers.ChoiceField(choices=['sqft_living', 'price', 'yr_built', 'yr_renovated'])
    operator = serializers.ChoiceField(choices=['gt', 'gte', 'lt', 'lte'])
    value = serializers.CharField()

class QuerySerializer(serializers.Serializer):
    table = serializers.ChoiceField(choices=['home'])
    AND = serializers.ListField(child=QueryOperatorSerializer(), required=False)
    OR = serializers.ListField(child=QueryOperatorSerializer(), required=False)
