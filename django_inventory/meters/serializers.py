from rest_framework import serializers

from .models import Meter, MeterVerification


class MeterSerializer(serializers.ModelSerializer):
    verification_date = serializers.SerializerMethodField()

    class Meta:
        model = Meter
        fields = ('__all__')

    def get_verification_date(self, obj):
        verification_entry = MeterVerification.objects.filter(meter=obj).order_by('-created_at').first()
        if verification_entry:
            return verification_entry.date
        return None


class MeterCreateSerializer(serializers.ModelSerializer):
    verification_date = serializers.DateField(required=False)

    class Meta:
        model = Meter
        fields = ('__all__')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['verification_date'] = None
        verification_entry = MeterVerification.objects.filter(meter=instance).order_by('-created_at').first()
        if verification_entry:
            representation['verification_date'] = verification_entry.date
        return representation

    def create(self, validated_data):
        verification_date = validated_data.pop('verification_date')
        meter = Meter.objects.create(**validated_data)
        if verification_date is not None:
            MeterVerification.objects.create(meter=meter, date=verification_date)
        return meter


class MeterUpdateSerializer(serializers.ModelSerializer):
    verification_date = serializers.DateField(required=False)

    class Meta:
        model = Meter
        exclude = ('uuid', 'created_at', 'updated_at')

    def update(self, instance, validated_data):
        verification_date = validated_data.pop('verification_date')
        if verification_date:
            MeterVerification.objects.create(meter=instance, date=verification_date)
        super().update(instance=instance, validated_data=validated_data)
        return instance
