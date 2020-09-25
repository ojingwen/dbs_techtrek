import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  email: string
	password: string
	loginError: boolean
	errorMessage: string
	isLogin: boolean
	loginForm: FormGroup;
  constructor(private fb: FormBuilder,private router: Router) { }

  ngOnInit() {
    this.loginError=false;
    this.loginForm = this.fb.group({
      email: ["", Validators.required],
      password: ["", [Validators.required]],
    });

  }

  onClickMe() {
    console.log("email" + this.email);
    console.log("password" + this.password);
    //to call service
  }

}
