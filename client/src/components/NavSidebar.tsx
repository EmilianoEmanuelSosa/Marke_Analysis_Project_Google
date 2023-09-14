import { Link } from "react-router-dom";
import { ChevronRight, File, Settings } from 'react-feather';
import ConfigBtn from "../views/ConfigBtn";

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
    <div className=''>
      <h1 className='text-[#52A2EC] font-bold text-xl'>{title}</h1>
      <nav className='text-[#F2F3F3]'>
        <ul className='flex flex-col'>
          {Object.keys(links).map(key => (
            <li key={key}>
              <Link className='px-4 py-2 flex items-center justify-between  hover:bg-[#3E3E3E] rounded-lg' to={`${links[key]}`}>
                {key}
                <ChevronRight className="w-5"/>
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

  const analiticsServicesLinks = {
    'Reporte de Streamlit':'https://streamlit.com',
    'Dashboard Interactivo':'/dashboard',
  }


  return (
    <div className="max-w-[290px] w-full h-[calc(100vh_-_72px)] px-4 py-6 bg-[#2E2E2E] flex-col flex justify-between">
      <div className="flex flex-col gap-4">
        <NavSidebarLinkList 
          title={'Servicios Basico'}
          links={basicServicesLinks}
        />
        <NavSidebarLinkList 
          title={'Machine Learning'}
          links={machineLearningServicesLinks}
        />
         <NavSidebarLinkList 
          title={'Machine Learning'}
          links={analiticsServicesLinks}
        />
      </div>
      <div>
        <nav>
          <ul>
            <li>
              <a className='px-4 py-2 block' href='/csv-loader'>
                <File />
                Cargar Datos
              </a>
            </li>
            <li>
              <ConfigBtn 
                className=""
              >
                <Settings />
                Configuracio
              </ConfigBtn>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  );
}