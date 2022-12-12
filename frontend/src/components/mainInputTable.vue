<template>
  <div class="container-fluid px-4">
    <div>
      <h1 class="mt-4" style="font-family:Carter One;color:#171745">Prediction</h1>
      <ol class="breadcrumb mb-4">
        <li class="breadcrumb-item active">
          입력한 파라미터로 압연 공정을 진행했을 때 나오는 코일의 두께를
          예측합니다.
        </li>
      </ol>
      <div class="card mb-4">
        <div class="card-body">
          압연공정의 기본 정보를 입력해주세요.<br /><br />
          <label for="workerName">작업자명 :</label>
          <select id="workerName" class="basic-info-selector" name="workerName">
            <option value="서용득">서용득</option>
            <option value="조성우">조성우</option>
            <option value="정유진" selected>정유진</option>
            <option value="이정화">이정화</option>
          </select>
          <label for="rollingMillNum">압연기 번호 :</label>
          <select
            id="rollingMillNum"
            class="basic-info-selector"
            name="rollingMillNum"
          >
            <option value="1CRM">1CRM</option>
            <option value="2CRM" selected>2CRM</option>
            <option value="3CRM">3CRM</option>
          </select>
          <label for="coilNum">코일 번호 :</label>
          <input
            type="text"
            id="coilNum"
            placeholder="값을 입력해주세요"
            class="dashboard-input"
          />
        </div>
      </div>
    </div>
    <div class="card mb-4">
      <div class="card-header">
        <i class="fas fa-table me-1"></i>
        압연공정의 설정값을 입력해주세요.
      </div>
      <div class="card-body">
        <table class="inputTable">
            <tr>
              <td class="td-custom" v-for="(column, index) in fstRow" :key="index">
                {{ column.name }}
              </td>
            </tr>
          <tbody>
            <tr>
              <td v-for="(column, index) in fstRow" :key="index">
                <input
                  type="number"
                  step="0.001"
                  v-bind:id="column.id"
                  v-on:click="hidePredictResult()"
                  placeholder="값을 입력해주세요"
                  class="main-input"
                  v-model="init_FEATUREs_first[index]"
                />
              </td>
            </tr>
          </tbody>
        </table>
        <table class="inputTable">
            <tr>
              <td class="td-custom" v-for="(column, index) in scdRow" :key="index">
                {{ column.name }}
              </td>
            </tr>
          <tbody>
            <tr>
              <td v-for="(column, index) in scdRow" :key="index">
                <input
                  type="number"
                  step="0.001"
                  v-bind:id="column.id"
                  v-on:click="hidePredictResult()"
                  placeholder="값을 입력해주세요"
                  class="main-input"
                  v-model="init_FEATUREs_second[index]"
                />
              </td>
            </tr>
          </tbody>
        </table>
        <div class="main-input-table-button">
          <div
            id="reset-button"
            class="buttons"
            v-on:click="resetInputValues()"
          >
            초기화
          </div>
          <div
            id="predict-button"
            class="buttons"
            v-on:click="getInputValues()"
          >
            예측
          </div>
        </div>
        <div v-if="isShow === 1">
          <div id="predict-result">예측 결과 : {{ this.result }}</div>
          <div id="save-button" class="buttons" v-on:click="saveHistory()">
            저장
          </div>
        </div>
      </div>
    </div>
    <modal
      :show="showModal"
      @close="showModal = false"
      @moveHistory="moveHistory()"
    >
    </modal>
  </div>
</template>

<script>
import axios from "axios";
import Modal from "../components/Modal.vue";

export default {
  name: "mainInputTable",
  components: {
    Modal
  },
  methods: {
    resetInputValues() {
      this.init_FEATUREs_first = ["","","","","",""];
      this.init_FEATUREs_second = ["","","","","",""];
      this.hidePredictResult();
    },
    getInputValues() {
      const inputList = document.getElementsByClassName("main-input");
      let path = "http://localhost:8000/predict";
      let inputValueObj = {};
      for (let i = 0; i < inputList.length; i++) {
        if (inputList[i].value === "") {
          break;
        } else {
          inputValueObj[inputList[i].id] = inputList[i].value;
          this.historyObj[inputList[i].id] = inputList[i].value;
        }
      }
      axios.post(path, inputValueObj).then(res => {
        this.result = res.data;
        this.historyObj.THICKNESS_PRED = res.data;
      });
      this.isShow = 1;
    },
    hidePredictResult() {
      this.isShow = 0;
    },
    saveHistory() {
      let path = "http://localhost:8000/save_history";
      const workerName = document.getElementById("workerName");
      const rollingMillNum = document.getElementById("rollingMillNum");
      const coilNum = document.getElementById("coilNum");
      this.historyObj.DATE = new Date().toLocaleString("en-GB");
      this.historyObj.WORKER_NAME =
        workerName.options[workerName.selectedIndex].value;
      this.historyObj.CRM_ID =
        rollingMillNum.options[rollingMillNum.selectedIndex].value;
      this.historyObj.COIL_ID = coilNum.value;
      axios.post(path, this.historyObj);
      this.showModal = true;
    },
    moveHistory() {
      this.$router.push("/history");
    }
  },
  created() {
    this.$router.push({
      name: "Home",
      query: {
        FEATURE_1: "",
        FEATURE_2: "",
        FEATURE_3: "",
        FEATURE_4: "",
        FEATURE_5: "",
        FEATURE_6: "",
        FEATURE_7: "",
        FEATURE_8: "",
        FEATURE_9: "",
        FEATURE_10: "",
        FEATURE_11: "",
        FEATURE_12: ""
      }
    });
  },
  data() {
    return {
      showModal: false,
      init_FEATUREs_first: [
        this.$route.query.FEATURE_1,
        this.$route.query.FEATURE_2,
        this.$route.query.FEATURE_3,
        this.$route.query.FEATURE_4,
        this.$route.query.FEATURE_5,
        this.$route.query.FEATURE_6
      ],
      init_FEATUREs_second: [
        this.$route.query.FEATURE_7,
        this.$route.query.FEATURE_8,
        this.$route.query.FEATURE_9,
        this.$route.query.FEATURE_10,
        this.$route.query.FEATURE_11,
        this.$route.query.FEATURE_12
      ],
      result: "",
      isShow: 0,
      historyObj: {},
      fstRow: [
        {
          name: "코일의 평균 입측 두께",
          id: "FEATURE_1"
        },
        {
          name: "upper 롤 이동값",
          id: "FEATURE_2"
        },
        {
          name: "lower 롤 이동값",
          id: "FEATURE_3"
        },
        {
          name: "밴딩 DS",
          id: "FEATURE_4"
        },
        {
          name: "LH tension",
          id: "FEATURE_5"
        },
        {
          name: "RH tension",
          id: "FEATURE_6"
        }
      ],
      scdRow: [
        {
          name: "POR tension",
          id: "FEATURE_7"
        },
        {
          name: "POR tension (N/mm2)",
          id: "FEATURE_8"
        },
        {
          name: "롤 힘",
          id: "FEATURE_9"
        },
        {
          name: "롤 속도",
          id: "FEATURE_10"
        },
        {
          name: "좌 냉각수 유량",
          id: "FEATURE_11"
        },
        {
          name: "우 냉각수 유량",
          id: "FEATURE_12"
        }
      ]
    };
  }
};
</script>
