from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico, DocIdentificacao
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from enderecos.api.serializers import EnderecoSerializer
from rest_framework.fields import SerializerMethodField
from atracoes.models import Atracao
from enderecos.models import Endereco


class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True, read_only=True)
    endereco = EnderecoSerializer(read_only=True)
    descricao_completa = SerializerMethodField()
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'comentarios', 'avaliacoes', 'endereco', 'descricao_completa', 'descricao_completa2')
        read_only_fields = ('comentarios', 'avaliacoes')
    
    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)
    
    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)
        
        endereco = validated_data['endereco']
        del validated_data['endereco']
        end = Endereco.objcts.create(**endereco)
        ponto.endereco = end
        
        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdentificacao.objects.create(**doc)
        ponto.doc_identificacao = doci
        
        ponto.save()
        
        return ponto
        
    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.endereco)
