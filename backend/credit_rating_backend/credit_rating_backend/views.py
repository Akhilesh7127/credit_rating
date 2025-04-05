from.logging_config import logger
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .view_helper import determine_credit_rating
@api_view(['GET', 'POST'])
def mortgage_list_create(request):
    if request.method == 'GET':
        mortgages = Mortgage.objects.all().values()
        logger.info('Fetched mortgage list')
        return Response(list(mortgages))
    
    elif request.method == 'POST':
        errors = validate_mortgage_data(request.data)
        if errors:
            return Response(errors, status=400)
        credit_rating=determine_credit_rating(request.data)
        mortgage = Mortgage.objects.create(**{**request.data,'credit_rating': credit_rating})
        logger.info(f'Created mortgage entry: {mortgage.id}')
        response_data = {**request.data, 'credit_rating': mortgage.credit_rating}
        return Response(response_data, status=201)

@api_view(['PUT', 'DELETE'])
def mortgage_detail(request, pk):
    try:
        mortgage = Mortgage.objects.get(pk=pk)
    except Mortgage.DoesNotExist:
        logger.error(f'Mortgage ID {pk} not found')
        return Response({'error': 'Mortgage not found'}, status=404)
    
    if request.method == 'PUT':
        errors = validate_mortgage_data(request.data)
        if errors:
            return Response(errors, status=400)
        
        for key, value in request.data.items():
            setattr(mortgage, key, value)
        credit_rating=determine_credit_rating(request.data)
        mortgage.credit_rating=credit_rating
        mortgage.save()
        logger.info(f'Updated mortgage ID {pk}')
        return Response({**request.data, 'credit_rating': credit_rating},status=200)
    
    elif request.method == 'DELETE':
        mortgage.delete()
        logger.info(f'Deleted mortgage ID {pk}')
        return Response({'message': 'Deleted mortgage entry'}, status=200)
def validate_mortgage_data(data):
    errors = {}
    if not (300 <= data.get('credit_score', 0) <= 850):
        errors['credit_score'] = 'Credit score must be between 300 and 850.'
    if data.get('loan_amount', 0) <= 0:
        errors['loan_amount'] = 'Loan amount must be greater than zero.'
    if data.get('property_value', 0) <= 0:
        errors['property_value'] = 'Property value must be greater than zero.'
    if data.get('annual_income', 0) <= 0:
        errors['annual_income'] = 'Annual income must be greater than zero.'
    if data.get('debt_amount', 0) < 0:
        errors['debt_amount'] = 'Debt amount cannot be negative.'
    if 'loan_type' not in data or data['loan_type'] not in ['fixed', 'adjustable']:
        errors['loan_type'] = 'Loan type must be either fixed or adjustable.'
    if 'property_type' not in data or data['property_type'] not in ['single_family', 'condo']:
        errors['property_type'] = 'Property type must be either single_family or condo.'
    if errors:
        logger.warning(f'Validation errors: {errors}')
        return errors
    return None