import {Injectable} from '@angular/core';
import {Http, Response, Headers, RequestOptions} from "@angular/http";
import 'rxjs/Rx';

@Injectable()
export class LocalObjectService {
  constructor(private http: Http){
    
  }
}
