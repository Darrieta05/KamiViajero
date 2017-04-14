import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import {RouterModule} from '@angular/router';

import { fakeBackendProvider } from './fake-backend';
import { MockBackend, MockConnection } from '@angular/http/testing';
import { BaseRequestOptions } from '@angular/http';
import { AlertComponent } from './alert.component';
import { AuthGuard } from './auth.guard';
import { AuthenticationService } from './authentication.service';
import { AlertService } from './alert.service';
import { UserService } from './user.service';
import { HomeComponent } from './home.component';

import {KeysPipe} from './pipe'
import {AppRoutingModule} from './app-routing.module';
import { AppComponent } from './app.component';
import {DesdeComponent} from './desde.component'
import {HastaComponent} from './hasta.component'
import {AppService} from './app.service';
import {PageNotFoundComponent} from './not-found.component';
import {LoginComponent} from './login.component';
import {RegisterComponent} from './register.component';
import {TransporteComponent} from './transporte.component';
import {DetallesComponent} from './detalles.component';
import {Top5Component} from './top5.component';

@NgModule({
  declarations: [
    AppComponent,
    DesdeComponent,
    HastaComponent,
    PageNotFoundComponent,
    LoginComponent,
    RegisterComponent,
    KeysPipe,
    AlertComponent,
    HomeComponent,
    TransporteComponent,
    DetallesComponent,
    Top5Component
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    AppRoutingModule,

  ],
  providers: [
    AppService,
    AuthGuard,
    AlertService,
    AuthenticationService,
    UserService,

    // providers used to create fake backend
    fakeBackendProvider,
    MockBackend,
    BaseRequestOptions
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
