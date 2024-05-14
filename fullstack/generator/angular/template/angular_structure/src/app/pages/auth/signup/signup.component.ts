import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { AuthService } from '../auth.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss'],
})
export class SignupComponent {
  fullName: string = '';
  email: string = '';
  password: string = '';

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit() {
    this.authService
      .register({
        fullName: this.fullName,
        email: this.email,
        password: this.password,
      })
      .subscribe(
        (res: any) => {
          alert('You have registered successfully!');
          this.router.navigate(['']);
        },
        (err) => {
          alert('Unable to register! Try again!');
          this.reset();
        }
      );
  }

  reset() {
    this.fullName = '';
    this.email = '';
    this.password = '';
  }
}
