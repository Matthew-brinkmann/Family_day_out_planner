import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";

// CSS Modules, react-datepicker-cssmodules.css
// import 'react-datepicker/dist/react-datepicker-cssmodules.css';
const DateSelect = ({ startDate, newStartDate }) => {
  const date = new Date();

  return (
    <DatePicker
      className="datepicker"
      dateFormat="dd/MM/yyyy"
      minDate={new Date()}
      maxDate={new Date(date.setMonth(date.getMonth() + 2))}
      selected={startDate}
      onChange={(date) => newStartDate(date)}
      showDisabledMonthNavigation
    >
      <div style={{ color: "red" }}> Choose date no more than two months</div>
    </DatePicker>
  );
};

export default DateSelect;
