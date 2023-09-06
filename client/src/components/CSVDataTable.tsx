import React from "react";

const CSVDataTable = ({ 
    data 
}:{
    data: Array<{[key: string]:string}>
}) => {
  const headers = data.length > 0 ? Object.keys(data[0]) : [];

    const rows = data.slice(0, 100)

  return (
    <div className="bg-[#FEFEFE] h-full w-full  overflow-y-scroll shadow">
      {data.length === 0 ? (
        <p>No data available.</p>
      ) : (
        <div className="rounded-sm bg-slate-500 overflow-x-scroll  overflow-y-scroll">
          <table className="bg-[#FEFEFE] relative overflow-x-scroll overflow-y-scroll border-collapse ">
            <thead className=" w-full">
                <tr className=" w-full">
                {headers.map((header, index) => (
                    <th key={index} className="bg-[#eeeff2] text-[#555555] font-bold border p-4">
                    {header}
                    </th>
                ))}
                </tr>
            </thead>
            <tbody className="overflow-y-scroll">
                {rows.map((row, index) => (
                <tr key={index}>
                    {headers.map((header, columnIndex) => (
                    <td key={columnIndex} className="p-4 border-x bg-red">
                        {row[header]}
                    </td>
                    ))}
                </tr>
                ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default CSVDataTable;