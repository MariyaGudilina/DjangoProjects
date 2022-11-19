import * as React from "react";
import axios from "axios";
import Table from 'react-bootstrap/Table';

import "../styles/WeatherNow.css";

function WeatherNow(){
    const [weather, viewWeatherNow] = React.useState([]);
    const [wind, viewWindNow] = React.useState([]);

    if(!weather.length) {
        axios.get("https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&units=metric&appid=ff2380d7531890c964de29924c0fc1c1").then(res => {
            console.log(res.data.main.temp);
            viewWeatherNow(res.data.main.temp);
            viewWindNow(res.data.wind.speed);
        });
    }
    return(
        <Table striped bordered hover className={"weather"}>
        <thead><tr><th>Город</th><th>Температура</th><th>Скорость ветра</th></tr></thead>
        <tbody>
        <tr>
            <td>{weather}</td>
            <td>{weather} °C</td>
            <td>{wind} метр/сек</td>
            <td></td>
        </tr>
        </tbody>
    </Table>


    )

    
}

export default WeatherNow;
