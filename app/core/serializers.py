from rest_framework import serializers


class DynamicModelSerializer(serializers.ModelSerializer):
    """Allows to specify fields to be included"""

    def __init__(self, *args, **kwargs):
        """Logic for specifying fields"""
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)

        super(DynamicModelSerializer, self).__init__(*args, **kwargs)

        if bool(fields) != bool(exclude):
            if fields is not None:
                allowed = set(fields)
                existing = set(self.fields)
                for field in existing - allowed:
                    self.fields.pop(field)
            elif exclude is not None:
                for field in exclude:
                    self.fields.pop(field)
