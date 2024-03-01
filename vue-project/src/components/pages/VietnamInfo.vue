<template>
  <div class="flex flex-col items-center">
    <h1 class="text-2xl font-bold">Vietnamese Information</h1>
  </div>
  <form id="form" class="flex flex-col items-center" v-if="!isSubmit">
    <div id="age" class="w-10/12 mx-auto my-5">
      <label class="text-xl font-bold">What is your age</label>
      <p>This tool calculates risk for women between the ages of 20 and 90.</p>
      <input
        type="number"
        class="border-2 border-black px-1"
        placeholder="Age"
        v-model="age"
        min="20"
        max="90"
      />
      <p class="mx-auto my-3 text-xs text-red-500" v-if="!checkAge()">
        The age must be between 20 and 90
      </p>
    </div>

    <div id="breast-density" class="w-10/12 mx-auto my-5">
      <label class="text-xl font-bold">What is your breast density?</label>
      <p>Please enter a number from 0 to 100 (unit: percent)</p>
      <input
        type="number"
        class="border-2 border-black px-1"
        placeholder="Breast density"
        v-model="breastDensity"
        min="0"
        max="100"
      />
      <p class="mx-auto my-3 text-xs text-red-500" v-if="!checkBreastDensity()">
        The density must be between 0 and 100
      </p>
    </div>

    <div id="ageMen" class="w-10/12 mx-auto my-5">
      <p class="text-xl font-bold">
        What was the your age at the time of your first menstrual period?
      </p>
      <div class="grid">
        <div class="inline-block my-1">
          <input type="radio" v-model="ageMen" value="10" />
          <label class="mx-2">&lt;14 </label>
        </div>

        <div class="inline-block my-1">
          <input type="radio" v-model="ageMen" value="15" />
          <label class="mx-2">14 and older</label>
        </div>
      </div>
      <p class="mx-auto my-3 text-xs text-red-500" v-if="!checkAgeMen()">
        Please choose one option
      </p>
    </div>

    <div id="noPregnancies" class="w-10/12 mx-auto my-5">
      <p class="text-xl font-bold">How many times have you been pregnant?</p>
      <div class="grid">
        <div class="inline-block my-1">
          <input type="radio" v-model="noPregnancies" value="0" />
          <label class="mx-2">No births</label>
        </div>

        <div class="inline-block my-1">
          <input type="radio" v-model="noPregnancies" value="1" />
          <label class="mx-2">1 - 2</label>
        </div>

        <div class="inline-block my-1">
          <input type="radio" v-model="noPregnancies" value="3" />
          <label class="mx-2">more than 2</label>
        </div>
      </div>
      <p class="mx-auto my-3 text-xs text-red-500" v-if="!checkNoPregnancies()">
        Please choose one option
      </p>
    </div>

    <div id="noBabies" class="w-10/12 mx-auto my-5">
      <p class="text-xl font-bold">How many babies have you had?</p>
      <div class="grid">
        <div class="inline-block my-1">
          <input type="radio" v-model="noBabies" value="0" />
          <label class="mx-2">No births</label>
        </div>

        <div class="inline-block my-1">
          <input type="radio" v-model="noBabies" value="1" />
          <label class="mx-2">1</label>
        </div>

        <div class="inline-block my-1">
          <input type="radio" v-model="noBabies" value="2" />
          <label class="mx-2">2 or more</label>
        </div>
      </div>
      <p class="mx-auto my-3 text-xs text-red-500" v-if="!checkNoBabies()">
        Please choose one option
      </p>
    </div>

    <div id="hormone" class="w-10/12 mx-auto my-5">
      <p class="text-xl font-bold">Do you use hormone therapy</p>
      <div class="grid">
        <div class="inline-block my-1">
          <input type="radio" v-model="hormoneTherapy" value="1" />
          <label class="mx-2">Yes</label>
        </div>

        <div class="inline-block my-1">
          <input type="radio" v-model="hormoneTherapy" value="0" />
          <label class="mx-2">No</label>
        </div>
      </div>
      <p class="mx-auto my-3 text-xs text-red-500" v-if="!checkNoPregnancies()">
        Please choose one option
      </p>
    </div>

    <button
      class="bg-blue-500 text-white mx-auto px-3 py-1"
      @click.prevent="calc"
      type="button"
    >
      Calculate
    </button>
    <p class="mx-auto my-3 text-xs text-red-500" v-if="!checkData()">
      Please check your input data
    </p>
  </form>

  <div class="result" v-if="isSubmit" style="padding: 5%">
    <CanvasJSChart
      :options="options"
      :style="styleOptions"
      @chart-ref="chartInstance"
    />
    <div class="information">
      <div class="my-5">
        <h1 class="text-2xl font-bold">Your Information</h1>
      </div>
      <table class="table-auto">
        <tbody>
          <tr>
            <td class="border px-4 py-2">Age</td>
            <td class="border px-4 py-2">{{ age }}</td>
          </tr>
          <tr>
            <td class="border px-4 py-2">Breast density</td>
            <td class="border px-4 py-2">{{ breastDensity }}%</td>
          </tr>
          <tr>
            <td class="border px-4 py-2">Hormone Therapy</td>
            <td class="border px-4 py-2">
              {{ hormoneTherapy.toString() === "1" ? "Yes" : "No" }}
            </td>
          </tr>
          <tr>
            <td class="border px-4 py-2">
              Age at the time of your first menstrual period
            </td>
            <td class="border px-4 py-2">
              {{ ageMen.toString() === "10" ? "< 14" : "14 and older" }}
            </td>
          </tr>
          <tr>
            <td class="border px-4 py-2">Number of pregnancies</td>
            <td class="border px-4 py-2">
              {{
                noPregnancies.toString() === "0"
                  ? "No pregnancies"
                  : noPregnancies.toString() === "1"
                  ? "1 - 2 times"
                  : "more than 2 times"
              }}
            </td>
          </tr>
          <tr>
            <td class="border px-4 py-2">Number of babies</td>
            <td class="border px-4 py-2">
              {{
                noBabies.toString() === "0"
                  ? "No babies"
                  : noBabies.toString() === "1"
                  ? "1 baby"
                  : "2 or more babies"
              }}
            </td>
          </tr>
        </tbody>
      </table>
      <button
        class="bg-blue-500 text-white mx-auto my-4 px-3 py-1"
        @click.prevent="edit"
        type="button"
      >
        Edit your information
      </button>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { BASE_URL } from "../../axiosConstants";

