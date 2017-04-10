import {Injectable} from '@angular/core';
import {Http, Response, Headers, RequestOptions} from "@angular/http";
import 'rxjs/Rx';
import {Punto} from './punto'

@Injectable()
export class AppService {
  constructor(private http: Http){
  }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }

  getPuntos() {
    return this.http.get('http://swapi.co/api/people/1')
    .map((res:Response) => res.json());
  }

  getLista(): Promise<Punto[]> {
    return this.http.get('http://127.0.0.1:5000/')
      .toPromise()
      .then(response => response.json().data as Punto[])
      .catch(this.handleError);
  }

  sendPuntos(puntos: Punto[]) {
    let headers = new Headers({'Content-Type': 'application/json'});
    let options = new RequestOptions({headers: headers});
    let body = JSON.stringify(puntos);

    return this.http.post('http/127.0.0.1:5000/inserta', body, headers).map((res:Response) => res.json());
  }

}
