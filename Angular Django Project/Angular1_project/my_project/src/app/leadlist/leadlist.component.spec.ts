import { ComponentFixture, TestBed } from '@angular/core/testing';

import { leadListComponent } from './leadlist.component';

describe('LeadlistComponent', () => {
  let component: leadListComponent;
  let fixture: ComponentFixture<leadListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ leadListComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(leadListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
