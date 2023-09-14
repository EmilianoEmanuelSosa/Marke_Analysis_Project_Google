import { useState, Fragment  } from 'react'
import useConfig from '../hooks/useConfig'
import { SubmitHandler, useForm } from 'react-hook-form'
import { Dialog, Transition } from '@headlessui/react'
import axios from 'axios'

export default function ConfigBtn(props:React.HtmlHTMLAttributes<HTMLButtonElement>) {
  
  const { setRestaurant } = useConfig()
  const [isOpen, setIsOpen] = useState(false)

  const { register, handleSubmit }  = useForm<{id: string}>({defaultValues: {
    id: ''
  }}) 
  
  const onSubmit:SubmitHandler<{id:string}> = (data:{id:string}) => {
    axios.get(`http://127.0.0.1:8000/api/restaurantes_id/${data.id}/?format=json`)
      .then(response => {setRestaurant(response.data)})  
      .catch(reject => console.log(reject))
    // axios.get(`${location.hash}/api/restaurantes_id/${data.id}/?format=json`)
    //   .then(response => {setRestaurant(response.data)})  
    //   .catch(reject => console.log(reject))
  }

  function closeModal() {
    setIsOpen(false)
  }

  function openModal() {
    setIsOpen(true)
  }

  return (
    <div>
      <button onClick={openModal} {...props} />
      <Transition appear show={isOpen} as={Fragment}>
        <Dialog as="div" className="relative z-10" onClose={closeModal}> 
          <Transition.Child
            as={Fragment}
            enter="ease-out duration-300"
            enterFrom="opacity-0"
            enterTo="opacity-100"
            leave="ease-in duration-200"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
          >
            <div className="fixed inset-0 bg-black bg-opacity-25" />
          </Transition.Child>
          <div className="fixed inset-0 overflow-y-auto">
            <div className="flex min-h-full items-center justify-center p-4 text-center">
              <Transition.Child
                as={Fragment}
                enter="ease-out duration-300"
                enterFrom="opacity-0 scale-95"
                enterTo="opacity-100 scale-100"
                leave="ease-in duration-200"
                leaveFrom="opacity-100 scale-100"
                leaveTo="opacity-0 scale-95"
              >
                <Dialog.Panel className="w-full max-w-md transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all">
                  <Dialog.Title
                    as="h3"
                    className="text-xl font-medium leading-6 text-gray-900"
                  >
                    Configuracion
                  </Dialog.Title>
                  <div className="mt-3">
                    <p className="text-sm text-gray-500">
                      Utiliza tu identificador para cargar tus datos. RestaurantTracking tomará como referencias tus datos de geolocalizacion para los diferentes servicios.
                    </p>
                  </div>
                  <form onSubmit={handleSubmit(onSubmit)}>
                    <fieldset className="flex flex-col mt-4">
                      <label htmlFor='id' className="text-sm text-gray-900 font-bold">Identificador:</label>
                      <input {...register('id',)}  className='border-gray-500 mt-1 border p-2 rounded-md'/>
                    </fieldset>
                    <div className="mt-4 flex justify-end">
                      <button
                        type="submit"
                        className="inline-flex justify-center rounded-md border border-transparent bg-blue-100 px-4 py-2 text-sm font-medium text-blue-900 hover:bg-blue-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
                      >
                        Cargar Datos
                      </button>
                     </div>
                  </form>
                </Dialog.Panel>
              </Transition.Child>
            </div>
          </div>
        </Dialog>
      </Transition>
    </div>
  )
}