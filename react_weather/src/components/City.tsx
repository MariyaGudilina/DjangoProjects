import * as React from "react";


function City(props){

    const {city, codeCity} = props;

    const handlerCity = (e)=>{
        codeCity(e.target.value); 
    }

    return (
        <div className= "input-city">
    <select onChange={handlerCity}>
                <option >--------------------</option>
                <option value="London">Лондон</option>
                <option value="Msk">Москва</option>
                <option value="Spb">Санкт-Петербург</option>
                <option value="Paris">Париж</option>
                <option value="Prague">Прага</option>
            </select>

        </div>
    );
}

export default City;