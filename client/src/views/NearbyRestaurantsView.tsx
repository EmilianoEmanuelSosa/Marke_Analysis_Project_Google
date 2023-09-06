import React from 'react'
import { MapContainer, TileLayer, useMap, Marker, Popup} from 'react-leaflet'
import { static_restaurants } from '../utils/static_restaurants';
import 'leaflet/dist/leaflet.css';

export default function NearbyRestaurants() {
  
  const handleOnSubmit = () => {
    
  }


  return (
  
    <MapContainer center={[51.505, -0.09]} zoom={13}>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {/* <Square center={center} size={1000} /> */}
      {static_restaurants.map( (rest, i) => {
        return (
          <Marker key={i} position={[rest.latitude, rest.longitude]}>
          <Popup>
            A pretty CSS3 popup. <br /> Easily customizable.
          </Popup>
        </Marker>
        )
      })}
     
      <Marker position={[51.505, -0.09]}>
        <Popup>
          A pretty CSS3 popup. <br /> Easily customizable.
        </Popup>
      </Marker>
      <Marker position={[62.505, -0.09]}>
        <Popup>
          A pretty CSS3 popup. <br /> Easily customizable.
        </Popup>
      </Marker>
      <Marker position={[73.505, -0.09]}>
        <Popup>
          A pretty CSS3 popup. <br /> Easily customizable.
        </Popup>
      </Marker>
      <Marker position={[84.505, -0.09]}>
        <Popup>
          A pretty CSS3 popup. <br /> Easily customizable.
        </Popup>
      </Marker>
    </MapContainer>
   
  )
}
