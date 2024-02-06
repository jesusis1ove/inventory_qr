from rest_framework import serializers

from .models import Meter, MeterVerification, MeterAddress


class MeterSerializer(serializers.ModelSerializer):
    verification_date = serializers.DateField(required=False)
    address = serializers.CharField(max_length=255, required=False)

    class Meta:
        model = Meter
        fields = ('__all__')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['verification_date'] = None
        representation['address'] = None
        verification_entry = MeterVerification.objects.filter(meter=instance).order_by('-created_at').first()
        address_entry = MeterAddress.objects.filter(meter=instance).order_by('-created_at').first()
        if verification_entry:
            representation['verification_date'] = verification_entry.date
        if address_entry:
            representation['address'] = address_entry.address
        return representation

    def create(self, validated_data):
        verification_date = validated_data.pop('verification_date', None)
        address = validated_data.pop('address', None)
        meter = Meter.objects.create(**validated_data)
        self.create_verification_date(meter, verification_date)
        self.create_address(meter, address)
        return meter

    def update(self, instance, validated_data):
        self.create_verification_date(instance, validated_data.pop('verification_date', None))
        self.create_address(instance, validated_data.pop('address', None))
        super().update(instance=instance, validated_data=validated_data)
        return instance

    def create_address(self, instance, address):
        if address:
            MeterAddress.objects.create(meter=instance, address=address)

    def create_verification_date(self, instance, date):
        if date:
            MeterVerification.objects.create(meter=instance, date=date)
