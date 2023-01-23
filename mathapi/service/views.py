import math

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class MinView(APIView):
    def post(self, request):
        if request.data is None:
            return status.HTTP_400_BAD_REQUEST
        request_data = request.data.copy()
        numbers = request_data.get('numbers', [])
        if len(numbers) == 0:
            return status.HTTP_400_BAD_REQUEST

        min_number = float('inf')
        for num in numbers:
            min_number = min(min_number, num)
        return Response(min_number)


class MaxView(APIView):
    def post(self, request):
        if request.data is None:
            return status.HTTP_400_BAD_REQUEST
        request_data = request.data.copy()
        numbers = request_data.get('numbers', [])
        if len(numbers) == 0:
            return status.HTTP_400_BAD_REQUEST

        max_number = float('-inf')
        for num in numbers:
            max_number = max(max_number, num)
        return Response(max_number)


class AvgView(APIView):
    def post(self, request):
        if request.data is None:
            return status.HTTP_400_BAD_REQUEST
        request_data = request.data.copy()
        numbers = request_data.get('numbers', [])
        if len(numbers) == 0:
            return status.HTTP_400_BAD_REQUEST

        sum = 0
        for num in numbers:
            sum += num
        return Response(sum / len(numbers))


class MedianView(APIView):
    def post(self, request):
        if request.data is None:
            return status.HTTP_400_BAD_REQUEST
        request_data = request.data.copy()
        numbers = request_data.get('numbers', [])
        if len(numbers) == 0:
            return status.HTTP_400_BAD_REQUEST
        numbers = sorted(numbers)
        mid_idx = len(numbers) // 2
        if len(numbers) % 2 == 1:
            median = numbers[mid_idx]
        else:
            median = (numbers[mid_idx] + numbers[mid_idx + 1]) / 2
        return Response(median)


class PercentileView(APIView):
    def post(self, request):
        if request.data is None:
            return status.HTTP_400_BAD_REQUEST
        request_data = request.data.copy()
        numbers = request_data.get('numbers', [])
        percentile = request_data.get('percentile', 0)
        if len(numbers) == 0:
            return status.HTTP_400_BAD_REQUEST
        
        n  = len(numbers)
        p = n * percentile / 100
        if isinstance(p, int):
            ans = sorted(numbers)[int[p]]
        else:
            ans = sorted(numbers)[int(math.ceil(p)) - 1]
        return Response(ans)

