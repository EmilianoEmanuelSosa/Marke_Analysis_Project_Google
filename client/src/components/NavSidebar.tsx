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
    'Resenas':'/reviews'
  }

  const machineLearningServicesLinks = {
    'Clasificador de Resenas':'/natural-language-interpreter',
  }

  const analiticsServicesLinks = {
    'Reporte de Streamlit':'https://streamlit.com',
    'Dashboard Interactivo':'/dashboard',
  }


  return (
    <div className="max-w-[290px] w-full h-[calc(100vh_-_72px)] px-4 py-6 bg-[#2E2E2E] shadow-[3px_0px_3px_0px_#00000055] flex-col flex justify-between">
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
        <nav className="border-t border-[#F2F3F3]">
          <ul className="text-[#F2F3F3] mt-4 fill-[#F2F3F3]">
            <li>
              <a className='px-4 py-2 flex flex-row hover:underline underline-offset-4 gap-8' href='/csv-loader'>
                <File />
                Cargar Datos
              </a>
            </li>
            <li >
              <ConfigBtn 
                className="px-4 py-2 flex flex-row hover:underline underline-offset-4 gap-8"
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