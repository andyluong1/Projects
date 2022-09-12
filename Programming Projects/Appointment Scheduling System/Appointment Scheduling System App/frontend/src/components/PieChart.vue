<template>
<div>
    <div class="row">
        <div class="w-100 text-center" style="font-size: min(4.5vw, 20px); padding-left: 15px;">
            Top Zipcodes Distribution (last month)
        </div>
    </div>
    <div class="row mt-4">
        <canvas ref="myChart" style="height: 400px; width: 450px;"></canvas>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import Chart from 'chart.js/auto'

export default {
  props: {
    label: {
      type: Array,
    },
    chartData: {
      type: Array,
    },
  },
  data() {
    return {
      testChart: null
    }
  },
  async mounted() {
    const data = await axios.get('http://localhost:3000/dashboard/analytics/PieChart')
    const testChart = new Chart(this.$refs.myChart, {
      type: "pie",
      data: {
        labels: [],
        datasets: [{
          data: [],
          backgroundColor: [
            '#3f53cf',
            '#c45dd0',
            '#cc2f2f',
            'rgb(255,111,0)',
            '#2bc859',
          ],
          hoverOffset: 4
        }]
      },
      options: {
        plugins:{   
          legend: {
            display: true
          }
        },
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
              },
            },
          ],
        },
      },
    })
    testChart.data.datasets[0].data = data.data.datasets[0].data;
    testChart.data.labels = data.data.labels;
    testChart.update()
  }
};

</script>