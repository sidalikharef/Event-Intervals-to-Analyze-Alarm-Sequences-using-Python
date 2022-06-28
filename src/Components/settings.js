import React,{useState} from 'react';
import { Form, Container, Button } from 'react-bootstrap';
import axios from 'axios';

import 'bootstrap/dist/css/bootstrap.min.css';

const Settings = () => {
    const mystyle = {
        padding:"80px"
      };
  const [tempi, setTemp] = useState('3');
  const [datas, setDatas] = useState('');

  const handleSubmit = event => {
    event.preventDefault();

    // 👇️ access input values here
    console.log(tempi);
    console.log(datas.slice(12));
    let tempis=tempi;
    let datis=datas.slice(12);


    axios.post('http://127.0.0.1:5000/add', {
      temp:tempis,
      data:datis
    }).then(function(response) {
      console.log(response);
    }).catch(function(error) {
      console.log(error);
    })
    setTemp('');
    setDatas('');
  };


  return (
    <>

    <Container>
    <div className=' settings' style={mystyle}>
        <Form onSubmit = {handleSubmit}  >
        <Form.Group  md="4" controlId="validationCustom01">
          <Form.Label>Time interval</Form.Label>
          <Form.Control
            required
            type="text"
            placeholder="Time (s)"
            defaultValue="3"
            value={tempi}
            onChange={event => setTemp(event.target.value)}

          />
        </Form.Group>


        <Form.Group controlId="formFileLg" className="mb-3">
          <Form.Label>Input Dataset (.cvs)</Form.Label>
          <Form.Control type="file"
          value={datas}
          onChange={event => setDatas(event.target.value)}
          />
        </Form.Group>

        <Button type="submit">Send</Button>
        </Form>
        </div>
        </Container>

    </>
  );
};
export default Settings ;
