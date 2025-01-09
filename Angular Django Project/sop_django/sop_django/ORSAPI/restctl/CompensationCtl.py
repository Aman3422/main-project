from .BaseCtl import BaseCtl
from ORSAPI.utility.DataValidator import DataValidator
from service.models import Compensation
from service.service.CompensationService import CompensationService
from django.http.response import JsonResponse
import json


# from django.core import serializers

class CompensationCtl(BaseCtl):

    def preload(self, request, params={}):
        preloadList = [
            {'stid': 1, 'staffMember': 'Raj Singh'},
            {'stid': 2, 'staffMember': 'Jalaj Singh'},
            {'stid': 3, 'staffMember': 'Aman Soni'},
            {'stid': 4, 'staffMember': 'Ajay Sharma'},
            {'stid': 5, 'staffMember': 'Tarun Indoria'},
            {'stid': 6, 'staffMember': 'Rahul Suroliya'},
        ]
        return JsonResponse({"preloadList": preloadList})

    def preload1(self, request, params={}):
        preloadList =[
            {'sid': 1, 'state':'Active'},
            {'sid': 2, 'state':'In Active'}

        ]
        return JsonResponse({"preloadList1": preloadList})

    def request_to_form(self, requestForm):
        self.form["id"] = requestForm["id"]
        self.form['paymentAmount'] = requestForm["paymentAmount"]
        self.form['dateApplied'] = requestForm["dateApplied"]
        self.form['stid'] = requestForm["stid"]
        self.form['sid'] = requestForm["sid"]

    def input_validation(self):
        inputError = self.form["inputError"]

        if DataValidator.isNull(self.form['dateApplied']):
            inputError['dateApplied'] = "Open Date can not be Null"
            self.form['error'] = True
        else:
            if DataValidator.isDate(self.form['dateApplied']):
                inputError['dateApplied'] = "Incorrect Open Date format, should be DD-MM-YYYY format and dob should in past or present"
                self.form['error'] = True


        if (DataValidator.isNull(self.form['paymentAmount'])):
            self.form["error"] = True
            inputError["paymentAmount"] = "insuranceAmount can not be null"
        elif (DataValidator.is_0(self.form['paymentAmount'])):
            self.form["error"] = True
            inputError["paymentAmount"] = "amount can not be zero or less"


        else:
            if (DataValidator.max_len_10(self.form['paymentAmount'])):
                inputError['paymentAmount'] = "insuranceAmount can be only 10 digit"
                self.form['error'] = True


        if (DataValidator.isNull(self.form['stid'])):
            self.form["error"] = True
            inputError["stid"] = "Assign To can not be null"


        if (DataValidator.isNull(self.form['sid'])):
            self.form["error"] = True
            inputError["sid"] = "taskStatus can not be null"



        return self.form["error"]

    def input_validation1(self):
        inputError = self.form["inputError"]

        if DataValidator.isNotNull(self.form['dateApplied']):
            if DataValidator.isDate(self.form['dateApplied']):
                inputError['dateApplied'] = "Incorrect Date format, should be DD-MM-YYYY format and dob should in past or present"
                self.form['error'] = True

        if (DataValidator.isNotNull(self.form["paymentAmount"])):
            if (DataValidator.max_len_10(self.form['paymentAmount'])):
                inputError['paymentAmount'] = "amount can should be above 10 digit"
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
        json_request = json.loads(request.body)
        if (json_request):
            params["creationDate"] = json_request.get("creationDate", None)
            params["pageNo"] = json_request.get("pageNo", None)
        c = self.get_service().search(params)
        res = {"mesg": ""}
        if (c != None):
            res["data"] = c["data"]
            if res["data"] == []:
                res["mesg"] = "No record found"
            res["MaxId"] = c["MaxId"]
            res["index"] = c["index"]
            res["LastId"] = Compensation.objects.last().id
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
            # params["staffMember"] = json_request.get("staffMember", None)
            params["dateApplied"] = json_request.get("dateApplied", None)
            params["stid"] = json_request.get("stid", None)
            params["sid"] = json_request.get("sid", None)
            params["pageNo"] = json_request.get("pageNo", None)
        self.request_to_form(json_request)
        if (self.input_validation1()):
            print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
            res["error"] = True
            res["mesg"] = "No record found"
        else:
            c = self.get_service().search1(params)
            # res = {"mesg": ""}
            if (c != None):
                res["data"] = c["data"]
                if res["data"] == []:
                    res["mesg"] = "No record found"
                res["MaxId"] = c["MaxId"]
                res["index"] = c["index"]
                res["LastId"] = Compensation.objects.last().id
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

        preload_response = self.preload1(None).content.decode()
        preload_data = json.loads(preload_response)
        preload_list1 = preload_data["preloadList1"]

        index = self.find_dict_index(preload_list, 'stid', self.form['stid'])
        index1 = self.find_dict_index(preload_list1, 'sid', self.form['sid'])


        print("ORS API Compensation ============ Form to model------------------------")
        pk = int(self.form["id"])
        if (pk > 0):
            obj.id = pk


        obj.dateApplied = self.form["dateApplied"]
        obj.paymentAmount = self.form["paymentAmount"]
        obj.staffMember = preload_list[index]['staffMember']
        obj.state = preload_list1[index1]['state']
        obj.stid = self.form["stid"]
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
                dup = Compensation.objects.exclude(id=self.form['id']).filter(stid=self.form["stid"])
                if (dup.count() > 0):
                    res["error"] = True
                    res["message"] = "staff Member already exists"
                else:
                    r = self.form_to_model(Compensation())
                    self.get_service().save(r)
                    if (r != None):
                        res["data"] = r.to_json()
                        res["error"] = False
                        res["message"] = "Data has been Updated Successfully"
                return JsonResponse({"data": res, "form": self.form})
            else:
                duplicate = Compensation.objects.filter(stid=self.form["stid"])
                if (duplicate.count() > 0):
                    res["error"] = True
                    res["message"] = "staff Member already exists"
                else:
                    r = self.form_to_model(Compensation())
                    self.get_service().save(r)
                    if (r != None):
                        res["data"] = r.to_json()
                        res["error"] = False
                        res["message"] = "Data has been Saved successfully"
        return JsonResponse({"data": res, "form": self.form})

    # Service of Compensation
    def get_service(self):
        return CompensationService()

