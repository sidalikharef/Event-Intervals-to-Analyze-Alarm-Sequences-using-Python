import React from 'react';
import { ProSidebar, Menu, MenuItem } from 'react-pro-sidebar';
import 'react-pro-sidebar/dist/css/styles.css';
import { FaRegSun } from "react-icons/fa";
import { FaWallet } from "react-icons/fa";



const SideBare = ({ target, setDisplayContent }) => {
  const clickHandler = () => {
    setDisplayContent(target.data);
  };
  const clickHandlerone = () => {
    setDisplayContent(target.PrePro);
  };
  const clickHandlerzero = () => {
    setDisplayContent(target.Dashboard);
  };
  const clickHandlersett= () => {
    setDisplayContent(target.Sett);
  };

  return (
   <ProSidebar className="col-md-12 d-none d-md-block bg-light sidebar"  style={{height:"2000px"}}>
  <Menu iconShape="square">
    <MenuItem onClick={clickHandlerzero}><FaWallet />  Dashboard</MenuItem>
    <MenuItem onClick={clickHandlerone} > <FaWallet /> Pre-processing Data Table CVS</MenuItem>
    <MenuItem onClick={clickHandler} ><FaWallet /> DATA CVS</MenuItem>
    <MenuItem onClick={clickHandlersett}><FaRegSun /> Settings</MenuItem>




  </Menu>
  </ProSidebar>
  );
};
export default SideBare;
