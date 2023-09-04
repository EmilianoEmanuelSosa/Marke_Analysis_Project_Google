import { Link } from "react-router-dom";

export default function Root() {
  return (
    <div className="max-w-[300px] h-[calc(100vh_-_56px)] bg-[#2E2E2E]">
      <div >
        <h1>React Router Contacts</h1>
        <div>
        </div>
        <nav>
          <ul>
            <li>
              <Link to={`contacts/1`}>Your Name</Link>
            </li>
            <li>
              <Link to={`contacts/1`}>Your Name</Link>
            </li>
          </ul>
        </nav>
      </div>
      <div>
        <a>Dashbaor</a>
      </div>
    </div>
  );
}