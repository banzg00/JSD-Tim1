import { useNavigate } from "react-router-dom";
import "./PageNotFound.scss";
import React from "react";

const PageNotFound: React.FC = () => {
  const navigate = useNavigate();

  const handleGoHomeClick = (): void => {
    navigate("/home");
  }

  return (
    <div className="position">
        <img src="/page-not-found.gif" alt="home" className="image"/>
        <h1>Ooops!</h1>
        <h3>It looks like you've gotten lost.</h3>

        <div className="homeButton">
            <div className="wrapper">
                <button className="button" onClick={handleGoHomeClick}>
                    <p className="label"> Go home </p>
                </button>
            </div>
        </div>
    </div>
  );
};

export default PageNotFound;