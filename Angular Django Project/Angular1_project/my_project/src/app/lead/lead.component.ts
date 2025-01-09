import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { leadService } from '../service/lead.service';
/**
 * Activated route is used to read route parameters
 */
@Component({
  selector: 'app-lead',
  templateUrl: './lead.component.html',
  styleUrls: ['./lead.component.css']
})
export class leadComponent implements OnInit {

  // lead form
  form = {
    "id":0,
    "date":"",
    // "status":"",
    "sid":"",
    "contactname":"",
    "mobile":"",
  }

  // Input errors
  inputError = {
    "date":"",
    // "status":"",
    "sid":"",
    "contactname":"",
    "mobile":""
  }

  // Server success/fail message
  message = "";

  // Server error
  success: boolean = true;

/**
 * Injects Services
 * @param aroute 
 * @param router 
 * @param service 
 */
  constructor(private aroute:ActivatedRoute,private router:Router,private service:leadService) { }

  /**
   * Displays record if primary key is received
   */
  ngOnInit(): void {
    var _self = this;
    _self.form.id = parseInt(this.aroute.snapshot.paramMap.get("id") || "{}");
    if ( !isNaN(_self.form.id) && _self.form.id > 0){
      this.service.get(_self.form.id, function (res:any, error:any){
        if (error){
          alert("Error:----" + error.message);
          return ;
        }
        _self.form = res.data;
      });
    }
    this.preload();

  }
  /**
   * Save a record
   */

  save(){
    var _self = this;
    this.ngOnInit();
    if (isNaN(this.form.id)){
      this.form.id = 0;
    }
    this.service.save(this.form, function (res:any, error:any){
      if (res.data.error){
        _self.success = false;
        _self.message = res.data.message;
        _self.inputError = res.form.inputError;
        return;
      }
      _self.success = res.data.message;
      if(_self.success){
        _self.success = true;
        _self.message = res.data.message;
        _self.form = res.data.data;
        _self.inputError = {
          "date":"",
          // "status":"",
          "sid":"",
          "contactname":"",
          "mobile":""
        }
      }else{
        _self.message = "Data was not saved"
      }
    });
  }

  preloadData : any = []
  preload() {
    var _self = this;
    this.service.preload(function(res:any, error:any){
      if(error){
        alert("Preload Error:" + error.message);
        return;
      }
      _self.preloadData = res.preloadList;
      console.log("PreloadList ------->", res.preloadList);
    });
  }

  reset(){
    this.form = {
      "id":0,
      "date":"",
      // "status":"",
      "sid":"",
      "contactname":"",
      "mobile":""
    };
    this.ngOnInit();
    this.inputError = {
      "date":"",
      // "status":"",
      "sid":"",
      "contactname":"",
      "mobile":""
    };
    this.message = "";
  }

}

