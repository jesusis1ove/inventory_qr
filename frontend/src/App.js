import BarMenu from "./components/BarMenu";
import Content from "./components/Content";
import { useEffect } from "react";
import { useLocation, useNavigate, useParams } from "react-router-dom";

function App() {
  const { uuid } = useParams();
  const location = useLocation();
  let navigate = useNavigate();
  console.log(location);
  useEffect(() => {
    if (location.pathname === "/") {
      navigate(`meters/${uuid}`);
    }
  }, []);
  return (
    <div className="App">
      <BarMenu />
      <Content />
    </div>
  );
}

export default App;
