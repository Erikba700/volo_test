from rest_framework import serializers
from .models import PersonalCard, VaccinationDetail

class PersonalCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalCard
        fields = ['id', 'name', 'middle_name', 'last_name', 'age', 'gender', 'vaccinated']
        read_only_fields = ['id']

class VaccinationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinationDetail
        fields = ['id', 'person', 'place', 'vaccination_date', 'vaccination_name', 'valid_until']
        read_only_fields = ['id']

class PersonalCardDetailSerializer(PersonalCardSerializer):
    vaccinations = VaccinationDetailSerializer(many=True, read_only=True)

    class Meta(PersonalCardSerializer.Meta):
        fields = PersonalCardSerializer.Meta.fields + ['vaccinations']
