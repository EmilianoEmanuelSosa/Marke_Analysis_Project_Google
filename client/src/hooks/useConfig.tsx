import { useState, useContext, createContext, ReactNode } from 'react'
import { RestaurantType } from '../utils/types'
// import axios from 'axios'
// import { useLocation } from 'react-router'

interface ConfigI {
  setRestaurant: React.Dispatch<React.SetStateAction<RestaurantType | undefined>>
  restaurant?: RestaurantType
}

//context with
const ConfigContext = createContext<ConfigI | undefined>(undefined)
const defaultContext: ConfigI= {
  setRestaurant: _ => {}, 
  restaurant: undefined,
}

const ConfigProvider = (props:{
  children:ReactNode,
}):JSX.Element => {
  const context = useContext(ConfigContext)
  return context 
    ? <>props.children</>
    : <Config {...props}/>
}

const Config = ({
  children,
}:{
  children: React.ReactNode,
}):JSX.Element => {
  
  const [restaurant, setRestaurant] = useState<RestaurantType | undefined>(undefined);

  const providervalue = {
    setRestaurant,
    restaurant
  }

  return (
    <ConfigContext.Provider value={providervalue}>
      {children}
    </ConfigContext.Provider>
  )
}

const useConfig = () => ({...useContext(ConfigContext) ?? defaultContext, ConfigProvider})
export default useConfig;