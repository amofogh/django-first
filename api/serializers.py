from rest_framework import serializers

from Eshop_news.models import news
from Eshop_products.models import products

class ProductSerilizer(serializers.ModelSerializer):

    def get_tag(self, obj):
        tags = []
        for object in obj.tag.all():
            tags.append(object.title) 
        return tags

    def get_category(self, obj):
        categories = []
        for object in obj.category.all():
            categories.append(object.title) 
        return categories
        
    tag = serializers.SerializerMethodField('get_tag')
    category = serializers.SerializerMethodField('get_category')
    
    class Meta:
        model = products
        fields = '__all__'
        
class NewsSerializer(serializers.ModelSerializer):
    
    def get_username(self,obj):
        return obj.user.username
    
    user = serializers.SerializerMethodField('get_username')
    class Meta:
        model = news
        fields = '__all__'