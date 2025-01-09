import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { observable } from 'rxjs';
import { data } from 'jquery';

@Injectable({
  providedIn: 'root'
})
export class EmployeeService {

  // Reset Endpoint
  endpoint = "http://localhost:8000/ORSAPI/Employee/"

  /**
   * Constructor injects HTTP service
   *
   * @param http
   */

  constructor(private http:HttpClient) { }

    /**
     * get College
     * @params id
     * @params response
     */

  get(id:number, compCB:any){
    let url = this.endpoint + "get/" + id;
    var observable = this.http.get(url);
    observable.subscribe(
      function success(data){
      compCB(data);      
    },function fail(data){
      compCB(data, true);
    });
}
 /**
   * Delets a College
   *
   * @param id
   * @param response
   */
  delete(id:number, compCB:any){
    let url = this.endpoint + "delete/" + id;
    this.http.get(url).subscribe(
      (data) => {
        compCB(data);
      }, (data) => {
        compCB(data,true);
      }
    );
  }
   /**
   * Searches vehicle
   *
   * @param response
   */

   search(form:any, compCB:any){
    let url = this.endpoint + "search";
    this.http.post(url,form).subscribe(
      (data) => {
        compCB(data);
      },(data) => {
        compCB(data,true);
      }
    );
   }
   search1(form:any, compCB:any){
    let url = this.endpoint + "search1";
    this.http.post(url,form).subscribe(
      (data) => {
        compCB(data);
      },(data) => {
        compCB(data,true);
      }
    );
   }
  

 /**
   * Add/Update vehicle
   * @param form Adds or updates a record
   * @param response
   */

  


  save(form:any, compCB:any){
    let url = this.endpoint + "save";
    this.http.post(url,form).subscribe(
      (data) => {
        compCB(data);
      }, (data) => {
        compCB(data,true);
      }
    );
  }

}