import { Component } from '@angular/core';
import { Location } from '@angular/common';

import {Punto} from './punto';
import {AppService} from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './html/app.component.html',
  styleUrls: ['./css/app.component.css']
})

export class AppComponent {
  constructor(private _appService: AppService){

  }

  title = 'TRIBOT COSTA RICA';
  desc = 'Ocupas saber la ruta más rápida? TriBot';
  desc2 = 'Hotel? Trivago';

  puntoPartida;
  puntoDestino;
  ruta;
  transporte;
  disponible;


  cambiaPartida(event){
    this.puntoPartida = event;
  }

  cambiaDestino(event){
    this.puntoDestino = event;
  }

  cambiaTransporte(event){
    this.transporte = event;
  }

  checkTransporte(){
    console.log("Busca Transporte")
    this._appService.sendPuntos(this.puntoPartida, this.puntoDestino)
    .subscribe(data => this.disponible = data);
  }

  checkRuta(){
    console.log("Busca Ruta")
    this._appService.sendTransporte(this.transporte, this.puntoPartida, this.puntoDestino)
    .subscribe(data => this.ruta = data);
    console.log(this.ruta);
  }
}
