import * as React from "react";
import axios from "axios";
import "../styles/Header.css";


function Header(){
    const [nameCity, getCity] = React.useState([]);  

    return (
    <header>   
        <div className="header-main">
            <h4>Выберите город:</h4> 
            <input className="input-city" type="type"></input>
            <button className="Now">Сейчас</button>
        </div>
     </header> 
    )
}

export default Header;