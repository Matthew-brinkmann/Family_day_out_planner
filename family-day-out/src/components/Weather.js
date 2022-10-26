import React, { useEffect, useState } from "react";
import "./Weather.css";

function Weather({
  maxtemp_c,
  mintemp_c,
  daily_chance_of_rain,
  daily_chance_of_snow,
  condition_text,
  condition_icon,
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
      windowHeight >= window.innerHeight * 0.743
        ? setStickyClass("sticky-nav")
        : setStickyClass("");
    }
  };

  return (
    <div className={`navbar ${stickyClass}`}>
      <div className="weather_section">
        <div id="weather_text">Max temp: {maxtemp_c}°C</div>
        <div id="weather_text">Min temp: {mintemp_c}°C</div>
        <div id="weather_text"> {condition_text}</div>
        <img src={condition_icon} alt="" />
        <div id="weather_text">
          Daily chance of rain: {daily_chance_of_rain}%
        </div>
        <div id="weather_text">
          Daily chance of snow: {daily_chance_of_snow}%
        </div>

        <div id="weather_text">uv: {uv}</div>
      </div>
      <div id="weather_heading">Local temperature</div>
    </div>
  );
}
export default Weather;
