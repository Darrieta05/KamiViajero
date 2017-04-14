import {Component, Input, Output, EventEmitter} from '@angular/core'
import 'rxjs/Rx';

@Component({
   selector: 'transporte',
   templateUrl: './html/transporte.component.html',
   styleUrls: ['./css/transporte.component.css']
})

export class TransporteComponent {
  transporte;

  @Input()
  disponible;

  @Output('cambio')
  change: EventEmitter<any> = new EventEmitter<any>();

  onSubmit(){
    this.change.emit(this.transporte);
   }
}
