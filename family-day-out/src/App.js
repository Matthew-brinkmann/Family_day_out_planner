import Header from "./components/Header";
import PlaceSearch from "./components/PlaceSearch";
import backgrounImg from './img/familyfun.jpeg';

function App() {
  return (
    <div className="container">
      {/* <Header title="Family Day Out Planner" /> */}
      <img src={backgrounImg} alt="" />
      <PlaceSearch />
    </div>
  );
}

export default App;
