from rest_framework import serializers, exceptions
from user.models import TripyUser


class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, style={'input_type': 'password'}, required=False)
    first_name = serializers.CharField(max_length=127, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=127, required=False, allow_blank=True)
    address = serializers.CharField(max_length=255, required=False, allow_null=True, allow_blank=True)
    phone = serializers.CharField(max_length=63, required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = TripyUser
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'address', 'phone',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        else:
            raise exceptions.ValidationError('Password is required!')
        instance.save()
        return instance
