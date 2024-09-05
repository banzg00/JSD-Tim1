import axios, { AxiosResponse } from 'axios';

const API_BASE_URL = 'http://localhost:8442/api';

class AuthService {
  register(user: any): Promise<any> {
    return axios.post(API_BASE_URL + '/auth/register', user)
      .then((response: AxiosResponse<any>) => response.data)
      .catch((error: any) => {
        console.error('There was an error registering the user!', error);
      });
  }

  login(data: any): Promise<any> {
    return axios.post(API_BASE_URL + '/auth/login', data)
      .then((response: AxiosResponse<any>) => response.data)
      .catch((error: any) => {
        console.error('There was an error logging in!', error);
      });
  }

  getToken(): string {
    const token = localStorage.getItem('User-token');
    return token ? `Bearer ${token}` : '';
  }
}

export default new AuthService();