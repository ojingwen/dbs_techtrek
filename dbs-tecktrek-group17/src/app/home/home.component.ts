import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { TokenStorageService } from '../_services/token-storage.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private router: Router, private tokenStorage: TokenStorageService) { }

  ngOnInit(): void {
  }

  onLogout(){
    this.tokenStorage.signOut();
    this.router.navigateByUrl("/login");
  }
}
