import { useState, useRef } from "react";
import validator from "validator";
import classes from "./AuthForm.module.css";
import bcrypt from "bcryptjs";

const AuthForm = ({ isShowLogin, newToken }) => {
  const usernameInputRef = useRef();
  const passwordInputRef = useRef();
  const hashedPassword = bcrypt.genSaltSync(10);

  const [isLogin, setIsLogin] = useState(true);
  const [isLoading, setIsLoading] = useState(false);
  const switchAuthModeHandler = () => {
    setIsLogin((prevState) => !prevState);
  };
  const [errorMessage, setErrorMessage] = useState("");

  const validate = (value) => {
    if (
      validator.isStrongPassword(value, {
        minLength: 8,
        minLowercase: 1,
        minUppercase: 1,
        minNumbers: 1,
        minSymbols: 1,
      })
    ) {
      setErrorMessage("Is Strong Password");
    } else {
      setErrorMessage("Is Not Strong Password");
    }
  };
  const submitHandler = (event) => {
    event.preventDefault();

    const enteredusername = usernameInputRef.current.value;
    // const enteredPassword = passwordInputRef.current.value;

    setIsLoading(true);
    if (isLogin) {
      // fetch("http://0.0.0.0:5006/api/login");
    } else {
      fetch("http://0.0.0.0:5006/api/test/login_success", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: enteredusername,
          password: hashedPassword,
        }),
      }).then(async (res) => {
        setIsLoading(false);
        if (res.ok) {
          const data = await res.json();
          const formattedData = JSON.parse(data);
          newToken(formattedData.token);
          console.log(formattedData.token);
        } else {
          const data_2 = await res.json();
          console.log(data_2);
        }
      });
    }
  };

  return (
    <div className={`${!isShowLogin ? "active" : ""} show`}>
      <section className={classes.auth}>
        <h1>{isLogin ? "Login" : "Sign Up"}</h1>
        <form onSubmit={submitHandler}>
          <div className={classes.control}>
            {/* <label htmlFor="email">Your Email</label> */}
            {/* <input type="email" id="email" required ref={usernameInputRef} /> */}
            <label>Username</label>
            <input type="text" required ref={usernameInputRef} />
          </div>
          <div className={classes.control}>
            <label htmlFor="password">Your Password</label>
            <p>
              minLength: 8, min 1 Lowercase, min 1 Uppercase, min 1 Numbers, min
              1 Symbols
            </p>
            <input
              type="password"
              id="password"
              required
              ref={passwordInputRef}
              onChange={(e) => validate(e.target.value)}
            />{" "}
            <br />
            {errorMessage === "" ? null : (
              <span
                style={{
                  fontWeight: "bold",
                  color: "red",
                }}
              >
                {errorMessage}
              </span>
            )}
          </div>
          <div className={classes.actions}>
            {!isLoading && (
              <button>{isLogin ? "Login" : "Create Account"}</button>
            )}
            {isLoading && <p>Loading....</p>}
            <button
              type="button"
              className={classes.toggle}
              onClick={switchAuthModeHandler}
            >
              {isLogin ? "Create new account" : "Login with existing account"}
            </button>
          </div>
        </form>
      </section>
    </div>
  );
};

export default AuthForm;
