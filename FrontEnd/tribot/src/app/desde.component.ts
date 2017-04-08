import {Component, Input} from '@angular/core';
import {AppService} from './app.service';
import 'rxjs/Rx';

import {Punto} from './punto'
import {PUNTOS} from './mock-puntos'

@Component({
  selector: 'desde',
  templateUrl: './html/desde.component.html',
  styleUrls: ['/css/desde.component.css']
})

export class DesdeComponent {
  public puntos;
  public puntos_error:Boolean = false;

  @Input()
  puntoin: string = 'yep';


  constructor(private _appService: AppService){
  }

  profile = {};

  loadUser() {
    this._appService.getPuntos().subscribe(data => this.profile = data);
  }

  getPuntos() {
    this._appService.getPuntos().subscribe(
      data => { this.puntos = data},
      err => { this.puntos_error = true }
    );
  }

  getLista(){
    this._appService.getLista()
    .then(puntos => this.puntos);
    console.log(this.puntos);
  }

  clickMessage = '';

  onClickMe() {
    this.clickMessage = 'You are my hero!';
  }

  ngOnInit() {
  //  this.getPuntos();
  //  this.getLista();
 }

  selectedPunto: Punto;

  model = new Punto(4, 'Escazú', {tren: false, taxi: true, avion: false, bus: false});


  onSelect(punto: Punto): void{
    this.selectedPunto = punto;
  }

  submitted = false;

  onSubmit() { this.submitted = true; }

  get diagnostic() {
    return JSON.stringify(this.model);
  }

}