const isSubmit = ref(false);
const breastDensity = ref(null);
const age = ref(null);
const ageMen = ref(-1);
const noPregnancies = ref(-1);
const noBabies = ref(-1);
const hormoneTherapy = ref(-1);
const responseData = ref(null);

var options: any = null;
var styleOptions: any = null;
var chartInstance: any = null;
const isClick = ref(false);

interface VietnameseForm {
  t1: number;
  breastDensity: number;
  ageMen: number;
  pregnancyNumber: number;
  babyNumber: number;
  hormoneTherapy: number;
}

const checkAge = () => {
  return !(
    isClick.value &&
    age.value !== null &&
    age.value !== undefined &&
    (age.value <= 19 || age.value >= 91 || isNaN(age.value))
  );
};

const checkBreastDensity = () => {
  return !(
    isClick.value &&
    breastDensity.value !== null &&
    breastDensity.value !== undefined &&
    (breastDensity.value < 0 ||
      breastDensity.value > 100 ||
      isNaN(breastDensity.value))
  );
};

const checkAgeMen = () => {
  return !(isClick.value && ageMen.value < 0);
};

const checkNoPregnancies = () => {
  return !(isClick.value && noPregnancies.value < 0);
};

const checkNoBabies = () => {
  return !(isClick.value && noBabies.value < 0);
};

const checkHomeoneTherapy = () => {
  return !(isClick.value && hormoneTherapy.value < 0);
};

const checkAgeNull = () => {
  if (age.value == null) return true;
};

const checkData = () => {
  console.log(isClick.value);
  if (isClick.value)
    return (
      checkAge() &&
      checkBreastDensity() &&
      checkAgeMen() &&
      checkNoPregnancies() &&
      checkNoBabies() &&
      checkHomeoneTherapy()
    );
  return true;
};

const edit = async () => {
  isSubmit.value = false;
};

const calc = async () => {
  // check input
  isClick.value = true;
  console.log("Click");
  console.log("is check data: ", checkData());
  if (checkData()) {
    const new_data: VietnameseForm = {
      t1: age.value ?? 20,
      breastDensity: breastDensity.value ?? 0,
      ageMen: ageMen.value,
      pregnancyNumber: noPregnancies.value,
      babyNumber: noBabies.value,
      hormoneTherapy: hormoneTherapy.value,
    };
    try {
      const response = await axios.post(`${BASE_URL}/vn/`, new_data);
      console.log(response.status);
      responseData.value = response["data"];
      console.log(responseData.value);

      var dataPoints1 = [];
      var dataPoints2 = [];

      if (responseData.value !== null) {
        for (const key in responseData.value["absolute risk"] as Record<string, any>) {
          var temp = {
            label: key,
            y: responseData.value["absolute risk"][key],
          };
          dataPoints1.push(temp);
        }

        for (const key in responseData.value["absolute average"] as Record<string, any>) {
          var temp = {
            label: key,
            y: responseData.value["absolute average"][key],
          };
          dataPoints2.push(temp);
        }

        console.log(dataPoints1);
        console.log(dataPoints2);

        options = {
          animationEnabled: true,
          exportEnabled: true,
          theme: "light2",
          title: {
            text: "Breast Cancer Risk",
          },
          axisX: {
            title: "age",
            valueFormatString: "YY",
            labelTextAlign: "center",
            labelAngle: 0,
          },
          axisY: {
            title: "Breast Cancer Risk",
            valueFormatString: "#%",
          },
          toolTip: {
            shared: true,
          },
          legend: {
            cursor: "pointer",
            itemclick: function (e: any) {
              if (
                typeof e.dataSeries.visible === "undefined" ||
                e.dataSeries.visible
              ) {
                e.dataSeries.visible = false;
              } else {
                e.dataSeries.visible = true;
              }
              e.chart.render();
            },
          },
          data: [
            {
              type: "line",
              name: "absolute risk",
              showInLegend: true,
              color: "#F7C705",
              toolTipContent: "{name}: {y}",
              yValueFormatString: "##.##%",
              dataPoints: dataPoints1,
            },
            {
              type: "line",
              name: "absolute average",
              showInLegend: true,
              color: "#012066",
              toolTipContent: "{name}: {y}",
              yValueFormatString: "##.##%",
              dataPoints: dataPoints2,
            },
          ],
        };

        styleOptions = {
          width: "90%",
          height: "500px",
        };

        chartInstance = (chart: any) => {
          chart.value = chart;
        };
      }
      isSubmit.value = true;
    } catch (error) {
      console.log(error);
      window.alert("Failed to send message: " + error);
    }
  } else {
    var form = document.getElementById("form");
  }
};

onMounted(() => {
  // Your code to work with the chart after it's mounted
});
</script>
