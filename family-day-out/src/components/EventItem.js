import "./EventItem.css";
import Icon_location from "../img/location_icon.png";

function EventItem({
  title,
  event_address,
  event_address_sub,
  event_date,
  event_image,
  description,
  event_link,
  event_location_image,
  event_location_direction,
}) {
  return (
    <article className="event-item">
        <div>
          <img id="event_image" src={event_image} alt="" />
        </div>
        <div className="event-item_description">
          <h2>{title}</h2>
          <div>{description}</div>
          <div>
            <a href={event_link}>To know more please click here</a>
          </div>
          <div>{event_address}</div>
          <div>{event_address_sub}</div>
          <div>{event_date}</div>
          {/* add if condition, if doesn't exit => "No Image Available" */}
          {/* <img src={event_location_image} alt="" /> */}
          <div className="event-item_location">
            <img id="icon_location" src={Icon_location} alt="" />
            <a href={event_location_direction}>How to get here</a>
          </div>
        </div>
    </article>
  );
}

export default EventItem;
