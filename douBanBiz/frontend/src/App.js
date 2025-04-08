import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ActorChart from './components/ActorChart';
import CountryChart from './components/CountryChart';
import DirectorChart from './components/DirectorChart';
import GenreChart from './components/GenreChart';

function App() {
  const [actorsData, setActorsData] = useState([]);
  const [countriesData, setCountriesData] = useState([]);
  const [directorsData, setDirectorsData] = useState([]);
  const [genresData, setGenresData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        
        // 并行获取所有数据
        const [actorsResponse, countriesResponse, directorsResponse, genresResponse] = await Promise.all([
          axios.get('/api/stats/actors'),
          axios.get('/api/stats/countries'),
          axios.get('/api/stats/directors'),
          axios.get('/api/stats/genres')
        ]);
        
        setActorsData(actorsResponse.data);
        setCountriesData(countriesResponse.data);
        setDirectorsData(directorsResponse.data);
        setGenresData(genresResponse.data);
        
        setLoading(false);
      } catch (err) {
        console.error('Error fetching data:', err);
        setError('数据加载失败，请稍后再试');
        setLoading(false);
      }
    };
    
    fetchData();
  }, []);

  if (loading) {
    return <div className="app-container">加载中...</div>;
  }

  if (error) {
    return <div className="app-container">{error}</div>;
  }

  return (
    <div className="app-container">
      <div className="header">
        <h1>豆瓣电影Top250数据分析</h1>
        <p>基于豆瓣电影Top250的统计分析与可视化</p>
      </div>
      
      <div className="charts-container">
        <div className="chart-card">
          <h3 className="chart-title">出演次数最多的演员</h3>
          <ActorChart data={actorsData} />
        </div>
        
        <div className="chart-card">
          <h3 className="chart-title">制片最多的国家</h3>
          <CountryChart data={countriesData} />
        </div>
        
        <div className="chart-card">
          <h3 className="chart-title">出现次数最多的导演</h3>
          <DirectorChart data={directorsData} />
        </div>
        
        <div className="chart-card">
          <h3 className="chart-title">各类型电影数量</h3>
          <GenreChart data={genresData} />
        </div>
      </div>
    </div>
  );
}

export default App; 