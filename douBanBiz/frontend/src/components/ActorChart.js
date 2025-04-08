import React from 'react';
import ReactECharts from 'echarts-for-react';

const ActorChart = ({ data }) => {
  // 确保我们有数据并且限制为前10名
  const topActors = data.slice(0, 10);
  
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
      type: 'category',
      data: topActors.map(actor => actor.name),
      axisLabel: {
        interval: 0,
        rotate: 30,
        fontSize: 10
      }
    },
    yAxis: {
      type: 'value',
      name: '电影数量',
      nameTextStyle: {
        fontSize: 12
      }
    },
    series: [
      {
        name: '出演电影数',
        type: 'bar',
        data: topActors.map(actor => actor.movie_count),
        itemStyle: {
          color: '#5470c6'
        },
        label: {
          show: true,
          position: 'top'
        }
      }
    ]
  };
  
  return <ReactECharts option={option} style={{ height: '100%', width: '100%' }} />;
};

export default ActorChart; 