import React from 'react'
import { Link } from "react-router-dom";

const NavSidebarLinkList = ({
  title,
  links
}:{
  title: string,
  links: {
    [key: string]: string
  }
}) => {

  return (
    <div className='mt-4'>
      <h1 className='text-[#52A2EC] font-bold text-xl'>{title}</h1>
      <nav className='text-[#F2F3F3]'>
        <ul className='flex flex-col'>
          {Object.keys(links).map(key => (
            <li key={key}>
              <Link className='px-4 py-2 block' to={`${links[key]}`}>
                {key}
              </Link>
           </li>
          ))}
        </ul>
      </nav>
    </div>
  )
} 


export default function Root() {


  const basicServicesLinks = {
    'Competidores Cercanos':'/nearby-restaurants',
    'Categorias':'/categories',
    'Resenas':'/reviews'
  }

  const machineLearningServicesLinks = {
    'Clientes Potenciales':'/potencial-clients',
    'Clasificador de Resenas':'/natural-language-interpreter',
  }


  return (
    <div className="max-w-[300px] w-full h-[calc(100vh_-_72px)] p-4 bg-[#2E2E2E] flex-col flex justify-between">
      <div>
        <NavSidebarLinkList 
          title={'Servicios Basico'}
          links={basicServicesLinks}
        />
        <NavSidebarLinkList 
          title={'Machine Learning'}
          links={machineLearningServicesLinks}
        />
      </div>
      <div>
        <nav>
          <ul>
            <li>
              <a className='px-4 py-2 block' href='/csv-loader'>
                Cargar Datos
              </a>
            </li>
            <li>
              <Link className='px-4 py-2 block' to={`/settings}`}>
                Configuracio
              </Link>
            </li>
            <li>
              <a className='px-4 py-2 block' href='https://streamlit.com'>
                Dashboard De Streamit
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  );
}