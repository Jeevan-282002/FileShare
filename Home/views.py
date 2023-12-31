from django.shortcuts import render
from rest_framework.views import APIView
from . models import FilesModel, FolderModel
from . serializers import FileSerializer, FileListSerializer
from rest_framework.response import Response
from django.views import View

# Create your views here.


def download(request, uid):
    context = {'uid': uid}
    return render(request, "Home/download.html", context)


class HandleFileUpload(APIView):
    def post(self, request):
        try:
            data = request.data

            serializer = FileListSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Files Uploaded Successfully', 'data': serializer.data})

            return Response({'message': 'Something went wrong', 'data': serializer.errors})

        except Exception as e:
            print(e)

    def get(self, request):
        data = FilesModel.objects.all()

        serializer = FileSerializer(data, many=True)

        return Response(serializer.data)


class Home_view(View):

    def get(self, request):
        return render(request, 'Home/Home.html')
