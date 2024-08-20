import React, { useState } from "react";
import AuthService from "../../services/AuthService";
import { Link } from "react-router-dom";

const SignUp = () => {
  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (event: any) => {
    event.preventDefault();
    try {
      await AuthService.register({ fullName, email, password });
      alert("You have registered successfully!");
      window.location.href = "/";
    } catch (error) {
      alert("Unable to register! Try again!");
      setFullName("");
      setEmail("");
      setPassword("");
    }
  };

  return (
    <div className="flex w-full h-full justify-center bg-gray-200">
      <form
        onSubmit={handleSubmit}
        className="mt-[10%] p-10 gap-y-8 h-fit w-[25vw] flex-col flex items-left rounded-xl bg-gray-300"
      >
        <div className="mx-auto font-semibold text-3xl">Signup</div>
        <div className="flex items-center justify-between">
          <label htmlFor="fullName">Full Name:</label>
          <input
            type="text"
            id="fullName"
            name="fullName"
            className="w-[15vw]"
            value={fullName}
            onChange={(e) => setFullName(e.target.value)}
            required
          />
        </div>
        <div className="flex items-center justify-between">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            name="email"
            className="w-[15vw]"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
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
        <button type="submit" className="w-full">
          Sign Up
        </button>
        <Link to={"/login"} className="underline text-sm mx-auto w-fit">
          Already a member? Login here
        </Link>
      </form>
    </div>
  );
};

export default SignUp;
