from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.serializers import AdvertisementSerializer
from advertisements.models import Advertisement
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters
from advertisements.filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAuthenticated()]
        return []

    def destroy(self, request, pk=None):
        user = request.user
        advert = Advertisement.objects.get(pk=pk)
        if user != advert.creator:
            resp = {'message': 'Удалить объявление может только его автор.'}
            return Response(resp, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, pk)
