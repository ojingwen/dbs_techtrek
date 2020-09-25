import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { AuthService } from '../_services/auth.service';
import { TokenStorageService } from '../_services/token-storage.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  form: any = {};
  isLoggedIn = false;
  isLoginFailed = false;
  errorMessage = '';

  constructor(private fb: FormBuilder,private router: Router, private authService: AuthService, private tokenStorage: TokenStorageService) { }

  ngOnInit() {
    if (this.tokenStorage.getToken()) {
      this.isLoggedIn = true;
    }
  }

  onSubmit() {
    this.authService.login(this.form).subscribe(
      data => {
        console.log('received data: ' , data);
        console.log('save user: ' , this.form.username);

        this.tokenStorage.saveToken(data);
        this.tokenStorage.saveUser(this.form.username);

        this.isLoginFailed = false;
        this.isLoggedIn = true;
        this.router.navigateByUrl("/home");
      },
      err => {
        console.log('error: ' , err);
        this.errorMessage = err.error.message;
        this.isLoginFailed = true;
      }
    );
  }

  // onClickMe() {
  //   console.log("email" + this.email);
  //   console.log("password" + this.password);
  //   //to call service
  // }

}
