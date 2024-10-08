from rest_framework import serializers

WEEK_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def hours_validator(value):
    if not type(value) is list:
        raise serializers.ValidationError('Not a list')
    last_type = ''
    last_value = -1
    for list_item in value:
        if not list_item.get('type') or not list_item.get('value'):
            raise serializers.ValidationError('List item not have "type" or "value" keys')
        if list_item.get('type') not in ('open', 'close'):
            raise serializers.ValidationError('Wrong type')
        value = list_item.get('value')
        if value < 0 or value > 86399:
            raise serializers.ValidationError('Time out of bounds')
        if last_type == list_item.get('type'):
            raise serializers.ValidationError('Wrong type order')
        last_type = list_item.get('type')
        if value <= last_value:
            raise serializers.ValidationError('Wrong value or time order')
        last_value = value


class RestaurantHoursSerialiser(serializers.Serializer):
    monday = serializers.ListField(required=True, validators=[hours_validator, ])
    tuesday = serializers.ListField(required=True, validators=[hours_validator, ])
    wednesday = serializers.ListField(required=True, validators=[hours_validator, ])
    thursday = serializers.ListField(required=True, validators=[hours_validator, ])
    friday = serializers.ListField(required=True, validators=[hours_validator, ])
    saturday = serializers.ListField(required=True, validators=[hours_validator, ])
    sunday = serializers.ListField(required=True, validators=[hours_validator, ])

    class Meta:
        fields = ['week_day', 'hours']

