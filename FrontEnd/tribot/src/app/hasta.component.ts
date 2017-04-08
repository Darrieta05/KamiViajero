import {Component} from '@angular/core';

import {Punto} from './punto'
import {PUNTOS} from './mock-puntos'

@Component({
  selector: 'hasta',
  templateUrl: './html/hasta.component.html',
  styleUrls: ['/css/hasta.component.css']
})

export class HastaComponent {
  puntos = PUNTOS;

  selectedPunto: Punto;

  model = new Punto(4, 'Escazú', {tren: false, taxi: true, avion: false, bus: false});


  onSelect(punto: Punto): void{
    this.selectedPunto = punto;
  }

  ngOnInit(){
    
  }

  submitted = false;

  onSubmit() { this.submitted = true; }

  get diagnostic() {
    return JSON.stringify(this.model);
  }

}
