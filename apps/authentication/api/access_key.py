# -*- coding: utf-8 -*-
#

from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.response import Response

from authentication.permissions import UserConfirmation
from common.api import JMSModelViewSet
from rbac.permissions import RBACPermission
from ..const import ConfirmType
from ..serializers import AccessKeySerializer


class AccessKeyViewSet(JMSModelViewSet):
    serializer_class = AccessKeySerializer
    search_fields = ['^id']
    permission_classes = [RBACPermission]

    def get_queryset(self):
        return self.request.user.access_keys.all()

    def get_permissions(self):
        if self.is_swagger_request():
            return super().get_permissions()

        if self.action == 'create':
            self.permission_classes = [
                RBACPermission, UserConfirmation.require(ConfirmType.PASSWORD)
            ]
        return super().get_permissions()

    def perform_create(self, serializer):
        user = self.request.user
        if user.access_keys.count() >= 10:
            raise serializers.ValidationError(_('Access keys can be created at most 10'))
        key = user.create_access_key()
        return key

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        key = self.perform_create(serializer)
        return Response({'secret': key.secret, 'id': key.id}, status=201)
