import React from 'react';
import { MDBRipple } from 'mdb-react-ui-kit';
import imgg from './1.png'
import '../App.scss';


const Pid = () => {
  return (
    <>
    <h1>P&ID</h1>
    <p>azdazdaz azdzadza<br /> zadaz dazazdaz dazdaz<br /> dza dazd az daz dzad<br />zadaz daz <br />dazd az daz<br /> dazd az daz dazdazdzadaz daz azdzad azd az d</p>
  
    <div className='pic'>
    <MDBRipple rippleTag='a'>
    <img
      src={imgg}
      className='img-fluid rounded'
      alt='example'
      style={{ maxWidth: '50rem' ,hight: '55rem'}}
    />
  </MDBRipple>
  </div>
    </>
  );
};
export default Pid;
