import BarMenu from "./components/BarMenu";
import Content from "./components/Content";
import { useEffect } from "react";
import { useLocation, useNavigate, useParams } from "react-router-dom";

function App() {
  const { uuid } = useParams();
  const location = useLocation();
  let navigate = useNavigate();

  useEffect(() => {
    localStorage.setItem("uuid", uuid);
    if (location.pathname === "/" && uuid) {
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
