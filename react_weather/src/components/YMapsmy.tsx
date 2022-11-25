import * as React from "react";
import { YMaps, Map, Placemark} from "react-yandex-maps";


function YMapsmy(){
    const [zoom, setZoom] = React.useState(9);
    const [center, getCenter] = React.useState([55.76, 37.64]);
    
    const mapState = React.useMemo(
      () => ({ center, zoom }),
      [zoom]
    );
  
return(
    <YMaps query={{ load: 'control.ZoomControl' }}>
        <>
          <Map state={{zoom: 9, center: [55.76, 37.64], controls: ['zoomControl'],}} onLoad={(ymaps=>console.log(ymaps))}/> 

        </>
    </YMaps>
);

}

export default YMapsmy;