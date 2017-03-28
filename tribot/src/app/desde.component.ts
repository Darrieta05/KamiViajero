import {Component} from '@angular/core';

import {Punto} from './punto'
import {PUNTOS} from './mock-puntos'

@Component({
  selector: 'desde',
  templateUrl: './html/desde.component.html',
  styleUrls: ['/css/desde.component.css']
})

export class DesdeComponent {
  clickMessage = '';

  onClickMe() {
    this.clickMessage = 'You are my hero!';
  }
  
  puntos = PUNTOS;

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
