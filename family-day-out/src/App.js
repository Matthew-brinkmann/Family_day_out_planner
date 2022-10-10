import PlaceSearch from "./components/PlaceSearch";
import backgrounImg from "./img/familyfun.jpeg";
import { useState } from "react";
import EventItem from "./components/EventItem";
import Moment from 'moment';
import { geocodeByAddress, getLatLng } from "react-places-autocomplete"; 

function App() {
  const [address, setAddress] = useState("");
  const [startDate, setStartDate] = useState(new Date());
  const [coordinates, setCoordinates] = useState({
    lat: null,
    lng: null
  });

  const handleSelect = async (value) => {
    console.log(value);
     const results = await geocodeByAddress(value);
     const latLng = await getLatLng(results[0]);
     setAddress(value);
     setCoordinates(latLng);
  };

  //click on suggestion to show address
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
      lng: null
    })
  }
//selected_days_weather_api
const now = new Date();
let Difference_In_Days = startDate.getTime() - now.getTime();
let totalDaysInDays = Math.ceil(Difference_In_Days / (1000 * 3600 * 24));

  const searchClick = () => {
    if (coordinates.lat === null || coordinates.lng === null)
    alert("Please select a place in the dropdown list");
    fetch('http://0.0.0.0:5000/api/event_information', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'crossDomain': true,
        },
        body: JSON.stringify({ 'place_address': address, 
          'place_latitude': coordinates.lat, 
          'place_longitude': coordinates.lng, 
          'selected_date_event_api': Moment(startDate).format('DD-MM-YYYY'), 
          'selected_days_weather_api': totalDaysInDays})
        })
  }

  return (
    <div className="container">
      {/* <Header title="Family Day Out Planner" /> */}
      <img src={backgrounImg} alt="" />
      <PlaceSearch handleSelect={handleSelect} handleClick={handleClick} handleChange={handleChange} searchClick={searchClick} address={address} newStartDate={setStartDate} startDate={startDate} />
      <EventItem />
      <EventItem />
      <EventItem />
    </div>
  );
  }
export default App;
