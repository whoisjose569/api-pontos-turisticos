from django.http import HttpResponse
from rest_framework.viewsets import  ModelViewSet
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = [SearchFilter]
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    search_fields = ['nome', 'descricao', 'endereco__linha1']
    #O lookup_field precisa ser unico 
    #lookup_field = 'nome'
    
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)
            
        #return PontoTuristico.objects.filter(aprovado=True)
        return queryset
    
    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, id):
        atracoes = request.data['ids']
        
        ponto = PontoTuristico.objects.get(id=id)
        
        ponto.atracoes.set(atracoes)
        
        ponto.save()
        
        return HttpResponse('ok')
    
    # def list(self, request, *args, **kwargs):
    #     return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)
    
    # def create(self, request, *args, **kwargs):
    #     return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)
    
    # def destroy(self, request, *args, **kwargs):
    #     return super(PontoTuristicoViewSet).destroy(request, *args, **kwargs)
    
    # def retrieve(self, request, *args, **kwargs):
    #     return super(PontoTuristicoViewSet).retrieve(request, *args, **kwargs)
    
    # def update(self, request, *args, **kwargs):
    #     return super(PontoTuristicoViewSet).update(request, *args, **kwargs)
    
    # def partial_update(self, request, *args, **kwargs):
    #     return super(PontoTuristicoViewSet).partial_update(request, *args, **kwargs)
    
    # Criar novas açoes
    # @action(methods=['get'], detail=True)
    # def denunciar(self, request, pk=None):
    #     pass
    
    # @action(methods=['get'], detail=False)
    # def teste(self, request):
    #     pass
        
