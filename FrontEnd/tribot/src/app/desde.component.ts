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
  public puntos;

  @Input()
  puntoin: string = 'yep';

  @Output('cambio')
  change: EventEmitter<string> = new EventEmitter<string>();


  constructor(private _appService: AppService){
  }

  profile = {};

 ngOnInit(){
   this.loadUser();
 }

  loadUser() {
    this._appService.getPuntos().subscribe(data => this.profile = data);
  }

  selectedPunto: Punto;

  onSubmit(){
    this.change.emit(this.puntoin);
   }

}
