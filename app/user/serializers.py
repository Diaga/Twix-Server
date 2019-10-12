from django.contrib.auth import authenticate

from rest_framework import serializers

from core.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    password = serializers.CharField(
        style={'input_type': 'password', },
        trim_whitespace=False,
        write_only=True,
        min_length=5
    )

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password')
        read_only_fields = ('id', )

    def create(self, validated_data):
        """Creates a new user and returns it"""
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Updates a user correctly"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Custom token authentication serializer"""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Authenticate and return user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            email=email,
            password=password
        )

        if not user:
            msg = "Unable to authenticate with provided credentials"
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
