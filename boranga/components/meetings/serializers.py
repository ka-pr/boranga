import logging

from django.conf import settings
from ledger_api_client.ledger_models import EmailUserRO as EmailUser, Address
from boranga.components.meetings.models import(
        Meeting,
    )
from boranga.ledger_api_utils import retrieve_email_user
from rest_framework import serializers
from django.db.models import Q


class ListMeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = (
                'id',
                'start_date',
                'end_date',
                'location',
                'title',
                
            )
        datatables_always_serialize = (
                'id',
                'start_date',
                'end_date',
                'location',
                'title',
            )  
        
class MeetingSerializer(serializers.ModelSerializer):
    #processing_status = serializers.SerializerMethodField(read_only=True)
    start_date= serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    end_date= serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Meeting
        fields = (
                'id',
                'start_date',
                'end_date',
                'location',
                'title',
                'meeting_type',
                'processing_status'
                
            )
        
    def get_processing_status(self,obj):
        return obj.get_processing_status_display()
    
class EditMeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = (
                'id',
                'start_date',
                'end_date',
                'location',
                'title',
                'meeting_type',
                'processing_status'
                
            )