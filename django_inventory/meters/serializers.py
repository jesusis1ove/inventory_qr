from rest_framework import serializers

from .models import Meter, MeterVerification


class MeterSerializer(serializers.ModelSerializer):
    verification_date = serializers.SerializerMethodField()

    class Meta:
        model = Meter
        fields = '__all__'

    def get_verification_date(self, obj):
        verification_entry = MeterVerification.objects.filter(meter=obj).order_by('-created_at').first()
        if verification_entry:
            return verification_entry['date']
        return None

    def create(self, validated_data):
        verification_date = validated_data.pop('verification_date')
        meter = Meter.objects.create(**validated_data)
        if verification_date is not None:
            MeterVerification.objects.create(meter=meter, date=verification_date)
        return meter
