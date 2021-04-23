from rest_framework import serializers

from .models import *



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    added_at = serializers.DateTimeField(format="%d/%m/%Y %H/%M/%S", read_only=True)
    liked_by_me = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'category', 'description', 'price', 'added_at', 'number_of_likes', 'liked_by_me')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation = instance.added_by.email
        representation['images'] = ProductImageSerializer(instance.images.all(),
                                                         many=True, context=self.context).data
        return representation

    def create(self, validated_data):
        request = self.context.get('request')
        user_id = request.user.id
        validated_data['author_id'] = user_id
        product = Product.objects.create(**validated_data)
        return product

    def get_liked_by_me(self, obj):
        user = self.context['request'].user
        return user in obj.likes.all()

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
                print(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation
