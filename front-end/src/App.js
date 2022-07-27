import logo from './logo.svg';
import './App.css';
import "antd/dist/antd.css";
import React, { useState, useEffect } from 'react';
import http from './http-common';
import { Layout, Col, Row } from 'antd';
import { Input, Space } from 'antd';
import MovieCards from './components/MovieCards'
const { Search } = Input;

const { Header, Footer, Sider, Content } = Layout;

function App() {

  useEffect(() => {
    http.get('movies')
    .then((res) => {
      // console.log(res.data.data)
      setMovieList(res.data.data)
    }).catch((error) => {
      setLoading(false)
    }).then(()=> {
      setLoading(false)
    })
  },[]);
  const [ loading, setLoading ] = useState(true);
  const [ movieList, setMovieList ] = useState([]);
  const onSearch = (value) => {
    http.get('brdddddd')
    .then((res) => {
      movieList(res.data.data)
    }).catch((error) => {
      setLoading(false)
    }).then(()=> {
      setLoading(false)
    })
    console.log(value);
  }
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
          <Col span={18} offset={3}>
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
            {!loading && <MovieCards movies={movieList}/>}
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


