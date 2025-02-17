from datetime import date

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PersonalCard, VaccinationDetail
from .serializers import PersonalCardSerializer, VaccinationDetailSerializer, PersonalCardDetailSerializer


# Create PersonalCard
@api_view(['POST'])
def create_or_get_personal_card(request):
    if request.method == 'POST':
        serializer = PersonalCardSerializer(data=request.data)
        if serializer.is_valid():
            try:
                personal_card = PersonalCard.objects.get(
                    name=serializer.validated_data['name'],
                    middle_name=serializer.validated_data.get('middle_name', None),
                    last_name=serializer.validated_data['last_name'],
                    age=serializer.validated_data['age']
                )
                created = False
            except PersonalCard.DoesNotExist:
                personal_card = serializer.save()
                created = True

            response_serializer = PersonalCardSerializer(personal_card)
            status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
            return Response(response_serializer.data, status=status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create a new VaccinationDetail
@api_view(['POST'])
def create_vaccination_detail(request):
    if request.method == 'POST':
        serializer = VaccinationDetailSerializer(data=request.data)
        if serializer.is_valid():
            try:
                personal_card = PersonalCard.objects.get(id=request.data['person'])
            except PersonalCard.DoesNotExist:
                return Response({'error': 'Personal card not found'}, status=status.HTTP_404_NOT_FOUND)

            if personal_card.vaccinated == 'No':
                personal_card.vaccinated = 'Yes'
                personal_card.save()

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List all Personal Cards ordered
@api_view(['GET'])
def list_personal_cards(request):
    if request.method == 'GET':
        personal_cards = PersonalCard.objects.all().order_by('last_name', 'name', 'middle_name')
        serializer = PersonalCardSerializer(personal_cards, many=True)
        return Response(serializer.data)

# Get information of a specific PersonalCard including vaccinations
@api_view(['GET'])
def personal_card_detail(request, pk):
    try:
        personal_card = PersonalCard.objects.get(id=pk)
    except PersonalCard.DoesNotExist:
        return Response({'error': 'Personal card not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PersonalCardDetailSerializer(personal_card)
    return Response(serializer.data)

# Check validity of vaccination for a specific person
@api_view(['GET'])
def check_vaccination_validity(request, person_id, vaccination_name):
    try:
        personal_card = PersonalCard.objects.get(id=person_id)
    except PersonalCard.DoesNotExist:
        return Response({'error': 'Personal card not found'}, status=status.HTTP_404_NOT_FOUND)

    vaccination = VaccinationDetail.objects.filter(
        person=personal_card, vaccination_name=vaccination_name
    ).first()

    now = date.today()

    if vaccination:
        is_valid = vaccination.valid_until is None or vaccination.valid_until >= now
        return Response({'valid': is_valid})
    else:
        return Response({'valid': False})
