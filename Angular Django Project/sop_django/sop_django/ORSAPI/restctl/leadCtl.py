from .BaseCtl import BaseCtl
from ORSAPI.utility.DataValidator import DataValidator
from service.models import Lead
from service.service.leadService import leadService
from django.http.response import JsonResponse
import json


# from django.core import serializers

class leadCtl(BaseCtl):

    def preload(self, request, params={}):
        preloadList = [
            {'sid': 1, 'status': "hot"},
            {'sid': 2, 'status': "warm"},
            {'sid': 3, 'status': "cold"},
        ]
        return JsonResponse({"preloadList": preloadList})

    def request_to_form(self, requestForm):
        self.form["id"] = requestForm["id"]
        self.form['date'] = requestForm['date']
        self.form['sid'] = requestForm["sid"]
        self.form['contactname'] = requestForm["contactname"]
        self.form['mobile'] = requestForm["mobile"]

    def input_validation(self):
        inputError = self.form["inputError"]


        if (DataValidator.isNull(self.form['contactname'])):
            self.form["error"] = True
            inputError["contactname"] = "Name can not be null"
        elif (DataValidator.max_len_50(self.form['contactname'])):
            inputError['contactname'] = "Name can should be below 50 character"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacheck(self.form['contactname'])):
                inputError['contactname'] = "Name contains only letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['sid'])):
            self.form["error"] = True
            inputError["sid"] = "category can not be null"

        if DataValidator.isNull(self.form['date']):
            inputError['date'] = "open date can not be Null"
            self.form['error'] = True
        else:
            if DataValidator.isDate(self.form['date']):
                inputError[
                    'date'] = "Incorrect Date format, should be DD-MM-YYYY format and dob should in past or present"
                self.form['error'] = True

        if DataValidator.isNull(self.form['mobile']):
            inputError['mobile'] = "Mobile No. can't be NUll"
            self.form['error'] = True
        else:
            if (DataValidator.ismobilecheck(self.form['mobile'])):
                inputError['mobile'] = "Mobile No. should start with 6,7,8,9 and no. must be of 10 digits"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['sid'])):
            self.form["error"] = True
            inputError["sid"] = "category can not be null"
        return self.form["error"]

    def input_validation1(self):
        inputError = self.form["inputError"]
        if DataValidator.isNotNull(self.form['mobile']):
            if (DataValidator.ismobilecheck(self.form['mobile'])):
                inputError['mobile'] = "Mobile No. should start with 6,7,8,9 and no. must be of 10 digits"
                self.form['error'] = True

        if (DataValidator.isNotNull(self.form['contactname'])):
            if (DataValidator.max_len_50(self.form['contactname'])):
                inputError['contactname'] = "Name can should be below 50 character"
                self.form['error'] = True
            else:
                if (DataValidator.isalphacheck(self.form['contactname'])):
                    inputError['contactname'] = "Name contains only letters"
                    self.form['error'] = True

        if (DataValidator.isNotNull(self.form['sid'])):
            pass

        if DataValidator.isNotNull(self.form['date']):
            if DataValidator.isDate(self.form['date']):
                inputError[
                    'date'] = "Incorrect Date format, should be DD-MM-YYYY format and dob should in past or present"
                self.form['error'] = True


        return self.form["error"]

    def get(self, request, params={}):
        c = self.get_service().get(params['id'])
        res = {}
        if (c != None):
            res["data"] = c.to_json()
            res["error"] = False
            res["message"] = "Data found"
        else:
            res["error"] = True
            res["message"] = "No record found"
        return JsonResponse({"data": res["data"]})

    def delete(self, request, params={}):
        c = self.get_service().get(params["id"])
        res = {}
        if (c != None):
            self.get_service().delete(params["id"])
            res["data"] = c.to_json()
            res["error"] = False
            res["message"] = "Data has been deleted Successfully"
        else:
            res["error"] = True
            res["message"] = "Data was not deleted"
        return JsonResponse({"data": res})

    def search(self, request, params={}):
        res = {}
        json_request = json.loads(request.body)
        if (json_request):
            params["name"] = json_request.get("name", None)
            params["pageNo"] = json_request.get("pageNo", None)
        c = self.get_service().search(params)
        res = {"mesg":""}
        if (c != None):
            res["data"] = c["data"]
            if res["data"] == []:
                res["mesg"] = "No record found"
            res["MaxId"] = c["MaxId"]
            res["index"] = c["index"]
            res["LastId"] = Lead.objects.last().id
            res["error"] = False
        else:
            res["error"] = True
            res["message"] = "No record found"
        return JsonResponse({"result": res})

    def search1(self, request, params={}):
        json_request = json.loads(request.body)
        json_request['id'] = 0
        # json_request['cid'] = 0
        print("----------------------", json_request)

        if (json_request):
            params["date"] = json_request.get("date", None)
            params["sid"] = json_request.get("sid", None)
            params["contactname"] = json_request.get("contactname", None)
            params["mobile"] = json_request.get("mobile", None)
            params["pageNo"] = json_request.get("pageNo", None)
        self.request_to_form(json_request)
        res = {}
        if (self.input_validation1()):
            print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
            res["error"] = True
            res["mesg"] = "NO record found"
        else:
            c = self.get_service().search1(params)
            res = {"mesg": ""}
            if (c != None):
                res["data"] = c["data"]
                if res["data"] == []:
                    res["mesg"] = "No record found"
                res["MaxId"] = c["MaxId"]
                res["index"] = c["index"]
                res["LastId"] = Lead.objects.last().id
                res["error"] = False
            else:
                res["error"] = True
                res["message"] = "No record found"
        return JsonResponse({"result": res, "form": self.form})

    def find_dict_index(self, dict_list, key, value):
        for index, item in enumerate(dict_list):
            if int(item.get(key)) == int(value):
                print('--------------', index)
                return index

    def form_to_model(self, obj):
        preload_response = self.preload(None).content.decode()
        preload_data = json.loads(preload_response)
        preload_list = preload_data["preloadList"]

        index = self.find_dict_index(preload_list, 'sid', self.form['sid'])

        print("ORS API Lead ============ Form to model------------------------")
        pk = int(self.form["id"])
        if (pk > 0):
            obj.id = pk
        obj.date = self.form["date"]
        obj.status = preload_list[index]["status"]
        obj.contactname = self.form["contactname"]
        obj.mobile = self.form["mobile"]
        obj.sid = self.form["sid"]
        return obj

    def save(self, request, params={}):
        json_request = json.loads(request.body)
        self.request_to_form(json_request)
        res = {}
        if (self.input_validation()):
            res["error"] = True
            res["message"] = ""
        else:
            if (self.form["id"] > 0):
                dup = Lead.objects.exclude(id=self.form['id']).filter(contactname=self.form["contactname"])
                if (dup.count() > 0):
                    res["error"] = True
                    res["message"] = "Lead Name already exists"
                else:
                    r = self.form_to_model(Lead())
                    self.get_service().save(r)
                    if (r != None):
                        res["data"] = r.to_json()
                        res["error"] = False
                        res["message"] = "Data has been Updated Successfully"
                return JsonResponse({"data": res, "form": self.form})
            else:
                duplicate = Lead.objects.filter(contactname=self.form["contactname"])
                if (duplicate.count() > 0):
                    res["error"] = True
                    res["message"] = "Lead Name already exists"
                else:
                    r = self.form_to_model(Lead())
                    self.get_service().save(r)
                    if (r != None):
                        res["data"] = r.to_json()
                        res["error"] = False
                        res["message"] = "Data has been Saved successfully"
        return JsonResponse({"data": res, "form": self.form})

    # Service of lead
    def get_service(self):
        return leadService()
