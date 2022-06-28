import React,{useState} from 'react';
import { MemoryRouter as Router, Routes, Route } from 'react-router-dom';
import './App.scss';

import { Row,Col} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import SideBare from './Components/SideBare';
import PreProData from './Components/PreProData';
import Data from './Components/Data';
import Dashboard from './Components/Dashboard';
import Settings from './Components/settings';


const Apps = () => {
  const target = {
    Dashboard:"Dashboard",
    PrePro: "PrePro",
    data: "data",
    Sett: "Settings",
  };
  const [displayContent, setDisplayContent] = useState(target.Dashboard);

  return (
    <Row >
    <Col Col xs={6} md={4} >
        <SideBare  target={target} setDisplayContent={setDisplayContent} />
    </Col>
    <Col xs={12} md={8}>
     {displayContent ===target.PrePro ?(<PreProData />
     ): displayContent === target.data ?( <Data />
     ): displayContent === target.Dashboard ?( <Dashboard />
     ):  displayContent === target.Sett ?( <Settings />):

     ( console.log('nothing sorry'))}
    </Col>
    </Row>

  );
};

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Apps />} />
      </Routes>
    </Router>
  );
}
