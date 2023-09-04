import { Outlet } from "react-router-dom"
import NavBar from '../components/NavBar'
import NavSidebar from '../components/NavSidebar'

function Root() {

  return (
    <main className="h-screen">
      <NavBar />
      <div className="flex">
        <NavSidebar />
        <div id="detail">
          <Outlet />
        </div>
      </div>
    </main>
  );
}

export default Root;
