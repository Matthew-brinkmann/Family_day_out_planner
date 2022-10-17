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
  event_rating,
}) {
  return (
    <article className="event-item">
      <div>
        <img id="event_image" src={event_image} alt="" />
      </div>
      <div className="event-item_description">
        <h2>{title}</h2>
        <div>{description}</div>
        {event_rating && <div>Review rating: {event_rating}</div>}
        <div>
          <a href={event_link} rel="noreferrer" target="_blank">
            To know more please click here
          </a>
        </div>
        <div>{event_address}</div>
        <div>{event_address_sub}</div>
        <div style={{ color: "red" }}>{event_date}</div>
        <img src={event_location_image} alt="" />
        {event_location_direction && (
          <div className="event-item_location">
            <img id="icon_location" src={Icon_location} alt="" />
            <a href={event_location_direction} rel="noreferrer" target="_blank">
              How to get here
            </a>
          </div>
        )}
      </div>
    </article>
  );
}

export default EventItem;
