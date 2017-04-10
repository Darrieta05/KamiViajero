import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';

import {DesdeComponent} from './desde.component';
import {HastaComponent} from './hasta.component';
import {LogInComponent} from './login.component';
import {RegisterComponent} from './register.component';
import {PageNotFoundComponent} from './not-found.component';

const routes: Routes = [
  {path: 'desde', component: DesdeComponent},
  {path: 'hasta', component: HastaComponent},
  {path: 'login', component: LogInComponent},
  {path: 'register', component: RegisterComponent}
]

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})

export class AppRoutingModule {}
