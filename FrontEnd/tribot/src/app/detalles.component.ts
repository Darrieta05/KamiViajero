import {Component, Input} from '@angular/core'
import 'rxjs/Rx';


@Component({
  selector: 'detalles',
  templateUrl: './html/detalles.component.html',
  styleUrls: ['./css/detalles.component.css']
})

export class DetallesComponent {
  @Input()
  ruta;
}
