from .BaseCtl import BaseCtl
from ORSAPI.utility.DataValidator import DataValidator
from service.models import Attribute
from service.service.AttributeService import AttributeService
from django.http.response import JsonResponse
import json


# from django.core import serializers

class AttributeCtl(BaseCtl):

    def preload(self, request, params={}):
        preloadList = [
            {'did': 1, 'dataType': "single"},
            {'did': 2, 'dataType': "double"},
            {'did': 3, 'dataType': "triple"},
        ]
        return JsonResponse({"preloadList": preloadList})

    def request_to_form(self, requestForm):
        self.form["id"] = requestForm["id"]
        self.form['displayName'] = requestForm['displayName']
        self.form['isActive'] = requestForm["isActive"]
        self.form['description'] = requestForm["description"]
        self.form['did'] = requestForm["did"]

    def input_validation(self):
        inputError = self.form["inputError"]


        if (DataValidator.isNull(self.form['displayName'])):
            self.form["error"] = True
            inputError["displayName"] = "displayName can not be null"
        elif (DataValidator.max_len_50(self.form['displayName'])):
            inputError['displayName'] = "displayName can should be below 50 character"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacheck(self.form['displayName'])):
                inputError['displayName'] = "displayName contains only letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['did'])):
            self.form["error"] = True
            inputError["did"] = "Data type can not be null"

        if DataValidator.isNull(self.form['isActive']):
            inputError['isActive'] = "Date can not be Null"
            self.form['error'] = True

        if DataValidator.isNull(self.form['description']):
            inputError['description'] = "description No. can't be NUll"
            self.form['error'] = True
        elif (DataValidator.max_len_50(self.form['description'])):
            inputError['description'] = "displayName can should be below 50 character"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacheck(self.form['description'])):
                inputError['description'] = "displayName contains only letters"
                self.form['error'] = True

        return self.form["error"]

    def input_validation1(self):
        inputError = self.form["inputError"]
        if (DataValidator.isNotNull(self.form['description'])):
            if (DataValidator.max_len_50(self.form['description'])):
                inputError['description'] = "displayName can should be below 50 character"
                self.form['error'] = True
            else:
                if (DataValidator.isalphacheck(self.form['description'])):
                    inputError['description'] = "displayName contains only letters"
                    self.form['error'] = True

        if (DataValidator.isNotNull(self.form['displayName'])):
            if (DataValidator.max_len_50(self.form['displayName'])):
                inputError['displayName'] = "displayName can should be below 50 character"
                self.form['error'] = True
            else:
                if (DataValidator.isalphacheck(self.form['displayName'])):
                    inputError['displayName'] = "displayName contains only letters"
                    self.form['error'] = True

        if (DataValidator.isNotNull(self.form['did'])):
            pass

        # if DataValidator.isNotNull(self.form['isActive']):
        #     if DataValidator.isDate(self.form['isActive']):
        #         inputError['isActive'] = "Incorrect Date format, should be DD-MM-YYYY format and isActive should in past or present"
        #         self.form['error'] = True


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
            params["displayName"] = json_request.get("displayName", None)
            params["pageNo"] = json_request.get("pageNo", None)
        c = self.get_service().search(params)
        res = {"mesg":""}
        if (c != None):
            res["data"] = c["data"]
            if res["data"] == []:
                res["mesg"] = "No record found"
            res["MaxId"] = c["MaxId"]
            res["index"] = c["index"]
            res["LastId"] = Attribute.objects.last().id
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
            params["displayName"] = json_request.get("displayName", None)
            params["did"] = json_request.get("did", None)
            params["isActive"] = json_request.get("isActive", None)
            params["description"] = json_request.get("description", None)
            params["pageNo"] = json_request.get("pageNo", None)
        self.request_to_form(json_request)
        res = {}
        if (self.input_validation1()):
            print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
            res["error"] = True
            res["mesg"] = "NO record found"
        else:
            c = self.get_service().search1(params)
            # res = {"mesg": ""}
            if (c != None):
                res["data"] = c["data"]
                if res["data"] == []:
                    res["mesg"] = "No record found"
                res["MaxId"] = c["MaxId"]
                res["index"] = c["index"]
                res["LastId"] = Attribute.objects.last().id
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

        index = self.find_dict_index(preload_list, 'did', self.form['did'])

        print("ORS API Attribute ============ Form to model------------------------")
        pk = int(self.form["id"])
        if (pk > 0):
            obj.id = pk
        obj.displayName = self.form["displayName"]
        obj.isActive = self.form["isActive"]
        obj.description = self.form["description"]
        obj.dataType = preload_list[index]["dataType"]
        obj.did = self.form["did"]
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
                dup = Attribute.objects.exclude(id=self.form['id']).filter(displayName=self.form["displayName"])
                if (dup.count() > 0):
                    res["error"] = True
                    res["message"] = "Attribute displayName already exists"
                else:
                    r = self.form_to_model(Attribute())
                    self.get_service().save(r)
                    if (r != None):
                        res["data"] = r.to_json()
                        res["error"] = False
                        res["message"] = "Data has been Updated Successfully"
                return JsonResponse({"data": res, "form": self.form})
            else:
                duplicate = Attribute.objects.filter(displayName=self.form["displayName"])
                if (duplicate.count() > 0):
                    res["error"] = True
                    res["message"] = "displayName already exists"
                else:
                    r = self.form_to_model(Attribute())
                    self.get_service().save(r)
                    if (r != None):
                        res["data"] = r.to_json()
                        res["error"] = False
                        res["message"] = "Data has been Saved successfully"
        return JsonResponse({"data": res, "form": self.form})

    # Service of Attribute
    def get_service(self):
        return AttributeService()
