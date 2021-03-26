from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny

from .models import Progammer, ProgrammerImage, City, Rating

class Test(ListModelMixin):
    pass