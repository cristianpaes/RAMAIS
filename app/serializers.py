from app.models import Ramais,Empresas,Setores
from rest_framework import  serializers

class ramaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ramais
        fields = '__all__'

