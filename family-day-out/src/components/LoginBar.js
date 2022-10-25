import "./LoginBar.css";

function LoginBar({ handleLoginClick }) {
  const handleClick = () => {
    handleLoginClick();
  };
  return (
    <button onClick={handleClick} className="Loginbutton">
      Sign In
    </button>
  );
}

export default LoginBar;
