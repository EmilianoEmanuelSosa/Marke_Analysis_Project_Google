import React, { useState} from 'react'
import CSVDataTable from "../components/CSVDataTable";
import { FileUploader } from "react-drag-drop-files";
import Papa from 'papaparse'

const Button = ({
  onClick,
  children
}:{
  onClick: () => void,
  children: React.ReactNode
}) => {
  return (
    <button className='w-8 h-8 rounded flex items-center justify-center bg-red-400' onClick={onClick}>{children}</button>
  )
}

const UploadFileIcon = ({classname}:{classname?:string}) => {

  return (  
    <svg className={classname} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
      <path d="M14 3v4a1 1 0 0 0 1 1h4" />
      <path d="M17 21h-10a2 2 0 0 1 -2 -2v-14a2 2 0 0 1 2 -2h7l5 5v11a2 2 0 0 1 -2 2z" />
      <line x1="12" y1="11" x2="12" y2="17" />
      <polyline points="9 14 12 11 15 14" />
    </svg>
  )
}


export default function CSVLoader() {

  const [csvData, setCsvData] = useState<{[key: string]:string}[]>([{}]);
  const [numberForPage, setNumberOfPage] = useState<number>(1000);
  const [limitRows, setLimitRows] = useState<number>(10000);
  const [page, setPage] = useState<number>(1);
  const [file, setFile] = useState<File | undefined>(undefined);

  const clamp = (num:number, min:number, max:number) => Math.min(Math.max(num, min), max);

  const handleIncrease = (difference:number) => {
    setNumberOfPage(value => clamp(value + difference, 0, limitRows))     
  }

  const handleDescrease = (difference:number) => {
    setNumberOfPage(value => clamp(value - difference, 0, limitRows))     
  }

  const handleDelete = () => { 
    setFile(undefined)
  }

  const handleUpload = () => {
    // TO-DO: Conectar Enpoint 
    
    setFile(undefined)
  }

  const handleFileChange = (csv_file: File) => {
    if (!csv_file) return  
    
    setFile(csv_file);
    const reader = new FileReader();

    reader.onload = (e: ProgressEvent<FileReader>) => {
      const csvText = e.target?.result;
      const {data} = Papa.parse(csvText, {header:true}) 
    
      const parsedData: {[key: string]:string}[] = [];

      data.forEach(row => {
        parsedData.push(row);
      });

      setCsvData(parsedData);
    };

    reader.readAsText(csv_file);
  };    

  return (
    <div className='w-[calc(100vw_-_300px)]'>
      <div className="max-h-[60px] p-4 flex"style={{marginBottom:'15px'}}>
        <label>page</label>
        
        <div className="flex flex-row gap-4 items-center">
          <div className='flex flex-row gap-2'>
            {[100,10,1].map(value => (
              <Button key={value} onClick={() => handleDescrease(100)}>{"<"}</Button>  
            ))}
          </div>

          <div>
            {numberForPage}
          </div>

          <div className='flex flex-row gap-2'>
            {[1,10,100].map(value => (
              <Button key={value} onClick={() => handleIncrease(100)}>{">"}</Button>  
            ))}
            <label>Registros por Pagina:</label>
          </div>
        </div>
        <div>
          {page +'/' +   Math.ceil(limitRows/numberForPage)}

        </div>
        <input type="number" />
        <button className='' onClick={handleDelete}>Borrar Dataset</button>
        <button className='' onClick={handleDelete}>Upload csv</button>
      </div>
      
      <div className='px-5'>
        <div className=' h-[calc(100vh_-_80px_-_72px)]  shadow-xl rounded-sm overflow-hidden bg-[#FEFEFE] '>
          {!file 
            ? <FileUploader handleChange={handleFileChange} name="file" types={['CSV']}>
                <div className=' border hover:border-[#52A2EC] hover:cursor-cell rounded-sm hover:bg-blue-50 h-full w-full flex items-center justify-center'>
                  <div className='flex flex-col items-center gap-2 justify-center'>
                    <UploadFileIcon classname='w-24 h-24 stroke-slate-400' />
                    <h1 className='w-72 text-center text-xl'>Arrastra y suelta tus archivos aqui (.csv)</h1>
                  </div>
                </div>
              </ FileUploader>    
            : <CSVDataTable data={csvData} />
          }
        </div>
      </div>
    </div>
  );
}
