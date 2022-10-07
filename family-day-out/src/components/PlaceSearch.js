import DateSelect from "./DateSelect";
import Header from "./Header";
import { useState } from "react";
import PlacesAutocomplete, { geocodeByAddress, getLatLng } from "react-places-autocomplete"; 
import Moment from 'moment';

const PlaceSearch = () => {
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
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'crossDomain': true,
        },
        body: JSON.stringify({ 'place_address': address, 
          'place_latitude': coordinates.lat, 
          'place_longitude': coordinates.lng, 
          'selected_date_evet_api': Moment(startDate).format('DD-MM-YYYY'), 
          'selected_days_weather_api': totalDaysInDays})
        })
      }

  return (
    <div><Header title="Family Day Out Planner" />
      <PlacesAutocomplete
        value={address}
        onChange={(value) => handleChange(value)}
        onSelect={handleSelect}
      >
        {({ getInputProps, suggestions, getSuggestionItemProps, loading }) => (
          <div class="search_buttons">
            <input
              id="id_address_autocomplete"
              {...getInputProps({ placeholder: "Search Places" })}
            />
            <div className="react-datepicker-container">
            <DateSelect newStartDate={setStartDate} startDate={startDate} />
            </div>
            <button onClick={searchClick} className="btn">Search</button>
            <div className="autocomplete-dropdown-container">
              {loading && <div>Loading...</div>}
              {suggestions.map((suggestion, index) => {
                const style = suggestion.active
                  ? { backgroundColor: "#41b6e6", cursor: "pointer" }
                  : { backgroundColor: "#ffffff", cursor: "pointer" };
                return (
                  <div
                    key={index}
                    {...getSuggestionItemProps(suggestion, { style })}
                    onClick={() => handleClick(suggestion)}
                  >
                    {suggestion.description}
                  </div>
                );
              })}
            </div>
          </div>
        )}
      </PlacesAutocomplete>
    </div>
  );
};
export default PlaceSearch
