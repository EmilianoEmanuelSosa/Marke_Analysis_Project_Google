import { Outlet } from "react-router-dom"
import NavBar from '../components/NavBar'
import NavSidebar from '../components/NavSidebar'
import useConfig from "../hooks/useConfig";

function Root() {

  const { ConfigProvider } = useConfig()

  return (
    <main className="h-screen font-inter">
      <ConfigProvider>
        <NavBar />
        <div className="flex h-[calc(100vh_-_72px)]">
          <NavSidebar />
          <div className="w-full h-full bg-[#ECF2F9]">
            <Outlet />
          </div>
        </div>
      </ConfigProvider>
    </main>
  );
}

export default Root;
