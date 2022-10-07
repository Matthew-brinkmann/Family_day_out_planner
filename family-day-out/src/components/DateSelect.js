import React, { useState } from "react";
import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";

// CSS Modules, react-datepicker-cssmodules.css
// import 'react-datepicker/dist/react-datepicker-cssmodules.css';

const DateSelect = () => {
  const [startDate, setStartDate] = useState(new Date());
  return (
    <DatePicker
      className="datepicker"
      dateFormat="dd/MM/yyyy"
      selected={startDate}
      onChange={(date) => setStartDate(date)}
    ></DatePicker>
  );
};

export default DateSelect;