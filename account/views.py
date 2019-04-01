from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import tabula
from .models import Save
from django.http import JsonResponse
import csv,json,os
import subprocess
from tika import parser
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings


# Create your views here.
@csrf_exempt
def upload_file(request):
    template="upload.html"
    if request.method=="POST":
        file=request.FILES["myfile"] #file taken
        f='somename.pdf'
        path = default_storage.save('somename.pdf', ContentFile(file.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
#------------- finding account holder's name-----------------
        raw = parser.from_file(f)
        for i in range(len(raw["content"])):
            if raw["content"][i] == "\t":
                break
        for j in range(i, len(raw["content"])):
            if raw["content"][j] == "\n":
                break
        name= ""
        for t in range(i + 1, j):
             name+=raw["content"][t]
        namef=" ".join(name.split())
        print(namef)
#--------------name found--------------------
#-----------converting pdf to csv  and json-------------------
        tabula.convert_into(f, "output.csv",lattice=True,pages='all',output_format="csv")
        # Open the CSV
        f = open('output.csv', 'r')
        # Change each fieldname to the appropriate field name. I know, so difficult.
        reader = csv.DictReader(f, fieldnames=(
        "Txn Date", "Value\nDate", "Description", "Ref No./Cheque\nNo.", "Debit", "Credit", "Balance"))
        # Parse the CSV into JSON

        out = json.dumps([row for row in reader])
        # Save the JSON
        f = open('file.json', 'w')
        f.write(out)

#-------------------removing invalid tags from json file liek \n,\r-----------------------
        with open('file.json', 'r', encoding='utf-8') as f:
            content = f.read()
            invalid_tags = ['\\r', '\\n', '<', '>', '-', ';']
            for invalid_tag in invalid_tags:
                content = content.replace(invalid_tag, '')
            content = content.replace('&u', 'ü')
#------------------saving the object iin database-------------------
            john = Save.objects.create(name=namef, json_field=content)
        subprocess.call(['rm', '-r'] + ['output.csv','file.json',tmp_file])
    return render(request, template)


@csrf_exempt
def view(request):
    template="get.html"
    if request.method == "POST":
        name=request.POST.get('name','')
        results = Save.objects.filter(name="Mr. KRISHNA KUNAL").values('json_field')
        print(results)
        # extra \ are coming in my json response which are not present in the results.
        return JsonResponse({"": list(results)})
    return render(request, template)


