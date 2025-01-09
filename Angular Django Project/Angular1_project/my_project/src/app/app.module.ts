import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { MenuComponent } from './menu/menu.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { WelcomeComponent } from './welcome/welcome.component';
import { UserComponent } from './user/user.component';
import { UserListComponent } from './user-list/user-list.component';
import { CollegeComponent } from './college/college.component';
import { CollegeListComponent } from './college-list/college-list.component';
import { CourseComponent } from './course/course.component';
import { CourseListComponent } from './course-list/course-list.component';
import { MarksheetComponent } from './marksheet/marksheet.component';
import { MarksheetListComponent } from './marksheet-list/marksheet-list.component';
import { MeritlistComponent } from './merit-list/merit-list.component';
import { RoleComponent } from './role/role.component';
import { RoleListComponent } from './role-list/role-list.component';
import { StudentComponent } from './student/student.component';
import { StudentListComponent } from './student-list/student-list.component';
import { SubjectComponent } from './subject/subject.component';
import { SubjectListComponent } from './subject-list/subject-list.component';
import { AddFacultyComponent } from './add-faculty/add-faculty.component';
import { AddfacultyListComponent } from './addfaculty-list/addfaculty-list.component';
import { TimetableComponent } from './timetable/timetable.component';
import { TimetableListComponent } from './timetable-list/timetable-list.component';
import { ChangepasswordComponent } from './changepassword/changepassword.component';
import { ForgetpasswordComponent } from './forgetpassword/forgetpassword.component';
import { DocumentComponent } from './document/document.component';
import { RegistrationComponent } from './registration/registration.component';
import { VehicleComponent } from './vehicle/vehicle.component';
import { VehicleListComponent } from './vehicle-list/vehicle-list.component';
import { projectComponent } from './project/project.component';
import { projectListComponent } from './projectlist/projectlist.component';
import { leadComponent } from './lead/lead.component';
import { leadListComponent } from './leadlist/leadlist.component';
import { OrderComponent } from './order/order.component';
import { OrderListComponent } from './orderlist/orderlist.component';
import { IssueComponent } from './issue/issue.component';
import { IssueListComponent } from './issue-list/issue-list.component';
import { OwnerComponent } from './owner/owner.component';
import { OwnerListComponent } from './owner-list/owner-list.component';
import { DoctorComponent } from './doctor/doctor.component';
import { DoctorListComponent } from './doctor-list/doctor-list.component';
import { EmployeeComponent } from './employee/employee.component';
import { EmployeeListComponent } from './employee-list/employee-list.component';
import { TaskComponent } from './task/task.component';
import { TaskListComponent } from './task-list/task-list.component';
import { AttributeComponent } from './attribute/attribute.component';
import { AttributeListComponent } from './attribute-list/attribute-list.component';
import { InitiativeComponent } from './initiative/initiative.component';
import { InitiativeListComponent } from './initiative-list/initiative-list.component';
import { CompensationComponent } from './compensation/compensation.component';
import { CompensationListComponent } from './compensation-list/compensation-list.component';
import { MedicationComponent } from './medication/medication.component';
import { MedicationListComponent } from './medication-list/medication-list.component';





@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    MenuComponent,
    WelcomeComponent,
    UserComponent,
    UserListComponent,
    CollegeComponent,
    CollegeListComponent,
    CourseComponent,
    CourseListComponent,
    MarksheetComponent,
    MarksheetListComponent,
    MeritlistComponent,
    RoleComponent,
    RoleListComponent,
    StudentComponent,
    StudentListComponent,
    SubjectComponent,
    SubjectListComponent,
    AddFacultyComponent,
    AddfacultyListComponent,
    TimetableComponent,
    TimetableListComponent,
    ChangepasswordComponent,
    ForgetpasswordComponent,
    DocumentComponent,
    RegistrationComponent,
    VehicleComponent,
    VehicleListComponent,
    projectComponent,
    projectListComponent,
    leadComponent,
    leadListComponent,
    OrderComponent,
    OrderListComponent,
    IssueComponent,
    IssueListComponent,
    OwnerComponent,
    OwnerListComponent,
    DoctorComponent,
    DoctorListComponent,
    EmployeeComponent,
    EmployeeListComponent,
    TaskComponent,
    TaskListComponent,
    AttributeComponent,
    AttributeListComponent,
    InitiativeComponent,
    InitiativeListComponent,
    CompensationComponent,
    CompensationListComponent,
    MedicationComponent,
    MedicationListComponent,

   
    
  ],


  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
   
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
