from django.contrib.auth import get_user_model
from rest_framework import serializers
User=get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,min_length=8)
    password_confirm=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["id","username","email","password","password_confirm"]
        read_only_fields=["id"]
    def validate_email(self,value):
        value=value.strip().lower()
        if User.objects.filter(email__iexact=value).exists(): raise serializers.ValidationError("Email already registered.")
        return value
    def validate(self,attrs):
        if attrs["password"] != attrs.pop("password_confirm"): raise serializers.ValidationError({"password_confirm":"Passwords do not match."})
        return attrs
    def create(self,validated_data): return User.objects.create_user(**validated_data)
