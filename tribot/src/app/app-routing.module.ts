import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';

import {DesdeComponent} from './desde.component';
import {HastaComponent} from './hasta.component';

const routes: Routes = [
  {path: '', redirectTo: '/desde', pathMatch: 'full'},
  {path: 'desde', component: DesdeComponent},
  {path: 'hasta', component: HastaComponent}
]

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})

export class AppRoutingModule {}
