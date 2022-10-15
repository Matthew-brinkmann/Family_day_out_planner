import React, { useEffect, useState } from "react";
import "./Weather.css";

function Weather({
  maxtemp_c,
  mintemp_c,
  daily_chance_of_rain,
  daily_chance_of_snow,
  // condition_text,
  // condition_icon,
  uv,
}) {
  const [stickyClass, setStickyClass] = useState("");

  useEffect(() => {
    window.addEventListener("scroll", stickNavbar);
    return () => window.addEventListener("scroll", stickNavbar);
  }, []);

  const stickNavbar = () => {
    if (window !== undefined) {
      let windowHeight = window.scrollY;
      windowHeight > 580 ? setStickyClass("sticky-nav") : setStickyClass("");
    }
  };
  return (
    <div className={`navbar ${stickyClass}`}>
      <div>
        <h2>{maxtemp_c}</h2>
      </div>
      <div>
        <h2>{mintemp_c}</h2>
      </div>
      <div>{/* <h2>{condition_text}</h2> */}</div>
      {/* <img src={condition_icon} alt="" /> */}
      <div>
        <h2>Daily chance of rain: {daily_chance_of_rain}</h2>
      </div>
      <div>
        <h2>{daily_chance_of_snow}</h2>
      </div>

      <div>
        <h2>{uv}</h2>
      </div>
    </div>
  );
}
export default Weather;
