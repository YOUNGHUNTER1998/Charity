from rest_framework import serializers

from .models import User

from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'phone', 'address', 'gender',
                  'age', 'description', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            password=make_password(validated_data['password']),
            phone=validated_data['phone'],
            address=validated_data['address'],
            gender=validated_data['gender'],
            age=validated_data['age'],
            description=validated_data['description'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.save()
        return user
