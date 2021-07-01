from rest_framework import serializers
from .models import Student

# def start_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError("Value Should Be Start with 'R'")

class StudentSerializer(serializers.ModelSerializer):
    # # name = serializers.CharField(read_only = True)
    # name = serializers.CharField(validators = [start_with_r])
    class Meta:
        model = Student
        fields = '__all__'
        # read_only_fields = ['name', 'city']
    # Field level validation
    def validate_roll(self, value):
        if value  >= 200:
            raise serializers.ValidationError("Seats are full")
        return value

    # # Object Level Validation
    # def validate(self, data):
    #     if data['name'].lower() == "rizwan" and data['city'] != "Okara":
    #         raise serializers.ValidationError("City name must be 'Okara'")
    #         return data






















# # Validators
# def start_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError("Value Should Start with 'R'")
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length = 100, validators = [start_with_r])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length = 100)
#     # Create new object
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     # Update
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance
# # Field Level validation
#     def validate_roll(self, value):
#         if value >= 200:
#             raise serializers.ValidationError("Seats are Full")
#         return value
# # Object level Validation
#     def validate(self, data):
#         a = data['name']
#         b = data.get('city')
#         if a.lower() == 'rizwan' and b.lower() != 'okara':
#             raise serializers.ValidationError("City Must Be Okara")
#             return data 