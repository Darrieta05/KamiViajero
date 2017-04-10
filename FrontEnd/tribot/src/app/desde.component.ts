import {Component, Input, Output, EventEmitter} from '@angular/core';
import 'rxjs/Rx';

import {AppService} from './app.service';


import {Punto} from './punto'

@Component({
  selector: 'desde',
  templateUrl: './html/desde.component.html',
  styleUrls: ['/css/desde.component.css']
})

export class DesdeComponent {

  @Input()
  puntoin: Object;

  @Output('cambio')
  change: EventEmitter<Object> = new EventEmitter<Object>();

  constructor(private _appService: AppService){}

  datos = {};

 ngOnInit(){
   this.loadUser();
 }

  loadUser() {
    this._appService.getPuntos().subscribe(data => this.datos = data);
  }

  onSubmit(){
    this.change.emit(this.puntoin);
   }

}
