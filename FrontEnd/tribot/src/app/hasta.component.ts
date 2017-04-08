import {Component, Input, Output, EventEmitter} from '@angular/core';
import 'rxjs/Rx';

import {AppService} from './app.service'

import {Punto} from './punto'

@Component({
  selector: 'hasta',
  templateUrl: './html/hasta.component.html',
  styleUrls: ['/css/hasta.component.css']
})

export class HastaComponent {
  public puntos;

  @Input()
  puntoout: string = 'yep';

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

  onSubmit() {
    this.change.emit(this.puntoout)
  }


}
