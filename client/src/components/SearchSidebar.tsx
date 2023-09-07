import React from 'react'
import { Link } from "react-router-dom";

export default function SearchSidebar() {


  const basicServicesLinks = {
    'Competidores Cercanos':'',
    'Categorias':'categories',
    'Resenas':'reviews',
    'Usuarios':'users'
  }

  const machineLearningServicesLinks = {
    'Clientes Potenciales':'adas',
    'Clasificador de Resenas':'dadas',
  }

  


  return (
    <div className="max-w-[300px] shadow-[4px_0px_4px_0px_#00000055] z-20 w-full  h-[calc(100vh_-_72px)] p-4 bg-[#ECF2F9] flex-col flex">
      <div>
        <nav>
          <ul>
          <li>
            <Link className='px-4 py-2 block' to={`/settings}`}>
              Configuraci
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