import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WikiSearchComponent } from './wiki-search.component';

describe('WikiSearchComponent', () => {
  let component: WikiSearchComponent;
  let fixture: ComponentFixture<WikiSearchComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [WikiSearchComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WikiSearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
