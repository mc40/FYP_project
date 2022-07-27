import logo from './logo.svg';
import './App.css';
import "antd/dist/antd.css";
import React from 'react';

import { Layout, Col, Row } from 'antd';
import { Input, Space } from 'antd';
import http from './http-common';

const { Search } = Input;

const { Header, Footer, Sider, Content } = Layout;
const onSearch = (value) => {
  // http.get('centres')
  //     .then(({status, data, message})=> {
  //       if (status === 200) {
  //         console.log(data)
  //         setCentres(data)
  //       } else {
  //         setError(message)
  //       }
  //     })
  //     .catch((error) => {
  //         console.log(error);
  //         setError(error)
  //       })
  //       .then(()=> {
  //         setloading(false)
  //       })
  console.log(value);
}
const axios = require('axios');
function App() {
  return (
    <div>
    <Layout>
    <Layout
  >
      <Header
        className="site-layout-background"
        style={{ backgroundColor: "#888888" }}
      >
        <Row>
          <Col span={1}><img width="40" src={"https://icon-library.com/images/movie-icon/movie-icon-26.jpg"}/></Col>
          <Col span={23}><h1>Movie Searching</h1></Col>
        </Row>
      </Header>
      <Content
       style={{
        textAlign: 'center',
      }}>
        <>
        <Row>
          <Col span={12} offset={6}>
            <br/>
            <br/>
            <br/>
                <Search
                  addonBefore=""
                  placeholder="Free text Here"
                  onSearch={onSearch}
                  style={{
                    width: 304,
                  }}
                />
            <br/>
            <br/>
            <br/>
            <br/>
          </Col>
        </Row>
        </>
      </Content>
      <Footer
        style={{
          textAlign: 'center',
        }}
      >
        Movie Searching ©2022 Created by Ko Long
      </Footer>
    </Layout>
  </Layout>
  </div>
  );
}

export default App;


