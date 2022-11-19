import * as React from "react";
import "../styles/App.css";
import Header from "./Header";
import WeatherNow from "./WeatherNow";

//import Main from "./Main";

function App() {
   
    return (
        <>
            <img className= "logo"/>
            <Header />
            <div className="City">
            </div>
            <WeatherNow/>
        </>
    );
}

export default App;