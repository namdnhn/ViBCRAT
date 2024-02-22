<template>
    <CanvasJSChart :options="options" :style="styleOptions" @chart-ref="chartInstance"/>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const responseData = ref<any | null>(null);

const route = useRoute()

onMounted(() => {
  if (route.params.data) {
    // Lưu trữ responseData vào biến ref
    responseData.value = route.params.responseData;
    console.log("có rồi")
  }
});

console.log("Olala");
const chart = ref(null);

const options = {
  animationEnabled: true,
  exportEnabled: true,
  theme: "light2",
  title: {
    text: "UPI Transactions in India",
  },
  axisX: {
    valueFormatString: "YYYY",
    labelTextAlign: "center",
    labelAngle: 0,
  },
  axisY: {
    title: "Amount (in ₹ Crore)",
    valueFormatString: "₹##,##,##0cr",
  },
  data: [
    {
      type: "line",
      yValueFormatString: "₹##,##,##0.## crores",
      dataPoints: [
        { label: "2016", y: 893.07 },
        { label: "2017", y: 57020.87 },
        { label: "2018", y: 585710.45 },
        { label: "2019", y: 1836638.18 },
        { label: "2020", y: 3387744.72 },
        { label: "2021", y: 7159285.80 },
        { label: "2022 (Jan-Oct)", y: 10122170.33 },
      ],
    },
  ],
};

const styleOptions = {
  width: "90%",
  height: "400px",
};

const chartInstance = (chart) => {
  chart.value = chart;
};

onMounted(() => {
  // Your code to work with the chart after it's mounted
});
</script>