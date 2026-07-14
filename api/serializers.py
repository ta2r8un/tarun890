from rest_framework import serializers
from .models import Service, Feature, Technology, Outcome


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ["title"]


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ["name"]


class OutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outcome
        fields = ["label", "value"]


class ServiceSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True, read_only=True)
    technologies = TechnologySerializer(many=True, read_only=True)
    outcomes = OutcomeSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = [
            "id",
            "slug",
            "name",
            "short",
            "description",
            "starting_price",
            "icon",
            "features",
            "technologies",
            "outcomes",
        ]