import React, { useState, useEffect } from "react";
import { Table } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

const  Dashboard = () => {
  const [data, setData] = useState([]);
  useEffect(() => {
    fetch("http://localhost:5000/Dashboard")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []);
  return (
    <>
      <h1>Results</h1>
      <div className="PreProData">
      <div className="container">
        <Table striped bordered hover size="sm">
          <thead>
            <tr>
              <th>ALARM</th>
              <th>Tag</th>
              <th>Simple_Sliding %</th>
              <th>User_Sliding %"</th>
              <th>Proposed</th>
            </tr>
          </thead>
          <tbody>
            {data.map((data, i) => (
              <tr key={i}>
                <td>{data.ALARM}</td>
                <td>{data.Tag}</td>
                <td>{data.Simple_Sliding}</td>
                <td>{data.User_Sliding}</td>
                <td>{data.Proposed}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </div>
      </div>
      <br />
    </>
  );
};
export default Dashboard;