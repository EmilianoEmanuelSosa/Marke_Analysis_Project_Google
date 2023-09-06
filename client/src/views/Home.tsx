import { Link } from 'react-router-dom'

export default function Home() {
  return (
    <div className='h-full w-full flex items-center justify-center'>
      <div className='flex text-center gap-4 flex-col items-center'>
        <h1 className='text-3xl font-bold'>Restaurant Tracking</h1>
        <p className='mt-4 max-w-xl'>Rastrea a tus competidores en tiempo real, revisa ssu reviews mas imporantes y no dejes que la competencia de </p>
        <div className='w-full grid grid-cols-2 '>
            <Link to={''} className=''>Documentacion</Link>
            <Link to={''} className=''>Tutorial</Link>
        </div>
      </div>
    </div>
  )
}
