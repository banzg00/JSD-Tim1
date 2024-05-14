import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { AuthService } from '../auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit() {
    this.authService
      .login({
        email: this.username,
        password: this.password,
      })
      .subscribe(
        (data) => {
          localStorage.setItem('User-token', data.accessToken);
          localStorage.setItem('Expires-in', data.expiresIn);
          localStorage.setItem('Refresh-token', data.refreshToken);
          localStorage.setItem('Username', data.username);
          localStorage.setItem('User-role', data.role);

          this.reset();
          this.router.navigate(['']);
        },
        (error) => {
          if (error.status === 401) {
            alert('Wrong username or password');
          } else {
            alert("Error! Can't login now. Try again later.");
          }
        }
      );
  }

  reset() {
    this.username = '';
    this.password = '';
  }
}
