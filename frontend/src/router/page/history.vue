<script>
import mainHeader from "../../components/mainHeader";
import mainNav from "../../components/mainNav";
import historyHeader from "../../components/historyHeader";
import historyMainTable from "../../components/historyMainTable";
import historyFeatureTableHeader from "../../components/historyFeatureTableHeader";
import historyFeatureTable from "../../components/historyFeatureTable";
import mainFooter from "../../components/mainFooter";

export default {
  name: "History",
  components: {
    mainHeader,
    mainNav,
    historyHeader,
    historyMainTable,
    historyFeatureTableHeader,
    historyFeatureTable,
    mainFooter
  },
  data() {
    return {
      clicked_features: []
    }
  },
  methods: {
    showFeatures(clicked_features) {
      this.clicked_features = clicked_features
    },
    sendFeatures() {
      this.$router.push({
        name: "Home",
        query: {
          FEATURE_1: this.clicked_features[0],
          FEATURE_2: this.clicked_features[1],
          FEATURE_3: this.clicked_features[2],
          FEATURE_4: this.clicked_features[3],
          FEATURE_5: this.clicked_features[4],
          FEATURE_6: this.clicked_features[5],
          FEATURE_7: this.clicked_features[6],
          FEATURE_8: this.clicked_features[7],
          FEATURE_9: this.clicked_features[8],
          FEATURE_10: this.clicked_features[9],
          FEATURE_11: this.clicked_features[10],
          FEATURE_12: this.clicked_features[11],
        }
      });
    }
  }
};
</script>

<template>
  <div>
    <mainHeader />
    <div id="layoutSidenav">
      <mainNav />
      <div id="layoutSidenav_content">
        <div class="container-fluid px-4">
          <historyHeader />
          <historyMainTable 
            @clicked_features="showFeatures"
          />
          <div class="card my-4">
            <historyFeatureTableHeader />
            <historyFeatureTable 
              :FEATURE_values="clicked_features"
            />
            <div class="history-table-button">
              <div id="predict-button-2" @click="sendFeatures">
                해당 기록으로 예측
              </div>
            </div>
          </div>
        </div>
        <mainFooter />
      </div>
    </div>
  </div>
</template>

<style lang='scss'>
@import "~vue-tabulator/dist/scss/bootstrap/tabulator_bootstrap4";
@import '@/assets/sass/tabulator.scss';
</style>