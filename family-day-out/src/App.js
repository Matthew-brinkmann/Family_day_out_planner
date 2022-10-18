import PlaceSearch from "./components/PlaceSearch";
import backgrounImg from "./img/familyfun.jpeg";
import { useState } from "react";
import EventItem from "./components/EventItem";
import { geocodeByAddress, getLatLng } from "react-places-autocomplete";
import Moment from "moment";
import LoadingSpinner from "./components/LoadingSpinner";
import Weather from "./components/Weather";

function App() {
  const [address, setAddress] = useState("");
  const [startDate, setStartDate] = useState(new Date());
  const [errorMessage, setErrorMessage] = useState("");
  const [coordinates, setCoordinates] = useState({
    lat: null,
    lng: null,
  });
  const [eventDisplay, setEventDisplay] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [weatherDisplay, setWeatherDisplay] = useState({});

  const handleSelect = async (value) => {
    const results = await geocodeByAddress(value);
    const latLng = await getLatLng(results[0]);
    setAddress(value);
    setCoordinates(latLng);
  };

  const handleClick = async (suggestion) => {
    const results = await geocodeByAddress(suggestion.description);
    const latLng = await getLatLng(results[0]);
    const input = document.getElementById("id_address_autocomplete");
    input.blur();
    setAddress(suggestion.description);
    setCoordinates(latLng);
  };
  const handleChange = (value) => {
    setAddress(value);
    setCoordinates({
      lat: null,
      lng: null,
    });
  };

  const now = new Date();
  let Difference_In_Days = startDate.getTime() - now.getTime();
  let totalDaysInDays = Math.ceil(Difference_In_Days / (1000 * 3600 * 24));

  const searchClick = async () => {
    setIsLoading(true);
    if (coordinates.lat === null || coordinates.lng === null) {
      setIsLoading(false);
      alert("Please select a place in the dropdown list");
    }

    const response = await fetch("http://0.0.0.0:5006/api/event_information", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        crossDomain: true,
      },
      body: JSON.stringify({
        place_address: address,
        place_latitude: coordinates.lat,
        place_longitude: coordinates.lng,
        selected_date_event_api: Moment(startDate).format("MMM Do YYYY"),
        selected_days_weather_api: totalDaysInDays,
      }),
    });

    const body = await response.json();

    if (body.error1 || coordinates.lat === null) {
      setIsLoading(false);
      setErrorMessage(body.error1);
    } else {
      setErrorMessage("");
      setIsLoading(false);
      setWeatherDisplay(JSON.parse(body).weatherInformation);
      setEventDisplay(JSON.parse(body).eventList);
    }
  };

  return (
    <div className="container">
      <section>
        <img id="top-pic" src={backgrounImg} alt="" />
        <PlaceSearch
          isLoading={isLoading}
          handleSelect={handleSelect}
          handleClick={handleClick}
          handleChange={handleChange}
          searchClick={searchClick}
          address={address}
          newStartDate={setStartDate}
          startDate={startDate}
        />

        {errorMessage !== "" ||
          (Object.keys(weatherDisplay).length > 0 && (
            <Weather
              maxtemp_c={weatherDisplay.maxtemp_c}
              mintemp_c={weatherDisplay.mintemp_c}
              daily_chance_of_rain={weatherDisplay.daily_chance_of_rain}
              daily_chance_of_snow={weatherDisplay.daily_chance_of_snow}
              condition_text={
                weatherDisplay.condition && weatherDisplay.condition.text
                  ? weatherDisplay.condition.text
                  : ""
              }
              condition_icon={
                weatherDisplay.condition &&
                weatherDisplay.condition.icon &&
                weatherDisplay.condition.icon.slice("//")
              }
              uv={weatherDisplay.uv}
            />
          ))}
      </section>

      <section className="events_display">
        {errorMessage !== "" && (
          <div id="errorMessage">
            <h2>{errorMessage}</h2>
          </div>
        )}
        {isLoading && <LoadingSpinner />}

        {errorMessage === "" &&
          eventDisplay.map((event, index) => (
            <EventItem
              key={index}
              title={event.title}
              event_rating={
                event.venue && event.venue.rating ? event.venue.rating : ""
              }
              event_date={event.date.when}
              event_address={event.address[0]}
              event_address_sub={event.address[1]}
              event_image={event.image}
              description={event.description}
              event_link={event.link}
              event_location_image={
                event.event_location_map && event.event_location_map.image
              }
              event_location_direction={
                event.event_location_map && event.event_location_map.link
              }
            />
          ))}
      </section>
    </div>
  );
}
export default App;
