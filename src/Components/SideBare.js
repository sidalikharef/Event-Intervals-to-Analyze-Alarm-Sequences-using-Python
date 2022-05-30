import React from 'react';
import { ProSidebar, Menu, MenuItem } from 'react-pro-sidebar';
import 'react-pro-sidebar/dist/css/styles.css';

const SideBare = ({ target, setDisplayContent }) => {
  const clickHandler = () => {
    setDisplayContent(target.data);
  };
  const clickHandlerone = () => {
    setDisplayContent(target.PrePro);
  };
  const clickHandlertwo = () => {
    setDisplayContent(target.Pid);
  };
  const clickHandlerzero = () => {
    setDisplayContent(target.Dashboard);
  };

  return (
   <ProSidebar className="col-md-12 d-none d-md-block bg-light sidebar">
  <Menu iconShape="square">
    <MenuItem onClick={clickHandlerzero}>Dashboard</MenuItem>
    <MenuItem onClick={clickHandlertwo}>PI&D</MenuItem>
    <MenuItem onClick={clickHandlerone} >DataPreProcecing CVS</MenuItem>
    <MenuItem onClick={clickHandler} >DATA CVS</MenuItem>




  </Menu>
  </ProSidebar>
  );
};
export default SideBare;
