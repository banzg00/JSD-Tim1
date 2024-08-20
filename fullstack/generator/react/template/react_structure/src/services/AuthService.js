import axios from 'axios';

const API_BASE_URL = 'http://localhost:8442/api';

class AuthService {
  register(user) {
    return axios.post(API_BASE_URL + '/auth/register', user)
      .then(response => response.data)
      .catch(error => console.error('There was an error registering the user!', error));
  }

  login(data) {
    return axios.post(API_BASE_URL + '/auth/login', data)
      .then(response => response.data)
      .catch(error => console.error('There was an error logging in!', error));
  }

  getToken() {
    let token = localStorage.getItem('User-token');
    return token == null ? '' : 'Bearer ' + token;
  }
}

export default new AuthService();
