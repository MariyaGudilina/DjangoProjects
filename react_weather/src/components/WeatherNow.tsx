import * as React from "react";
import axios from "axios";
import Table from 'react-bootstrap/Table';
import "../styles/WeatherNow.css";

import {appid} from '../env';


function WeatherNow(props){
    const [weather, viewWeatherNow] = React.useState([]);
    const [wind, viewWindNow] = React.useState([]);

    const lat:String = props.cityParam.lat;
    const lon:String = props.cityParam.lon;
    
    const request = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&units=metric&appid="+appid;
   
    //console.log(request);
   
    if(!weather.length) {
        axios.get(request).then(res => {
            console.log(res.data.main.temp);
            viewWeatherNow(res.data.main.temp);
            viewWindNow(res.data.wind.speed);
        }).catch(function (error) {
            // обработка ошибки
            alert("Выберите город!");
            console.log(error);
          })
    }
    return(
        <Table striped bordered hover className={"weather"}>
        <thead><tr><th>Город</th><th>Температура</th><th>Скорость ветра</th></tr></thead>
        <tbody>
        <tr>
            <td>{props.cityParam.nameCyr}</td>
            <td>{weather} °C</td>
            <td>{wind} метр/сек</td>
            <td></td>
        </tr>
        </tbody>
    </Table>


    )

    
}

export default WeatherNow;
