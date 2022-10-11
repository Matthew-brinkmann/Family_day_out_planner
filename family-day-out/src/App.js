import PlaceSearch from "./components/PlaceSearch";
import backgrounImg from "./img/familyfun.jpeg";
import { useState } from "react";
import EventItem from "./components/EventItem";
import Moment from "moment";
import { geocodeByAddress, getLatLng } from "react-places-autocomplete";

const events_results = [
  {
    title: "Avi Avital",
    date: {
      start_date: "Sep 24",
      when: "Sat, Sep 24, 7 – 9 PM GMT+10",
    },
    address: [
      "Melbourne Recital Centre, 31 Sturt St",
      "Southbank VIC, Australia",
    ],
    link: "https://www.songkick.com/concerts/40429762-avi-avital-at-melbourne-recital-centre?utm_medium=organic&utm_source=microformat",
    event_location_map: {
      image:
        "https://www.google.com/maps/vt/data=2ikm3IrGV_2-ngdl3aatgFd0wRGHiRMlLfTnQSvphlNMH3xazkPtQ4KUzD4sHbI4oOtbXkhHtjTVyEEbdIJVdAUkIpLLwqoI4DzZf5gzszkeaJt8MPE",
      link: "https://www.google.com/maps/place//data=!4m2!3m1!1s0x6ad642ae1a5e9b83:0xef21a57877623bbe?sa=X&hl=en",
      serpapi_link:
        "https://serpapi.com/search.json?data=%214m2%213m1%211s0x6ad642ae1a5e9b83%3A0xef21a57877623bbe&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Melbourne%2C+Vic+on+24%2F09%2F2022&type=place",
    },

    description:
      "Avi Avital and Giovanni Sollima at Melbourne Recital Centre at 2022-09-24",
    image:
      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyv2akIbFVKQ436gGwt-NJuojN8gmv9G8yD5sss_HzTCT6JZlxJnPrtPgrUQ&s=10",
  },
  {
    title: "Main Stage @ Comedy Republic",
    date: {
      start_date: "Sep 24",
      when: "Sat, 8:30 – 10:00 PM",
    },
    address: ["Comedy Republic, 231 Bourke St", "Melbourne VIC, Australia"],
    link: "https://www.eventbrite.com.au/e/main-stage-comedy-with-harry-jun-prue-blake-more-tickets-368750993147",
    event_location_map: {
      image:
        "https://www.google.com/maps/vt/data=wIqWsp1-GGcNcCG9pcdLjM59HuZ4uRl54WfMXpwe5hDeZXlaD59rkC2ana1kq0chd-pQ_u-HXQac7-LihJazvkXFtLhVdLzSxLjisvn5-Vmptzt70D4",
      link: "https://www.google.com/maps/place//data=!4m2!3m1!1s0x6ad643f87996e99b:0xa4e5b67e456665b4?sa=X&hl=en",
      serpapi_link:
        "https://serpapi.com/search.json?data=%214m2%213m1%211s0x6ad643f87996e99b%3A0xa4e5b67e456665b4&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Melbourne%2C+Vic+on+24%2F09%2F2022&type=place",
    },
    description:
      "Prue Blake, Harry Jun, Lou Wall, Ben Searle, Rohan Ganju & More",
    image:
      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSi57_2UOkSqO3jnfmsK5tqqliMkZ0f5KXnwT5KxSsNbw&s=10",
  },
];

function App() {
  const [address, setAddress] = useState("");
  const [startDate, setStartDate] = useState(new Date());
  const [coordinates, setCoordinates] = useState({
    lat: null,
    lng: null,
  });
  // const [EventDisplay, setEventDisplay] = useState(events_results)

  const handleSelect = async (value) => {
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
      lng: null,
    });
  };
  //selected_days_weather_api
  const now = new Date();
  let Difference_In_Days = startDate.getTime() - now.getTime();
  let totalDaysInDays = Math.ceil(Difference_In_Days / (1000 * 3600 * 24));

  

  const searchClick = () => {
    if (coordinates.lat === null || coordinates.lng === null)
      alert("Please select a place in the dropdown list");
    fetch("http://0.0.0.0:3000/api/event_information", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        crossDomain: true,
      },
      body: JSON.stringify({
        place_address: address,
        place_latitude: coordinates.lat,
        place_longitude: coordinates.lng,
        selected_date_event_api: Moment(startDate).format("DD-MM-YYYY"),
        selected_days_weather_api: totalDaysInDays,
      }),
    });
    // setEventDisplay(EventDisplay.map((event, index) => (
    //   <EventItem
    //     key={index}
    //     title={event.title}
    //     event_date={event.date.when}
    //     event_address={event.address[0]}
    //     event_address_sub={event.address[1]}
    //     event_image={event.image}
    //     description={event.description}
    //     event_link={event.link}
    //     event_location_image={event.event_location_map.image}
    //     event_location_direction={event.event_location_map.link}
    //   />
    // )))
  };
  

  return (
    <div className="container">
      <img id="top-pic" src={backgrounImg} alt="" />
      <PlaceSearch
        handleSelect={handleSelect}
        handleClick={handleClick}
        handleChange={handleChange}
        searchClick={searchClick}
        address={address}
        newStartDate={setStartDate}
        startDate={startDate}
      />
      <section>
    {events_results.map((event, index) => (
      <EventItem
        key={index}
        title={event.title}
        event_date={event.date.when}
        event_address={event.address[0]}
        event_address_sub={event.address[1]}
        event_image={event.image}
        description={event.description}
        event_link={event.link}
        event_location_image={event.event_location_map.image}
        event_location_direction={event.event_location_map.link}
      />
    ))}
      </section>
    </div>
  );
}
export default App;
