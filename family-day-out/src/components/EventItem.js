import './EventItem.css'
function EventItem() {
  return (
    <div className='event-item'>
      <div>March 28th 2022</div>
      <div className='event-item_description'>
        <h2>Collingwood's Family Children Farm</h2>
        <div>weather</div>
        <div>opening hours: </div>
        <div>closing hours: </div>
        <div>URL to know more please click here</div>
      </div>
    </div>
  );
}

export default EventItem;
