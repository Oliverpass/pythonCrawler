import React from 'react';
import ReactECharts from 'echarts-for-react';

const CountryChart = ({ data }) => {
  // 确保我们有数据并且限制为前10名
  const topCountries = data.slice(0, 10);
  
  const option = {
    tooltip: {
      trigger: 'item',
      formatter: '{a} <br/>{b}: {c} ({d}%)'
    },
    legend: {
      orient: 'vertical',
      right: 10,
      top: 'center',
      data: topCountries.map(country => country.name),
      textStyle: {
        fontSize: 12
      }
    },
    series: [
      {
        name: '制片国家',
        type: 'pie',
        radius: ['40%', '70%'],
        center: ['40%', '50%'],
        avoidLabelOverlap: false,
        itemStyle: {
          borderRadius: 10,
          borderColor: '#fff',
          borderWidth: 2
        },
        label: {
          show: false,
          position: 'center'
        },
        emphasis: {
          label: {
            show: true,
            fontSize: 14,
            fontWeight: 'bold'
          }
        },
        labelLine: {
          show: false
        },
        data: topCountries.map(country => ({
          value: country.movie_count,
          name: country.name
        }))
      }
    ]
  };
  
  return <ReactECharts option={option} style={{ height: '100%', width: '100%' }} />;
};

export default CountryChart; 