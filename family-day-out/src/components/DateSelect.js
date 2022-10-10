
import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";

// CSS Modules, react-datepicker-cssmodules.css
// import 'react-datepicker/dist/react-datepicker-cssmodules.css';
const DateSelect = ({ startDate, newStartDate }) => {
  return (
    <DatePicker
      className="datepicker"
      dateFormat="dd/MM/yyyy"
      selected={startDate}
      onChange={(date) => newStartDate(date)}
    ></DatePicker>
  );
};

export default DateSelect;