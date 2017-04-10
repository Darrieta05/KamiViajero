import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';

import {DesdeComponent} from './desde.component';
import {HastaComponent} from './hasta.component';
import {LoginComponent} from './login.component';
import {RegisterComponent} from './register.component';
import {PageNotFoundComponent} from './not-found.component';

import { HomeComponent } from './home.component';
import { AuthGuard } from './auth.guard';


const routes: Routes = [
  {path: 'desde', component: DesdeComponent},
  {path: 'hasta', component: HastaComponent},
  {path: 'login', component: LoginComponent},
  {path: 'register', component: RegisterComponent},
  { path: '', component: HomeComponent, canActivate: [AuthGuard] },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: '**', redirectTo: '' }
]

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})

export class AppRoutingModule {}
