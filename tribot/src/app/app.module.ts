import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import {RouterModule} from '@angular/router';

import {AppRoutingModule} from './app-routing.module';
import { AppComponent } from './app.component';
import {DesdeComponent} from './desde.component'
import {HastaComponent} from './hasta.component'

@NgModule({
  declarations: [
    AppComponent,
    DesdeComponent,
    HastaComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
