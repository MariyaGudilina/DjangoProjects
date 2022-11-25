import * as React from "react";
import axios from "axios";
import "../styles/Header.css";
//import YMapsmy from "./YMapsmy";
import City from "./City";


function Header(props){
    const {city, codeCity} = props;

    const handlerNow =()=>{
        
    }
   
    return (
    <header>
        <img alt="Logo" src="../src/photo_2022-11-23_18-45-19.jpg"/>
        <div className="header-main">
            <h4>Выберите город:  </h4> 
            <City city={city} codeCity={codeCity}/>
            <button className="now" onClick={handlerNow}>Сейчас</button>
        </div>
         
        
     </header> 
    )
}

export default Header;