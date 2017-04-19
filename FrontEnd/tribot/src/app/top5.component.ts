import {Component, Input, OnInit} from '@angular/core';

import {AppService} from './app.service';

@Component({
  selector: 'top5',
  templateUrl: './html/top5.component.html',
  styleUrls: ['./css/top5.component.css']
})

export class Top5Component {
  constructor(private _appService: AppService){}

  top5rutas;

  ngOnInit(){
    this.getTop();
  }

  getTop(){
    console.log("Busca top 5");
    this._appService.getTop5().subscribe(data => this.top5rutas = data);
  }

}
