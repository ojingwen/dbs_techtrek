import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

import { AuthService } from '../_services/auth.service';

const TOKEN_KEY = 'auth-token';
const USER_KEY = 'auth-user';

@Injectable({
  providedIn: 'root'
})
export class TokenStorageService {

  timer = null;

  constructor(private authService: AuthService, private router: Router) { }

  signOut() {
    localStorage.clear();
    clearTimeout(this.timer);
    this.router.navigateByUrl("/login");
  }

  public saveToken(token: string) {
    localStorage.removeItem(TOKEN_KEY);
    localStorage.setItem(TOKEN_KEY, token);
    this.timer = setTimeout(()=> {
      if (confirm("Session is expiring, do you want to extend?") == true) {
        this.authService.extend(localStorage.getItem(TOKEN_KEY)).subscribe(
          data => {
            console.log('new token data: ', data);
            this.saveToken(data);
          },
          err => {
            console.log('error: ', err);
          }
        );
      } else {
        this.signOut();
      }
    }, 3000);
  }

  public getToken(): string {
    return localStorage.getItem(TOKEN_KEY);
  }

  public saveUser(user) {
    localStorage.removeItem(USER_KEY);
    localStorage.setItem(USER_KEY, JSON.stringify(user));
  }

  public getUser() {
    return JSON.parse(localStorage.getItem(USER_KEY));
  }
}