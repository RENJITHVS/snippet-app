from rest_framework import serializers
from .models import Snippet,Tag
from users.serializers import CustomUserSerializer

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title']

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True)
    url = serializers.HyperlinkedIdentityField(view_name="snippetapp:retrive_update_destroy_snippet_items")
    
    class Meta:
        model = Snippet
        fields = ('title', 'text', 'timestamp', 'tags', 'url',)
        read_only_fields = ['url']
        

    
class SnippetCreateUpdateSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)


    class Meta:
        model = Snippet
        fields = ['title', 'text', 'tags']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        snippet = Snippet.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(title=tag_data['title'])
            snippet.tags.add(tag)
        return snippet

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.save()

        instance.tags.clear()
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(title=tag_data['title'])
            instance.tags.add(tag)
        return instance    

