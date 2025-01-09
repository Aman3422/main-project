import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RegistrationComponent } from './registration/registration.component';
import { MenuComponent } from './menu/menu.component';
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






const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'registration', component:RegistrationComponent },
  { path: 'menu', component: MenuComponent },
  { path : 'welcome', component:WelcomeComponent},
  { path : 'user', component:UserComponent},
  { path : 'user/:id', component:UserComponent},
  { path : 'userlist', component:UserListComponent },
  { path : 'college', component:CollegeComponent},
  { path : 'college/:id', component:CollegeComponent},
  { path : 'collegelist', component:CollegeListComponent},
  { path : 'course', component:CourseComponent},
  { path : 'course/:id', component:CourseComponent},
  { path : 'courselist', component:CourseListComponent},
  { path : 'marksheet', component:MarksheetComponent},
  { path : 'marksheetlist', component:MarksheetListComponent },
  { path : 'meritlist', component:MeritlistComponent },
  { path : 'role', component:RoleComponent},
  { path : 'rolelist', component:RoleListComponent},
  { path : 'role/:id', component:RoleComponent},
  { path : 'student', component:StudentComponent },
  { path : 'studentlist', component:StudentListComponent },
  { path : 'student/:id', component:StudentComponent },
  { path : 'subject', component:SubjectComponent },
  { path : 'subjectlist', component:SubjectListComponent },
  { path : 'subject/:id', component:SubjectComponent },
  { path : 'addfaculty', component:AddFacultyComponent },
  { path : 'addfacultylist', component:AddfacultyListComponent },
  { path : 'addfaculty/:id', component:AddFacultyComponent },
  { path : 'timetable', component:TimetableComponent },
  { path : 'timetablelist', component:TimetableListComponent },
  { path : 'timetable/:id', component:TimetableComponent },
  { path : 'changepassword', component:ChangepasswordComponent },
  { path : 'forgetpassword', component:ForgetpasswordComponent },
  { path : 'logout', component:MenuComponent},
  { path : 'vehicle', component:VehicleComponent},
  { path : 'vehicle/:id', component:VehicleComponent},
  { path : 'vehiclelist', component:VehicleListComponent},
  { path : 'project', component:projectComponent},
  { path : 'project/:id', component:projectComponent},
  { path : 'projectlist', component:projectListComponent},
  { path : 'lead', component:leadComponent},
  { path : 'lead/:id', component:leadComponent},
  { path : 'leadlist', component:leadListComponent},
  { path : 'order', component:OrderComponent},
  { path : 'order/:id', component:OrderComponent},
  { path : 'orderlist', component:OrderListComponent},
  { path : 'issue', component:IssueComponent},
  { path : 'issue/:id', component:IssueComponent},
  { path : 'issuelist', component:IssueListComponent},
  { path : 'owner', component:OwnerComponent},
  { path : 'owner/:id', component:OwnerComponent},
  { path : 'ownerlist', component:OwnerListComponent},
  { path : 'doctor', component:DoctorComponent},
  { path : 'doctor/:id', component:DoctorComponent},
  { path : 'doctorlist', component:DoctorListComponent},
  { path : 'employee', component:EmployeeComponent},
  { path : 'employee/:id', component:EmployeeComponent},
  { path : 'employeelist', component:EmployeeListComponent},
  { path : 'task', component:TaskComponent},
  { path : 'task/:id', component:TaskComponent},
  { path : 'tasklist', component:TaskListComponent},
  { path : 'attribute', component:AttributeComponent},
  { path : 'attribute/:id', component:AttributeComponent},
  { path : 'attributelist', component:AttributeListComponent},
  { path : 'initiative', component:InitiativeComponent},
  { path : 'initiative/:id', component:InitiativeComponent},
  { path : 'initiativelist', component:InitiativeListComponent},
  { path : 'compensation', component:CompensationComponent},
  { path : 'compensation/:id', component:CompensationComponent},
  { path : 'compensationlist', component:CompensationListComponent},
  { path : 'medication', component:MedicationComponent},
  { path : 'medication/:id', component:MedicationComponent},
  { path : 'medicationlist', component:MedicationListComponent},



  { path : '**', component:DocumentComponent },
  

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
