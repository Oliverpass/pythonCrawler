import React from 'react';
import ReactECharts from 'echarts-for-react';

const DirectorChart = ({ data }) => {
  // 确保我们有数据并且限制为前10名
  const topDirectors = data.slice(0, 10);
  
  const option = {
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    grid: {
      left: '5%',
      right: '5%',
      bottom: '10%',
      top: '10%',
      containLabel: true
    },
    xAxis: {
      type: 'value',
      name: '电影数量',
      nameTextStyle: {
        fontSize: 12
      }
    },
    yAxis: {
      type: 'category',
      data: topDirectors.map(director => director.name).reverse(),
      axisLabel: {
        fontSize: 12
      }
    },
    series: [
      {
        name: '执导电影数',
        type: 'bar',
        data: topDirectors.map(director => director.movie_count).reverse(),
        itemStyle: {
          color: '#91cc75'
        },
        label: {
          show: true,
          position: 'right'
        }
      }
    ]
  };
  
  return <ReactECharts option={option} style={{ height: '100%', width: '100%' }} />;
};

export default DirectorChart; 