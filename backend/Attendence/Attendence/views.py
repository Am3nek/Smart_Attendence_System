#here we create all the endpoints
from django.http import JsonResponse,HttpResponse
from .models import StudentData
from .serializers import SDataSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render


verify = set()

#This function will take a get request
@api_view(['GET'])
def SData_list(request):
    if request.method == 'GET':
        SData = StudentData.objects.all()
        serilizer = SDataSerializers(SData,many = True)
        return Response({'Sdata':serilizer.data})
        #return HttpResponse(serilizer.data)
        
@api_view(['GET'])
def verify_Attendence(request, Reg_num):
    try:
        SD_Data = StudentData.objects.get(pk = Reg_num)
    except StudentData.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        if (SD_Data.vESP and SD_Data.vRFID):
            SD_Data.attendence = 'P'
            SD_Data.save()
            return Response({
                "val":"P"
                })
        else:
            SD_Data.attendence = 'A'
            SD_Data.save()
            return Response({
                "val":'A'
                })
        
@api_view(['GET'])
def RFID_data(request,RFID_num):
    try:
        SD_Data = StudentData.objects.get(RFID = RFID_num)
        global data_RFID
        data_RFID = SD_Data.Reg_num
        print("Working : RFID", data_RFID)
        SD_Data.vRFID = True
        SD_Data.save()
        return Response(status.HTTP_200_OK)
    except StudentData.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
   

@api_view(['GET'])
def ESP32_data(request,ESP_32):
    try:
        cam_data = StudentData.objects.get(pk = ESP_32)
        cam_data.vESP = True
        cam_data.save()
        print("Working")
        return Response(status.HTTP_200_OK )
    except StudentData.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
