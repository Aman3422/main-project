from .BaseCtl import BaseCtl
from ORSAPI.utility.DataValidator import DataValidator
from service.models import Initiative
from service.service.InitiativeService import InitiativeService
from service.service.UserService import UserService
from django.http.response import JsonResponse
import json


# from django.core import serializers

class InitiativeCtl(BaseCtl):

    def preload(self, request, params={}):
        preloadList = [
            {'did': 1, 'type': 'string'},
            {'did': 2, 'type': 'integer'},
            {'did': 3, 'type': 'bigint'},
            {'did': 4, 'type': 'boolean'},
            {'did': 5, 'type': 'character'}

        ]
        return JsonResponse({"preloadList": preloadList})

    def request_to_form(self, requestForm):
        self.form["id"] = requestForm["id"]
        self.form['initiativeName'] = requestForm["initiativeName"]
        # self.form['description'] = requestForm["description"]
        self.form['startDate'] = requestForm["startDate"]

        self.form['did'] = requestForm["did"]

    def input_validation(self):
        inputError = self.form["inputError"]

        if (DataValidator.isNull(self.form['initiativeName'])):
            self.form["error"] = True
            inputError["initiativeName"] = "initiativeName can not be null"
        elif (DataValidator.max_len_50(self.form['initiativeName'])):
            inputError['initiativeName'] = "initiativeName can should be below 50 character"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacheck(self.form['initiativeName'])):
                inputError['initiativeName'] = "initiativeName contains only letters"
                self.form['error'] = True

        # if (DataValidator.isNull(self.form['description'])):
        #     self.form["error"] = True
        #     inputError["description"] = "description can not be null"
        # elif (DataValidator.max_len_100(self.form['description'])):
        #     inputError['description'] = "description can should be below 100 character"
        #     self.form['error'] = True
        # else:
        #     if (DataValidator.isalphacheck(self.form['description'])):
        #         inputError['description'] = "description contains only letters"
        #         self.form['error'] = True

        if DataValidator.isNull(self.form['startDate']):
            inputError['startDate'] = "Date can not be Null"
            self.form['error'] = True
        else:
            if DataValidator.isDate(self.form['startDate']):
                inputError['startDate'] = "Incorrect Date format, should be DD-MM-YYYY format and start date should in past or present"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['did'])):
            self.form["error"] = True
            inputError["did"] = "taskStatus can not be null"



        return self.form["error"]

    def input_validation1(self):
        inputError = self.form["inputError"]

        if (DataValidator.isNotNull(self.form['initiativeName'])):
            if (DataValidator.max_len_50(self.form['initiativeName'])):
                inputError['initiativeName'] = "initiativeName can should be below 50 character"
                self.form['error'] = True
            else:
                if (DataValidator.isalphacheck(self.form['initiativeName'])):
                    inputError['initiativeName'] = "initiativeName contains only letters"
                    self.form['error'] = True

        # if (DataValidator.isNotNull(self.form['description'])):
        #     if (DataValidator.max_len_100(self.form['description'])):
        #         inputError['description'] = "description can should be below 100 character"
        #         self.form['error'] = True
        #     else:
        #         if (DataValidator.isalphacheck(self.form['description'])):
        #             inputError['description'] = "description contains only letters"
        #             self.form['error'] = True

        if DataValidator.isNotNull(self.form['startDate']):
            if DataValidator.isDate(self.form['startDate']):
                inputError[
                    'startDate'] = "Incorrect Date format, should be DD-MM-YYYY format and start date should in past or present"
                self.form['error'] = True

        return self.form["error"]

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
        json_request = json.loads(request.body)
        if (json_request):
            params["initiativeName"] = json_request.get("initiativeName", None)
            params["pageNo"] = json_request.get("pageNo", None)
        c = self.get_service().search(params)
        res = {"mesg": ""}
        if (c != None):
            res["data"] = c["data"]
            if res["data"] == []:
                res["mesg"] = "No record found"
            res["MaxId"] = c["MaxId"]
            res["index"] = c["index"]
            res["LastId"] = Initiative.objects.last().id
            res["error"] = False
        else:
            res["error"] = True
            res["message"] = "No record found"
        return JsonResponse({"result": res})

    def search1(self, request, params={}):
        res = {}
        json_request = json.loads(request.body)
        json_request['id'] = 0
        # json_request['pid'] = 0
        print("----------------------", json_request)

        if (json_request):
            params["initiativeName"] = json_request.get("initiativeName", None)
            params["startDate"] = json_request.get("startDate",None)
            # params["description"] = json_request.get("description", None)
            params["did"] = json_request.get("did", None)
            params["pageNo"] = json_request.get("pageNo", None)
        self.request_to_form(json_request)
        if (self.input_validation1()):
            print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
            res["error"] = True
            res["mesg"] = "No record found"
        else:
            c = self.get_service().search1(params)
            res = {"mesg": ""}
            if (c != None):
                res["data"] = c["data"]
                if res["data"] == []:
                    res["mesg"] = "No record found"
                res["MaxId"] = c["MaxId"]
                res["index"] = c["index"]
                res["LastId"] = Initiative.objects.last().id
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

        r = UserService().get(self.form["did"])
        index = self.find_dict_index(preload_list, 'did', self.form['did'])

        print("ORS API Initiative ============ Form to model------------------------")
        pk = int(self.form["id"])
        if (pk > 0):
            obj.id = pk
        obj.initiativeName = self.form["initiativeName"]
        obj.startDate = self.form["startDate"]
        obj.type = preload_list[index]['type']
        # obj.description = self.form["description"]
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
                dup = Initiative.objects.exclude(id=self.form['id']).filter(initiativeName=self.form["initiativeName"])
                if (dup.count() > 0):
                    res["error"] = True
                    res["message"] = "initiativeName already exists"
                else:
                    r = self.form_to_model(Initiative())
                    self.get_service().save(r)
                    if (r != None):
                        res["data"] = r.to_json()
                        res["error"] = False
                        res["message"] = "Data has been Updated Successfully"
                return JsonResponse({"data": res, "form": self.form})
            else:
                duplicate = Initiative.objects.filter(initiativeName=self.form["initiativeName"])
                if (duplicate.count() > 0):
                    res["error"] = True
                    res["message"] = "initiativeName already exists"
                else:
                    r = self.form_to_model(Initiative())
                    self.get_service().save(r)
                    if (r != None):
                        res["data"] = r.to_json()
                        res["error"] = False
                        res["message"] = "Data has been Saved successfully"
        return JsonResponse({"data": res, "form": self.form})

    # Service of Initiative
    def get_service(self):
        return InitiativeService()
