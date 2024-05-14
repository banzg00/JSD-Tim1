import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  constructor(private http: HttpClient) {}

  register(user: {}) {
    return this.http.post<any>(
      environment.API_BASE_URL + '/auth/register',
      user
    );
  }

  login(data: any) {
    return this.http.post<any>(environment.API_BASE_URL + '/auth/login', data);
  }

  getToken() {
    let token = localStorage.getItem('User-token');
    return token == null ? '' : 'Bearer ' + token;
  }
}
