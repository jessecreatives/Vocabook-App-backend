from django.db import models

class Vocabulary(models.Model):
    """Model definition for Vocabary."""

    tag = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    pronounce = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Vocabuary."""

        verbose_name = 'Vocabary'
        verbose_name_plural = 'Vocabuarys'

    def __str__(self):
        """Unicode representation of Vocabul ary."""
        return self.title

class Definition(models.Model):
    """Model definition for Definition."""

    vocabulary = models.ForeignKey(Vocabulary, related_name="definitions", on_delete=models.CASCADE)
    value = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Definition."""

        verbose_name = 'Definition'
        verbose_name_plural = 'Definitions'

    def __str__(self):
        """Unicode representation of Definition."""
        return self.value

class Example(models.Model):
    """Model definition for Example."""

    vocabulary = models.ForeignKey(Vocabulary, related_name="examples", on_delete=models.CASCADE)
    value = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Example."""

        verbose_name = 'Example'
        verbose_name_plural = 'Examples'

    def __str__(self):
        """Unicode representation of Example."""
        return self.value



