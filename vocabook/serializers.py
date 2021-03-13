from rest_framework import serializers

from .models import Example, Definition, Vocabulary

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = '__all__'

class DefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definition
        fields = '__all__'

class VocabularySerializer(serializers.ModelSerializer):
    definitions = DefinitionSerializer(many=True, required=False)
    examples = ExampleSerializer(many=True, required=False)
    class Meta:
        model = Vocabulary
        fields = ['id', 'tag', 'date', 'title', 'pronounce', 'definitions', 'examples']