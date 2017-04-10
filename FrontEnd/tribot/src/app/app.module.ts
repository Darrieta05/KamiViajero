import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import {RouterModule} from '@angular/router';

import {AppRoutingModule} from './app-routing.module';
import { AppComponent } from './app.component';
import {DesdeComponent} from './desde.component'
import {HastaComponent} from './hasta.component'
import {AppService} from './app.service';
import {PageNotFoundComponent} from './not-found.component';
import {LogInComponent} from './login.component';
import {RegisterComponent} from './register.component';

@NgModule({
  declarations: [
    AppComponent,
    DesdeComponent,
    HastaComponent,
    PageNotFoundComponent,
    LogInComponent,
    RegisterComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    AppRoutingModule
  ],
  providers: [AppService],
  bootstrap: [AppComponent]
})
export class AppModule { }
