from rest_framework import serializers

from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "content", "creation_date"]
        read_only_fields = [
            "creation_date",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["author_name"] = instance.author.username
        return representation


class PostSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="post_detail_url", lookup_field="id"
    )
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "url",
            "creation_date",
            "upvotes_amount",
            "comments",
        ]
        read_only_fields = [
            "creation_date",
            "upvotes_amount",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["author_name"] = instance.author.username
        return representation

    def create(self, validated_data):
        request = self.context.get("request")
        author = request.user
        new_post = Post.objects.create(author=author, title=validated_data["title"])
        return new_post
