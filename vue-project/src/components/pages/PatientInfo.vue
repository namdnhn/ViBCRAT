<template>
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

    <div id="race" class="w-10/12 mx-auto my-5">
      <label class="text-xl font-bold">What is your race/ethnicity?</label>
      <p>Choose the race</p>
      <select name="race" class="border-2 border-black" v-model="race" required>
        <option value="" disabled selected>Select your option</option>
        <option value="1">White</option>
        <option value="2">African-American</option>
        <option value="3">Hispanic-American (US born)</option>
        <option value="4">Native American and other</option>
        <option value="5">Hispanic-American (Foreign born)</option>
        <option value="6">Chinese-American</option>
        <option value="7">Japanese-American</option>
        <option value="8">Filipino-American</option>
        <option value="9">Hawaiian-American</option>
        <option value="10">Other Pacific Islander</option>
        <option value="11">Other Asian</option>
      </select>
      <p class="mx-auto my-3 text-xs text-red-500" v-if="!checkRace()">
        Please choose one option
      </p>
    </div>

    <div id="nBiops1" class="w-10/12 mx-auto my-5">
      <p class="text-xl font-bold">
        Have you ever had a breast biopsy with a benign (not cancer) diagnosis?
      </p>
      <div class="grid">
        <div class="inline-block my-1">
          <input type="radio" v-model="nBiops1" value="1" />
          <label class="mx-2">Yes</label>
        </div>

        <div class="inline-block my-1">
          <input type="radio" v-model="nBiops1" value="0" />
          <label class="mx-2">No</label>
        </div>

        <div class="inline-block my-1">
          <input type="radio" v-model="nBiops1" value="99" />
          <label class="mx-2">Unknown</label>
        </div>
      </div>
      <p class="mx-auto my-3 text-xs text-red-500" v-if="!checkNBiops1()">
        Please choose one option
      </p>
    </div>

    <div id="nBiops2" class="w-8/12 mx-auto my-5" v-if="nBiops1 === '1'">
      <p class="text-xl font-bold">
        How many breast biopsies with a benign diagnosis have you had?
      </p>
      <div class="grid">
        <div class="inline-block my-1">
          <input type="radio" v-model="nBiops2" value="1" />
          <label class="mx-2">1</label>
        </div>

        <div class="inline-block my-1">
          <input type="radio" v-model="nBiops2" value="2" />
          <label class="mx-2">2 or more</label>
        </div>
      </div>
      <p class="mx-auto my-3 text-xs text-red-500" v-if="!checkNBiops2()">
        Please choose one option
      </p>
    </div>

    <div id="nBiops3" class="w-8/12 my-5" v-if="nBiops1 === '1'">
      <p class="text-xl font-bold">
        Have you ever had a breast biopsy with atypical hyperplasia?
      </p>
      <div class="grid">
        <div class="inline-block my-1">
          <input type="radio" v-model="RHyp" value="1" />
          <label class="mx-2">Yes</label>
        </div>

        <div class="inline-block my-1">
          <input type="radio" v-model="RHyp" value="0" />
          <label class="mx-2">No</label>
        </div>

        <div class="inline-block my-1">
          <input type="radio" v-model="RHyp" value="99" />
          <label class="mx-2">Unknown</label>
        </div>
      </div>
      <p class="mx-auto my-3 text-xs text-red-500" v-if="!checkRHyp()">
        Please choose one option
      </p>
    </div>

    <div id="ageMen" class="w-10/12 mx-auto my-5">
      <p class="text-xl font-bold">
        What was the your age at the time of your first menstrual period?
      </p>
      <div class="grid">
        <div class="inline-block my-1">
          <input type="radio" v-model="ageMen" value="10" />
          <label class="mx-2">7 - 11</label>
        </div>

        <div class="inline-block my-1">
          <input type="radio" v-model="ageMen" value="12" />
          <label class="mx-2">12 - 13</label>
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

    <div id="age1st" class="w-10/12 mx-auto my-5">
      <p class="text-xl font-bold">
        What was your age when you gave birth to your first child?
      </p>
      <div class="grid">
        <div class="inline-block my-1">
          <input
            type="radio"
            v-model="ageFirst"
            value="0"
            :disabled="age == null"
          />
          <label class="mx-2">No births</label>
        </div>

        <div class="inline-block my-1">
          <input
            type="radio"
            v-model="ageFirst"
            value="19"
            :disabled="age == null"
          />
          <label class="mx-2"> younger than 20 </label>
        </div>

        <div class="inline-block my-1">
          <input
            type="radio"
            v-model="ageFirst"
            value="24"
            :disabled="age < 20"
          />
          <label class="mx-2">20 - 24</label>
        </div>

        <div class="inline-block my-1">
          <input
            type="radio"
            v-model="ageFirst"
            value="29"
            :disabled="age < 25"
          />
          <label class="mx-2">25 - 29</label>
        </div>

        <div class="inline-block my-1">
          <input
            type="radio"
            v-model="ageFirst"
            value="30"
            :disabled="age < 30"
          />
          <label class="mx-2">30 or older</label>
        </div>

        <div class="inline-block my-1">
          <input
            type="radio"
            v-model="ageFirst"
            value="99"
            :disabled="age == null"
          />
          <label class="mx-2">Unknown</label>
        </div>
      </div>
      <p class="mx-auto my-3 text-xs text-red-500" v-if="checkAgeNull()">
        Please give your age first
      </p>
      <p class="mx-auto my-3 text-xs text-red-500" v-if="!checkAgeFirst()">
        Please choose one option
      </p>
    </div>

    <div id="nRel" class="w-10/12 mx-auto my-5">
      <p class="text-xl font-bold">
        How many of your first-degree relatives (mother, sisters, daughters)
        have had breast cancer?
      </p>
      <div class="grid">
        <div class="inline-block my-1">
          <input type="radio" v-model="nRels" value="0" />
          <label class="mx-2">None</label>
        </div>
        <div class="inline-block my-1">
          <input type="radio" v-model="nRels" value="1" />
          <label class="mx-2">One</label>
        </div>

        <div class="inline-block my-1">
          <input type="radio" v-model="nRels" value="12" />
          <label class="mx-2">More than 1</label>
        </div>

        <div class="inline-block my-1">
          <input type="radio" v-model="nRels" value="99" />
          <label class="mx-2">Unknown</label>
        </div>
      </div>
      <p class="mx-auto my-3 text-xs text-red-500" v-if="!checkRels()">
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
      VPlease check your input data
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
            <td class="border px-4 py-2">Race/Ethnicity</td>
            <td class="border px-4 py-2">{{ raceOptions[race] }}</td>
          </tr>
          <tr>
            <td class="border px-4 py-2">
              Breast biopsy with a benign diagnosis
            </td>
            <td class="border px-4 py-2">
              {{ nBiops1 === "1" ? "Yes" : nBiops1 === "0" ? "No" : "Unknown" }}
            </td>
          </tr>
          <tr v-if="nBiops1 === '1'">
            <td class="border px-4 py-2">
              Number of breast biopsies with a benign diagnosis
            </td>
            <td class="border px-4 py-2">
              {{
                nBiops1 === "1" ? (nBiops2 === "1" ? "1" : "2 or more") : "N/A"
              }}
            </td>
          </tr>
          <tr v-if="nBiops1 === '1'">
            <td class="border px-4 py-2">Atypical hyperplasia</td>
            <td class="border px-4 py-2">
              {{ RHyp === "1" ? "Yes" : RHyp === "0" ? "No" : "Unknown" }}
            </td>
          </tr>
          <tr>
            <td class="border px-4 py-2">
              Age at the time of your first menstrual period
            </td>
            <td class="border px-4 py-2">
              {{
                ageMen === "10"
                  ? "7 - 11"
                  : ageMen === "12"
                  ? "12 - 13"
                  : "14 and older"
              }}
            </td>
          </tr>
          <tr>
            <td class="border px-4 py-2">
              Number of your 1st-degree relatives with breast cancer
            </td>
            <td class="border px-4 py-2">
              {{
                nRels === "0"
                  ? "None"
                  : nRels === "1"
                  ? "One"
                  : nRels === "12"
                  ? "More than 1"
                  : "Unknown"
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

const isSubmit = ref(false);
const nBiops1 = ref(-1);
const nBiops2 = ref(-1);
const age = ref(null);
const race = ref(-1);
const RHyp = ref(-1);
const ageMen = ref(-1);
const ageFirst = ref(-1);
const nRels = ref(-1);
const responseData = ref(null);
const raceOptions = ref([
  "",
  "White",
  "African-American",
  "Hispanic-American (US born)",
  "Native American and other",
  "Hispanic-American (Foreign born)",
  "Chinese-American",
  "Japanese-American",
  "Filipino-American",
  "Hawaiian-American",
  "Other Pacific Islander",
  "Other Asian",
]);
var options = null;
var styleOptions = null;
var chartInstance = null;
const isClick = ref(false);

interface Form {
  t1: number;
  t2: number;
  nBiops: number;
  hypPlas: number;
  ageMen: number;
  age1st: number;
  nRela: number;
  race: number;
}

const checkAge = () => {
  return !(
    isClick.value &&
    (age.value <= 19 || age.value >= 91 || isNaN(age.value))
  );
};

const checkAgeMen = () => {
  return !(isClick.value && ageMen.value < 0);
};

const checkRace = () => {
  return !(isClick.value && race.value < 0);
};

const checkNBiops1 = () => {
  return !(isClick.value && nBiops1.value < 0);
};

const checkNBiops2 = () => {
  if (nBiops1.value !== 1) return true;
  return !(isClick.value && nBiops2.value < 0);
};

const checkRHyp = () => {
  if (nBiops1.value !== 1) return true;
  return !(isClick.value && RHyp.value < 0);
};

const checkAgeNull = () => {
  if (age.value == null) return true;
};
const checkAgeFirst = () => {
  if (checkAgeNull()) return true;
  else return !(isClick.value && ageFirst.value < 0);
};

const checkRels = () => {
  return !(isClick.value && nRels.value < 0);
};

const checkData = () => {
  console.log(isClick.value);
  if (isClick.value)
    return (
      checkAge() &&
      checkRace() &&
      checkNBiops1() &&
      checkNBiops2() &&
      checkAgeMen() &&
      checkRHyp() &&
      checkRels() &&
      checkAgeFirst() &&
      !checkAgeNull()
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
    var nBiops = -1;
    if (nBiops1.value == 0) {
      nBiops = 0;
    } else if (nBiops1.value == 99) {
      nBiops = 99;
    } else {
      nBiops = nBiops2.value;
    }

    if (RHyp.value === -1) {
      RHyp.value = 0;
    }

    const new_data: Form = {
      t1: age.value,
      t2: age.value + 5,
      nBiops: nBiops,
      hypPlas: RHyp.value,
      ageMen: ageMen.value,
      age1st: ageFirst.value,
      nRela: nRels.value,
      race: race.value,
    };
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/form/",
        new_data
      );
      console.log(response.status);
      responseData.value = response["data"];
      console.log(responseData.value);

      var dataPoints1 = [];
      var dataPoints2 = [];

      for (const key in responseData.value["absolute risk"]) {
        var temp = {
          label: key,
          y: responseData.value["absolute risk"][key],
        };
        dataPoints1.push(temp);
      }

      for (const key in responseData.value["absolute average"]) {
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
          itemclick: function (e) {
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

      chartInstance = (chart) => {
        chart.value = chart;
      };
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
