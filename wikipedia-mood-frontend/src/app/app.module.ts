import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { WikiSearchComponent } from './wiki-search/wiki-search.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
// import { WikiSearchModule } from './wiki-search/wiki-search.module';
@NgModule({
  declarations: [
    AppComponent,
    WikiSearchComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
    // WikiSearchModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
