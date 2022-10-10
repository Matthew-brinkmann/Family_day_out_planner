import DateSelect from "./DateSelect";
import Header from "./Header";
import PlacesAutocomplete from "react-places-autocomplete"; 

const PlaceSearch = ({ address, handleClick, handleSelect, handleChange, searchClick, newStartDate, startDate }) => {

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
            <DateSelect newStartDate={newStartDate} startDate={startDate} />
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