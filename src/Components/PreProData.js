import React,{useState,useEffect} from 'react';
import { Table} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

const PreProData = () => {
  const [data, setData] = useState([]);
  useEffect(() => {
    fetch("http://localhost:5000/PreProData")
      .then(res => res.json()   
      ).then(data => {
        setData(data);
       console.log(data)
      });
 
  }, [])
  return (
    <>
    
    <h1>PreProcecing Data Table</h1>
    <div className='PreProData'>
    <Table striped bordered hover size="sm" >
    <thead>
    <tr>
      <th>#</th>
      <th>Heure</th>
      <th>Tag </th>
      <th>Time</th>
      <th>Alarm</th>
    </tr>
    </thead>
    <tbody>
        {data.map((data, i) => (
            <tr key={i}>
                <td>{i}</td>
                <td>{data.Heure}</td>
                <td>{data.Tag}</td>
                <td>{data.Time}</td>
                <td>{data.Alarm}</td>
            </tr>
        ))}
    </tbody>
    </Table>
    </div>
    </>
  );
};
export default PreProData ;
