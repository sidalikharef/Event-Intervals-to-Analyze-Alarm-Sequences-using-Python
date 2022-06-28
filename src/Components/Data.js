import React, { useState, useEffect } from "react";
import { Table } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

const Data = () => {
  const [data, setData] = useState([]);
  useEffect(() => {
    fetch("http://localhost:5000/table")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []);
  return (
    <>
      <h1> Data Table</h1>
      <div className="PreProData">
      <div className="container">
        <Table striped bordered hover size="sm">
          <thead>
            <tr>
              <th>#</th>
              <th>Date</th>
              <th>Heure </th>
              <th>Tag</th>
              <th>Alarm</th>
            </tr>
          </thead>
          <tbody>
            {data.map((data, i) => (
              <tr key={i}>
                <td>{i}</td>
                <td>{data.Date}</td>
                <td>{data.Heure}</td>
                <td>{data.Tag}</td>
                <td>{data.Alarm}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </div>
      </div>
    </>
  );
};
export default Data;
