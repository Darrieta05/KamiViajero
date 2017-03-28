import {Transporte} from './transporte';

export class Punto {
  id: number;
  nombre: string;
  transportes?: Transporte;

  constructor(
    id: number,
    nombre: string,
    transportes?: Transporte){}


}
