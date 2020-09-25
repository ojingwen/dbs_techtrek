import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

const AUTH_API = 'http://techtrek2020.ap-southeast-1.elasticbeanstalk.com/';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'text/json' })
};

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { }

  login(credentials): Observable<any> {
    console.log('USERNAME: ' + credentials.username);
    console.log('PW: ' + credentials.password);

    return this.http.post(AUTH_API + 'login', {
      username: credentials.username,
      password: credentials.password
    },{ responseType: 'text' })
  }
}