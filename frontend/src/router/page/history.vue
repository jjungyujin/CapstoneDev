<script>
import mainHeader from "../../components/mainHeader";
import mainNav from "../../components/mainNav";
import historyHeader from "../../components/historyHeader";
import historyMainTable from "../../components/historyMainTable";
import historyFeatureTableHeader from "../../components/historyFeatureTableHeader";
import historyFeatureTable from "../../components/historyFeatureTable";
import mainFooter from "../../components/mainFooter";

export default {
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
      example_data: []
    }
  },
  methods: {
    showFeatures(example_data) {
      this.example_data = example_data
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
            @example_data="showFeatures"
          />
          <div class="card my-4">
            <historyFeatureTableHeader />
            <historyFeatureTable 
              :FEATURE_values="example_data"
            />
            <div class="main-input-table-button">
              <div id="predict-button" style="width:130px">
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