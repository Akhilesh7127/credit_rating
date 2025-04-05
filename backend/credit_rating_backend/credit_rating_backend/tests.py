import unittest
from unittest.mock import patch, MagicMock
from django.test import RequestFactory
from rest_framework.test import force_authenticate
from rest_framework import status
from .views import mortgage_list_create, mortgage_detail
from .models import Mortgage

class MortgageViewTests(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.valid_data = {
            "credit_score": 750,
            "loan_amount": 200000,
            "property_value": 250000,
            "annual_income": 60000,
            "debt_amount": 15000,
            "loan_type": "fixed",
            "property_type": "single_family"
        }

    @patch('credit_rating_backend.credit_rating_backend.views.Mortgage.objects')
    def test_get_all_mortgages(self, mock_objects):
        mock_objects.all.return_value.values.return_value = [self.valid_data]
        request = self.factory.get('/api/mortgages/')
        response = mortgage_list_create(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    @patch('credit_rating_backend.credit_rating_backend.views.Mortgage.objects.create')
    @patch('credit_rating_backend.credit_rating_backend.views.determine_credit_rating')
    def test_create_valid_mortgage(self, mock_rating, mock_create):
        mock_rating.return_value = 'AAA'
        mock_create.return_value = MagicMock(id=1, credit_rating='AAA')
        request = self.factory.post('/api/mortgages/', data=self.valid_data, content_type='application/json')
        response = mortgage_list_create(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['credit_rating'], 'AAA')

    def test_create_invalid_mortgage(self):
        invalid_data = self.valid_data.copy()
        invalid_data['credit_score'] = 100  # invalid score
        request = self.factory.post('/api/mortgages/', data=invalid_data, content_type='application/json')
        response = mortgage_list_create(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('credit_score', response.data)

    @patch('credit_rating_backend.credit_rating_backend.views.Mortgage.objects.get')
    @patch('credit_rating_backend.credit_rating_backend.views.determine_credit_rating')
    def test_put_mortgage_update(self, mock_rating, mock_get):
        mock_rating.return_value = 'BBB'
        mortgage = MagicMock()
        mortgage.credit_rating = 'AAA'
        mock_get.return_value = mortgage
        request = self.factory.put('/api/mortgages/1/', data=self.valid_data, content_type='application/json')
        response = mortgage_detail(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['credit_rating'], 'BBB')

    @patch('credit_rating_backend.credit_rating_backend.views.Mortgage.objects.get')
    def test_delete_mortgage(self, mock_get):
        mortgage = MagicMock()
        mock_get.return_value = mortgage
        request = self.factory.delete('/api/mortgages/1/')
        response = mortgage_detail(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Deleted mortgage entry')

    @patch('credit_rating_backend.credit_rating_backend.views.Mortgage.objects.get')
    def test_get_mortgage_not_found(self, mock_get):
        mock_get.side_effect = Mortgage.DoesNotExist()
        request = self.factory.put('/api/mortgages/999/', data=self.valid_data, content_type='application/json')
        response = mortgage_detail(request, pk=999)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('error', response.data)
