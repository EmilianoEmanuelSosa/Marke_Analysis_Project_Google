import { useState, useMemo } from 'react'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import SearchSidebar  from '../components/SearchSidebar'
import { static_restaurants } from '../utils/static_restaurants';
import 'leaflet/dist/leaflet.css';
import { LeafletEventHandlerFnMap } from 'leaflet';

type RestuaranType = {
  restaurant_id: string,
  name: string,
  address: string,
  latitude: number,
  longitude: number,
  rating: number,
  review_count: number,
  categories: string,
  Restaurant: number,
}

export default function NearbyRestaurants() {
  
  const [selectedRestaurant, setSelectedRestaurant] = useState<RestuaranType | null>(null)
  const handleOnSubmit = () => {
    
  }

  const handleSelect = (restaurant:RestuaranType) => {
    setSelectedRestaurant(restaurant)
  } 

  const own_restaruants =  static_restaurants[500]

  return (
    <div className='flex flex-row h-full'>
      <SearchSidebar ></SearchSidebar >
      <div className='h-full w-full'>
        <MapContainer className='h-[60%] z-10' center={[own_restaruants.latitude, own_restaruants.longitude]} zoom={13}>
          <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          {/* <Square center={center} size={1000} /> */}
          {static_restaurants.slice(0,200).map( (rest, i) => {
            return (
              <Marker eventHandlers={{click(){handleSelect(rest)}}} key={i} position={[rest.latitude, rest.longitude]}>
              <Popup>
                {rest.name}
              </Popup>
            </Marker>
            )
          })}
        </MapContainer>
        <div className='w-full h-[300px] pt-4 px-4   relative z-20 shadow-[0px_-4px_4px_0px_#00000055]'>
          <div className='bg-white w-full h-full rounded-xl shadow-[0px_0px_4px_0px_#00000055]'>
            <div>
              <h1>{selectedRestaurant?.name}</h1>
              <div>{selectedRestaurant?.latitude}</div>
              <div>{selectedRestaurant?.longitude}</div>
              <div>{selectedRestaurant?.rating}</div>
              <div>{selectedRestaurant?.address}</div>
              <div>{selectedRestaurant?.review_count}</div>

            </div>
            <div className=''>
              <h2>Juan Pablo Guerrero</h2>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

            </div>
          </div>  
        </div>
      </div>
    </div>
  )
}
