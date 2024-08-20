import React, { useState } from 'react';
import AuthService from '../../services/AuthService';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const data = await AuthService.login({ email: username, password });
      localStorage.setItem('User-token', data.accessToken);
      localStorage.setItem('Expires-in', data.expiresIn);
      localStorage.setItem('Refresh-token', data.refreshToken);
      localStorage.setItem('Username', data.username);
      localStorage.setItem('User-role', data.role);

      setUsername('');
      setPassword('');
      window.location.href = '/';
    } catch (error) {
      if (error.response?.status === 401) {
        alert('Wrong username or password');
      } else {
        alert("Error! Can't login now. Try again later.");
      }
    }
  };

  return (
    <div className="flex w-full h-full justify-center bg-gray-200">
      <form
        onSubmit={handleSubmit}
        className="mt-[10%] p-10 gap-y-8 h-fit w-[25vw] flex-col flex items-left rounded-xl bg-gray-300"
      >
        <div className="mx-auto font-semibold text-3xl">Login</div>
        <div className="flex items-center justify-between">
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            name="username"
            className="w-[15vw]"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div className="flex items-center justify-between">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            name="password"
            className="w-[15vw]"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit" className="w-full">Login</button>

        <a href="/signup" className="underline text-sm mx-auto w-fit">
          Don't have an account? Signup here
        </a>
      </form>
    </div>
  );
};

export default Login;
