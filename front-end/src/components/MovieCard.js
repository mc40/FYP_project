import React from 'react';
import { Divider, Row, Col, Button } from 'antd';
import 'antd/dist/antd.css';
import { Card, Avatar } from 'antd';
import { LoadingOutlined } from '@ant-design/icons';
import { WomanOutlined, ManOutlined } from '@ant-design/icons';

export default ({movie}) => {
  console.log(movie)
  if (movie.type !== undefined) {
    movie.types = movie.type.split(/[, ]+/);
  }
//   if (movie.actors !== undefined) {
//     movie.actors = movie.actors.split(/[, ]+/);
//     console.log('movie.actors  ', movie.actors)
//   }
  console.log(movie.type)
//   let birth = movie.birthday? new Date(movie.birthday).toISOString().split('T')[0] : ""
  return (
    <Card
      onClick={() => {
        console.log("go")
      }}
      style={{width: 250, margin: "auto"}}
      hoverable={true}
      cover={
        movie.poster?
          <img width="250" style={{ objectFit: "cover"}} src={movie.poster}/>
          : <div style={{ width: 250, height: 250, display: "flex", justifyContent: "center", alignItems: "center", backgroundColor: "#f3f2f2" }}><LoadingOutlined /></div>
      }
    >
      <Card.Meta
        // avatar={<Avatar src="https://joeschmoe.io/api/v1/random" />}
        title={movie.title}
        description={
        <>
            <p>Director: {movie.id}</p>
            {movie.actors && <p> {movie.actors.substring(0, 100) + '...'}</p>}
            <p>runtime: {movie.runtime}</p>
            <p>Release Date: {movie.releaseDate}</p>
            {movie.types !== undefined && movie.types.map((t, index) => (
                <Button type="primary" shape="round" size={'small'}>
                {t}
            </Button>
            ))
            }
            
        </>
        }
      />
    </Card>
  )
  };