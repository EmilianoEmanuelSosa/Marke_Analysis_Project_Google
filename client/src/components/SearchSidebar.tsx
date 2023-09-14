import { RestaurantType } from "../utils/types";

export default function SearchSidebar({
  data,
}:{
  data: RestaurantType[],
}) {

  return (
    <div className="max-w-[300px] shadow-[4px_0px_4px_0px_#00000055] z-20 w-full  h-[calc(100vh_-_72px)] bg-[#ECF2F9] flex-col flex">

        <div className='border border-b-[#A8A8A8] px-4 py-6'>
          <div>
            <h1 className='text-[#2D2D2D] font-bold text-xl'>Competidores cercanos</h1>
            <p className='text-xs text-[#4E4E4E] mt-1'>Rastrea la ubicación de los competidores cercanos a tu establecimiento.</p>
          </div>
          <form className='flex flex-col gap-2 mt-4'>
            <fieldset className="relative">
              <input
                className='shadow-[0px_0px_3px_0px_#00000055] py-2 px-2  rounded-md bg-[#FEFEFE]'
                placeholder='Km2'
              />
            </fieldset>
            <fieldset className="relative">
              <select 
                className='w-full shadow-[0px_0px_3px_0px_#00000055] py-2.5 text-[#4E4E4E] px-2 rounded-md bg-[#FEFEFE] '
                name="languages" 
                id="lang">
                <option value="javascript">JavaScript</option>
                <option value="php">PHP</option>
                <option value="java">Java</option>
                <option value="golang">Golang</option>
                <option value="python">Python</option>
                <option value="c#">C#</option>
                <option value="C++">C++</option>
                <option value="erlang">Erlang</option>
              </select>      
            </fieldset>
          </form>
        </div>
        <h1 className='px-4 pt-6 text-[#2D2D2D] font-bold text-md'>Resultados</h1>
        <div className='px-4 mt-2 overflow-y-scroll'>
        <nav className="bg-[#FEFEFE] text-[#4E4E4E] overflow-y-scroll w-full h-full rounded-md shadow-[0px_0px_3px_0px_#00000055]">
          <ul className=''>
            {data.map((restaurantData, index) => {
              
              return (
                <li key={index}>
                  <button 
                    className='w-full py-3 px-2 flex items-center text-left'
                    // onClick={() => setData(restaurantData.restaurant_id)}
                    >
                    {restaurantData.name}
                  </button>
                </li>
              )
            })}
          </ul>
        </nav>
      </div>
    </div>
  );
}