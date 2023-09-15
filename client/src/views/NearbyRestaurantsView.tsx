import { useState,  useEffect } from 'react'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import SearchSidebar  from '../components/SearchSidebar'
import { Star } from 'react-feather';
import axios  from 'axios'
import { RestaurantType } from '../utils/types';
import 'leaflet/dist/leaflet.css';
import useConfig from '../hooks/useConfig';

export default function NearbyRestaurants() {
  
  const [restaurantList, setRestaurantList] = useState<RestaurantType[] | null>(null)
  const [selectedRestaurant, setSelectedRestaurant] = useState<RestaurantType | null>(null)
  const [km2, _] = useState<number>(0.1)
  const { restaurant } = useConfig()
  
  useEffect(() => {
    if (!restaurant) return;

    axios.get(`https://restauranttracking.onrender.com/api/restaurantes_en_radio/${restaurant.restaurant_id}/${km2}/?format=json`).then((response) => {
      setRestaurantList(response.data)
    })
  }, [restaurant]);

  const handleSelect = (restaurant:RestaurantType) => {
    setSelectedRestaurant(restaurant)
  } 

  const getScore = (score: number) => {
    return Math.round(score)
  }

  function createArray(N:number) {
    return [...Array(N).keys()].map(i => i + 1);
}

  return !restaurantList 
  ? <></>
  : (
    <div className='flex flex-row h-full'>
      <SearchSidebar 
        data={restaurantList} 
      ></SearchSidebar >
      <div className='h-full w-full'>
        {(!restaurant || !restaurantList)
          ? <div className='bg-slate-900 text-white font-bold flex items-center justify-center h-[60%]'>
              Cargando...
            </div>   
          : <MapContainer className='h-[60%] z-10' center={[restaurant.latitude, restaurant.longitude]} zoom={13}>
              <TileLayer
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              />
              {/* <Square center={center} size={1000} /> */}
              {restaurantList.slice(0,200).map( (rest, i) => {
                return (
                  <Marker eventHandlers={{click(){handleSelect(rest)}}} key={i} position={[rest.latitude, rest.longitude]}>
                  <Popup>
                    {rest.name}
                  </Popup>
                </Marker>
                )
              })}
            </MapContainer>
        }
        <div className='w-full h-[300px] pt-4 px-4   relative z-20 shadow-[0px_-4px_4px_0px_#00000055]'>
          <div className='bg-[#FEFEFE] text-[#4E4E4E] grid grid-cols-3 w-full h-full rounded-xl shadow-[0px_0px_4px_0px_#00000055]'>
            <div className="p-4">
              <h1 className='text-lg text-bold'>{selectedRestaurant?.name}</h1>
              <div>{selectedRestaurant?.latitude}</div>
              <div>{selectedRestaurant?.longitude}</div>
              <div><span className='font-bold'>Direccion:</span> {selectedRestaurant?.address}</div>
              <div><span className='font-bold'>Numero de reseñas: </span>{selectedRestaurant?.review_count}</div>
              <div className='flex flex-row gap-0.5'>
                <h2 className='font-bold'>Valoracion:</h2>
                {createArray(getScore(selectedRestaurant?.rating ?? 1)).map(()=>{
                  return <Star className="fill-[#FFE81A] stroke-[#FFE81A] "/>  
                })}
                {createArray(5 - getScore(selectedRestaurant?.rating ?? 1)).map(()=>{
                  return <Star className="stroke-[#2E2E2E]"/>  
                })}
              </div>            
            </div>
            <div className=' col-span-2'>
              <h2>Juan Pablo Guerrero</h2>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

            </div>
          </div>  
        </div>
      </div>
    </div>
  )
}
