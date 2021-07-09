from rest_framework import serializers

from .models import Benefactor
from .models import Charity, Task


class BenefactorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Benefactor
        fields = ['experience', 'free_time_per_week']

    def create(self, validated_data):
        benefactor = Benefactor(experience=validated_data['experience'],
                                free_time_per_week=validated_data['free_time_per_week'])
        benefactor.save()
        return benefactor


class CharitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Charity
        fields = ['name', 'reg_number']

    def create(self, validated_data):
        charity = Charity(name=validated_data['name'], reg_number=validated_data['reg_number'])
        charity.save()
        return charity


class TaskSerializer(serializers.ModelSerializer):
    pass
