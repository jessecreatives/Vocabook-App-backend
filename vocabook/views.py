from rest_framework import viewsets

from .models import Vocabulary, Definition, Example
from .serializers import VocabularySerializer, DefinitionSerializer, ExampleSerializer

class VocabularyViewSet(viewsets.ModelViewSet):
    serializer_class = VocabularySerializer
    queryset = Vocabulary.objects.all()

class DefinitionViewSet(viewsets.ModelViewSet):
    serializer_class = DefinitionSerializer
    queryset = Definition.objects.all()

class ExampleViewSet(viewsets.ModelViewSet):
    serializer_class = ExampleSerializer
    queryset = Example.objects.all()