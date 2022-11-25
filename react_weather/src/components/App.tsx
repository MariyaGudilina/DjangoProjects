import * as React from "react";
import "../styles/App.css";
import Header from "./Header";
import WeatherNow from "./WeatherNow";

//import Main from "./Main";

//const map = 


function App() {

    var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
    };
    Object.defineProperty(exports, "__esModule", { value: true });

    const data = __importDefault(require("../data.json"));
    const [city, codeCity] = React.useState('Msk');
    let cityParam ={};

    const cityData = JSON.stringify(data);
    const ddd = JSON.parse(cityData);

    for(let i in ddd.default.cityData){
        if(ddd.default.cityData[i].id == city){
            cityParam = ddd.default.cityData[i];
            console.log(ddd.default.cityData[i]);

        } 
    }
    //console.log(ddd.default.cityData);

    

    return (
        <>
            <Header city={city} codeCity={codeCity}/>
            <WeatherNow cityParam={cityParam}/>
        </>
    );
}

export default App;