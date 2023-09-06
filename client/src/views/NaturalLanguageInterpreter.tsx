import React, { useState, useEffect } from 'react'

export default function NaturalLanguageInterpreter() {

    const handleOnSubmit = () => {
    
    }
  
    return (
      <div className='p-8'>
        <h1 className='text-3xl mb-4'>Interpretador de Lenguaje Natural</h1>
        <p className='mb-4'>Utiliza el siguiente interp alimentado por Aprneidjzae Automatico para determinar el Scoring de una resena. </p>
        <p>Por que model? Este modelo sirve para poder clasificar de una forma rapida y eficinete un grupo, aliviando la tarea . Asi se pueden fitrar las resenas, y darle prioridad asi sea a las positivas o negativas</p>
        <form className='flex flex-col items-end' onSubmit={handleOnSubmit}>
          <textarea className='p-4 border mt-4 w-full h-80' />
          <button className='bg-blue-400 mt-4 px-4 py-2 rounded' type='submit'> Enviar</button>
        </form>
        <h2>Resultado: {}</h2>  
      </div>
    )
}
