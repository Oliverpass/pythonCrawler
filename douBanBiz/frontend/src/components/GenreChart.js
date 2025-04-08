import React from 'react';
import ReactECharts from 'echarts-for-react';

const GenreChart = ({ data }) => {
  const option = {
    tooltip: {
      trigger: 'item'
    },
    series: [
      {
        name: '电影类型',
        type: 'pie',
        radius: '70%',
        center: ['50%', '50%'],
        data: data.map(genre => ({
          value: genre.movie_count,
          name: genre.name
        })),
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
        },
        label: {
          formatter: '{b}: {c} ({d}%)',
          fontSize: 12
        }
      }
    ]
  };
  
  return <ReactECharts option={option} style={{ height: '100%', width: '100%' }} />;
};

export default GenreChart; 